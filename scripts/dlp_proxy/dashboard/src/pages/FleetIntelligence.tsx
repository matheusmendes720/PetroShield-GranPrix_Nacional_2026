import { useState, useMemo } from 'react';
import {
  RadarChart, Radar, PolarGrid, PolarAngleAxis, PolarRadiusAxis,
  ResponsiveContainer, BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, Cell,
} from 'recharts';
import {
  VENDOR_RISK_DB, FLEET_REGISTRY, XR_DEVICES,
  getFleetHealth, getVendorRiskDistribution, type VendorRisk, type FleetNode
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

// ── Vendor Card ───────────────────────────────────────────────────
function VendorCard({ vendor, isSelected, onSelect }: { vendor: VendorRisk; isSelected: boolean; onSelect: () => void }) {
  const color = vendor.risk_level === 'CRITICAL' ? '#FF3333' : vendor.risk_level === 'HIGH' ? '#FF6200' : vendor.risk_level === 'MEDIUM' ? '#FF9500' : '#00FF41';
  const badgeClass = vendor.risk_level === 'CRITICAL' ? 'critical' : vendor.risk_level === 'HIGH' ? 'high' : vendor.risk_level === 'MEDIUM' ? 'medium' : 'low';

  return (
    <div
      className={`glass-card ${isSelected ? 'variant-cyan' : ''}`}
      onClick={onSelect}
      style={{ cursor: 'pointer', padding: 'var(--gap-md)', borderColor: isSelected ? '#00FFFF' : undefined }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 8 }}>
        <div>
          <div style={{ fontFamily: 'var(--font-mono)', fontWeight: 600, fontSize: '0.85rem', marginBottom: 2, color: '#e8e8e8' }}>{vendor.vendor_name}</div>
          <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: '#666' }}>{vendor.sector}</div>
        </div>
        <span className={`neon-badge ${badgeClass}`}>{vendor.risk_level}</span>
      </div>

      {/* Risk Score Bar */}
      <div style={{ marginBottom: 8 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
          <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: '#999' }}>Risk Score</span>
          <span style={{ fontFamily: 'var(--font-terminal)', fontSize: '1.1rem', color }}>{vendor.risk_score}</span>
        </div>
        <div className="progress-bar">
          <div
            className={`progress-fill ${vendor.risk_score > 80 ? 'red' : vendor.risk_score > 50 ? 'orange' : 'green'}`}
            style={{ width: `${vendor.risk_score}%` }}
          />
        </div>
      </div>

      <div style={{ display: 'flex', gap: 12, fontFamily: 'var(--font-mono)', fontSize: '0.65rem', color: '#999' }}>
        <span>Contract: R$ {(vendor.contract_value_brl / 1e9).toFixed(1)}B</span>
        <span>XR: {vendor.xr_device_count}</span>
        {vendor.dark_web_exposure && <span style={{ color: '#FF3333' }}>⚠ DARK WEB</span>}
        {vendor.auto_suspend && <span style={{ color: '#FF3333' }}>🔒 SUSPENDED</span>}
      </div>
    </div>
  );
}

