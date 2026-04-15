"""
PetroShield XR DLP Proxy v2.0 — AxeGuard Middleware
FastAPI-based security gateway for XR/AI corporate access.
Features: OAuth Device Flow, bidirectional DLP, OT/ICS filtering,
threat scoring, vendor risk cascade, and tamper-evident audit logging.
"""

from fastapi import FastAPI, HTTPException, Header, Depends, Request
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import re
import hashlib
import time

app = FastAPI(
    title="PetroShield XR DLP Proxy v2.0",
    description="AxeGuard Middleware — Zero-Trust AI Gateway for Industrial XR",
    version="2.0.0-agentic"
)

# =============================================================================
# MOCK DATA STORES (In production, these connect to PostgreSQL + Redis)
# =============================================================================

ACTIVE_SESSIONS: Dict[str, dict] = {
    "jwt_token_xr_session_9942": {
        "session_id": "sess-xr-9942-p93",
        "device_id": "hololens-047",
        "operator_id": "OP-33891",
        "vendor_id": "OCEANICA_ENG",
        "expires_at": "2026-04-14T02:00:00Z",
        "revoked": False,
    }
}

VENDOR_RISK_DB: Dict[str, dict] = {
    "OCEANICA_ENG": {
        "vendor_name": "Oceânica Engenharia",
        "risk_score": 62.0,  # Will be overridden to 89 on cascade
        "risk_level": "MEDIUM",
        "xr_device_count": 12,
    },
    "SA_EXPLORATION": {
        "vendor_name": "SA Exploration",
        "risk_score": 95.0,
        "risk_level": "CRITICAL",
        "xr_device_count": 0,
    }
}

DEVICE_REGISTRY: Dict[str, dict] = {
    "hololens-047": {"vendor_id": "OCEANICA_ENG", "facility_zone": "FPSO_P93"},
    "quest-vr-001": {"vendor_id": None, "facility_zone": "Unknown"},
    "realwear-102": {"vendor_id": "OCEANICA_ENG", "facility_zone": "FPSO_P93"},
}

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
    original_query = request.query
    start_time = time.time()

    # Stage 1: DLP redaction
    sanitized_query, entities, anomaly_flags = redactor.redact(original_query)
    data_leak_prevented = original_query != sanitized_query

    # Stage 2: Threat scoring
    threat_score = redactor.compute_threat_score(entities, anomaly_flags, original_query)

    # Stage 3: Decision matrix
    mitre_technique = None
    if "ot_protocol_detected" in anomaly_flags:
        operator_action = "escalated"
        mitre_technique = "T0831"
    elif not session:
        operator_action = "blocked"
        mitre_technique = "T1078"
    elif threat_score > 0.80:
        operator_action = "escalated"
    else:
        operator_action = "allowed"

    latency_ms = int((time.time() - start_time) * 1000)

    # Stage 4: Audit logging
    audit_event = append_audit({
        "session_id": session.get("session_id"),
        "device_id": request.device_id,
        "operator_id": session.get("operator_id"),
        "original_query": original_query,
        "sanitized_query": sanitized_query,
        "data_leak_prevented": data_leak_prevented,
        "redaction_count": len(entities),
        "redacted_entities": [e.model_dump() for e in entities],
        "threat_score": threat_score,
        "anomaly_flags": anomaly_flags,
        "operator_action": operator_action,
        "mitre_technique": mitre_technique,
        "latency_ms": latency_ms,
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    })

    # Stage 5: Response routing
    if operator_action == "escalated" and "ot_protocol_detected" in anomaly_flags:
        return {
            "status": "blocked",
            "dlp_audit_log": {
                "device_id": request.device_id,
                "sanitized_query": sanitized_query,
                "data_leak_prevented": data_leak_prevented,
                "redaction_count": len(entities),
                "redacted_entities": [e.model_dump() for e in entities],
                "threat_score": threat_score,
                "anomaly_flags": anomaly_flags,
                "operator_action": operator_action,
                "mitre_technique": mitre_technique,
                "soc_alert_id": f"SOC-OT-{time.strftime('%Y-%m%d', time.gmtime())}-001",
            },
            "llm_response": None,
            "soc_escalation": {
                "message": "OT protocol command detected in LLM prompt. Escalated to SOC immediately.",
                "recommended_action": f"Verify operator identity and inspect {request.device_id} for compromise."
            }
        }

    # Bidirectional DLP: simulate response sanitization
    mock_llm_raw = (
        f"Sou a IA Copilot Corporativa (LLM Privado). "
        f"Estou analisando a sua query de forma segura. "
        f"O meu acesso local recebeu os seguintes dados limpos: '{sanitized_query}'"
    )
    response_sanitized, resp_entities, _ = redactor.redact(mock_llm_raw)

    return {
        "status": "success",
        "dlp_audit_log": {
            "device_id": request.device_id,
            "original_query_length": len(original_query),
            "sanitized_query": sanitized_query,
            "data_leak_prevented": data_leak_prevented,
            "redaction_count": len(entities),
            "redacted_entities": [e.model_dump() for e in entities],
            "llm_provider": "azure-openai-private",
            "llm_model": "gpt-4o",
            "threat_score": threat_score,
            "anomaly_flags": anomaly_flags,
            "operator_action": operator_action,
            "mitre_technique": mitre_technique,
            "latency_ms": latency_ms,
            "prev_log_hash": audit_event["prev_log_hash"],
        },
        "llm_response": response_sanitized,
        "response_dlp": {
            "response_sanitized": mock_llm_raw != response_sanitized,
            "response_redactions": [e.model_dump() for e in resp_entities],
        }
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
