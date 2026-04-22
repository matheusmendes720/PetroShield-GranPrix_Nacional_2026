/**
 * ThreatMap — Mapa de ameaças global com pontos simulados.
 * Removida dependência do D3.js — usa SVG estático com posicionamento relativo.
 */
import { useState, useEffect } from 'react';
import { motion } from 'motion/react';
import { cn } from '../lib/utils';

interface ThreatEvent {
  id: string;
  x: number; // percentage
  y: number; // percentage
  type: 'SQLi' | 'DDoS' | 'Exfiltration' | 'SCADA';
  severity: 'critical' | 'warn' | 'info';
  location: string;
  timestamp: string;
}

const MOCK_THREATS: ThreatEvent[] = [
  { id: '1', x: 42, y: 55, type: 'SCADA', severity: 'critical', location: 'Camaçari, BA', timestamp: new Date().toISOString() },
  { id: '2', x: 45, y: 48, type: 'SQLi', severity: 'warn', location: 'Rio de Janeiro, RJ', timestamp: new Date().toISOString() },
  { id: '3', x: 44, y: 60, type: 'DDoS', severity: 'info', location: 'Curitiba, PR', timestamp: new Date().toISOString() },
  { id: '4', x: 30, y: 30, type: 'Exfiltration', severity: 'warn', location: 'New York, US', timestamp: new Date().toISOString() },
  { id: '5', x: 50, y: 25, type: 'SQLi', severity: 'critical', location: 'London, UK', timestamp: new Date().toISOString() },
  { id: '6', x: 75, y: 35, type: 'SCADA', severity: 'info', location: 'Tokyo, JP', timestamp: new Date().toISOString() },
];

export const ThreatMap = () => {
  const [threats, setThreats] = useState<ThreatEvent[]>(MOCK_THREATS);

  useEffect(() => {
    const interval = setInterval(() => {
      const types: ThreatEvent['type'][] = ['SQLi', 'DDoS', 'Exfiltration', 'SCADA'];
      const severities: ThreatEvent['severity'][] = ['critical', 'warn', 'info'];
      const newThreat: ThreatEvent = {
        id: Math.random().toString(36).substr(2, 6),
        x: 10 + Math.random() * 80,
        y: 15 + Math.random() * 65,
        type: types[Math.floor(Math.random() * types.length)],
        severity: severities[Math.floor(Math.random() * severities.length)],
        location: `Node-${Math.floor(Math.random() * 999)}`,
        timestamp: new Date().toISOString(),
      };
      setThreats(prev => [...prev.slice(-12), newThreat]);
    }, 12000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="glass-panel rounded-xl overflow-hidden relative">
      <div className="flex items-center justify-between px-4 py-2 border-b border-white/5">
        <span className="text-[10px] font-mono text-accent-cyan/70 tracking-widest">PetroShield Global Asset Map</span>
        <div className="flex items-center gap-4 text-[9px] font-mono">
          <span className="flex items-center gap-1"><span className="w-1.5 h-1.5 rounded-full bg-accent-red" /> Critical</span>
          <span className="flex items-center gap-1"><span className="w-1.5 h-1.5 rounded-full bg-yellow-400" /> Warning</span>
          <span className="flex items-center gap-1"><span className="w-1.5 h-1.5 rounded-full bg-accent-cyan" /> Info</span>
        </div>
      </div>
      {/* Map Area */}
      <div className="relative w-full" style={{ paddingBottom: '50%', background: 'radial-gradient(ellipse at 50% 50%, #0a1929 0%, #050505 100%)' }}>
        {/* Grid lines */}
        <svg className="absolute inset-0 w-full h-full" viewBox="0 0 100 50" preserveAspectRatio="none">
          {Array.from({ length: 10 }, (_, i) => (
            <line key={`h${i}`} x1={0} y1={i * 5} x2={100} y2={i * 5} stroke="#00f2ff" strokeOpacity={0.03} strokeWidth={0.1} />
          ))}
          {Array.from({ length: 20 }, (_, i) => (
            <line key={`v${i}`} x1={i * 5} y1={0} x2={i * 5} y2={50} stroke="#00f2ff" strokeOpacity={0.03} strokeWidth={0.1} />
          ))}
        </svg>
        {/* Threat dots */}
        {threats.map((threat) => (
          <motion.div
            key={threat.id}
            className="absolute group"
            style={{ left: `${threat.x}%`, top: `${threat.y}%`, transform: 'translate(-50%, -50%)' }}
            initial={{ scale: 0 }}
            animate={{ scale: 1 }}
          >
            <div className={cn(
              "w-3 h-3 rounded-full animate-pulse",
              threat.severity === 'critical' && 'bg-accent-red shadow-[0_0_10px_rgba(255,49,49,0.5)]',
              threat.severity === 'warn' && 'bg-yellow-400 shadow-[0_0_10px_rgba(255,200,0,0.5)]',
              threat.severity === 'info' && 'bg-accent-cyan shadow-[0_0_10px_rgba(0,242,255,0.5)]',
            )} />
            <div className="hidden group-hover:block absolute bottom-full left-1/2 -translate-x-1/2 mb-2 bg-black/90 border border-white/10 rounded-lg p-2 text-[9px] font-mono whitespace-nowrap z-50">
              <div className="text-accent-cyan">{threat.type}</div>
              <div className="text-white/50">{threat.location}</div>
              <div className="text-white/30">{new Date(threat.timestamp).toLocaleTimeString()}</div>
            </div>
          </motion.div>
        ))}
      </div>
      {/* Threat List */}
      <div className="p-3 border-t border-white/5 space-y-1 max-h-[150px] overflow-y-auto">
        <div className="text-[9px] font-mono text-accent-cyan/50 tracking-widest mb-2">Active Incidents</div>
        {threats.map((threat) => (
          <div key={threat.id} className="flex items-center gap-2 text-[10px] font-mono py-1 border-b border-white/5 last:border-0">
            <span className={cn(
              "text-[8px] uppercase font-bold px-1 rounded",
              threat.severity === 'critical' && 'bg-accent-red/20 text-accent-red',
              threat.severity === 'warn' && 'bg-yellow-400/20 text-yellow-400',
              threat.severity === 'info' && 'bg-accent-cyan/20 text-accent-cyan',
            )}>{threat.severity}</span>
            <span className="text-white/30">{new Date(threat.timestamp).toLocaleTimeString()}</span>
            <span className="text-white/60">{threat.type}</span>
            <span className="text-accent-cyan/30 ml-auto">{threat.location}</span>
          </div>
        ))}
      </div>
    </div>
  );
};
