/**
 * BeaconApp — Entry point do módulo Beacon (Finance CyberSec Dashboard).
 * Todas as chamadas a /api/* foram substituídas por dados mockados para deploy estático.
 */
import { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Shield } from 'lucide-react';
import { Terminal } from './components/Terminal';
import { ThreatTrendChart, SavingsChart, ScadaHealthChart } from './components/DashboardCharts';
import { Radar } from './components/Radar';
import { ThreatMap } from './components/ThreatMap';
import { AgentDetailModal } from './components/AgentDetailModal';
import { cn } from './lib/utils';

type Page = 'ops' | 'map' | 'dlp' | 'profit' | 'eval';

// Mock stats — replaces /api/stats
const MOCK_STATS = {
  threatsBlocked: 1248,
  dataSaves: '4.2 TB',
  profitSaved: '$12.5M',
  systemHealth: 99.2,
  agentEfficiency: 98.5,
  dlpPrevention: 99.98,
};

// Mock vendors — replaces /api/vendors
const MOCK_VENDORS = [
  { id: 'OCEANICA_ENG', name: 'Oceânica Engenharia', riskLevel: 'CRITICAL', riskScore: 88 },
  { id: 'PETRO_TECH', name: 'PetroTech Solutions', riskLevel: 'MODERATE', riskScore: 45 },
];

