import React from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { X } from 'lucide-react';

interface AgentDetailModalProps {
  agent: { label: string; status: string; score: number } | null;
  onClose: () => void;
}

export const AgentDetailModal: React.FC<AgentDetailModalProps> = ({ agent, onClose }) => {
  if (!agent) return null;

  return (
    <AnimatePresence>
      <motion.div
        className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
      >
        <motion.div
          className="w-full max-w-lg bg-[#0a1929] border border-white/10 rounded-2xl p-6 relative"
          initial={{ scale: 0.9, opacity: 0 }}
          animate={{ scale: 1, opacity: 1 }}
          exit={{ scale: 0.9, opacity: 0 }}
          onClick={(e) => e.stopPropagation()}
        >
          {/* Header */}
          <div className="flex justify-between items-start mb-6">
            <div>
              <h3 className="text-lg font-semibold text-accent-cyan">{agent.label}</h3>
              <p className="text-[10px] text-white/40 font-mono">Autonomous Agent Profile</p>
            </div>
            <button onClick={onClose} className="text-white/30 hover:text-white">
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-3 gap-4 mb-6">
            <div className="text-center p-3 rounded-lg bg-white/5">
              <div className="text-[9px] text-white/40 font-mono">Reliability</div>
              <div className="text-lg font-bold text-accent-green">{(agent.score * 100).toFixed(1)}%</div>
            </div>
            <div className="text-center p-3 rounded-lg bg-white/5">
              <div className="text-[9px] text-white/40 font-mono">Status</div>
              <div className="text-lg font-bold text-accent-cyan">{agent.status}</div>
            </div>
            <div className="text-center p-3 rounded-lg bg-white/5">
              <div className="text-[9px] text-white/40 font-mono">Uptime</div>
              <div className="text-lg font-bold text-white">99.9%</div>
            </div>
          </div>

          {/* Performance Chart Placeholder */}
          <div className="p-4 rounded-lg bg-white/3 border border-white/5 mb-4">
            <div className="text-[9px] text-white/40 font-mono mb-2">Performance Baseline</div>
            <div className="flex items-end gap-[2px] h-20">
              {Array.from({ length: 24 }).map((_, i) => (
                <div
                  key={i}
                  className="flex-1 bg-accent-cyan/20 rounded-t"
                  style={{ height: `${30 + Math.random() * 70}%` }}
                />
              ))}
            </div>
          </div>

          {/* Footer */}
          <button
            onClick={onClose}
            className="w-full py-2 mt-2 text-[10px] font-mono text-accent-cyan/70 border border-accent-cyan/20 rounded-lg hover:bg-accent-cyan/5 transition-colors"
          >
            Close Profile
          </button>
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
};
