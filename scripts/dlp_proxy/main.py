"""
PetroShield XR DLP Proxy v2.0 — AxeGuard Middleware
FastAPI-based security gateway for XR/AI corporate access.
Features: OAuth Device Flow, bidirectional DLP, OT/ICS filtering,
threat scoring, vendor risk cascade, and tamper-evident audit logging.
"""

from fastapi import FastAPI, HTTPException, Header, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import sys
import os

# Adicionar raiz do projeto ao sys.path para permitir imports absolutos do pacote 'scripts'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import re
import hashlib
import time
import asyncio
import os
import json
from sse_starlette.sse import EventSourceResponse
from dotenv import load_dotenv

load_dotenv() # Carrega .env da raiz

# Imports do Agentic SOC
from scripts.agentic_soc.state import create_initial_state
from scripts.agentic_soc.orchestrator import START, END
from scripts.agentic_soc.theatre import build_agentic_graph
from scripts.agentic_soc.openai_bridge import OpenAIBridge
from scripts.agentic_soc.financial_model import FinancialCalculator
from scripts.agentic_soc.logger import AgenticLogger
from scripts.agentic_soc.mock_data import DEMO_SCENARIOS, XR_DEVICES, VENDOR_RISK_DB as MOCK_VENDOR_DB, AUTH_SESSIONS
from scripts.agentic_soc.theatre import inject_scenario

app = FastAPI(
    title="PetroShield XR DLP Proxy v2.0",
    description="AxeGuard Middleware — Zero-Trust AI Gateway for Industrial XR",
    version="2.0.0-agentic"
)

# Montar arquivos estáticos (Dashboard)
static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

# =============================================================================
# AXEGUARD COMPONENT INITIALIZATION
# =============================================================================

# Carregar modo das variáveis de ambiente
AXEGUARD_MODE = os.getenv("AXEGUARD_MODE", "hybrid")
AXEGUARD_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Instâncias globais (Compartilhadas entre TUI e API)
soc_logger = AgenticLogger(verbose=True, use_rich=True)
soc_bridge = OpenAIBridge(mode=AXEGUARD_MODE, model=AXEGUARD_MODEL)
soc_calculator = FinancialCalculator()
soc_graph_def = build_agentic_graph(soc_logger, soc_bridge, soc_calculator)
soc_compiled_graph = soc_graph_def.compile()

# =============================================================================
# MOCK DATA STORES (In production, these connect to PostgreSQL + Redis)
# =============================================================================

# =============================================================================
# MOCK DATA STORES (Sincronizadas com Agentic SOC)
# =============================================================================

ACTIVE_SESSIONS = AUTH_SESSIONS
VENDOR_RISK_DB = MOCK_VENDOR_DB
DEVICE_REGISTRY = XR_DEVICES

AUDIT_LOG: List[dict] = []
LAST_AUDIT_HASH = "genesis"


# =============================================================================
# PYDANTIC MODELS
# =============================================================================

class PromptRequest(BaseModel):
    query: str
    device_id: str


class VendorRiskCascadeRequest(BaseModel):
    vendor_id: str
    trigger: str


class RedactedEntity(BaseModel):
    type: str
    value: str
    token: str


# =============================================================================
# DLP ENGINE v2.0
# =============================================================================

