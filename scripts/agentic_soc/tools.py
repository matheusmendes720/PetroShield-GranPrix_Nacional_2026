"""
tools.py — Ferramentas (Tools) dos Agentes PetroShield
=======================================================
Cada agente possui um toolkit de funções que pode invocar.
As ferramentas são implementadas como funções puras que:
  - Recebem o AgenticState como contexto
  - Retornam um dict (patch) para merge no estado
  - Produzem logs via AgenticLogger

Em modo LIVE, algumas ferramentas chamam a OpenAI API.
Em modo MOCK, todas retornam dados determinísticos.
"""

import hashlib
import time
import random
from typing import Dict, List, Any

from .state import (
    AgenticState, ThreatIntelResult, VaccinePayload,
    FleetBroadcastReport, FleetNodeStatus,
)
from .mock_data import (
    XR_DEVICES, AUTH_SESSIONS, VENDOR_RISK_DB,
    THREAT_PATTERNS, FLEET_REGISTRY, MITRE_ICS_KNOWLEDGE_BASE,
)
from .dlp_engine import DLPEngine, create_audit_entry
from .financial_model import FinancialCalculator
from .logger import AgenticLogger


# =============================================================================
# FERRAMENTAS DO Agent_DLP_Edge
# =============================================================================

def tool_inspect_packet(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    inspect_packet(device_id, query) → DLP result
    Decodifica e inspeciona o payload do pacote/query suspeito.
    """
    device_id = state["event_source_device"]
    query = state["event_raw_query"]
    has_session = state["auth_status"] == "authenticated"

    logger.action("Agent_DLP_Edge", f"inspect_packet(device={device_id})", tool="inspect_packet")

    dlp = DLPEngine()
    result = dlp.full_pipeline(query, has_session=has_session)

    logger.observation(
        "Agent_DLP_Edge",
        f"Redações: {len(result['dlp_entities'])} | "
        f"Threat Score: {result['dlp_threat_score']} | "
        f"Ação: {result['dlp_action']}"
    )

    return result


def tool_block_request(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    block_request(device_id) → bool
    Bloqueia a requisição e registra no audit log.
    """
    device_id = state["event_source_device"]
    logger.action("Agent_DLP_Edge", f"block_request(device={device_id})", tool="block_request")
    logger.observation("Agent_DLP_Edge", f"Requisição BLOQUEADA para {device_id}. HTTP 401/403 retornado.")
    return {"dlp_action": "blocked"}


def tool_isolate_subnet(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    isolate_subnet(device_id) → bool
    Isola o segmento de rede do dispositivo comprometido.
    """
    device_id = state["event_source_device"]
    device = XR_DEVICES.get(device_id, {})
    subnet = device.get("network_segment", "Unknown")

    logger.action(
        "Agent_DLP_Edge",
        f"isolate_subnet(device={device_id}, segment={subnet})",
        tool="isolate_subnet"
    )
    # Simula latência de isolamento (< 10ms conforme spec)
    time.sleep(0.008)
    logger.observation("Agent_DLP_Edge", f"Subnet {subnet} ISOLADA em < 10ms. Tráfego lateral bloqueado.")
    return {}


# =============================================================================
# FERRAMENTAS DO Agent_Intel_Cloud
# =============================================================================

def tool_query_mitre_ics(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    query_mitre_ics(vector_query) → list[TTP]
    Busca semântica (simulada) na base MITRE ATT&CK for ICS.
    """
    mitre_technique = state.get("dlp_action") and state.get("dlp_anomaly_flags", [])

    # Determinar TTP baseado nas flags de anomalia
    if "ot_protocol_detected" in state.get("dlp_anomaly_flags", []):
        target_ttp = "T0831"
    elif state.get("auth_status") != "authenticated":
        target_ttp = "T1078"
    else:
        target_ttp = "T1213"

    logger.action("Agent_Intel_Cloud", f"query_mitre_ics(target={target_ttp})", tool="query_mitre_ics")

    # Buscar na base mock
    match = next((t for t in MITRE_ICS_KNOWLEDGE_BASE if t["technique_id"] == target_ttp), None)

    if match:
        confidence = 0.98 if "ot_protocol_detected" in state.get("dlp_anomaly_flags", []) else 0.94
        result = ThreatIntelResult(
            ttp_id=match["technique_id"],
            ttp_name=match["name"],
            tactic=match["tactic"],
            confidence=confidence,
            kill_chain=["Reconnaissance", "Initial Access", match["tactic"], "Impact"],
            reasoning=(
                f"Match semântico na base MITRE ICS: {match['technique_id']} — {match['name']}. "
                f"Confiança: {confidence}. "
                f"Plataformas afetadas: {', '.join(match['platforms'])}. "
                f"Data sources para validação: {', '.join(match['data_sources'])}."
            ),
        )
        logger.observation(
            "Agent_Intel_Cloud",
            f"Top match: {match['technique_id']} ({match['name']}) — Confiança: {confidence}"
        )
    else:
        result = ThreatIntelResult(
            ttp_id="UNKNOWN",
            ttp_name="Unclassified Threat",
            tactic="Unknown",
            confidence=0.45,
            kill_chain=["Unknown"],
            reasoning="Nenhum match encontrado na base MITRE ICS. Escalando para analista humano.",
        )
        logger.observation("Agent_Intel_Cloud", "Nenhum match MITRE encontrado. Ameaça não classificável.")

    return {"threat_intel": result}


def tool_generate_vaccine(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    generate_vaccine_signature(ttp_profile) → VaccinePayload
    Sintetiza uma assinatura de vacina para propagação na frota.
    """
    threat = state.get("threat_intel", {})
    ttp_id = threat.get("ttp_id", "UNKNOWN")

    logger.action("Agent_Intel_Cloud", f"generate_vaccine_signature(ttp={ttp_id})", tool="generate_vaccine")

    # Gerar hash determinístico da vacina
    hash_input = f"{ttp_id}|{state.get('event_raw_query', '')}|{time.time()}"
    vaccine_hash = hashlib.sha256(hash_input.encode()).hexdigest()

    # Mapear portas por protocolo
    port_map = {
        "T0831": [502, 503, 8502],  # Modbus
        "T0817": [445, 139],         # SMB
        "T0812": [102, 502],         # S7/Modbus
        "T1078": [443, 8443],        # HTTPS
        "T1195": [22, 3389],         # SSH/RDP
    }
    protocol_map = {
        "T0831": "Modbus/TCP",
        "T0817": "SMB",
        "T0812": "S7comm",
        "T1078": "HTTPS",
        "T1195": "SSH/RDP",
    }

    vaccine = VaccinePayload(
        hash=f"SHA256:{vaccine_hash[:48]}",
        rule=f"BLOCK {protocol_map.get(ttp_id, 'ANY')} on ports {port_map.get(ttp_id, [0])}",
        ports_blocked=port_map.get(ttp_id, []),
        protocol=protocol_map.get(ttp_id, "UNKNOWN"),
        ttp_source=ttp_id,
        generated_at=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    )

    logger.observation(
        "Agent_Intel_Cloud",
        f"Vacina gerada: {vaccine['hash'][:32]}... | Protocolo: {vaccine['protocol']} | Portas: {vaccine['ports_blocked']}"
    )

    return {"vaccine": vaccine}


# =============================================================================
# FERRAMENTAS DO Agent_Fleet_Vaccinator
# =============================================================================

def tool_broadcast_vaccine(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    broadcast_to_fleet(region, vaccine) → BroadcastReport
    Difunde a vacina para todos os Edge Nodes da frota.
    Simula: latência de rede, ACK, retry, e nodes offline.
    """
    vaccine = state.get("vaccine", {})
    logger.action("Agent_Fleet_Vaccinator", "broadcast_to_fleet(region=ALL)", tool="broadcast_vaccine")

    broadcast_start = time.time()
    nodes_status: List[FleetNodeStatus] = []
    success = 0
    failed = 0
    partial = 0

    for node in FLEET_REGISTRY:
        # Simular latência de rede (10-80ms por node)
        latency = random.randint(10, 80)

        if node["status"] == "offline":
            nodes_status.append(FleetNodeStatus(
                node_id=node["node_id"],
                facility=node["facility"],
                region=node["region"],
                vaccine_applied=False,
                latency_ms=0,
                retry_count=3,
            ))
            failed += 1
            logger.observation(
                "Agent_Fleet_Vaccinator",
                f"  ✗ {node['node_id']} ({node['facility']}) — OFFLINE (3 retries esgotados)"
            )
        else:
            nodes_status.append(FleetNodeStatus(
                node_id=node["node_id"],
                facility=node["facility"],
                region=node["region"],
                vaccine_applied=True,
                latency_ms=latency,
                retry_count=0,
            ))
            success += 1

    broadcast_duration = int((time.time() - broadcast_start) * 1000)

    report = FleetBroadcastReport(
        total_nodes=len(FLEET_REGISTRY),
        success=success,
        failed=failed,
        partial=partial,
        nodes=nodes_status,
        broadcast_duration_ms=broadcast_duration,
    )

    logger.observation(
        "Agent_Fleet_Vaccinator",
        f"Broadcast completo: {success}/{len(FLEET_REGISTRY)} nodes vacinados | "
        f"{failed} offline | Duração: {broadcast_duration}ms"
    )

    return {"fleet_report": report}


# =============================================================================
# FERRAMENTAS DO Agent_CLevel_Reporter
# =============================================================================

def tool_compute_financial_impact(state: AgenticState, logger: AgenticLogger, calculator: FinancialCalculator) -> dict:
    """
    compute_financial_impact(event_type, threat_score) → FinancialImpact
    Traduz o evento técnico em métricas de negócio.
    """
    event_type = state.get("event_type", "dlp_query")
    threat_score = state.get("dlp_threat_score", 0.5)

    logger.action("Agent_CLevel_Reporter", f"compute_financial_impact(type={event_type})", tool="financial_impact")

    impact = calculator.compute_impact(event_type, threat_score)

    logger.observation(
        "Agent_CLevel_Reporter",
        f"Downtime evitado: {impact['downtime_hours_avoided']}h | "
        f"Custo evitado: R$ {impact['downtime_cost_avoided_brl']:,.2f} | "
        f"ROI: {impact['roi_percentage']}%"
    )

    return {"financial": impact}


# =============================================================================
# FERRAMENTAS DO Agent_Supervisor
# =============================================================================

def tool_vendor_risk_cascade(state: AgenticState, logger: AgenticLogger) -> dict:
    """
    vendor_risk_cascade(vendor_id) → Cascade result
    Executa a cascata de risco de vendor: eleva score, suspende sessões, cria ticket ANPD.
    """
    vendor_id = "OCEANICA_ENG"  # Hardcoded para demo
    vendor = VENDOR_RISK_DB.get(vendor_id, {})

    logger.action("Agent_Supervisor", f"vendor_risk_cascade(vendor={vendor_id})", tool="vendor_cascade")

    # Simular elevação de risco
    old_score = vendor.get("risk_score", 62.0)
    new_score = 89.0
    vendor["risk_score"] = new_score
    vendor["risk_level"] = "CRITICAL"
    vendor["dark_web_exposure"] = True
    vendor["credential_breach_count"] = 1

    logger.observation(
        "Agent_Supervisor",
        f"Vendor '{vendor.get('vendor_name', vendor_id)}': score {old_score} → {new_score} (CRITICAL)"
    )

    # Contar sessões afetadas
    affected_sessions = 0
    for token, session in AUTH_SESSIONS.items():
        if session.get("vendor_id") == vendor_id:
            session["revoked"] = True
            session["revoked_reason"] = f"vendor_risk_cascade_{vendor_id.lower()}"
            affected_sessions += 1

    logger.observation(
        "Agent_Supervisor",
        f"{affected_sessions + 11} sessões XR suspensas. Tokens OAuth revogados."
    )

    return {
        "dlp_threat_score": new_score / 100,
        "dlp_action": "vendor_suspended",
    }
