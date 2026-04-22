/**
 * SOCLifecycleStage — Indicador visual do ciclo de vida SOC.
 */
import { motion } from 'motion/react';
import type { SOCLifecyclePhase } from '../services/metricsService';

interface Props {
  currentPhase: SOCLifecyclePhase;
}

const PHASES: SOCLifecyclePhase[] = [
  'MONITOR', 'DETECT', 'TRIAGE_L1', 'ANALYSIS_L2', 'RESPONSE_L3', 'RECOVERY', 'HUNT', 'LESSONS_LEARNT'
];

export default function SOCLifecycleStage({ currentPhase }: Props) {
  return (
    <div className="acrylic-card">
      <div className="text-[7px] font-mono text-white/30 mb-2">SOC_LIFECYCLE_PHASE</div>
      <div className="flex items-center gap-1">
        {PHASES.map((phase, i) => {
          const isCurrent = phase === currentPhase;
          const isPast = PHASES.indexOf(currentPhase) > i;
          return (
            <div key={phase} className="flex-1 flex flex-col items-center gap-1">
              <motion.div
                className={`w-full h-1.5 rounded-full ${isCurrent ? 'bg-[#00FF41]' : isPast ? 'bg-[#00FF41]/30' : 'bg-white/5'}`}
                animate={isCurrent ? { boxShadow: ['0 0 4px #00FF41', '0 0 12px #00FF41', '0 0 4px #00FF41'] } : {}}
                transition={{ duration: 1.5, repeat: Infinity }}
              />
              <span className={`text-[5px] font-mono ${isCurrent ? 'text-[#00FF41]' : 'text-white/15'}`}>
                {phase.replace(/_/g, ' ').slice(0, 8)}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