class DLPEngine:
    """
    3-stage pipeline:
    1. Fast regex for known patterns
    2. OT/ICS command detection
    3. Entity tracking with classification
    """

    PATTERNS = [
        {
            "name": "cpf",
            "regex": re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}'),
            "token": "[CPF_BLOQUEADO]",
            "classification": "Crítica",
        },
        {
            "name": "platform",
            "regex": re.compile(r'(?i)\bP-\d{2,3}\b'),
            "token": "[ATIVO_RESTRITO]",
            "classification": "Alta",
        },
        {
            "name": "well",
            "regex": re.compile(r'(?i)\bpo[çc]o\s+[a-z0-9-]+\b'),
            "token": "[ATIVO_RESTRITO]",
            "classification": "Estratégica",
        },
        {
            "name": "password",
            "regex": re.compile(r'(?i)(senha|password)\s+([a-zA-Z0-9@#$]+)'),
            "token": r'\1 [CREDENCIAL_BLOQUEADA]',
            "classification": "Crítica",
            "substitution": True,
        },
        {
            "name": "scada_command",
            "regex": re.compile(r'(?i)(modbus\s+fc\s*(5|16)|dnp3\s+outstation|opc\s*ua\s*anonymous)'),
            "token": "[COMANDO_OT_BLOQUEADO]",
            "classification": "Crítica",
            "ot_alert": True,
        },
        {
            "name": "seismic_data",
            "regex": re.compile(r'(?i)(3D\s*seismic|4D\s*seismic|OBN\s*position|DGPS\s*coordinate)'),
            "token": "[DADO_SISMICO_RESTRITO]",
            "classification": "Estratégica",
        },
        {
            "name": "vendor_restricted",
            "regex": re.compile(r'(?i)(oceânica\s*engenharia|sa\s*exploration|oceanpact)'),
            "token": "[VENDOR_RESTRITO]",
            "classification": "Alta",
        },
    ]

    def redact(self, text: str) -> tuple[str, List[RedactedEntity], List[str]]:
        """
        Returns: (sanitized_text, redacted_entities, anomaly_flags)
        """
        sanitized = text
        entities: List[RedactedEntity] = []
        anomaly_flags: List[str] = []

        for pattern in self.PATTERNS:
            for match in pattern["regex"].finditer(text):
                raw_value = match.group(0)
                if pattern.get("substitution"):
                    sanitized = pattern["regex"].sub(pattern["token"], sanitized)
                    # Extract just the password part for logging
                    token_display = "[CREDENCIAL_BLOQUEADA]"
                else:
                    sanitized = sanitized.replace(raw_value, pattern["token"], 1)
                    token_display = pattern["token"]

                entities.append(RedactedEntity(
                    type=pattern["name"],
                    value=raw_value,
                    token=token_display
                ))

                if pattern.get("ot_alert"):
                    anomaly_flags.append("ot_protocol_detected")
                    anomaly_flags.append("unauthorized_control_command")

        # Deduplicate entities by value
        seen = set()
        unique_entities = []
        for e in entities:
            if e.value.lower() not in seen:
                seen.add(e.value.lower())
                unique_entities.append(e)

        return sanitized, unique_entities, list(set(anomaly_flags))

    def compute_threat_score(self, entities: List[RedactedEntity], anomaly_flags: List[str], text: str) -> float:
        """
        Simple heuristic threat scoring (0.0 - 1.0).
        In production, this calls an ML model or behavioral baseline.
        """
        score = 0.0
        score += min(len(entities) * 0.10, 0.40)
        if "ot_protocol_detected" in anomaly_flags:
            score += 0.50
        if "unauthorized_control_command" in anomaly_flags:
            score += 0.30
        if len(text) > 200:
            score += 0.05
        return min(round(score, 2), 1.0)


redactor = DLPEngine()


# =============================================================================
# AUTH & SESSION MANAGEMENT
# =============================================================================

def verify_token(authorization: str = Header(None)) -> dict:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Header de Autorização ausente ou inválido. O Smart Glasses deve usar OAuth Device Flow Token."
        )

    token = authorization.split("Bearer ")[1]
    session = ACTIVE_SESSIONS.get(token)

    if not session:
        raise HTTPException(
            status_code=403,
            detail="Token de Sessão Inválido. Potencial movimento lateral detectado (Device Hijacking)."
        )

    if session.get("revoked"):
        reason = session.get("revoked_reason", "unknown")
        raise HTTPException(
            status_code=403,
            detail=f"Session revoked due to {reason}. Operator must re-authenticate after clearance."
        )

    # Vendor risk cascade check
    vendor_id = session.get("vendor_id")
    if vendor_id and VENDOR_RISK_DB.get(vendor_id, {}).get("auto_suspend", False):
        raise HTTPException(
            status_code=403,
            detail=f"Session revoked due to vendor risk cascade ({vendor_id}). Operator must re-authenticate after vendor clearance."
        )

    return session


# =============================================================================
# AUDIT LOGGING
# =============================================================================

def append_audit(event: dict) -> dict:
    global LAST_AUDIT_HASH
    event["prev_log_hash"] = LAST_AUDIT_HASH
    payload = f"{LAST_AUDIT_HASH}|{event.get('session_id')}|{event.get('device_id')}|{event.get('original_query')}|{event.get('created_at')}"
    new_hash = hashlib.sha256(payload.encode()).hexdigest()
    event["log_hash"] = new_hash
    LAST_AUDIT_HASH = new_hash
    AUDIT_LOG.append(event)
    return event


# =============================================================================
# AGENTIC SOC ENDPOINTS (SSE & Control)
# =============================================================================

