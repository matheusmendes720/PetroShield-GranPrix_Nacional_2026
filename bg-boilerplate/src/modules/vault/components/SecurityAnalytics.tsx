/**
 * SecurityAnalytics — Painel de análise de ameaças com histograma e score.
 */
import { motion } from 'motion/react';
import type { ThreatEvent } from '../services/metricsService';

interface Props {
  threatData: { time: string; count: number }[];
  threatScore: number;
  threatStream: ThreatEvent[];
}

export default function SecurityAnalytics({ threatData, threatScore, threatStream: _threatStream }: Props) {
  return (
    <div className="acrylic-card flex flex-col">
      <div className="text-[7px] font-mono text-white/30 mb-2">THREAT_ANALYSIS_ENGINE</div>
      <div className="flex items-center gap-2 mb-2">
        <span className="text-[7px] font-mono text-white/20">SCORE:</span>
        <span className={`text-[12px] font-bold font-mono ${threatScore > 60 ? 'text-[#ef4444] glow-text-red' : 'text-[#00FF41] glow-text-green'}`}>
          {threatScore}
        </span>
        <span className="text-[7px] text-white/20 font-mono">/100</span>
      </div>
      <div className="flex items-end gap-px h-[50px] flex-1">
        {threatData.map((d, i) => (
          <motion.div
            key={i}
            className="flex-1 rounded-t"
            style={{ backgroundColor: d.count > 60 ? '#ef4444' : d.count > 30 ? '#FF6200' : '#00FF41' }}
            initial={{ height: 0 }}
            animate={{ height: `${Math.min(100, (d.count / 100) * 100)}%`, opacity: 0.4 + (d.count / 100) * 0.6 }}
            transition={{ duration: 0.3, delay: i * 0.03 }}
          />
        ))}
      </div>
      <div className="flex justify-between text-[6px] font-mono text-white/15 mt-1">
        {threatData.slice(0, 4).map((d, i) => <span key={i}>{d.time}</span>)}
      </div>
    </div>
  );
}
