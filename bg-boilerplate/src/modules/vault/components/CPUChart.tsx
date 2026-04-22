/**
 * CPUChart — Indicador de uso de CPU estilizado com barra animada.
 */
import { motion } from 'motion/react';

export default function CPUChart({ usage }: { usage: number }) {
  const barColor = usage > 80 ? '#ef4444' : usage > 50 ? '#FF6200' : '#00FF41';

  return (
    <div className="acrylic-card flex-1">
      <div className="text-[7px] font-mono text-white/30 mb-2">CPU_LOAD_REAL_TIME</div>
      <div className="flex items-end gap-1 h-[60px]">
        {Array.from({ length: 20 }, (_, i) => {
          const h = Math.max(5, usage + Math.sin(i * 0.8) * 15);
          return (
            <motion.div
              key={i}
              className="flex-1 rounded-t"
              style={{ backgroundColor: barColor }}
              initial={{ height: 0 }}
              animate={{ height: `${Math.min(100, h)}%`, opacity: 0.3 + (h / 100) * 0.7 }}
              transition={{ duration: 0.4, delay: i * 0.02 }}
            />
          );
        })}
      </div>
      <div className="flex justify-between mt-1">
        <span className="text-[7px] font-mono text-white/20">0%</span>
        <span className="text-[9px] font-mono font-bold" style={{ color: barColor }}>{usage}%</span>
        <span className="text-[7px] font-mono text-white/20">100%</span>
      </div>
    </div>
  );
}
