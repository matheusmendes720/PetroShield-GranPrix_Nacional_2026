import { useState } from 'react';
import {
  PieChart, Pie, Cell, BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, AreaChart, Area,
  RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis,
} from 'recharts';
import {
  MONTHLY_METRICS, THREAT_PATTERNS, OKRS,
  getAlertDistribution, getScenarioFinancialImpact, getIncidentFunnel, getCumulativeCostAvoided
} from '../data/mockData';

// ── Custom Tooltip ────────────────────────────────────────────────
function CustomTooltip({ active, payload, label }: { active?: boolean; payload?: Array<{ value: number; name: string; color: string }>; label?: string }) {
  if (!active || !payload) return null;
  return (
    <div style={{
      background: 'rgba(10,10,10,0.9)', border: '1px solid rgba(0,255,65,0.2)',
      borderRadius: 8, padding: '10px 14px', backdropFilter: 'blur(12px)',
      fontFamily: 'var(--font-mono)', fontSize: '0.75rem',
    }}>
      <div style={{ color: '#00FFFF', marginBottom: 4 }}>{label}</div>
      {payload.map((p, i) => (
        <div key={i} style={{ color: p.color || '#00FF41' }}>
          {p.name}: {typeof p.value === 'number' ? p.value.toLocaleString() : p.value}
        </div>
      ))}
    </div>
  );
}

