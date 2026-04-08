import json
import random
from typing import Dict, Any

class EconometricRiskEngine:
    """
    Motor de Cyber-Econometria para o GP SENAI 2026.
    Converte achados técnicos brutos (OSINT/Dorks) em métricas de 
    Risco Financeiro (VaR) e passivos de balanço (C-Level).
    """

    def __init__(self, company_annual_revenue: float, industry_avg_breach_cost: float = 5560000.0):
        self.revenue = company_annual_revenue
        # IBM Report 2024: Manufacturing Avg Breach Cost (USD)
        self.avg_breach_cost = industry_avg_breach_cost
        
        # Parâmetros de Custo Base no Brasil (Estimativas para ROI)
        self.lgpd_fine_per_record = 164.0 * 5.5 # USD 164 convertido a BRL (Aprox)
        self.downtime_cost_per_hour = (self.revenue / 252) / 24 # Baseado em dias úteis
    
    def calculate_downtime_risk(self, exposed_ics_ports: int) -> float:
        """
        Cada porta Industrial/SCADA exposta representa um risco percentual
        de downtime na esteira de produção.
        """
        # Ex: Risco de 12 horas de parada se houver exposição
        if exposed_ics_ports == 0:
            return 0.0
        
        hours_at_risk = 12 * (1 + (exposed_ics_ports * 0.1))
        return round(hours_at_risk * self.downtime_cost_per_hour, 2)
    
    def calculate_lgpd_liability(self, leaked_credentials: int) -> float:
        """
        Passivo atuarial de multas LGPD baseado no tamanho do vazamento.
        """
        return round(leaked_credentials * self.lgpd_fine_per_record, 2)
    
    def calculate_capex_opex_inefficiency(self, shadow_it_instances: int) -> float:
        """
        Dinheiro queimado em infraestruturas perdidas/esquecidas na nuvem
        Custo médio anual de instância perdida: R$ 12.000,00
        """
        return round(shadow_it_instances * 12000.0, 2)

    def process_osint_feed(self, osint_data_file: str) -> Dict[str, Any]:
        """
        Lê o output do Dorking Engine (JSON) e gera o relatório financeiro C-Level.
        Neste mockup, usamos valores simulados baseados na tese se não houver arquivo real.
        """
        # Mocking or reading raw OSINT data
        try:
            with open(osint_data_file, 'r') as f:
                raw_intel = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Fallback data se o dorking engine não rodou
            raw_intel = {
                "exposed_ics_ports": random.randint(1, 5),
                "leaked_credentials": random.randint(100, 5000),
                "shadow_it_instances": random.randint(3, 15)
            }
        
        # Cálculos Econômicos
        downtime_risk = self.calculate_downtime_risk(raw_intel.get("exposed_ics_ports", 0))
        lgpd_risk = self.calculate_lgpd_liability(raw_intel.get("leaked_credentials", 0))
        capex_waste = self.calculate_capex_opex_inefficiency(raw_intel.get("shadow_it_instances", 0))
        
        total_value_at_risk = downtime_risk + lgpd_risk + capex_waste
        
        roi_report = {
            "financial_risk_profile": {
                "total_circulating_liability_brl": total_value_at_risk,
                "downtime_exposure_brl": downtime_risk,
                "compliance_lgpd_risk_brl": lgpd_risk,
                "capex_opex_inefficiency_brl": capex_waste
            },
            "technical_triggers": raw_intel,
            "executive_summary": f"Exposição Crítica: Mitigação imediata com nossa solução pode salvar R$ {total_value_at_risk:,.2f} no balanço fiscal deste ano."
        }
        
        return roi_report

if __name__ == "__main__":
    # Exemplo: Empresa parceira faturou R$ 500 milhões / ano.
    engine = EconometricRiskEngine(company_annual_revenue=500_000_000)
    
    report = engine.process_osint_feed("raw_osint.json")
    
    with open("c_level_dashboard_feed.json", "w") as out:
        json.dump(report, out, indent=4, ensure_ascii=False)
    
    print("📈 [ECONOMETRIA AGRESSIVA] Concluído!")
    print(report["executive_summary"])
