import { useState, useEffect, useRef, useCallback } from 'react';
import {
  DEMO_SCENARIOS, OKRS, generateAuditEvents, getCumulativeCostAvoided,
  getFleetHealth, VENDOR_RISK_DB, XR_DEVICES, type AuditEvent
} from '../data/mockData';

// ── Tipos do Terminal ─────────────────────────────────────────────
interface TermLine {
  text: string;
  color: string;
  ts: string;
}

// ── Sub-Componente: Terminal Integrado ─────────────────────────────
function AgentTerminal() {
  const [lines, setLines] = useState<TermLine[]>([]);
  const [input, setInput] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const now = () => new Date().toLocaleTimeString('pt-BR');

  const addLine = useCallback((text: string, color = '#00FF41') => {
    setLines(prev => [...prev.slice(-200), { text, color, ts: now() }]);
  }, []);

  useEffect(() => {
    addLine('╔══════════════════════════════════════════════════════════╗', '#00FFFF');
    addLine('║  PetroShield AxeGuard SOC Terminal v2.0                 ║', '#FF6200');
    addLine('║  Agentic Security Operations Center                    ║', '#FF6200');
    addLine('╚══════════════════════════════════════════════════════════╝', '#00FFFF');
    addLine('');
    addLine('Digite "help" para ver comandos disponíveis.', '#999');
    addLine('');
  }, [addLine]);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [lines]);

  const simulateAgentRun = useCallback(async (sceneId: string) => {
    const scene = DEMO_SCENARIOS.find(s => s.scene_id === sceneId);
    if (!scene) {
      addLine(`[ERRO] Playbook de Mitigação "${sceneId}" não encontrado.`, '#FF3333');
      return;
    }

    setIsRunning(true);
    addLine(`\n═══ ORQUESTRANDO: ${scene.scene_title} ═══`, '#FF6200');

    const phases = ['MONITOR', 'DETECT', 'ANALYSE', 'RESPOND', 'HUNT', 'LESSONS'];

    for (const narr of scene.narration) {
      await sleep(600);
      addLine(`  ▸ ${narr}`, '#00FFFF');
    }

    for (const phase of phases) {
      await sleep(400);
      addLine(`  [${phase}] ✓ Completo`, '#00FF41');
    }

    await sleep(300);
    addLine(`\n  ⚡ EXECUÇÃO AUTÔNOMA: action=${scene.expected_action} | mitre=${scene.expected_mitre || 'N/A'}`, '#FF6200');
    addLine(`  ✓ Playbook de Mitigação ${sceneId} concluído com sucesso.\n`, '#00FF41');
    setIsRunning(false);
  }, [addLine]);

  const handleCommand = useCallback(async (cmd: string) => {
    const trimmed = cmd.trim().toLowerCase();
    addLine(`pshield> ${cmd}`, '#00FFFF');

    if (trimmed === 'help') {
      addLine('  Comandos disponíveis:', '#999');
      addLine('    execute playbook <id> — Executar resposta autônoma (pb_alpha_01, pb_dlp_44, etc)', '#00FF41');
      addLine('    execute all           — Executar todas as mitigações (Simulação C-Level)', '#00FF41');
      addLine('    analyze status        — Dashboard de métricas core ao vivo', '#00FF41');
      addLine('    audit fleet           — Status da infraestrutura de edge nodes', '#00FF41');
      addLine('    audit vendor          — Tabela dinâmica de risco de terceiros', '#00FF41');
      addLine('    report okrs           — Relatório síntese: OKRs e KPIs', '#00FF41');
      addLine('    clear                 — Limpar buffer do terminal', '#00FF41');
      addLine('');
    } else if (trimmed.startsWith('execute ')) {
      const sceneId = trimmed.replace('execute playbook ', '').replace('execute ', '');
      if (sceneId === 'all') {
        for (const s of DEMO_SCENARIOS) {
          await simulateAgentRun(s.scene_id);
        }
      } else {
        await simulateAgentRun(sceneId);
      }
    } else if (trimmed === 'analyze status') {
      const fleet = getFleetHealth();
      const cost = getCumulativeCostAvoided();
      addLine('╔══ PETROSHIELD STATUS ══╗', '#00FFFF');
      addLine(`  Status: ONLINE`, '#00FF41');
      addLine(`  Sessions Ativas: ${Object.keys(XR_DEVICES).length}`, '#00FFFF');
      addLine(`  Fleet Coverage: ${fleet.coverage_pct}%`, '#00FF41');
      addLine(`  Custo Evitado YTD: R$ ${(cost / 1e6).toFixed(2)}M`, '#FF6200');
      addLine(`  MTTD: 47s | MTTR: 23min`, '#00FFFF');
      addLine('╚═══════════════════════╝\n', '#00FFFF');
    } else if (trimmed === 'audit fleet') {
      const fleet = getFleetHealth();
      addLine(`  Fleet: ${fleet.online}/${fleet.total} online | ${fleet.upToDate} vacinados | ${fleet.outdated} pendentes`, '#00FF41');
    } else if (trimmed === 'audit vendor') {
      addLine('  VENDOR                    SCORE  LEVEL      DARK WEB', '#999');
      addLine('  ─────────────────────────────────────────────────────', '#333');
      Object.values(VENDOR_RISK_DB).forEach(v => {
        const color = v.risk_level === 'CRITICAL' ? '#FF3333' : v.risk_level === 'HIGH' ? '#FF6200' : '#00FF41';
        addLine(`  ${v.vendor_name.padEnd(24)} ${String(v.risk_score).padStart(4)}   ${v.risk_level.padEnd(10)} ${v.dark_web_exposure ? '⚠ YES' : '  NO'}`, color);
      });
      addLine('');
    } else if (trimmed === 'report okrs') {
      Object.values(OKRS).forEach(okr => {
        const bar = '█'.repeat(Math.floor(okr.progress_pct / 5)) + '░'.repeat(20 - Math.floor(okr.progress_pct / 5));
        const color = okr.status === 'on_track' ? '#00FF41' : '#FF6200';
        addLine(`  ${okr.name}`, '#00FFFF');
        addLine(`    [${bar}] ${okr.progress_pct}% — ${okr.current}`, color);
      });
      addLine('');
    } else if (trimmed === 'clear') {
      setLines([]);
    } else if (trimmed) {
      addLine(`  [ERRO] Comando desconhecido: "${trimmed}". Digite "help".`, '#FF3333');
    }
  }, [addLine, simulateAgentRun]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isRunning) return;
    handleCommand(input);
    setInput('');
  };

  return (
    <div className="terminal-container" style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
      <div className="terminal-header">
        <span className="dot-red" />
        <span className="dot-yellow" />
        <span className="dot-green" />
        <span style={{ marginLeft: 8 }}>pshield@axeguard-soc:~</span>
        <span style={{ marginLeft: 'auto', color: isRunning ? '#FF6200' : '#00FF41' }}>
          {isRunning ? '● RUNNING' : '● READY'}
        </span>
      </div>
      <div
        className="terminal-body"
        style={{ flex: 1, overflow: 'auto', cursor: 'text' }}
        onClick={() => inputRef.current?.focus()}
      >
        {lines.map((line, i) => {
          const isGlitch = line.text.includes('[ERRO]') || line.text.includes('⚠') || line.text.includes('CRITICAL');
          return (
            <div key={i} className={isGlitch ? 'glitch-text' : ''} style={{ color: line.color, whiteSpace: 'pre', minHeight: '1.4em', fontFamily: 'var(--font-mono)', fontSize: '0.82rem' }}>
              {line.text}
            </div>
          );
        })}
        <div ref={bottomRef} />
      </div>
      <form onSubmit={handleSubmit} style={{ display: 'flex', borderTop: '1px solid rgba(0,255,65,0.1)', background: 'rgba(0,0,0,0.5)' }}>
        <span style={{ padding: '8px 4px 8px 12px', color: '#00FFFF', fontFamily: 'var(--font-mono)', fontSize: '0.85rem' }}>pshield&gt;</span>
        <input
          ref={inputRef}
          value={input}
          onChange={e => setInput(e.target.value)}
          disabled={isRunning}
          placeholder={isRunning ? 'Aguardando...' : 'Digite um comando...'}
          style={{
            flex: 1,
            background: 'transparent',
            border: 'none',
            outline: 'none',
            color: '#00FF41',
            fontFamily: 'var(--font-mono)',
            fontSize: '0.85rem',
            padding: '8px',
            caretColor: '#00FF41',
          }}
          autoFocus
        />
      </form>
    </div>
  );
}