// ── Sub: Threat Analytics ─────────────────────────────────────────
function ThreatAnalytics() {
  const alertDist = getAlertDistribution();
  const funnel = getIncidentFunnel();
  const mitreData = THREAT_PATTERNS
    .sort((a, b) => b.detection_count_30d - a.detection_count_30d)
    .slice(0, 8)
    .map(t => ({ name: t.pattern_name, count: t.detection_count_30d, technique: t.mitre_technique }));

  const mttrData = MONTHLY_METRICS.map(m => ({
    month: m.month.replace('20', ''),
    latency: m.avg_latency_ms,
    blocked: m.incidents_blocked,
    escalated: m.incidents_escalated,
  }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)' }}>
      {/* Row 1: Donut + Funnel + MITRE */}
      <div className="grid-3">
        {/* Alert Distribution Donut */}
        <div className="glass-card animate-in">
          <div className="glass-card-title"><span className="indicator" /> Alert Distribution</div>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <ResponsiveContainer width="100%" height={220}>
              <PieChart>
                <Pie data={alertDist} cx="50%" cy="50%" innerRadius={55} outerRadius={85} paddingAngle={3} dataKey="value">
                  {alertDist.map((entry, i) => <Cell key={i} fill={entry.color} stroke="transparent" />)}
                </Pie>
                <Tooltip content={<CustomTooltip />} />
              </PieChart>
            </ResponsiveContainer>
          </div>
          <div style={{ display: 'flex', justifyContent: 'center', gap: 12, marginTop: 8 }}>
            {alertDist.map(a => (
              <div key={a.name} style={{ textAlign: 'center' }}>
                <div style={{ fontFamily: 'var(--font-terminal)', fontSize: '1.3rem', color: a.color }}>{a.value}</div>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.6rem', color: '#999' }}>{a.name}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Incident Funnel */}
        <div className="glass-card animate-in animate-in-delay-1">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> Incident Funnel</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 16 }}>
            {funnel.map((stage, i) => {
              const widthPct = (stage.value / funnel[0].value) * 100;
              return (
                <div key={i} style={{ textAlign: 'center' }}>
                  <div style={{
                    margin: '0 auto', padding: '10px 16px',
                    background: `${stage.color}15`, border: `1px solid ${stage.color}40`,
                    borderRadius: 6, width: `${Math.max(widthPct, 20)}%`,
                    fontFamily: 'var(--font-terminal)', fontSize: '1.1rem',
                    color: stage.color, transition: 'width 1s ease',
                  }}>
                    {stage.value.toLocaleString()}
                  </div>
                  <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.6rem', color: '#999', marginTop: 2 }}>{stage.stage}</div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Top MITRE Tactics */}
        <div className="glass-card animate-in animate-in-delay-2">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF3333' }} /> Top MITRE ATT&CK</div>
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={mitreData} layout="vertical" margin={{ left: 16, right: 16 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
              <XAxis type="number" stroke="#555" tick={{ fill: '#999', fontSize: 11 }} />
              <YAxis dataKey="name" type="category" width={130} stroke="#555" tick={{ fill: '#aaa', fontSize: 10 }} />
              <Tooltip content={<CustomTooltip />} />
              <Bar dataKey="count" radius={[0, 4, 4, 0]}>
                {mitreData.map((_, i) => (
                  <Cell key={i} fill={i === 0 ? '#FF3333' : i < 3 ? '#FF6200' : '#00FF41'} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Row 2: MTTR Trend + Incidents over Time */}
      <div className="grid-2">
        <div className="glass-card animate-in animate-in-delay-3">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> MTTR Trend (Latência Média)</div>
          <ResponsiveContainer width="100%" height={240}>
            <AreaChart data={mttrData}>
              <defs>
                <linearGradient id="gradLatency" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#00FFFF" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#00FFFF" stopOpacity={0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
              <XAxis dataKey="month" stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
              <YAxis stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
              <Tooltip content={<CustomTooltip />} />
              <Area type="monotone" dataKey="latency" stroke="#00FFFF" fill="url(#gradLatency)" strokeWidth={2} dot={{ fill: '#00FFFF', r: 3 }} />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        <div className="glass-card animate-in animate-in-delay-4">
          <div className="glass-card-title"><span className="indicator" /> Incidents — Blocked vs Escalated</div>
          <ResponsiveContainer width="100%" height={240}>
            <BarChart data={mttrData}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
              <XAxis dataKey="month" stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
              <YAxis stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
              <Tooltip content={<CustomTooltip />} />
              <Bar dataKey="blocked" fill="#00FF41" radius={[4, 4, 0, 0]} name="Blocked" />
              <Bar dataKey="escalated" fill="#FF6200" radius={[4, 4, 0, 0]} name="Escalated" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}

// ── Sub: Financial Impact ─────────────────────────────────────────
function FinancialImpact() {
  const scenarioData = getScenarioFinancialImpact();
  const cumCost = getCumulativeCostAvoided();
  const monthlyTrend = MONTHLY_METRICS.map(m => ({
    month: m.month.replace('20', ''),
    cost: m.cost_avoided_brl / 1e6,
    queries: m.queries_processed / 1000,
    leaks: m.leaks_prevented,
  }));

  const radarData = [
    { subject: 'DLP', A: 99.8, fullMark: 100 },
    { subject: 'OT Shield', A: 97, fullMark: 100 },
    { subject: 'Vendor Risk', A: 88, fullMark: 100 },
    { subject: 'Fleet Vax', A: 93, fullMark: 100 },
    { subject: 'LGPD', A: 100, fullMark: 100 },
    { subject: 'MTTD', A: 92, fullMark: 100 },
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)' }}>
      {/* Top KPIs */}
      <div className="grid-4 animate-in">
        <div className="glass-card glow-green metric-card">
          <div className="glass-card-title"><span className="indicator" /> Custo Evitado Total</div>
          <div className="metric-value" style={{ fontSize: '2rem' }}>R$ {(cumCost / 1e6).toFixed(1)}M</div>
          <div className="metric-label">Acumulado 12 meses</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> Revenue Protected</div>
          <div className="metric-value orange" style={{ fontSize: '2rem' }}>R$ 4.2B</div>
          <div className="metric-label">Valor de contratos protegidos</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> Downtime Saved</div>
          <div className="metric-value cyan" style={{ fontSize: '2rem' }}>2,340h</div>
          <div className="metric-label">Horas de operação salvas</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF3333' }} /> Fines Avoided</div>
          <div className="metric-value red" style={{ fontSize: '2rem' }}>R$ 50M</div>
          <div className="metric-label">Multa LGPD máxima evitada</div>
        </div>
      </div>

      {/* Charts Row */}
      <div className="grid-2">
        <div className="glass-card animate-in animate-in-delay-1">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> Financial Impact por Playbook (R$)</div>
          <ResponsiveContainer width="100%" height={280}>
            <BarChart data={scenarioData}>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
              <XAxis dataKey="scenario" stroke="#555" tick={{ fill: '#999', fontSize: 10 }} angle={-30} textAnchor="end" height={60} />
              <YAxis stroke="#555" tick={{ fill: '#999', fontSize: 10 }} tickFormatter={v => `${(v/1000).toFixed(0)}k`} />
              <Tooltip content={<CustomTooltip />} />
              <Bar dataKey="cost_avoided" radius={[6, 6, 0, 0]} name="Cost Avoided (R$)">
                {scenarioData.map((_, i) => (
                  <Cell key={i} fill={['#00FF41', '#00cc34', '#FF6200', '#FF9500', '#FF3333', '#00FFFF', '#00cccc', '#FF6200'][i]} />
                ))}
              </Bar>
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="glass-card animate-in animate-in-delay-2">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> AxeGuard Coverage Radar</div>
          <ResponsiveContainer width="100%" height={280}>
            <RadarChart data={radarData}>
              <PolarGrid stroke="rgba(255,255,255,0.08)" />
              <PolarAngleAxis dataKey="subject" tick={{ fill: '#999', fontSize: 11 }} />
              <PolarRadiusAxis tick={false} axisLine={false} />
              <Radar name="Coverage" dataKey="A" stroke="#00FF41" fill="#00FF41" fillOpacity={0.15} strokeWidth={2} />
            </RadarChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Monthly Cost Trend + OKRs */}
      <div className="grid-2">
        <div className="glass-card animate-in animate-in-delay-3">
          <div className="glass-card-title"><span className="indicator" /> Cost Avoided Trend (R$ Milhões)</div>
          <ResponsiveContainer width="100%" height={240}>
            <AreaChart data={monthlyTrend}>
              <defs>
                <linearGradient id="gradCost" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="#00FF41" stopOpacity={0.3} />
                  <stop offset="95%" stopColor="#00FF41" stopOpacity={0} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
              <XAxis dataKey="month" stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
              <YAxis stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
              <Tooltip content={<CustomTooltip />} />
              <Area type="monotone" dataKey="cost" stroke="#00FF41" fill="url(#gradCost)" strokeWidth={2} dot={{ fill: '#00FF41', r: 3 }} name="R$ Milhões" />
            </AreaChart>
          </ResponsiveContainer>
        </div>

        <div className="glass-card animate-in animate-in-delay-4">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> OKRs & KPIs</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 14, marginTop: 8 }}>
            {Object.values(OKRS).slice(0, 6).map((okr, i) => (
              <div key={i}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
                  <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.7rem', color: '#ccc' }}>
                    {okr.status === 'on_track' ? '✓' : '⚠'} {okr.name}
                  </span>
                  <span style={{ fontFamily: 'var(--font-terminal)', fontSize: '0.9rem', color: okr.status === 'on_track' ? '#00FF41' : '#FF6200' }}>
                    {okr.progress_pct}%
                  </span>
                </div>
                <div className="progress-bar">
                  <div
                    className={`progress-fill ${okr.status === 'on_track' ? 'green' : 'orange'}`}
                    style={{ width: `${okr.progress_pct}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

// ── Página: SOC Metrics ───────────────────────────────────────────
export default function SOCMetrics() {
  const [activeTab, setActiveTab] = useState<'threat' | 'financial'>('threat');

  return (
    <div className="page-container">
      <div className="sub-tabs animate-in">
        <button className={`sub-tab ${activeTab === 'threat' ? 'active' : ''}`} onClick={() => setActiveTab('threat')}>
          ▸ Threat Analytics
        </button>
        <button className={`sub-tab ${activeTab === 'financial' ? 'active' : ''}`} onClick={() => setActiveTab('financial')}>
          ▸ Financial Impact
        </button>
      </div>
      {activeTab === 'threat' ? <ThreatAnalytics /> : <FinancialImpact />}
    </div>
  );
}
