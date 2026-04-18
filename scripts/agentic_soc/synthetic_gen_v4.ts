/**
 * AxeGuard Engine v4.2 - Synthetic Data Generator (PT-BR)
 * Gerador de dados de alta fidelidade para o PetroShield SOC.
 */

export interface ThreatLog {
    timestamp: string;
    level: 'INFO' | 'WARN' | 'CRITICAL' | 'SUCCESS';
    node: string;
    message: string;
    action?: string;
    financial_impact?: number; // ROI prevented in Millions
    dpi_details?: string;      // Packet hex dump / anomaly tag
}

export interface AgentDialogue {
    agent: 'SUPERVISOR_V2' | 'DLP_GUARDIAN' | 'INTEL_HUNTER' | 'IMMUNIZER_X';
    text: string;
    threat_ref?: string;
}

const NODES = ['Camaçari-01', 'Camaçari-02', 'Feira-01', 'Poço-Tupi-10', 'RLAM-Refinaria'];
const ACTIONS = ['BLOQUEADO', 'ANALISANDO', 'IMUNIZADO', 'ESCALADO'];

const LOG_MESSAGES = [
    'Tentativa de movimentação lateral via SMB detectada.',
    'Escaneamento de portas UDP originado de IP externo não autorizado.',
    'Assinatura de ransomware LockBit v3.0 identificada em payload.',
    'Tráfego anômalo em protocolo industrial Modbus/TCP.',
    'Tentativa de acesso não autorizado à API de controle de válvulas.',
    'Deteccção de vazamento de dados sensíveis (Matrícula Petrobras).',
    'Exfiltração de logs de auditoria via túnel DNS.',
    'Execução de script PowerShell obscuro em node de monitoramento.'
];

const AGENT_TALKS: Record<string, string[]> = {
    'DLP_GUARDIAN': [
        "Identifiquei um padrão de exfiltração em massa no dispositivo ${node}. DPI aponta túnel DNS.",
        "Anomalia crítica no protocolo OT detectada. Payload Modbus malformado interceptado.",
        "Vazamento de dados (CPF/Matrícula) detectado em headset RealWear. Bloqueio preventivo ativado."
    ],
    'INTEL_HUNTER': [
        "Cruzando dados com base MITRE... Técnica T1021.002 (SMB Lateral Movement) identificada.",
        "Variante 'PetroShield-Killer' detectada em base Búzios. Assinatura de ameaça atualizada.",
        "RAG Intel: recomendação de isolamento imediato para prevenir parada de produção de $10M/dia."
    ],
    'SUPERVISOR_V2': [
        "Incidente de Nível 3 em progresso na planta ${node}. Iniciando protocolo de contenção.",
        "Ordem direta: IMMUNIZER_X, dispare o broadcast de regras de firewall para toda a frota.",
        "Ação agentica concluída com sucesso. Risco financeiro mitigado em R$ ${val}M."
    ],
    'IMMUNIZER_X': [
        "Gerando vacina digital v4.21 para o node ${node}. Remediando vulnerabilidade DNP3.",
        "Broadcast de regras de borda concluído. 100% dos dispositivos edge imunizados.",
        "Ameaça neutralizada. O isolamento lógico impediu o comprometimento do PLC central."
    ]
};

export class SyntheticDataEngine {
    static generateLog(): ThreatLog {
        const node = NODES[Math.floor(Math.random() * NODES.length)];
        return {
            timestamp: new Date().toISOString(),
            level: Math.random() > 0.8 ? 'CRITICAL' : (Math.random() > 0.5 ? 'WARN' : 'INFO'),
            node,
            message: LOG_MESSAGES[Math.floor(Math.random() * LOG_MESSAGES.length)],
            action: ACTIONS[Math.floor(Math.random() * ACTIONS.length)]
        };
    }

    static generateDialogue(agentKey: string, node?: string): AgentDialogue {
        const agent = agentKey as keyof typeof AGENT_TALKS;
        const choices = AGENT_TALKS[agent];
        const msg = choices[Math.floor(Math.random() * choices.length)];
        const val = (Math.random() * 5 + 1).toFixed(1);
        
        return {
            agent: agent as any,
            text: msg.replace('${node}', node || 'PLATAFORMA-74')
                     .replace('${val}', val)
        };
    }

    static generateMetricsMatrix() {
        return Array.from({ length: 12 }, (_, i) => ({
            month: `2026-0${i+1}`,
            downtime_prevented: Math.floor(Math.random() * 500),
            threats_neutralized: Math.floor(Math.random() * 1500),
            mitigated_loss: (Math.random() * 10).toFixed(2) // em Milhões de Reais
        }));
    }
}
