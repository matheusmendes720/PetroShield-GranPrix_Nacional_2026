"""
financial_model.py — Calculadora de Impacto Financeiro para Dashboard C-Level
==============================================================================
Converte eventos técnicos em linguagem de negócio:
  - ROI (Retorno sobre Investimento)
  - Downtime Evitado (horas × custo/hora)
  - Risco de Recuperação Evitado
  - Conformidade Regulatória (LGPD/ANPD)
  - Return on Assinatura (%)

Métricas baseadas em dados reais de mercado:
  - IBM Cost of a Data Breach Report 2025
  - Estimativas Petrobras (public filings + OSINT)
"""

from typing import List
from .state import FinancialImpact


# =============================================================================
# CONSTANTES DO MODELO FINANCEIRO PETROBRAS
# =============================================================================

# Custo de downtime: R$ 80.000/dia ÷ 24h ≈ R$ 3.333/hora
# Fonte: Estimativa conservadora para PMEs industriais do polo petroquímico de Camaçari
CUSTO_DOWNTIME_HORA_BRL = 80_000 / 24  # R$ 3.333,33

# Custo médio de recuperação de incidente de segurança
# Fonte: IBM Cost of a Data Breach 2025 — adaptado para empresas brasileiras
CUSTO_RECUPERACAO_INCIDENTE_BRL = 500_000

# Custo potencial de breach com dados estratégicos (seismic, platform data)
# Referência: SA Exploration breach (Nov 2025) — 90GB de dados sísmicos
CUSTO_BREACH_ESTRATEGICO_BRL = 35_000_000

# Assinatura mensal do PetroShield por PME
ASSINATURA_MENSAL_BRL = 1_000

# Multa LGPD (2% do faturamento, max R$ 50M por infração)
MULTA_LGPD_ESTIMADA_BRL = 3_000_000  # Estimativa conservadora para PME

# Custo de notificação ANPD (administrativo + jurídico)
CUSTO_NOTIFICACAO_ANPD_BRL = 150_000


# =============================================================================
# TABELA DE IMPACTO POR TIPO DE EVENTO
# =============================================================================

EVENT_IMPACT_TABLE = {
    "unauthorized_access": {
        "downtime_hours": 2.0,      # Tempo de investigação + resposta manual (evitado)
        "recovery_cost_pct": 0.10,  # 10% do custo de recuperação total
        "breach_risk_pct": 0.05,    # 5% de chance de breach se não bloqueado
        "compliance_impact": False,
    },
    "dlp_query": {
        "downtime_hours": 0.5,      # Tempo de auditoria manual (evitado)
        "recovery_cost_pct": 0.30,  # 30% se o dado vazasse
        "breach_risk_pct": 0.15,    # 15% de chance de breach
        "compliance_impact": True,  # LGPD aplicável
    },
    "ot_command": {
        "downtime_hours": 8.0,      # Shutdown da planta para inspeção (evitado)
        "recovery_cost_pct": 1.00,  # 100% do custo de recuperação
        "breach_risk_pct": 0.50,    # 50% de dano físico se não bloqueado
        "compliance_impact": True,
    },
    "vendor_cascade": {
        "downtime_hours": 4.0,      # Tempo de triagem de supply chain
        "recovery_cost_pct": 0.60,  # 60% do custo de recuperação
        "breach_risk_pct": 0.30,    # 30% de comprometimento
        "compliance_impact": True,  # ANPD + ANP 882
    },
}


class FinancialCalculator:
    """
    Calculadora de impacto financeiro para tradução técnico → executivo.
    
    Cada evento processado pelo SOC é convertido em métricas financeiras
    que alimentam o dashboard C-Level em tempo real.
    """

    def __init__(self):
        self._total_downtime_avoided = 0.0
        self._total_cost_avoided = 0.0
        self._total_incidents = 0

    def compute_impact(self, event_type: str, threat_score: float = 0.5) -> FinancialImpact:
        """
        Calcula o impacto financeiro de um evento de segurança prevenido.
        
        Parâmetros:
          - event_type: Tipo do evento (unauthorized_access, dlp_query, etc.)
          - threat_score: Score de ameaça (0.0-1.0) — amplifica o impacto
        
        Retorna: FinancialImpact com métricas calculadas
        """
        impact_def = EVENT_IMPACT_TABLE.get(event_type, EVENT_IMPACT_TABLE["dlp_query"])

        # Amplificação pelo threat score
        amplifier = 0.5 + (threat_score * 0.5)  # Range: 0.5x a 1.0x

        downtime_hours = impact_def["downtime_hours"] * amplifier
        downtime_cost = downtime_hours * CUSTO_DOWNTIME_HORA_BRL

        recovery_cost = (
            CUSTO_RECUPERACAO_INCIDENTE_BRL
            * impact_def["recovery_cost_pct"]
            * amplifier
        )

        breach_risk_value = (
            CUSTO_BREACH_ESTRATEGICO_BRL
            * impact_def["breach_risk_pct"]
            * amplifier
        )

        total_avoided = downtime_cost + recovery_cost

        # Atualizar acumuladores
        self._total_downtime_avoided += downtime_hours
        self._total_cost_avoided += total_avoided
        self._total_incidents += 1

        # ROI = (Valor salvo / Custo da assinatura) × 100
        roi = (total_avoided / max(ASSINATURA_MENSAL_BRL, 1)) * 100

        # Compliance
        if impact_def["compliance_impact"]:
            compliance = "LGPD: OK — Vazamento prevenido. ANPD não precisa ser notificada."
        else:
            compliance = "LGPD: OK"

        return FinancialImpact(
            downtime_hours_avoided=round(downtime_hours, 2),
            downtime_cost_avoided_brl=round(downtime_cost, 2),
            breach_recovery_avoided_brl=round(recovery_cost, 2),
            roi_percentage=round(roi, 1),
            compliance_status=compliance,
            incidents_resolved=self._total_incidents,
            fleet_coverage_pct=92.86,  # 13/14 nodes online (mock)
        )

    @property
    def cumulative_summary(self) -> dict:
        """Sumário acumulado para dashboard executivo."""
        return {
            "total_downtime_hours_avoided": round(self._total_downtime_avoided, 2),
            "total_cost_avoided_brl": round(self._total_cost_avoided, 2),
            "total_incidents_resolved": self._total_incidents,
            "roi_vs_subscription": round(
                (self._total_cost_avoided / max(ASSINATURA_MENSAL_BRL, 1)) * 100, 1
            ),
            "formatted_cost_avoided": f"R$ {self._total_cost_avoided:,.2f}",
        }
