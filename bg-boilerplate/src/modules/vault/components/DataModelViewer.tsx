/**
 * DataModelViewer — Exibição simplificada da estrutura de dados do MetricSnapshot.
 */
import { useState } from 'react';
import type { MetricSnapshot } from '../services/metricsService';

interface Props {
  metrics: MetricSnapshot;
}

export default function DataModelViewer({ metrics }: Props) {
  const [expanded, setExpanded] = useState(false);

  const summary = {
    cpu: metrics.cpu,
    mem: `${metrics.memory.percentage}%`,
    net_rx: `${metrics.network.rx} KB/s`,
    net_tx: `${metrics.network.tx} KB/s`,
    entropy: metrics.disk.entropy.toFixed(5),
    agents: metrics.agents.length,
    incidents: metrics.incidents.length,
    phase: metrics.currentPhase,
  };

  return (
    <div className="acrylic-card">
      <button
        onClick={() => setExpanded(!expanded)}
        className="text-[7px] font-mono text-[#00FFFF]/50 hover:text-[#00FFFF] transition-colors w-full text-left"
      >
        {expanded ? '[-]' : '[+]'} DATA_MODEL_INSPECTOR
      </button>
      {expanded && (
        <pre className="text-[7px] font-mono text-white/30 mt-2 whitespace-pre-wrap leading-relaxed overflow-auto max-h-[120px] custom-scrollbar">
          {JSON.stringify(summary, null, 2)}
        </pre>
      )}
    </div>
  );
}