// ── Sub: Vendor Risk ──────────────────────────────────────────────
function VendorRiskView() {
  const vendors = useMemo(() => Object.values(VENDOR_RISK_DB), []);
  const [selectedVendor, setSelectedVendor] = useState<string | null>(null);
  const riskDist = getVendorRiskDistribution();

  const selected = selectedVendor ? VENDOR_RISK_DB[selectedVendor] : null;

  const radarData = selected ? [
    { dim: 'Risk Score', value: selected.risk_score },
    { dim: 'Contract ($B)', value: Math.min((selected.contract_value_brl / 1e9) * 10, 100) },
    { dim: 'XR Devices', value: (selected.xr_device_count / 12) * 100 },
    { dim: 'Breach Count', value: selected.credential_breach_count * 50 },
    { dim: 'Dark Web', value: selected.dark_web_exposure ? 100 : 0 },
    { dim: 'MFA', value: selected.mfa_enforced ? 100 : 20 },
  ] : [];

  const barData = vendors.map(v => ({ name: v.vendor_name.split(' ').slice(0, 2).join(' '), score: v.risk_score, level: v.risk_level }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)' }}>
      {/* Risk Distribution KPIs */}
      <div className="grid-4 animate-in">
        <div className="glass-card variant-red metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF3333' }} /> Critical</div>
          <div className="metric-value red">{riskDist.CRITICAL}</div>
          <div className="metric-label">Auto-Suspended</div>
        </div>
        <div className="glass-card variant-orange metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> High</div>
          <div className="metric-value orange">{riskDist.HIGH}</div>
          <div className="metric-label">Under Review</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF9500' }} /> Medium</div>
          <div className="metric-value" style={{ color: '#FF9500' }}>{riskDist.MEDIUM}</div>
          <div className="metric-label">Monitored</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" /> Low</div>
          <div className="metric-value">{riskDist.LOW}</div>
          <div className="metric-label">Compliant</div>
        </div>
      </div>

      <div className="grid-2">
        {/* Vendor Cards Grid */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-sm)' }}>
          {vendors.map((v, i) => (
            <div key={v.vendor_id} className={`animate-in animate-in-delay-${Math.min(i + 1, 4)}`}>
              <VendorCard
                vendor={v}
                isSelected={selectedVendor === v.vendor_id}
                onSelect={() => setSelectedVendor(selectedVendor === v.vendor_id ? null : v.vendor_id)}
              />
            </div>
          ))}
        </div>

        {/* Vendor Detail / Risk Radar */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)' }}>
          {selected ? (
            <div className="glass-card variant-cyan animate-in" style={{ borderColor: 'rgba(0,255,255,0.3)' }}>
              <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> {selected.vendor_name} — Risk Profile</div>
              <ResponsiveContainer width="100%" height={260}>
                <RadarChart data={radarData}>
                  <PolarGrid stroke="rgba(255,255,255,0.08)" />
                  <PolarAngleAxis dataKey="dim" tick={{ fill: '#999', fontSize: 10 }} />
                  <PolarRadiusAxis tick={false} axisLine={false} />
                  <Radar dataKey="value" stroke="#00FFFF" fill="#00FFFF" fillOpacity={0.15} strokeWidth={2} />
                </RadarChart>
              </ResponsiveContainer>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, marginTop: 8 }}>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.7rem', color: '#999' }}>Access Level: <span style={{ color: '#00FFFF' }}>{selected.access_level}</span></div>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.7rem', color: '#999' }}>MFA: <span style={{ color: selected.mfa_enforced ? '#00FF41' : '#FF3333' }}>{selected.mfa_enforced ? 'Enforced' : 'NOT ENFORCED'}</span></div>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.7rem', color: '#999' }}>Breach: <span style={{ color: selected.credential_breach_count > 0 ? '#FF3333' : '#00FF41' }}>{selected.credential_breach_count}</span></div>
                <div style={{ fontFamily: 'var(--font-mono)', fontSize: '0.7rem', color: '#999' }}>Dark Web: <span style={{ color: selected.dark_web_exposure ? '#FF3333' : '#00FF41' }}>{selected.dark_web_exposure ? '⚠ EXPOSED' : 'CLEAR'}</span></div>
              </div>
            </div>
          ) : (
            <div className="glass-card" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', minHeight: 200, color: '#555', fontFamily: 'var(--font-mono)', fontSize: '0.8rem' }}>
              Selecione um vendor para ver o perfil de risco ↑
            </div>
          )}

          <div className="glass-card animate-in animate-in-delay-2">
            <div className="glass-card-title"><span className="indicator" /> Vendor Risk Comparison</div>
            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={barData} layout="vertical" margin={{ left: 8, right: 16 }}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.04)" />
                <XAxis type="number" domain={[0, 100]} stroke="#555" tick={{ fill: '#999', fontSize: 10 }} />
                <YAxis dataKey="name" type="category" width={100} stroke="#555" tick={{ fill: '#aaa', fontSize: 10 }} />
                <Tooltip content={<CustomTooltip />} />
                <Bar dataKey="score" name="Risk Score" radius={[0, 4, 4, 0]}>
                  {barData.map((entry, i) => (
                    <Cell key={i} fill={entry.level === 'CRITICAL' ? '#FF3333' : entry.level === 'HIGH' ? '#FF6200' : entry.level === 'MEDIUM' ? '#FF9500' : '#00FF41'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}

// ── Sub: Fleet Health ─────────────────────────────────────────────
function FleetHealthView() {
  const fleet = getFleetHealth();
  const deviceList = Object.values(XR_DEVICES);

  const regionGroups = useMemo(() => {
    const groups: Record<string, FleetNode[]> = {};
    FLEET_REGISTRY.forEach(node => {
      if (!groups[node.region]) groups[node.region] = [];
      groups[node.region].push(node);
    });
    return groups;
  }, []);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--gap-md)' }}>
      {/* Fleet KPIs */}
      <div className="grid-4 animate-in">
        <div className="glass-card glow-green metric-card">
          <div className="glass-card-title"><span className="indicator" /> Nodes Online</div>
          <div className="metric-value">{fleet.online}/{fleet.total}</div>
          <div className="metric-label">Edge nodes ativos</div>
        </div>
        <div className="glass-card metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> Vaccination</div>
          <div className="metric-value cyan">{fleet.upToDate}/{fleet.total}</div>
          <div className="metric-label">Rulesets atualizados</div>
        </div>
        <div className="glass-card variant-orange metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> XR Devices</div>
          <div className="metric-value orange">{deviceList.length}</div>
          <div className="metric-label">Assets monitorados</div>
        </div>
        <div className="glass-card variant-red metric-card">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF3333' }} /> Compromised</div>
          <div className="metric-value red">{deviceList.filter(d => d.mdm_enrollment_status === 'compromised').length}</div>
          <div className="metric-label">Devices bloqueados</div>
        </div>
      </div>

      {/* Fleet Coverage Progress */}
      <div className="glass-card animate-in animate-in-delay-1">
        <div className="glass-card-title"><span className="indicator" /> Fleet Vaccination Progress</div>
        <div style={{ marginTop: 12 }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
            <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.8rem', color: '#ccc' }}>Global Coverage</span>
            <span style={{ fontFamily: 'var(--font-terminal)', fontSize: '1.4rem', color: '#00FF41' }}>{Math.round((fleet.upToDate / fleet.total) * 100)}%</span>
          </div>
          <div className="progress-bar" style={{ height: 10 }}>
            <div className="progress-fill green" style={{ width: `${(fleet.upToDate / fleet.total) * 100}%` }} />
          </div>
        </div>
      </div>

      <div className="grid-2">
        {/* Edge Nodes by Region */}
        <div className="glass-card animate-in animate-in-delay-2">
          <div className="glass-card-title"><span className="indicator" style={{ background: '#00FFFF' }} /> Edge Nodes por Região</div>
          <div style={{ display: 'flex', flexDirection: 'column', gap: 12, marginTop: 12 }}>
            {Object.entries(regionGroups).map(([region, nodes]) => {
              const online = nodes.filter(n => n.status === 'online').length;
              return (
                <div key={region}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
                    <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', color: '#00FFFF' }}>{region.replace(/_/g, ' ')}</span>
                    <span style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', color: '#999' }}>{online}/{nodes.length} online</span>
                  </div>
                  <div style={{ display: 'flex', gap: 4, flexWrap: 'wrap' }}>
                    {nodes.map(node => (
                      <div key={node.node_id} title={`${node.node_id} — ${node.facility}`} style={{
                        width: 28, height: 28, borderRadius: 4, display: 'flex', alignItems: 'center', justifyContent: 'center',
                        fontSize: '0.55rem', fontFamily: 'var(--font-mono)', cursor: 'pointer', transition: 'all 0.3s ease',
                        background: node.status === 'online' ? 'rgba(0,255,65,0.1)' : 'rgba(255,51,51,0.1)',
                        border: `1px solid ${node.status === 'online' ? 'rgba(0,255,65,0.3)' : 'rgba(255,51,51,0.3)'}`,
                        color: node.status === 'online' ? '#00FF41' : '#FF3333',
                        boxShadow: node.status === 'online' ? '0 0 6px rgba(0,255,65,0.15)' : '0 0 6px rgba(255,51,51,0.15)',
                      }}>
                        {node.vaccine_status === 'up_to_date' ? '✓' : node.vaccine_status === 'pending' ? '◔' : '✗'}
                      </div>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* XR Device Fleet Table */}
        <div className="glass-card animate-in animate-in-delay-3" style={{ overflow: 'auto' }}>
          <div className="glass-card-title"><span className="indicator" style={{ background: '#FF6200' }} /> XR Device Fleet</div>
          <table className="data-table" style={{ marginTop: 8 }}>
            <thead>
              <tr>
                <th>Device</th>
                <th>Type</th>
                <th>Zone</th>
                <th>Status</th>
                <th>Vendor</th>
              </tr>
            </thead>
            <tbody>
              {deviceList.map(d => {
                return (
                  <tr key={d.device_id}>
                    <td style={{ fontFamily: 'var(--font-mono)', fontSize: '0.75rem', color: '#00FFFF' }}>{d.device_id}</td>
                    <td style={{ fontSize: '0.75rem' }}>{d.device_type}</td>
                    <td style={{ fontSize: '0.75rem', color: '#999' }}>{d.facility_zone}</td>
                    <td>
                      <span className={`neon-badge ${d.mdm_enrollment_status === 'compromised' ? 'critical' : d.mdm_enrollment_status === 'kiosk' ? 'online' : 'low'}`}>
                        {d.mdm_enrollment_status}
                      </span>
                    </td>
                    <td style={{ fontSize: '0.7rem', color: '#999' }}>{d.assigned_vendor_id || '—'}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

// ── Página: Fleet Intelligence ────────────────────────────────────
export default function FleetIntelligence() {
  const [activeTab, setActiveTab] = useState<'vendor' | 'fleet'>('vendor');

  return (
    <div className="page-container">
      <div className="sub-tabs animate-in">
        <button className={`sub-tab ${activeTab === 'vendor' ? 'active' : ''}`} onClick={() => setActiveTab('vendor')}>
          ▸ Vendor Risk Map
        </button>
        <button className={`sub-tab ${activeTab === 'fleet' ? 'active' : ''}`} onClick={() => setActiveTab('fleet')}>
          ▸ Fleet Health
        </button>
      </div>
      {activeTab === 'vendor' ? <VendorRiskView /> : <FleetHealthView />}
    </div>
  );
}
