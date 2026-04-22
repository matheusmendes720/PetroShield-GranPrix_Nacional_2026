import type { ThreatEvent } from './types';

/**
 * @const MOCK_THREATS
 * Conjunto de dados sintéticos de alta fidelidade para simulação de incidentes.
 */
export const MOCK_THREATS: ThreatEvent[] = [
  { id: 'TH-001', timestamp: new Date().toISOString(), source: 'Nó_Borda_Camaçari_VLAN40', type: 'MOVIMENTAÇÃO_LATERAL_SCADA', severity: 'CRITICAL', description: 'Movimentação lateral detectada visando PLC Siemens S7-1500.', mitigationSteps: ['Edge_DLP: Bloquear portas TCP 102.', 'Supervisor: Isolar VLAN 40.', 'RAG_Intel: Mapear tática MITRE T0801.', 'Recovery_Engine: Rotação de chaves.', 'Threat_Hunter: Varrear nós adjacentes.'] },
  { id: 'TH-002', timestamp: new Date().toISOString(), source: 'Refinaria_Abreu_e_Lima_WAN', type: 'BEACONING_RANSOMWARE', severity: 'HIGH', description: 'Tráfego C2 detectado para proxies LockBit 3.0.', mitigationSteps: ['Edge_DLP: Bloquear IPs de destino.', 'Threat_Hunter: Localizar processo pai.', 'RAG_Intel: Cruzar IoCs.', 'Recovery_Engine: Isolar endpoint.', 'CLevel_Reporter: Emitir alerta.'] },
  { id: 'TH-003', timestamp: new Date().toISOString(), source: 'Bacia_de_Santos_FPSO_IoT', type: 'EXFILTRAÇÃO_DLP', severity: 'MEDIUM', description: 'Volume atípico de saída de dados do servidor de modelagem.', mitigationSteps: ['Edge_DLP: Traffic Shaping.', 'Supervisor: Suspender credenciais.', 'Threat_Hunter: Analisar logs.', 'RAG_Intel: Verificar PII.', 'CLevel_Reporter: Avaliar LGPD.'] },
  { id: 'TH-004', timestamp: new Date().toISOString(), source: 'Gateway_E-mail_VP_Corporativo', type: 'PHISHING_IA_APRIMORADO', severity: 'HIGH', description: 'Spear-phishing visando C-Level com deepfake de voz clonada.', mitigationSteps: ['Supervisor: Revogar tokens.', 'Edge_DLP: Bloquear URLs.', 'RAG_Intel: Sandbox analysis.', 'CLevel_Reporter: Comunicação de crise.', 'Recovery_Engine: MFA reforçado.'] },
  { id: 'TH-005', timestamp: new Date().toISOString(), source: 'Infraestrutura_Cloud_Azure_BR', type: 'CRIPTOMINERAÇÃO_LATERAL', severity: 'LOW', description: 'Aumento de 400% em CPU em pods Kubernetes.', mitigationSteps: ['Supervisor: Identificar pods.', 'Edge_DLP: Bloquear pools.', 'Recovery_Engine: Reconstruir nodes.', 'Threat_Hunter: Investigar credencial.', 'RAG_Intel: Auditar RBAC.'] },
];

export const AGENT_LIST = [
  'Supervisor', 'Edge_DLP', 'RAG_Intel', 'CLevel_Reporter', 'Threat_Hunter', 'Recovery_Engine'
];
