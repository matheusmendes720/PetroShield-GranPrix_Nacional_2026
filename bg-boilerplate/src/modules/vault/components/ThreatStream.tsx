/**
 * ThreatStream — Feed de eventos de ameaça em tempo real.
 */
import { motion } from 'motion/react';
import type { ThreatEvent } from '../services/metricsService';

interface Props {
  events: ThreatEvent[];
}

export default function ThreatStream({ events }: Props) {
  return (
    <div className="acrylic-card flex flex-col overflow-hidden">
      <div className="text-[7px] font-mono text-white/30 mb-2">THREAT_STREAM_LIVE</div>
      <div className="flex-1 overflow-y-auto custom-scrollbar space-y-0.5">
        {events.slice(-15).reverse().map((ev, i) => (
          <motion.div
            key={ev.id + i}
            initial={{ opacity: 0, x: -10 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex items-center gap-2 text-[7px] font-mono py-0.5"
          >
            <div className={`w-1.5 h-1.5 rounded-full shrink-0 ${ev.severity === 'CRITICAL' ? 'bg-[#ef4444]' : ev.severity === 'HIGH' ? 'bg-[#FF6200]' : 'bg-[#00FF41]'}`} />
            <span className="text-white/20 shrink-0">{ev.id}</span>
            <span className="text-white/40 truncate">{ev.type}</span>
            <span className="text-[#00FFFF]/40 ml-auto shrink-0">{ev.source}</span>
          </motion.div>
        ))}
        {events.length === 0 && (
          <div className="text-[8px] font-mono text-white/15 text-center py-4">AWAITING_TELEMETRY...</div>
        )}
      </div>
    </div>
  );
}