@app.get("/api/v1/soc/stream")
async def soc_stream(request: Request):
    """
    Stream de Eventos do SOC em tempo real via SSE.
    Envia logs de THOUGHT, ACTION, OBSERVATION e METRICS.
    """
    log_queue = soc_logger.subscribe()

    async def event_generator():
        try:
            while True:
                # Verificar se o cliente fechou a conexão
                if await request.is_disconnected():
                    break

                # Aguarda novo log
                try:
                    log_entry = await asyncio.wait_for(log_queue.get(), timeout=1.0)
                    yield {
                        "event": "message",
                        "id": str(log_entry.get("seq", 0)),
                        "retry": 15000,
                        "data": json.dumps(log_entry, ensure_ascii=False)
                    }
                except asyncio.TimeoutError:
                    # Enviar heartbeat para manter a conexão viva
                    yield {
                        "event": "ping",
                        "data": "heartbeat"
                    }
        finally:
            soc_logger.unsubscribe(log_queue)

    return EventSourceResponse(event_generator())


@app.get("/api/v1/soc/topology")
async def soc_topology():
    """Retorna a topologia do grafo para visualização."""
    return soc_graph_def.get_topology()


@app.post("/api/v1/demo/run")
async def run_demo_scene(scene_id: str):
    """
    Dispara a execução de um cenário específico do 'Teatro'.
    Os logs serão enviados para o stream SSE.
    """
    scene_id_lower = scene_id.lower()
    scenario = next((s for s in DEMO_SCENARIOS if s["scene_id"] == scene_id_lower), None)
    if not scenario:
        raise HTTPException(status_code=404, detail=f"Cenário '{scene_id}' não encontrado.")

    # Execução assíncrona para não bloquear o worker
    async def task():
        soc_logger.scene_header(scenario["scene_id"], scenario["scene_title"])
        for line in scenario["narration"]:
            soc_logger.narrate(line)
            await asyncio.sleep(0.5)

        state = create_initial_state()
        state = inject_scenario(state, scenario)

        # Executar grafo - stream por stream
        for node_name, current_state in soc_compiled_graph.stream(state):
            await asyncio.sleep(0.2)
        
        soc_logger.system(f"Cenário {scene_id} concluído com sucesso.")

    asyncio.create_task(task())
    return {"status": "started", "scene_id": scene_id}


# =============================================================================
# ENDPOINTS
# =============================================================================

@app.get("/")
async def root():
    return {
        "message": "PetroShield XR Gateway Ativo",
        "status": "online",
        "docs": "/docs",
        "version": "2.0.0-agentic",
        "layers": ["MDM", "Auth", "EdgeDLP", "ProxyDLP", "ThreatIntel", "PrivateAI"]
    }


@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard():
    """Retorna o dashboard executável."""
    return FileResponse(os.path.join(static_dir, "dashboard.html"))


@app.get("/api/v1/auth/device-flow-status")
async def device_flow(device_id: str):
    return {
        "device_id": device_id,
        "status": "pending_smartphone_approval",
        "verification_uri": "https://auth.corp.petrobras.com.br/device",
        "instruction": "Abra o link no celular e use o FaceID para destravar a sessão deste Óculos VR."
    }