export default function BeaconApp() {
  const [activePage, setActivePage] = useState<Page>('ops');
  const [selectedAgent, setSelectedAgent] = useState<any>(null);
  const [stats] = useState(MOCK_STATS);
  const [vendors] = useState(MOCK_VENDORS);

  const NavItem = ({ label, id, active }: { label: string; id: Page; active: boolean }) => (
    <button
      onClick={() => setActivePage(id)}
      className={cn(
        "px-4 py-2 text-[11px] uppercase tracking-widest transition-all duration-300 relative",
        active ? "text-accent-cyan" : "text-white/40 hover:text-white/60"
      )}
    >
      {label}
      {active && (
        <motion.div layoutId="activeTab" className="absolute bottom-0 left-0 right-0 h-[2px] bg-accent-cyan" />
      )}
    </button>
  );

  return (
    <div className="w-full min-h-screen flex flex-col" style={{ background: '#05070a' }}>
      {/* Header */}
      <header className="flex items-center justify-between px-6 py-3 border-b border-white/5 bg-black/40 backdrop-blur-md">
        <div className="flex items-center gap-3">
          <Shield className="w-5 h-5 text-accent-cyan" />
          <span className="text-[11px] font-mono text-accent-cyan/80 tracking-widest">NEBULA SOC / UNIT-01</span>
        </div>
        <nav className="hidden md:flex items-center gap-1">
          <NavItem label="Operations" id="ops" active={activePage === 'ops'} />
          <NavItem label="Threat Map" id="map" active={activePage === 'map'} />
          <NavItem label="DLP Shield" id="dlp" active={activePage === 'dlp'} />
          <NavItem label="Profit" id="profit" active={activePage === 'profit'} />
          <NavItem label="Agent Eval" id="eval" active={activePage === 'eval'} />
        </nav>
        <div className="flex items-center gap-4 text-[9px] font-mono text-white/30">
          <span>System Load: 14%</span>
          <span>Active Agents: 08</span>
        </div>
      </header>

      <div className="flex flex-1 overflow-hidden">
        {/* Sidebar */}
        <aside className="hidden lg:flex flex-col w-[280px] border-r border-white/5 bg-black/20 p-4 gap-4 overflow-y-auto">
          <div className="p-4 rounded-xl bg-white/3 border border-white/5">
            <div className="text-[9px] text-white/40 font-mono mb-1">Total Profit Saved (MTD)</div>
            <div className="text-2xl font-bold text-accent-green">{stats.profitSaved}</div>
            <div className="text-[9px] text-accent-green/60 mt-1">+14.2% vs Prev Qtr</div>
          </div>
          <div className="p-4 rounded-xl bg-white/3 border border-white/5">
            <div className="text-[9px] text-white/40 font-mono mb-2">Vendor Risk Spotlight</div>
            {vendors.filter(v => v.riskLevel === 'CRITICAL').map(vendor => (
              <div key={vendor.id} className="p-2 rounded-lg bg-accent-red/5 border border-accent-red/20 mb-2">
                <div className="text-[11px] text-white/70">{vendor.name}</div>
                <div className="text-[9px] text-accent-red font-mono">CRITICAL</div>
                <div className="text-[9px] text-white/30">Risk Score: {vendor.riskScore}</div>
                {vendor.id === 'OCEANICA_ENG' && (
                  <div className="text-[8px] text-yellow-400 mt-1 font-mono">AUTO-SUSPEND TRIGGERED</div>
                )}
              </div>
            ))}
          </div>
          <div className="p-4 rounded-xl bg-white/3 border border-white/5">
            <div className="text-[9px] text-white/40 font-mono mb-1">DLP Shield Status</div>
            <div className="text-xl font-bold text-accent-cyan">{stats.dlpPrevention}%</div>
            <div className="text-[9px] text-accent-cyan/50 mt-1">90GB Leak Prevented</div>
          </div>
          <div className="p-4 rounded-xl bg-white/3 border border-white/5">
            <div className="text-[9px] text-white/40 font-mono mb-1">Agent Reliability</div>
            <div className="text-xl font-bold text-accent-green">{stats.agentEfficiency}%</div>
            <div className="text-[9px] text-accent-green/50 mt-1">LUMEN-7: ACTIVE</div>
          </div>
        </aside>

        {/* Main Content Area */}
        <main className="flex-1 p-4 md:p-6 overflow-y-auto">
          <AnimatePresence mode="wait">
            {activePage === 'ops' && (
              <motion.div key="ops" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-6">
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  {/* Threat Velocity */}
                  <div className="glass-panel rounded-xl p-4">
                    <div className="text-[10px] text-accent-cyan/50 font-mono mb-3">Threat Propagation Velocity</div>
                    <div className="flex items-end gap-1 h-20 px-2">
                      {[20, 35, 45, 65, 75, 55, 40, 60].map((h, i) => (
                        <motion.div
                          key={i}
                          className="flex-1 bg-accent-cyan/20 rounded-t"
                          initial={{ height: 0 }}
                          animate={{ height: `${h}%` }}
                          transition={{ delay: i * 0.1 }}
                        />
                      ))}
                    </div>
                    <div className="flex justify-between text-[8px] text-white/20 font-mono mt-2 px-2">
                      <span>08:00</span><span>12:00</span><span>16:00</span><span>20:00</span>
                    </div>
                  </div>
                  {/* SCADA Grid */}
                  <div className="glass-panel rounded-xl p-4">
                    <div className="text-[10px] text-accent-cyan/50 font-mono mb-3">SCADA Defensive Grid</div>
                    <Radar />
                  </div>
                </div>
                {/* Live Feed & Charts */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  <div className="glass-panel rounded-xl p-4">
                    <div className="text-[10px] text-accent-cyan/50 font-mono mb-3">Live Threat Feed</div>
                    {[
                      { time: '14:22:01', msg: 'SQLi Attempt blocked at Refinery DMZ', type: 'critical' },
                      { time: '14:18:55', msg: 'Unusual traffic pattern in HR subnet', type: 'warn' },
                      { time: '14:10:12', msg: 'DLP Trigger: Unauthorized exfil', type: 'critical' },
                      { time: '14:05:30', msg: 'Modbus packet isolated on Port 502', type: 'info' },
                    ].map((alert, i) => (
                      <div key={i} className="flex items-center gap-3 py-2 border-b border-white/5 last:border-0 text-[10px] font-mono">
                        <span className="text-white/30">{alert.time}</span>
                        <span className={cn(
                          alert.type === 'critical' && 'text-accent-red',
                          alert.type === 'warn' && 'text-yellow-400',
                          alert.type === 'info' && 'text-accent-cyan/60',
                        )}>{alert.msg}</span>
                      </div>
                    ))}
                  </div>
                  <div className="glass-panel rounded-xl p-4">
                    <div className="text-[10px] text-accent-cyan/50 font-mono mb-3">Historical SCADA Asset Health (24h)</div>
                    <ScadaHealthChart />
                  </div>
                </div>
                {/* Terminal */}
                <div className="h-[300px]">
                  <Terminal />
                </div>
              </motion.div>
            )}

            {activePage === 'map' && (
              <motion.div key="map" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}>
                <ThreatMap />
              </motion.div>
            )}

            {activePage === 'dlp' && (
              <motion.div key="dlp" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-6">
                <div className="grid grid-cols-3 gap-4">
                  {[
                    { label: 'Exfiltration Attempts', value: '1,248' },
                    { label: 'Protected Endpoints', value: '4,502' },
                    { label: 'Policy Violations', value: '0' },
                  ].map((stat, i) => (
                    <div key={i} className="glass-panel rounded-xl p-4 text-center">
                      <div className="text-[9px] text-white/40 font-mono">{stat.label}</div>
                      <div className="text-2xl font-bold text-accent-cyan mt-2">{stat.value}</div>
                    </div>
                  ))}
                </div>
                <div className="glass-panel rounded-xl p-4">
                  <div className="text-[10px] text-accent-cyan/50 font-mono mb-3">DLP Detection Trend (24h)</div>
                  <ThreatTrendChart />
                </div>
              </motion.div>
            )}

            {activePage === 'profit' && (
              <motion.div key="profit" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-4">
                <div className="glass-panel rounded-xl p-6">
                  <div className="text-[10px] text-accent-cyan/50 font-mono mb-4">Profit Saved by Sector</div>
                  {[
                    { sector: 'SCADA Infrastructure', amount: '$5.2M', trend: '+8%' },
                    { sector: 'Data Loss Prevention', amount: '$4.1M', trend: '+12%' },
                    { sector: 'Network Security', amount: '$2.1M', trend: '+5%' },
                    { sector: 'IoT Defense', amount: '$1.08M', trend: '+15%' },
                  ].map((item, i) => (
                    <div key={i} className="flex items-center justify-between py-3 border-b border-white/5 last:border-0">
                      <span className="text-[11px] text-white/70">{item.sector}</span>
                      <span className="text-accent-green font-mono text-sm">{item.amount}</span>
                      <span className="text-[9px] text-accent-green/60 font-mono">{item.trend}</span>
                    </div>
                  ))}
                </div>
                <div className="glass-panel rounded-xl p-4">
                  <SavingsChart />
                </div>
              </motion.div>
            )}

            {activePage === 'eval' && (
              <motion.div key="eval" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} className="space-y-6">
                <div className="glass-panel rounded-xl p-6">
                  <div className="text-[10px] text-accent-cyan/50 font-mono mb-4">Agentic Loop Performance</div>
                  <div className="grid grid-cols-2 gap-4">
                    {[
                      { label: 'DLP_AGENT_01', status: 'Optimal', score: 0.98 },
                      { label: 'SCADA_GUARD_04', status: 'Optimal', score: 0.99 },
                      { label: 'NETWORK_SCAN_02', status: 'Learning', score: 0.85 },
                      { label: 'AUTH_SENTRY_09', status: 'Optimal', score: 0.97 },
                    ].map((agent, i) => (
                      <motion.div
                        key={i}
                        whileHover={{ scale: 1.02 }}
                        onClick={() => setSelectedAgent(agent)}
                        className="p-4 rounded-lg bg-white/3 border border-white/5 cursor-pointer transition-all"
                      >
                        <div className="text-[10px] font-mono text-accent-cyan/80">{agent.label}</div>
                        <div className="text-[9px] text-white/40 mt-1">{agent.status}</div>
                        <div className="text-lg font-bold text-accent-green mt-2">{(agent.score * 100).toFixed(0)}%</div>
                      </motion.div>
                    ))}
                  </div>
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </main>
      </div>

      {/* Global Modal */}
      <AgentDetailModal agent={selectedAgent} onClose={() => setSelectedAgent(null)} />
    </div>
  );
}