// ── Sub-Componente: Agent Loop Viz ─────────────────────────────────
function AgentLoopViz() {
  const [activePhase, setActivePhase] = useState(0);
  const phases = ['MONITOR', 'DETECT', 'ANALYSE', 'RESPOND', 'HUNT', 'LESSONS'];

  useEffect(() => {
    const timer = setInterval(() => {
      setActivePhase(p => (p + 1) % phases.length);
    }, 2000);
    return () => clearInterval(timer);
  }, [phases.length]);

  const [events] = useState<AuditEvent[]>(() => generateAuditEvents(25));
  const [visibleCount, setVisibleCount] = useState(5);

  useEffect(() => {
    const timer = setInterval(() => {
      setVisibleCount(c => Math.min(c + 1, events.length));
    }, 1500);
    return () => clearInterval(timer);
  }, [events.length]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)', height: '100%' }}>
      {/* Agentic Loop Diagram */}
      <div className="glass-card" style={{ padding: 'var(--gap-md)' }}>
        <div className="glass-card-title"><span className="indicator" /> Agentic Loop — Ciclo OODA+</div>
        <div style={{ display: 'flex', gap: 8, marginTop: 12 }}>
          {phases.map((phase, i) => (
            <div
              key={phase}
              style={{
                flex: 1,
                padding: '12px 8px',
                borderRadius: 'var(--radius-sm)',
                textAlign: 'center',
                fontFamily: 'var(--font-terminal)',
                fontSize: '1rem',
                letterSpacing: 1,
                background: i === activePhase ? 'rgba(0,255,65,0.12)' : 'rgba(255,255,255,0.02)',
                border: `1px solid ${i === activePhase ? '#00FF41' : 'rgba(255,255,255,0.05)'}`,
                color: i <= activePhase ? '#00FF41' : '#555',
                boxShadow: i === activePhase ? '0 0 15px rgba(0,255,65,0.2)' : 'none',
                transition: 'all 0.4s ease',
                position: 'relative',
              }}
            >
              {i <= activePhase && <span style={{ marginRight: 4 }}>✓</span>}
              {phase}
              {i === activePhase && (
                <div style={{
                  position: 'absolute', bottom: -4, left: '50%', transform: 'translateX(-50%)',
                  width: 8, height: 8, borderRadius: '50%', background: '#00FF41',
                  boxShadow: '0 0 10px rgba(0,255,65,0.5)',
                  animation: 'statusPulse 1s ease-in-out infinite',
                }} />
              )}
            </div>
          ))}
        </div>
      </div>

      {/* Live Event Stream */}
      <div className="glass-card" style={{ flex: 1, overflow: 'hidden', display: 'flex', flexDirection: 'column' }}>
        <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> Live Event Stream</div>
        <div style={{ flex: 1, overflow: 'auto', marginTop: 8 }}>
          <table className="data-table">
            <thead>
              <tr>
                <th>Action</th>
                <th>Device</th>
                <th>Score</th>
                <th>Latency</th>
                <th>Query</th>
              </tr>
            </thead>
            <tbody>
              {events.slice(0, visibleCount).map((ev, i) => {
                const color = ev.operator_action === 'blocked' ? '#FF3333' : ev.operator_action === 'escalated' ? '#FF6200' : '#00FF41';
                return (
                  <tr key={i} className={i === visibleCount - 1 ? 'animate-in' : ''}>
                    <td><span className={`neon-badge ${ev.operator_action === 'blocked' ? 'critical' : ev.operator_action === 'escalated' ? 'high' : 'low'}`}>{ev.operator_action}</span></td>
                    <td style={{ color: '#00FFFF', fontFamily: 'var(--font-mono)', fontSize: '0.75rem' }}>{ev.device_id}</td>
                    <td style={{ color, fontFamily: 'var(--font-mono)' }}>{ev.threat_score}</td>
                    <td style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem' }}>{ev.latency_ms}ms</td>
                    <td style={{ fontSize: '0.75rem', maxWidth: 200, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{ev.original_query}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

// ── Página Principal: Command Center ──────────────────────────────
export default function CommandCenter() {
  const [activeTab, setActiveTab] = useState<'terminal' | 'agent-loop'>('terminal');

  // Top KPI metrics
  const fleet = getFleetHealth();
  const cost = getCumulativeCostAvoided();
  const latestMetric = { leaks: 168, latency: 30, escalated: 11 };

  return (
    <div className="page-container" style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)' }}>
      {/* KPI Row */}
      <div className="grid-4 animate-in">
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" /> Sessions Ativas</div>
          <div className="metric-value">{Object.keys(XR_DEVICES).length}</div>
          <div className="metric-label">Dispositivos XR Monitorados</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" /> Leaks Prevenidos</div>
          <div className="metric-value">{latestMetric.leaks}</div>
          <div className="metric-delta positive">↑ 12% vs mês anterior</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> Custo Evitado YTD</div>
          <div className="metric-value orange">R$ {(cost / 1e6).toFixed(1)}M</div>
          <div className="metric-label">Acumulado 2025-2026</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> Fleet Coverage</div>
          <div className="metric-value cyan">{fleet.coverage_pct}%</div>
          <div className="metric-delta positive">{fleet.online}/{fleet.total} nodes online</div>
        </div>
      </div>

      {/* Sub Tabs */}
      <div className="sub-tabs animate-in animate-in-delay-1">
        <button className={`sub-tab ${activeTab === 'terminal' ? 'active' : ''}`} onClick={() => setActiveTab('terminal')}>
          ▸ Terminal SOC
        </button>
        <button className={`sub-tab ${activeTab === 'agent-loop' ? 'active' : ''}`} onClick={() => setActiveTab('agent-loop')}>
          ▸ Agent Loop & Events
        </button>
      </div>

      {/* Content */}
      <div className="animate-in animate-in-delay-2" style={{ flex: 1, minHeight: 0 }}>
        {activeTab === 'terminal' ? <AgentTerminal /> : <AgentLoopViz />}
      </div>
    </div>
  );
}

function sleep(ms: number) {
  return new Promise(r => setTimeout(r, ms));
}
