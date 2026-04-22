/**
 * VaultApp — SOC-sys Dashboard Entry Point.
 * Consolidated from SOC-sys_Dashboard repo for monorepo deployment.
 */
import { useState, useEffect } from 'react';
import type { ReactNode } from 'react';
import { motion } from 'motion/react';
import { metricsService } from './services/metricsService';
import type { MetricSnapshot, MetricsConfig } from './services/metricsService';
import CPUChart from './components/CPUChart';
import NetworkTrafficChart from './components/NetworkTrafficChart';
import TerminalInput from './components/TerminalInput';
import MetricsControllers from './components/MetricsControllers';
import SecurityAnalytics from './components/SecurityAnalytics';
import IncidentBoard from './components/IncidentBoard';
import ThreatStream from './components/ThreatStream';
import ReportingDocs from './components/ReportingDocs';
import SOCLifecycleStage from './components/SOCLifecycleStage';
import DataModelViewer from './components/DataModelViewer';
import { Cpu } from 'lucide-react';

export default function VaultApp() {
  const [metrics, setMetrics] = useState<MetricSnapshot | null>(null);
  const [config, setConfig] = useState<MetricsConfig>(metricsService.getConfig());
  const [history, setHistory] = useState<string[]>([
    'axeguard.dlp --enforce-all',
    'langgraph --init-soc-subgraph',
    'prometheus.query --entropy-check',
  ]);

  useEffect(() => {
    const update = () => setMetrics(metricsService.tick());
    update();
    const interval = setInterval(update, 1000);
    return () => clearInterval(interval);
  }, []);

  const handleConfigChange = (newConfig: Partial<MetricsConfig>) => {
    metricsService.setConfig(newConfig);
    setConfig(prev => ({ ...prev, ...newConfig }));
  };

  const handleExecute = (cmd: string) => {
    setHistory(prev => [cmd, ...prev].slice(0, 10));
  };

  if (!metrics) return null;

  return (
    <div className="w-full h-screen flex flex-col relative overflow-hidden" style={{ background: '#050505' }}>
      <BackgroundLayer />

      {/* Header */}
      <header className="relative z-10 flex items-center justify-between px-4 h-[48px] border-b border-white/5 bg-black/40 backdrop-blur-md shrink-0">
        <div className="flex items-center gap-3">
          <div className="w-2 h-2 rounded-full bg-[#00FF41] shadow-[0_0_8px_#00FF41]" />
          <span className="text-[11px] font-mono text-[#00FF41]/80 tracking-widest font-bold">AXE_GUARD_SOC_CORE</span>
          <span className="text-[8px] font-mono text-white/20 ml-2">AGENTIC_DLP_ORCHESTRATION_PLATFORM</span>
        </div>
        <div className="flex items-center gap-3">
          {metrics.kpis.map(kpi => (
            <div key={kpi.label} className="text-center px-2">
              <div className="text-[7px] font-mono text-white/30">{kpi.label}</div>
              <div className={`text-[10px] font-bold ${kpi.color === 'matrix' ? 'text-[#00FF41]' : kpi.color === 'cyan' ? 'text-[#00FFFF]' : 'text-[#FF6200]'}`}>
                {kpi.value}
              </div>
              {kpi.subValue && <div className="text-[6px] text-white/20">{kpi.subValue}</div>}
            </div>
          ))}
          <div className="text-[7px] font-mono text-[#00FF41]/40 ml-4">NODE_SYNC: OK</div>
        </div>
      </header>

      {/* Main Grid */}
      <div className="relative z-10 flex-1 flex overflow-hidden">
        {/* Left Sidebar */}
        <aside className="w-[200px] flex flex-col p-2 gap-2 border-r border-white/5 shrink-0 overflow-y-auto custom-scrollbar">
          <div className="acrylic-card text-center">
            <div className="text-[7px] font-mono text-white/30">GUARD_STATUS</div>
            <div className="text-[9px] font-mono text-[#00FF41] font-bold mt-1">AXE_SHIELD_V4.2</div>
            <div className={`text-[10px] font-bold mt-1 ${metrics.axeGuardStatus === 'ACTIVE' ? 'text-[#00FF41] glow-text-green' : 'text-[#ef4444] glow-text-red'}`}>
              {metrics.axeGuardStatus}
            </div>
          </div>
          {metrics.langGraphNodes.map(node => (
            <div key={node.id} className="flex items-center gap-2 px-2 py-1 text-[8px] font-mono">
              <div className={`w-1.5 h-1.5 rounded-full ${node.status === 'ACTIVE' ? 'bg-[#00FF41]' : 'bg-white/10'}`} />
              <span className="text-white/40">NODE.{node.id}</span>
              <span className={`ml-auto ${node.status === 'ACTIVE' ? 'text-[#00FF41]' : 'text-white/20'}`}>{node.status}</span>
            </div>
          ))}
          <div className="acrylic-card">
            <div className="text-[7px] font-mono text-white/30">DLP_ENTROPY</div>
            <div className="text-[12px] font-bold text-[#FF6200] glow-text-orange mt-1">{metrics.disk.entropy.toFixed(5)}</div>
          </div>
          <MetricsControllers config={config} onChange={handleConfigChange} />
        </aside>

        {/* Center Operations Zone */}
        <div className="flex-1 flex flex-col gap-2 p-2 overflow-y-auto custom-scrollbar">
          {/* SOC Lifecycle Stage */}
          <SOCLifecycleStage currentPhase={metrics.currentPhase} />

          {/* Primary Viewport */}
          <div className="flex-1 grid grid-cols-2 gap-2 min-h-0">
            <ReportingDocs reports={metrics.reportingAgent} />
            <SecurityAnalytics threatData={metrics.threatsHistory} threatScore={metrics.network.threatScore} threatStream={metrics.threatStream} />
            <ThreatStream events={metrics.threatStream} />
            <div className="flex flex-col gap-2">
              <CPUChart usage={metrics.cpu} />
              <NetworkTrafficChart rx={metrics.network.rx} tx={metrics.network.tx} />
            </div>
          </div>

          {/* Shell & History */}
          <div className="acrylic-card">
            <div className="flex items-center gap-2 mb-2">
              <div className="text-[7px] font-mono text-[#00FF41]/40">SHELL_S01</div>
              <div className="text-[7px] font-mono text-white/20 ml-auto">MISSION_OPERATIONAL_LOGS</div>
            </div>
            <TerminalInput onExecute={handleExecute} />
            <div className="mt-2 space-y-0.5 max-h-[80px] overflow-y-auto custom-scrollbar">
              {history.map((h, i) => (
                <div key={i} className="text-[8px] font-mono text-white/20">
                  <span className="text-white/10">[{new Date().toLocaleTimeString()}]</span>{' '}
                  CMD:// {h} <span className="text-[#00FF41]/30">_ACK_</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Right Panes */}
        <aside className="w-[260px] flex flex-col gap-2 p-2 border-l border-white/5 shrink-0 overflow-y-auto custom-scrollbar">
          <IncidentBoard incidents={metrics.incidents} agents={metrics.agents} />
          <StatCard label="CPU_UTILIZATION" value={`${metrics.cpu}%`} percentage={metrics.cpu} icon={<Cpu className="w-3 h-3" />} color="matrix" />
          <DataModelViewer metrics={metrics} />
          <div className="acrylic-card">
            <div className="text-[7px] font-mono text-white/30 mb-1">SURVIVABILITY_INDEX_STREAM</div>
            <div className="flex items-center gap-2 mb-2">
              <span className="text-[8px] text-[#00FFFF]">Neural_Sync</span>
              <div className="flex gap-px">
                {[...Array(5)].map((_, i) => (
                  <motion.div key={i} className="w-1 h-3 bg-[#00FF41]/60 rounded-sm" animate={{ scaleY: [0.4, 1, 0.4] }} transition={{ duration: 1.2, repeat: Infinity, delay: i * 0.15 }} />
                ))}
              </div>
            </div>
            <div className="text-[8px] font-mono text-white/30">
              Leak_Events: <span className="text-[#ef4444]">{metrics.incidents.length}</span> CRIT
            </div>
            <div className="text-[8px] font-mono text-white/30 mt-1">
              Hardening_Buffer: <span className="text-[#00FF41]">0.9997_SIGMA</span>
            </div>
          </div>
        </aside>
      </div>
    </div>
  );
}

function BackgroundLayer() {
  const [mousePos, setMousePos] = useState({ x: 0, y: 0 });
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      setMousePos({ x: e.clientX / window.innerWidth, y: e.clientY / window.innerHeight });
    };
    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, []);

  return (
    <motion.div
      className="parallax-layer"
      animate={{ x: mousePos.x * -20, y: mousePos.y * -20 }}
      transition={{ type: 'spring', stiffness: 50, damping: 30 }}
    />
  );
}

function StatCard({ label, value, icon, color }: { label: string; value: string; percentage?: number; icon: ReactNode; color: 'matrix' | 'orange' | 'cyan' }) {
  const themes = {
    matrix: { text: 'text-[#00FF41]', border: 'border-[#00FF41]/20', glow: 'shadow-[0_0_15px_rgba(0,255,65,0.1)]' },
    orange: { text: 'text-[#FF6200]', border: 'border-[#FF6200]/20', glow: 'shadow-[0_0_15px_rgba(255,98,0,0.1)]' },
    cyan: { text: 'text-[#00FFFF]', border: 'border-[#00FFFF]/20', glow: 'shadow-[0_0_15px_rgba(0,255,255,0.1)]' },
  }[color];

  return (
    <div className={`acrylic-card ${themes.border} ${themes.glow}`}>
      <div className="text-[7px] font-mono text-white/30">{label}</div>
      <div className="flex items-center gap-2 mt-1">
        {icon}
        <span className={`text-[14px] font-bold ${themes.text}`}>{value}</span>
      </div>
    </div>
  );
}
