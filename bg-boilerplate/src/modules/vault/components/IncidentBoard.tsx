/**
 * IncidentBoard — Painel de incidentes e status dos agentes.
 */
import type { SecurityIncident, SecurityAgent } from '../services/metricsService';
import { motion, AnimatePresence } from 'motion/react';

interface Props {
  incidents: SecurityIncident[];
  agents: SecurityAgent[];
}

export default function IncidentBoard({ incidents, agents }: Props) {
  return (
    <div className="acrylic-card">
      <div className="text-[7px] font-mono text-white/30 mb-2">INCIDENT_BOARD</div>
      <AnimatePresence>
        {incidents.length === 0 ? (
          <div className="text-[8px] font-mono text-[#00FF41]/40 text-center py-2">ALL_CLEAR — 0 ACTIVE INCIDENTS</div>
        ) : (
          incidents.map(inc => (
            <motion.div
              key={inc.id}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="p-2 border border-[#ef4444]/20 rounded mb-1 bg-[#ef4444]/5"
            >
              <div className="flex justify-between text-[8px] font-mono">
                <span className="text-[#ef4444]">{inc.id}</span>
                <span className="text-white/30">{inc.severity}</span>
              </div>
              <div className="text-[7px] text-white/40 mt-1">{inc.summary}</div>
            </motion.div>
          ))
        )}
      </AnimatePresence>
      <div className="mt-2 space-y-1">
        <div className="text-[7px] font-mono text-white/30">AGENT_POOL</div>
        {agents.map(a => (
          <div key={a.id} className="flex items-center justify-between text-[7px] font-mono">
            <span className="text-white/40">{a.name}</span>
            <span className={a.status === 'MITIGATING' ? 'text-[#ef4444]' : a.status === 'ANALYZING' ? 'text-[#FF6200]' : 'text-[#00FF41]'}>
              {a.status}
            </span>
          </div>
        ))}
      </div>
    </div>
  );
}
