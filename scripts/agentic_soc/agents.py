"""
agents.py — Definição dos 5 Agentes PetroShield
=================================================
Cada agente é uma função que:
  1. Recebe o AgenticState completo
  2. Executa raciocínio THOUGHT → ACTION → OBSERVATION (ReAct pattern)
  3. Retorna um dict (patch) para merge no estado
  4. Logueia cada passo no AgenticLogger

O grafo orquestra esses agentes via StateMachine (orchestrator.py).
O OpenAIBridge fornece raciocínio LLM no modo live.

Hierarquia de agentes:
  Agent_Supervisor
  ├── Agent_DLP_Edge
  ├── Agent_Intel_Cloud  
  ├── Agent_Fleet_Vaccinator
  └── Agent_CLevel_Reporter
"""

import time
from typing import Dict, Callable, Any

from .state import AgenticState, create_initial_state
from .logger import AgenticLogger
from .openai_bridge import OpenAIBridge
from .financial_model import FinancialCalculator
from .mock_data import XR_DEVICES, AUTH_SESSIONS, VENDOR_RISK_DB
from .tools import (
    tool_inspect_packet,
    tool_block_request,
    tool_isolate_subnet,
    tool_query_mitre_ics,
    tool_generate_vaccine,
    tool_broadcast_vaccine,
    tool_compute_financial_impact,
    tool_vendor_risk_cascade,
)
from .dlp_engine import create_audit_entry


# =============================================================================
# SYSTEM PROMPTS DOS AGENTES
# =============================================================================

SYSTEM_PROMPTS = {
    "supervisor": (
        "Você é o Agent_Supervisor do PetroShield AxeGuard — SOC Agêntico para "
        "infraestrutura industrial crítica. Sua função é:\n"
        "1. Receber eventos de segurança de dispositivos XR (HoloLens, RealWear, etc.)\n"
        "2. Validar autenticação e sessão\n"
        "3. Rotear o evento para o agente especializado correto\n"
        "4. Monitorar o progresso e decidir next steps\n"
        "Priorize velocidade de resposta e proteção de dados classificados Petrobras."
    ),
    "dlp_edge": (
        "Você é o Agent_DLP_Edge — primeira linha de defesa contra vazamento de dados. "
        "Sua responsabilidade é inspecionar CADA query de LLM que passa pelo perímetro e:\n"
        "1. Detectar entidades sensíveis (plataformas, poços, CPFs, comandos SCADA)\n"
        "2. Redatar essas entidades antes que cheguem ao LLM cloud\n"
        "3. Calcular o threat score da query\n"
        "4. Decidir: PERMITIR (com redação) | BLOQUEAR | ESCALAR\n"
        "Latência máxima permitida: 50ms."
    ),
    "intel_cloud": (
        "Você é o Agent_Intel_Cloud — analista de inteligência de ameaças cibernéticas. "
        "Quando recebe um evento escalado, sua função é:\n"
        "1. Classificar o vetor de ataque usando MITRE ATT&CK for ICS\n"
        "2. Inferir a kill chain provável\n"
        "3. Gerar uma assinatura de vacina para evitar ataques similares\n"
        "4. Prover chain-of-thought visível (Glass-Box Intelligence)\n"
        "Você tem acesso à base MITRE ICS e pode gerar regras de firewall."
    ),
    "fleet_vaccinator": (
        "Você é o Agent_Fleet_Vaccinator — responsável pela propagação de vacinas "
        "de segurança para toda a frota de Edge Nodes PetroShield. Sua função é:\n"
        "1. Receber uma assinatura de vacina do Agent_Intel_Cloud\n"
        "2. Fazer broadcast para todos os 14 Edge Nodes da frota\n"
        "3. Coletar ACK de cada node (com retry exponencial para nodes offline)\n"
        "4. Reportar cobertura da frota\n"
        "Tolerância zero para propagação parcial: se < 80%, escalar."
    ),
    "clevel_reporter": (
        "Você é o Agent_CLevel_Reporter — tradutor técnico→executivo. "
        "Sua função é pegar cada incidente técnico e convertê-lo em:\n"
        "1. Horas de downtime evitado\n"
        "2. Custo financeiro evitado (R$)\n"
        "3. ROI sobre a assinatura PetroShield\n"
        "4. Status de conformidade (LGPD, ANPD, ANP 882)\n"
        "Seu output alimenta o Dashboard Executivo em tempo real."
    ),
}


