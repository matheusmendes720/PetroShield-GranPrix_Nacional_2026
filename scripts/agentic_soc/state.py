"""
state.py — Definição Formal dos Estados do Grafo Agêntico PetroShield
=====================================================================
Implementa o TypedDict completo que flui pelo StateMachine (orchestrator.py).

Conceito: Cada transição no grafo lê e escreve neste estado compartilhado.
O estado é imutável por referência — cada nó retorna um PATCH (dict parcial)
que é mergeado no estado principal pelo motor de orquestração.

Estrutura inspirada no LangGraph StateGraph, reimplementada sem dependências.
"""

from typing import TypedDict, Optional, List, Dict, Any, Literal


# =============================================================================
# TIPOS ENUMERADOS (simulados como Literal para zero deps)
# =============================================================================

PhaseType = Literal[
    "IDLE",
    "MONITORING",
    "TRIAGING",
    "BLOCKING",
    "ESCALATING",
    "ANALYZING",
    "VACCINATING",
    "FLEET_SYNC",
    "REPORTING",
    "ALERT_HUMANO",
    "INCONCLUSIVE",
    "PARTIAL_SYNC",
    "RESOLVED",
]

SeverityType = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]

ActionType = Literal["allowed", "blocked", "escalated", "vendor_suspended"]


# =============================================================================
# ENTIDADES DE DOMÍNIO
# =============================================================================

class RedactedEntity(TypedDict):
    """Entidade sensível detectada e redatada pelo DLP Engine."""
    type: str               # "platform", "well", "cpf", "password", "scada_command", ...
    value: str              # Valor original capturado
    token: str              # Token de substituição (ex: [ATIVO_RESTRITO])
    classification: str     # "Estratégica", "Alta", "Crítica", "Média"


class ThreatIntelResult(TypedDict):
    """Resultado da análise de inteligência de ameaças (Agent_Intel_Cloud)."""
    ttp_id: str             # MITRE ATT&CK technique ID (ex: "T0817")
    ttp_name: str           # Nome legível (ex: "Drive-by Compromise")
    tactic: str             # Tática MITRE (ex: "Initial Access")
    confidence: float       # 0.0 a 1.0
    kill_chain: List[str]   # Cadeia de ataque inferida
    reasoning: str          # Chain-of-thought do agente (visível no TUI)


class VaccinePayload(TypedDict):
    """Assinatura de vacina gerada para propagação na frota."""
    hash: str               # SHA-256 da assinatura
    rule: str               # Regra de firewall/IDS gerada
    ports_blocked: List[int]
    protocol: str           # "SMB", "Modbus", "DNP3", "HTTP"
    ttp_source: str         # TTP que originou esta vacina
    generated_at: str       # Timestamp ISO 8601


class FleetNodeStatus(TypedDict):
    """Status de um Edge Node na frota após broadcast de vacina."""
    node_id: str
    facility: str
    region: str
    vaccine_applied: bool
    latency_ms: int
    retry_count: int


class FleetBroadcastReport(TypedDict):
    """Relatório de completude do broadcast de vacina para a frota."""
    total_nodes: int
    success: int
    failed: int
    partial: int
    nodes: List[FleetNodeStatus]
    broadcast_duration_ms: int


class FinancialImpact(TypedDict):
    """Métricas financeiras computadas pelo Agent_CLevel_Reporter."""
    downtime_hours_avoided: float
    downtime_cost_avoided_brl: float
    breach_recovery_avoided_brl: float
    roi_percentage: float
    compliance_status: str          # "LGPD: OK" | "ALERTA: Verificar Base"
    incidents_resolved: int
    fleet_coverage_pct: float


class AuditEntry(TypedDict):
    """Entrada no log de auditoria tamper-evident."""
    log_id: int
    session_id: Optional[str]
    device_id: str
    operator_id: Optional[str]
    original_query: str
    sanitized_query: str
    data_leak_prevented: bool
    redaction_count: int
    redacted_entities: List[RedactedEntity]
    threat_score: float
    anomaly_flags: List[str]
    operator_action: str
    mitre_technique: Optional[str]
    latency_ms: int
    prev_log_hash: str
    log_hash: str
    created_at: str


# =============================================================================
# ESTADO PRINCIPAL DO GRAFO AGÊNTICO
# =============================================================================

