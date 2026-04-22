/**
 * NetworkTrafficChart — Visualização de tráfego RX/TX em tempo real.
 */
import { motion } from 'motion/react';

export default function NetworkTrafficChart({ rx, tx }: { rx: number; tx: number }) {
  const maxVal = Math.max(rx, tx, 1);
  return (
    <div className="acrylic-card flex-1">
      <div className="text-[7px] font-mono text-white/30 mb-2">NETWORK_THROUGHPUT</div>
      <div className="space-y-2">
        <div>
          <div className="flex justify-between text-[7px] font-mono text-white/30 mb-0.5">
            <span>RX (Ingress)</span><span className="text-[#00FFFF]">{rx} KB/s</span>
          </div>
          <div className="h-2 bg-white/5 rounded-full overflow-hidden">
            <motion.div className="h-full bg-[#00FFFF] rounded-full" animate={{ width: `${(rx / maxVal) * 100}%` }} transition={{ duration: 0.5 }} />
          </div>
        </div>
        <div>
          <div className="flex justify-between text-[7px] font-mono text-white/30 mb-0.5">
            <span>TX (Egress)</span><span className="text-[#FF6200]">{tx} KB/s</span>
          </div>
          <div className="h-2 bg-white/5 rounded-full overflow-hidden">
            <motion.div className="h-full bg-[#FF6200] rounded-full" animate={{ width: `${(tx / maxVal) * 100}%` }} transition={{ duration: 0.5 }} />
          </div>
        </div>
      </div>
    </div>
  );
}