def create_agents(
    logger: AgenticLogger,
    bridge: OpenAIBridge,
    calculator: FinancialCalculator,
) -> Dict[str, Callable]:
    """
    Factory que cria os 5 agentes como funções de nó do grafo.
    
    Cada agente é um closure que captura (logger, bridge, calculator)
    e recebe (state: dict) como argumento do StateMachine.
    
    Retorna: Dict[nome -> fn(state) -> patch]
    """

    # =========================================================================
    # Agent_Supervisor — Router principal
    # =========================================================================
    def agent_supervisor(state: dict) -> dict:
        """Nó de entrada: valida, autentica e roteia o evento."""
        phase = state.get("phase", "IDLE")

        logger.thought(
            "Agent_Supervisor",
            f"Evento recebido: type={state.get('event_type')} "
            f"device={state.get('event_source_device')} "
            f"phase_current={phase}"
        )

        # Verificar autenticação
        device_id = state.get("event_source_device", "")
        device_info = XR_DEVICES.get(device_id, {})
        auth_token = state.get("session_id")

        # Evento de vendor cascade é especial — não precisa de device
        if state.get("event_type") == "vendor_cascade":
            logger.thought(
                "Agent_Supervisor",
                "Evento de vendor_cascade detectado. Roteando diretamente para análise de risco."
            )
            return {
                "phase": "TRIAGING",
                "previous_phase": phase,
                "auth_status": "N/A",
            }

        if auth_token and auth_token in AUTH_SESSIONS:
            session = AUTH_SESSIONS[auth_token]
            if session.get("revoked"):
                logger.thought("Agent_Supervisor", f"Sessão {auth_token} REVOGADA. Blocking.")
                return {
                    "phase": "BLOCKING",
                    "previous_phase": phase,
                    "auth_status": "revoked",
                    "operator_id": session.get("operator_id"),
                    "vendor_id": session.get("vendor_id"),
                }

            logger.thought(
                "Agent_Supervisor",
                f"Sessão válida: operator={session['operator_id']}, "
                f"vendor={session.get('vendor_id', 'N/A')}, MFA={session.get('mfa_verified')}"
            )
            return {
                "phase": "MONITORING",
                "previous_phase": phase,
                "auth_status": "authenticated",
                "session_id": session["session_id"],
                "operator_id": session["operator_id"],
                "vendor_id": session.get("vendor_id"),
            }
        else:
            # Device não-autenticado
            mdm_status = device_info.get("mdm_enrollment_status", "unknown")
            logger.thought(
                "Agent_Supervisor",
                f"ALERTATION: Device {device_id} SEM sessão válida. "
                f"MDM status: {mdm_status}. Roteando para BLOQUEIO."
            )
            return {
                "phase": "BLOCKING",
                "previous_phase": phase,
                "auth_status": "unauthenticated",
            }

    # =========================================================================
    # Agent_DLP_Edge — Pipeline DLP 3 estágios
    # =========================================================================
    def agent_dlp_edge(state: dict) -> dict:
        """Pipeline DLP: REDACT → SCORE → DECIDE."""
        logger.thought(
            "Agent_DLP_Edge",
            f"Inspecionando query do device {state.get('event_source_device')}..."
        )

        # Executar ferramenta de inspeção
        dlp_result = tool_inspect_packet(state, logger)

        # Criar entrada de auditoria
        entry = create_audit_entry(
            log_id=len(state.get("audit_entries", [])) + 1,
            session_id=state.get("session_id", "N/A"),
            device_id=state.get("event_source_device", ""),
            operator_id=state.get("operator_id", "N/A"),
            original_query=state.get("event_raw_query", ""),
            dlp_result=dlp_result,
            previous_hash=state.get("last_audit_hash", "genesis"),
        )

        audit_entries = list(state.get("audit_entries", []))
        audit_entries.append(entry)

        # Determinar fase baseado na ação do DLP
        action = dlp_result["dlp_action"]
        if action == "blocked":
            next_phase = "BLOCKING"
        elif action == "escalated":
            next_phase = "ESCALATING"
        else:
            next_phase = "ANALYZING"

        logger.phase_transition(state.get("phase", "MONITORING"), next_phase, reason=f"dlp_action={action}")

        return {
            **dlp_result,
            "phase": next_phase,
            "previous_phase": state.get("phase", "MONITORING"),
            "audit_entries": audit_entries,
            "last_audit_hash": entry["log_hash"],
        }

    # =========================================================================
    # Agent_Intel_Cloud — Análise MITRE + Vacina
    # =========================================================================
    def agent_intel_cloud(state: dict) -> dict:
        """Análise de inteligência: classificação MITRE + geração de vacina."""
        logger.thought(
            "Agent_Intel_Cloud",
            f"Analisando ameaça escalada. Threat score: {state.get('dlp_threat_score', 0)}"
        )

        # Usar OpenAI Bridge (mock ou live) para reasoning
        scenario_key = "analyze_threat_ot" if "ot_protocol_detected" in state.get("dlp_anomaly_flags", []) else "analyze_threat_auth"
        llm_result = bridge.reason(
            system_prompt=SYSTEM_PROMPTS["intel_cloud"],
            user_context=f"Analise o evento: {state.get('event_raw_query', '')}",
            scenario_key=scenario_key,
        )

        # Loggar cadeia de pensamento do LLM
        if "thought" in llm_result:
            logger.thought("Agent_Intel_Cloud", llm_result["thought"])
        if "classification" in llm_result:
            for line in llm_result["classification"].split("\n"):
                if line.strip():
                    logger.observation("Agent_Intel_Cloud", line.strip())

        # Executar ferramentas
        mitre_result = tool_query_mitre_ics(state, logger)
        state_with_mitre = {**state, **mitre_result}

        vaccine_result = tool_generate_vaccine(state_with_mitre, logger)

        # Log da vacina
        if "vaccine" in llm_result:
            for line in llm_result["vaccine"].split("\n"):
                if line.strip():
                    logger.observation("Agent_Intel_Cloud", line.strip())

        return {
            **mitre_result,
            **vaccine_result,
            "phase": "VACCINATING",
            "previous_phase": state.get("phase", "ESCALATING"),
            "llm_provider": bridge.mode,
            "llm_model": bridge.model,
        }

    # =========================================================================
    # Agent_Fleet_Vaccinator — Broadcast de vacina
    # =========================================================================
    def agent_fleet_vaccinator(state: dict) -> dict:
        """Propaga vacina para toda a frota de Edge Nodes."""
        logger.thought(
            "Agent_Fleet_Vaccinator",
            f"Preparando broadcast de vacina. Hash: {state.get('vaccine', {}).get('hash', 'N/A')[:32]}..."
        )

        result = tool_broadcast_vaccine(state, logger)

        # Determinar fase baseado na completude
        report = result.get("fleet_report", {})
        coverage = report.get("success", 0) / max(report.get("total_nodes", 1), 1) * 100

        if coverage >= 80:
            next_phase = "REPORTING"
        else:
            next_phase = "PARTIAL_SYNC"
            logger.error(
                "Agent_Fleet_Vaccinator",
                f"Cobertura insuficiente: {coverage:.0f}% (mínimo: 80%). Escalando para SOC humano."
            )

        logger.phase_transition(state.get("phase", "VACCINATING"), next_phase, reason=f"coverage={coverage:.0f}%")

        return {
            **result,
            "phase": next_phase,
            "previous_phase": state.get("phase", "VACCINATING"),
        }

    # =========================================================================
    # Agent_CLevel_Reporter — Tradução técnico→financeiro
    # =========================================================================
    def agent_clevel_reporter(state: dict) -> dict:
        """Converte eventos técnicos em métricas executivas."""
        logger.thought(
            "Agent_CLevel_Reporter",
            "Traduzindo evento técnico para linguagem de negócio..."
        )

        result = tool_compute_financial_impact(state, logger, calculator)

        # Sumário acumulado
        summary = calculator.cumulative_summary
        logger.metric("Custo Total Evitado (acumulado)", summary["formatted_cost_avoided"])
        logger.metric("ROI vs. Assinatura", f"{summary['roi_vs_subscription']}%")
        logger.metric("Incidentes Resolvidos", summary["total_incidents_resolved"])

        return {
            **result,
            "phase": "RESOLVED",
            "previous_phase": state.get("phase", "REPORTING"),
        }

    # =========================================================================
    # Blocker — Nó terminal de bloqueio
    # =========================================================================
    def agent_blocker(state: dict) -> dict:
        """Executa bloqueio e encerra o fluxo."""
        tool_block_request(state, logger)

        # Criar audit entry para bloqueio
        from .dlp_engine import DLPEngine
        dlp = DLPEngine()
        dlp_result = dlp.full_pipeline(
            state.get("event_raw_query", ""),
            has_session=state.get("auth_status") == "authenticated",
        )

        entry = create_audit_entry(
            log_id=len(state.get("audit_entries", [])) + 1,
            session_id=state.get("session_id", "N/A"),
            device_id=state.get("event_source_device", ""),
            operator_id=state.get("operator_id", "N/A"),
            original_query=state.get("event_raw_query", ""),
            dlp_result=dlp_result,
            previous_hash=state.get("last_audit_hash", "genesis"),
        )

        audit_entries = list(state.get("audit_entries", []))
        audit_entries.append(entry)

        return {
            **dlp_result,
            "phase": "RESOLVED",
            "audit_entries": audit_entries,
            "last_audit_hash": entry["log_hash"],
        }

    # =========================================================================
    # Vendor Risk Cascade — Nó especial
    # =========================================================================
    def agent_vendor_cascade(state: dict) -> dict:
        """Executa cascata de risco de vendor."""
        result = tool_vendor_risk_cascade(state, logger)
        return {
            **result,
            "phase": "VACCINATING",
            "previous_phase": "TRIAGING",
        }

    return {
        "supervisor": agent_supervisor,
        "dlp_edge": agent_dlp_edge,
        "intel_cloud": agent_intel_cloud,
        "fleet_vaccinator": agent_fleet_vaccinator,
        "clevel_reporter": agent_clevel_reporter,
        "blocker": agent_blocker,
        "vendor_cascade": agent_vendor_cascade,
    }


