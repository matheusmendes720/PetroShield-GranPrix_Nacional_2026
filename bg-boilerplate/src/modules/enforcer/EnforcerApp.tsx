/**
 * EnforcerApp — Módulo AxeGuard Multi-Agent Shell.
 * Removida dependência do GoogleGenAI — análise usa modo heurístico local.
 * Gerado automaticamente para deploy estático.
 */
import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  Shield, Terminal, AlertTriangle, Cpu, Lock, Activity,
  Database, CheckCircle2, Globe
} from 'lucide-react';
import type { SOCPhase, SOCState, LogEntry, ThreatEvent } from './types';
import { MOCK_THREATS, AGENT_LIST } from './simulationData';

/* ─── Componentes de Interface ─── */

const AxeTorch = () => (
  <div className="relative w-8 h-12 mx-auto">
    <motion.div
      className="absolute bottom-0 w-full h-full rounded-full"
      style={{ background: 'radial-gradient(ellipse at center bottom, #ffb000 0%, #ff3e3e 50%, transparent 70%)' }}
      animate={{ opacity: [0.6, 1, 0.6], scale: [0.95, 1.05, 0.95] }}
      transition={{ duration: 1.5, repeat: Infinity }}
    />
  </div>
);

const TerminalWindow = ({ logs }: { logs: LogEntry[] }) => {
  const scrollRef = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (scrollRef.current) scrollRef.current.scrollTop = scrollRef.current.scrollHeight;
  }, [logs]);

  return (
    <div className="flex flex-col h-full bg-black/60 border border-border-dim rounded-lg overflow-hidden">
      <div className="flex items-center gap-2 px-3 py-2 border-b border-border-dim text-[10px] font-mono text-accent-green/70">
        <Terminal className="w-3 h-3" /> AxeGuard_Orchestrator_v2.0
        <span className="ml-auto text-cyber-red text-[8px] animate-pulse">[LIVE]</span>
      </div>
      <div ref={scrollRef} className="flex-1 overflow-y-auto p-3 space-y-0.5 text-[10px] font-mono">
        {logs.map((log) => {
          let textColor = 'text-white';
          if (log.type === 'agent') textColor = 'text-amber-400';
          if (log.type === 'alert') textColor = 'text-cyber-red font-bold';
          if (log.type === 'tool') textColor = 'text-cyber-cyan italic';
          if (log.type === 'rag') textColor = 'text-purple-400';
          if (log.type === 'system') textColor = 'text-matrix-green/70';
          return (
            <motion.div key={log.id} initial={{ opacity: 0 }} animate={{ opacity: 1 }} className={`${textColor} leading-relaxed`}>
              <span className="text-white/20">[{log.timestamp}]</span>{' '}
              <span className="text-white/30">[{log.agent}]</span>{' '}
              {log.message}
            </motion.div>
          );
        })}
      </div>
      <div className="px-3 py-1.5 border-t border-border-dim text-[8px] font-mono text-white/20">
        axeguard@soc:~$ <span className="animate-pulse text-matrix-green">|</span>{' '}
        NODE_COUNT: 06 | DLP_ACTIVE: TRUE
      </div>
    </div>
  );
};

const MetricCard = ({ title, value, unit, colorClass = "text-matrix-green" }: any) => (
  <div className="bg-surface/50 border border-border-dim rounded-lg p-3">
    <div className="text-[8px] font-mono text-text-muted uppercase tracking-wider">{title}</div>
    <div className={`text-lg font-bold ${colorClass} mt-1`}>{value}</div>
    <div className="text-[9px] text-text-muted">{unit}</div>
  </div>
);

interface AgentStatusProps {
  agent: { id: string; name: string; task: string };
  phase: SOCPhase;
}