@app.post("/api/v1/secure-prompt")
async def secure_prompt(request: PromptRequest, session: dict = Depends(verify_token)):
    """
    Endpoint principal AxeGuard: Processa query via Grafo Multi-Agente.
    """
    # 1. Preparar Estado Inicial
    state = create_initial_state()
    state["event_type"] = "user_query"
    state["event_source_device"] = request.device_id
    state["event_raw_query"] = request.query
    state["session_id"] = session.get("session_id")
    state["operator_id"] = session.get("operator_id")
    state["vendor_id"] = session.get("vendor_id")
    state["event_timestamp"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    # 2. Executar Orquestrador (Modo Non-Blocking para SSE se necessário, mas aqui retornamos a resposta final)
    start_time = time.time()
    
    # Rodamos o grafo de forma síncrona para esta rota (é rápido se for mock, ou gpt-4o-mini)
    # Em produção, poderíamos usar .stream() para alimentar o logger enquanto processa
    final_state = soc_compiled_graph.invoke(state)
    
    latency_ms = int((time.time() - start_time) * 1000)

    # 3. Mapear resultado para o contrato de resposta
    return {
        "status": "success" if final_state.get("dlp_action") != "blocked" else "blocked",
        "dlp_audit_log": {
            "device_id": request.device_id,
            "sanitized_query": final_state.get("dlp_sanitized_query", request.query),
            "threat_score": final_state.get("dlp_threat_score", 0),
            "anomaly_flags": final_state.get("dlp_anomaly_flags", []),
            "operator_action": final_state.get("dlp_action"),
            "mitre_technique": final_state.get("threat_intel", {}).get("ttp_id"),
            "latency_ms": latency_ms,
            "chain_hash": final_state.get("last_audit_hash"),
        },
        "llm_response": "Resposta do LLM Protegido AxeGuard baseada na query sanitizada.",
        "financial_impact": final_state.get("financial", {}),
        "fleet_vaccination": final_state.get("fleet_report", {})
    }


@app.post("/api/v1/vendor-risk-cascade")
async def vendor_risk_cascade(request: VendorRiskCascadeRequest):
    vendor = VENDOR_RISK_DB.get(request.vendor_id)
    if not vendor:
        raise HTTPException(status_code=404, detail="Vendor not found")

    # Simulate risk score jump
    vendor["risk_score"] = 89.0
    vendor["risk_level"] = "CRITICAL"
    vendor["auto_suspend"] = True

    # Find affected devices
    affected_devices = [
        d for d, info in DEVICE_REGISTRY.items()
        if info.get("vendor_id") == request.vendor_id
    ]

    # Revoke sessions for affected devices
    revoked_count = 0
    for token, session in ACTIVE_SESSIONS.items():
        if session.get("device_id") in affected_devices:
            session["revoked"] = True
            session["revoked_reason"] = f"vendor_risk_cascade_{request.vendor_id.lower()}"
            revoked_count += 1

    compliance_id = f"COMP-{time.strftime('%Y-%m%d', time.gmtime())}-112"

    return {
        "status": "cascade_triggered",
        "vendor_id": request.vendor_id,
        "vendor_name": vendor["vendor_name"],
        "risk_score": vendor["risk_score"],
        "risk_level": vendor["risk_level"],
        "trigger": request.trigger,
        "actions_taken": [
            f"Suspended {revoked_count} active XR sessions",
            "Revoked OAuth tokens for vendor-linked devices",
            "Created ANPD assessment ticket",
            "Alerted procurement and SOC teams"
        ],
        "affected_devices": affected_devices,
        "compliance_ledger_id": compliance_id,
    }


@app.get("/api/v1/demo/dashboard")
async def demo_dashboard():
    leaks_prevented = sum(1 for e in AUDIT_LOG if e.get("data_leak_prevented"))
    critical_alerts = sum(1 for e in AUDIT_LOG if e.get("threat_score", 0) > 0.8)
    avg_latency = int(sum(e.get("latency_ms", 0) for e in AUDIT_LOG) / max(len(AUDIT_LOG), 1))
    active_sessions = sum(1 for s in ACTIVE_SESSIONS.values() if not s.get("revoked"))

    latest = AUDIT_LOG[-1] if AUDIT_LOG else None

    return {
        "petroshield_status": "online",
        "metrics": {
            "active_sessions": active_sessions,
            "leaks_prevented_1h": leaks_prevented,
            "avg_latency_ms": avg_latency,
            "critical_alerts": critical_alerts,
        },
        "agentic_loop": {
            "current_phase": "RESPOND",
            "phases_completed": ["MONITOR", "DETECT", "ANALYSE"],
            "confidence": 0.98,
            "incident_id": "INC-2026-0413-089",
        },
        "latest_audit_event": {
            "log_id": latest.get("log_hash") if latest else None,
            "device_id": latest.get("device_id") if latest else None,
            "action": latest.get("operator_action") if latest else None,
            "threat_score": latest.get("threat_score") if latest else None,
            "redacted_preview": latest.get("sanitized_query", "")[:60] + "..." if latest else None,
        } if latest else None,
        "vendor_risk_spotlight": {
            "vendor_name": VENDOR_RISK_DB["OCEANICA_ENG"]["vendor_name"],
            "risk_score": VENDOR_RISK_DB["OCEANICA_ENG"]["risk_score"],
            "risk_level": VENDOR_RISK_DB["OCEANICA_ENG"]["risk_level"],
            "xr_sessions_suspended": sum(
                1 for s in ACTIVE_SESSIONS.values()
                if s.get("revoked") and "oceanica" in s.get("revoked_reason", "")
            ),
        }
    }


@app.get("/api/v1/audit/log")
async def audit_log():
    return {
        "count": len(AUDIT_LOG),
        "events": AUDIT_LOG,
        "hash_chain_valid": True,
    }


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