class AgenticState(TypedDict, total=False):
    """
    Estado global compartilhado por todos os nós do grafo.
    
    Cada nó (agente) lê o estado completo e retorna um dict parcial
    com as chaves que deseja atualizar. O motor de orquestração
    faz o merge: state = {**state, **node_output}
    
    Arquitetura inspirada em LangGraph MessagesState,
    reimplementada sem dependências externas.
    """
    
    # --- Controle de Fluxo ---
    phase: PhaseType                    # Estado atual no DFA
    previous_phase: PhaseType           # Estado anterior (para rollback)
    scene_id: str                       # Identificador da cena no teatro (ex: "cena_1")
    scene_title: str                    # Título legível (ex: "O Intruso")
    
    # --- Evento Sendo Processado ---
    event_type: str                     # "unauthorized_access" | "dlp_query" | "ot_command" | "vendor_cascade"
    event_source_device: str            # device_id do dispositivo de origem
    event_source_ip: str                # IP de origem simulado
    event_raw_query: str                # Query original (antes do DLP)
    event_timestamp: str                # Timestamp ISO 8601
    
    # --- Sessão e Autenticação ---
    session_id: Optional[str]           # ID da sessão (None se não autenticado)
    operator_id: Optional[str]          # ID do operador
    vendor_id: Optional[str]            # ID do vendor associado
    auth_status: str                    # "authenticated" | "unauthenticated" | "revoked"
    
    # --- Resultado do DLP Engine ---
    dlp_sanitized_query: str            # Query após sanitização
    dlp_entities: List[RedactedEntity]  # Entidades detectadas
    dlp_anomaly_flags: List[str]        # Flags de anomalia
    dlp_threat_score: float             # Score de ameaça (0.0 - 1.0)
    dlp_action: ActionType              # Ação tomada
    dlp_latency_ms: int                 # Latência do processamento DLP
    
    # --- Resultado da Inteligência de Ameaças ---
    threat_intel: ThreatIntelResult     # Classificação MITRE ATT&CK
    
    # --- Resultado da Vacina ---
    vaccine: VaccinePayload             # Assinatura de vacina gerada
    fleet_report: FleetBroadcastReport  # Relatório de broadcast
    
    # --- Resultado Financeiro ---
    financial: FinancialImpact          # Métricas financeiras
    
    # --- Cadeia de Raciocínio (Glass-Box) ---
    agent_trace: List[Dict[str, str]]   # [{"agent": "...", "type": "THOUGHT|ACTION|OBSERVATION", "content": "..."}]
    
    # --- Auditoria ---
    audit_entries: List[AuditEntry]     # Hash chain completa
    last_audit_hash: str                # Último hash da cadeia
    
    # --- Resposta LLM ---
    llm_response: Optional[str]         # Resposta do LLM privado (se aplicável)
    llm_provider: str                   # "azure-openai-private" | "mock"
    llm_model: str                      # "gpt-4o" | "mock-deterministic"


def create_initial_state() -> AgenticState:
    """Cria o estado inicial zerado do grafo agêntico."""
    return AgenticState(
        phase="IDLE",
        previous_phase="IDLE",
        scene_id="",
        scene_title="",
        event_type="",
        event_source_device="",
        event_source_ip="",
        event_raw_query="",
        event_timestamp="",
        session_id=None,
        operator_id=None,
        vendor_id=None,
        auth_status="unauthenticated",
        dlp_sanitized_query="",
        dlp_entities=[],
        dlp_anomaly_flags=[],
        dlp_threat_score=0.0,
        dlp_action="allowed",
        dlp_latency_ms=0,
        threat_intel=ThreatIntelResult(
            ttp_id="", ttp_name="", tactic="",
            confidence=0.0, kill_chain=[], reasoning=""
        ),
        vaccine=VaccinePayload(
            hash="", rule="", ports_blocked=[],
            protocol="", ttp_source="", generated_at=""
        ),
        fleet_report=FleetBroadcastReport(
            total_nodes=0, success=0, failed=0, partial=0,
            nodes=[], broadcast_duration_ms=0
        ),
        financial=FinancialImpact(
            downtime_hours_avoided=0.0,
            downtime_cost_avoided_brl=0.0,
            breach_recovery_avoided_brl=0.0,
            roi_percentage=0.0,
            compliance_status="LGPD: OK",
            incidents_resolved=0,
            fleet_coverage_pct=0.0,
        ),
        agent_trace=[],
        audit_entries=[],
        last_audit_hash="genesis",
        llm_response=None,
        llm_provider="mock",
        llm_model="mock-deterministic",
    )