# =============================================================================
# ROUTER DO SUPERVISOR — Roteamento Condicional
# =============================================================================

def supervisor_router(state: dict) -> str:
    """
    Função de roteamento condicional do Agent_Supervisor.
    
    Decide o próximo nó baseado no estado:
      phase = BLOCKING → blocker
      phase = MONITORING → dlp_edge
      phase = TRIAGING (vendor_cascade) → vendor_cascade
    """
    from .orchestrator import END

    phase = state.get("phase", "IDLE")
    event_type = state.get("event_type", "")

    if phase == "BLOCKING":
        return "blocker"
    elif phase == "TRIAGING" and event_type == "vendor_cascade":
        return "vendor_cascade"
    elif phase == "MONITORING":
        return "dlp_edge"
    else:
        return "blocker"


def dlp_router(state: dict) -> str:
    """
    Roteamento após DLP:
      ESCALATING → intel_cloud
      BLOCKING → blocker
      ANALYZING → clevel_reporter (query permitida, reportar metrics)
    """
    from .orchestrator import END

    phase = state.get("phase", "")

    if phase == "ESCALATING":
        return "intel_cloud"
    elif phase == "BLOCKING":
        return "blocker"
    elif phase == "ANALYZING":
        return "clevel_reporter"
    else:
        return END


def fleet_router(state: dict) -> str:
    """
    Roteamento após Fleet Vaccinator:
      REPORTING → clevel_reporter
      PARTIAL_SYNC → clevel_reporter (com alerta)
    """
    return "clevel_reporter"