const AgentStatusCard = ({ agent, phase }: AgentStatusProps) => {
  const getAgentDetails = () => {
    switch (agent.id) {
      case 'SUPERVISOR':
        if (phase === 'INITIALIZING') return { status: 'INICIALIZANDO', active: true, color: 'text-accent-blue', icon: Cpu };
        if (['RESPOND', 'LESSONS_LEARNT'].includes(phase)) return { status: 'ORQUESTRANDO', active: true, color: 'text-accent-blue', icon: Activity };
        return { status: 'IDLE', active: false, color: 'text-text-muted', icon: Shield };
      case 'EDGE_DLP':
        if (phase === 'MONITOR') return { status: 'ESCANEANDO', active: true, color: 'text-accent-amber', icon: Activity };
        if (phase === 'DETECT') return { status: 'ALERTA', active: true, color: 'text-accent-red', icon: AlertTriangle };
        if (phase === 'RESPOND') return { status: 'ISOLANDO', active: true, color: 'text-accent-red', icon: Lock };
        if (phase === 'IR_RECOVERY') return { status: 'PATCHING', active: true, color: 'text-accent-green', icon: CheckCircle2 };
        return { status: 'IDLE', active: false, color: 'text-text-muted', icon: Shield };
      case 'RAG_INTEL':
        if (phase === 'ANALYSE') return { status: 'CONSULTANDO', active: true, color: 'text-accent-blue', icon: Database };
        return { status: 'SINCRONIZADO', active: false, color: 'text-accent-green', icon: CheckCircle2 };
      case 'THREAT_HUNTER':
        if (phase === 'HUNT') return { status: 'CAÇANDO', active: true, color: 'text-accent-blue', icon: Activity };
        return { status: 'IDLE', active: false, color: 'text-text-muted', icon: Shield };
      default:
        return { status: 'IDLE', active: false, color: 'text-text-muted', icon: Shield };
    }
  };

  const details = getAgentDetails();
  const AgentIcon = details.icon;

  return (
    <motion.div layout className={`relative bg-surface/50 border ${details.active ? 'border-accent-green/30' : 'border-border-dim'} rounded-lg p-3 overflow-hidden`}>
      {details.active && (
        <motion.div className="absolute inset-0 bg-gradient-to-r from-accent-green/5 to-transparent" animate={{ opacity: [0.3, 0.7, 0.3] }} transition={{ duration: 2, repeat: Infinity }} />
      )}
      <div className="relative z-10">
        <div className="flex items-center gap-2 mb-1">
          <div className="text-[10px] font-mono text-white/80">{agent.name}</div>
          {details.active ? (
            <AgentIcon className={`w-3 h-3 ${details.color}`} />
          ) : (
            <Shield className="w-3 h-3 text-text-muted/50" />
          )}
        </div>
        <div className="text-[8px] text-text-muted">Saúde: 98%</div>
        <div className={`text-[9px] font-mono mt-1 ${details.color}`}>{details.status}</div>
        {details.active && (
          <div className="flex gap-1 mt-2">
            {[1, 2, 3].map(i => (
              <motion.div key={i} className="w-1 h-1 rounded-full bg-accent-green" animate={{ opacity: [0.3, 1, 0.3] }} transition={{ duration: 0.8, repeat: Infinity, delay: i * 0.2 }} />
            ))}
          </div>
        )}
      </div>
    </motion.div>
  );
};

/* ─── Main App ─── */

export default function EnforcerApp() {
  const [state, setState] = useState<SOCState>({
    phase: 'INITIALIZING',
    currentIncident: null,
    logs: [],
    metrics: { threatsBlocked: 1242, uptimeEvaded: 48, moneySafeguarded: 580000, complianceStatus: 94 },
    connectedAgents: AGENT_LIST,
  });

  useEffect(() => {
    addLog('system', 'PetroShield_Core', 'Inicializando Framework Multi-Agente AxeGuard...');
    setTimeout(() => addLog('system', 'PetroShield_Core', 'Carregando Subgrafos: [Supervisor, Edge_DLP, RAG_Intel, CLevel_Reporter, Threat_Hunter]'), 500);
    setTimeout(() => addLog('system', 'PetroShield_Core', 'Monitorando Telemetria SCADA (Nó Camaçari) na porta 443...'), 1000);
    setTimeout(() => startCycle(), 2000);
  }, []);

  const addLog = (type: LogEntry['type'], agent: string, message: string) => {
    const newLog: LogEntry = {
      id: Math.random().toString(36).substr(2, 9),
      timestamp: new Date().toLocaleTimeString('pt-BR'),
      agent,
      message,
      type,
    };
    setState(prev => ({ ...prev, logs: [...prev.logs, newLog].slice(-100) }));
  };

  const updatePhase = (phase: SOCPhase) => setState(prev => ({ ...prev, phase }));

  const getHeuristicAnalysis = (threat: ThreatEvent) => {
    const insights = [
      `Anomalia detectada em ${threat.source}. Assinatura de comportamento sugere ${threat.type}. Recomendado isolamento imediato.`,
      `Padrão de tráfego em ${threat.source} correlaciona-se com táticas de ${threat.severity === 'CRITICAL' ? 'Exfiltração Ativa' : 'Reconhecimento'}.`,
      `Integridade de dados em risco em ${threat.source}. Protocolo LockShield sugere verificação de firmware CRC.`,
      `Alerta de alta severidade em ${threat.source}. Vetor de ataque: ${threat.type}. Acionando camadas de defesa proativa.`,
      `Insight Heurístico: Bloqueio Zero-Trust recomendado para conter a propagação de ${threat.type}.`,
    ];
    return insights[Math.floor(Math.random() * insights.length)];
  };

  const wait = (ms: number) => new Promise(resolve => setTimeout(resolve, ms));

  const startCycle = async () => {
    updatePhase('HUNT');
    addLog('system', 'Supervisor', 'Redirecionando ciclo para estado de `CAÇA` proativa...');
    addLog('agent', 'Threat_Hunter', 'Executando varredura heurística em busca de anomalias em rede...');
    addLog('tool', 'Threat_Hunter', 'Mapeando vetores de ataque potenciais e spot firewalls ativos.');
    await wait(3000);

    const foundSomething = Math.random() > 0.3;
    if (foundSomething) {
      addLog('alert', 'Threat_Hunter', '[INCIDENTE_DETECTADO] Padrão malicioso identificado em zona de baixa confiança!');
      await wait(1000);

      updatePhase('MONITOR');
      addLog('system', 'Supervisor', 'Iniciando monitoramento intensivo de fluxo de dados...');
      addLog('tool', 'Edge_DLP', 'Ingerindo Fluxo IoT: 4.8 MB/s do Polo Petroquímico de Camaçari.');
      await wait(2000);

      const threat = MOCK_THREATS[Math.floor(Math.random() * MOCK_THREATS.length)];
      setState(prev => ({ ...prev, currentIncident: threat, phase: 'DETECT' }));
      addLog('alert', 'Edge_DLP', `[ALERTA_CRÍTICO] ${threat.type} detectado em ${threat.source}`);
      addLog('agent', 'Edge_DLP', `Combinando assinatura de anomalia para: ${threat.description}`);
      await wait(2500);

      updatePhase('ANALYSE');
      addLog('system', 'RAG_Intel', 'Executando context_engineering_chain...');
      addLog('rag', 'RAG_Intel', 'Consultando Banco de Dados MITRE ICS e Arquivos Forenses Internos...');
      const aiAnalysis = getHeuristicAnalysis(threat);
      addLog('agent', 'RAG_Intel', `ANÁLISE HEURÍSTICA: ${aiAnalysis}`);
      await wait(4000);

      updatePhase('RESPOND');
      addLog('agent', 'Supervisor', 'Escalando protocolo de extração. Roteando para subgrafo de `RESPOSTA`.');
      addLog('tool', 'Edge_DLP', `AÇÃO: Executando block_port_and_isolate_subnet(target_ip="${threat.source}", strict=True)`);
      addLog('system', 'Edge_DLP', 'Isolando VLAN 40. Propagação interrompida.');
      await wait(2000);

      updatePhase('IR_RECOVERY');
      addLog('agent', 'Recovery_Engine', 'Atualizando firmware S7-1500. Verificando integridade CRC.');
      addLog('system', 'Recovery_Engine', 'Nó 10.0.0.12 estabilizado. Operações normais retomadas.');
      setState(prev => ({
        ...prev,
        metrics: {
          ...prev.metrics,
          threatsBlocked: prev.metrics.threatsBlocked + 1,
          uptimeEvaded: prev.metrics.uptimeEvaded + (Math.random() * 5),
          moneySafeguarded: prev.metrics.moneySafeguarded + 80000,
          complianceStatus: Math.min(100, prev.metrics.complianceStatus + 0.1),
        },
      }));
      await wait(3000);

      updatePhase('LESSONS_LEARNT');
      addLog('agent', 'CLevel_Reporter', 'Gerando relatório de incidente automatizado para revisão da diretoria.');
      addLog('rag', 'Supervisor', 'Indexando hash de vetor em memória de longo prazo. Vacinação multi-tenant concluída.');
      await wait(3000);
    } else {
      addLog('system', 'Threat_Hunter', 'Nenhuma ameaça emergente detectada. Mantendo vigilância proativa.');
      await wait(3000);
    }

    setTimeout(() => {
      updatePhase('STANDBY');
      addLog('system', 'Supervisor', 'Sistema em repouso. Entrando em modo STANDBY.');
      setTimeout(() => startCycle(), 5000);
    }, 1000);
  };

  return (
    <div className="w-full h-screen flex flex-col" style={{ background: '#0a0b0d', color: '#e2e8f0' }}>
      {/* Header */}
      <header className="flex items-center px-4 h-[50px] border-b border-border-dim bg-surface/30 shrink-0">
        <div className="flex items-center gap-2">
          <AxeTorch />
          <span className="text-[11px] font-mono text-accent-green tracking-widest ml-2">
            PETROSHIELD AXEGUARD
          </span>
        </div>
        <div className="ml-auto flex items-center gap-4 text-[8px] font-mono text-text-muted">
          <span>LATÊNCIA: 14ms</span>
          <span>NÓ: CAMAÇARI_BR_01</span>
          <span>UPTIME: 184:12:09</span>
          <span className="text-accent-green">PROTOCOLO_SEG: ATIVO</span>
        </div>
      </header>

      {/* Main Grid */}
      <div className="flex-1 grid grid-cols-[minmax(380px,1fr)_minmax(500px,2fr)] overflow-hidden">
        {/* Terminal Panel (Left) */}
        <div className="flex flex-col p-3 gap-2 border-r border-border-dim overflow-hidden">
          <div className="text-[8px] font-mono text-text-muted px-1">
            Stream: Logs_Orquestração_Ao_Vivo v2.5 [PT-BR]
          </div>
          <div className="flex-1 overflow-hidden">
            <TerminalWindow logs={state.logs} />
          </div>
        </div>

        {/* Dashboard Panel (Right) */}
        <div className="flex flex-col p-3 gap-3 overflow-y-auto">
          <div className="text-[9px] font-mono text-text-muted border-b border-border-dim pb-1">
            Métricas Executivas — Tensões na Cadeia de Valor em Tempo Real
          </div>

          <div className="grid grid-cols-4 gap-2">
            <MetricCard title="Ameaça Atual" value={state.phase === 'DETECT' ? "CRÍTICA" : (state.phase === 'HUNT' ? "CAÇANDO..." : "ESTÁVEL")} unit="" icon={AlertTriangle} colorClass={state.phase === 'DETECT' ? 'text-cyber-red' : 'text-accent-green'} />
            <MetricCard title="Perda Evitada" value={`R$ ${(state.metrics.moneySafeguarded / 1000).toFixed(0)}K`} unit="" icon={Shield} colorClass="text-accent-amber" />
            <MetricCard title="Anomalias 24H" value="4.821" unit="" icon={Activity} colorClass="text-cyber-cyan" />
            <MetricCard title="Downtime Salvo" value="14.2h" unit="" icon={Globe} colorClass="text-accent-green" />
          </div>

          {/* Incident Details */}
          <AnimatePresence>
            {state.currentIncident && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                className="bg-surface/50 border border-cyber-red/20 rounded-lg p-4 space-y-2"
              >
                <div className="text-[10px] font-mono text-cyber-red">Detalhes do Incidente Proativo</div>
                <div className="grid grid-cols-3 gap-2 text-[9px] font-mono">
                  <div><span className="text-text-muted">ID Alerta</span><br /><span className="text-white">{state.currentIncident.id}</span></div>
                  <div><span className="text-text-muted">Severidade</span><br /><span className="text-cyber-red">{state.currentIncident.severity}</span></div>
                  <div><span className="text-text-muted">Origem</span><br /><span className="text-cyber-cyan">{state.currentIncident.source}</span></div>
                </div>
                <div className="text-[9px] text-white/60 italic">"{state.currentIncident.description}"</div>
                {state.currentIncident.mitigationSteps && (
                  <div className="space-y-1">
                    <div className="text-[8px] font-mono text-accent-amber">Protocolo de Resposta</div>
                    {state.currentIncident.mitigationSteps.map((step, idx) => (
                      <div key={idx} className="text-[8px] font-mono text-white/50 flex gap-2">
                        <span className="text-accent-green">[{idx + 1}]</span> {step}
                      </div>
                    ))}
                  </div>
                )}
              </motion.div>
            )}
          </AnimatePresence>

          {/* Agent Pool */}
          <div>
            <div className="text-[9px] font-mono text-text-muted mb-2">Pool de Agentes Ativos</div>
            <div className="grid grid-cols-2 gap-2">
              {[
                { id: 'SUPERVISOR', name: 'SUPERVISOR_V2', task: 'Lógica de Orquestração' },
                { id: 'THREAT_HUNTER', name: 'THREAT_HUNTER', task: 'Caça Proativa de Ameaças' },
                { id: 'EDGE_DLP', name: 'EDGE_DLP_PROB', task: 'Inspeção Profunda de Pacotes' },
                { id: 'RAG_INTEL', name: 'RAG_INTEL_OPS', task: 'Contextualizador MITRE' },
              ].map(agent => (
                <AgentStatusCard key={agent.id} agent={agent} phase={state.phase} />
              ))}
            </div>
          </div>

          {/* MITRE Coverage */}
          <div className="bg-surface/50 border border-border-dim rounded-lg p-3">
            <div className="text-[8px] font-mono text-text-muted mb-2">Cobertura de Táticas MITRE (ICS)</div>
            <div className="flex gap-1 flex-wrap">
              {['INTR', 'EXEC', 'PERS', 'PRIV', 'EVAS', 'DISC', 'LATM', 'COLL', 'C&C', 'EXFI'].map((code, i) => (
                <span key={code} className={`text-[8px] font-mono px-1.5 py-0.5 rounded border ${i < 7 ? 'border-accent-green/30 text-accent-green bg-accent-green/5' : 'border-border-dim text-text-muted'}`}>
                  {code}
                </span>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Footer */}
      <footer className="flex items-center justify-between px-4 h-[30px] border-t border-border-dim bg-surface/30 text-[7px] font-mono text-text-muted shrink-0">
        <span>FONTE_LOGS: /var/log/axeguard/fluxo_agente.log</span>
        <span>CRIPTOGRAFIA: AES-256-GCM [FIPS-140-2]</span>
        <span>HORA DO SISTEMA: {new Date().toISOString().split('T')[0]} {new Date().toLocaleTimeString()} UTC</span>
      </footer>
    </div>
  );
}
