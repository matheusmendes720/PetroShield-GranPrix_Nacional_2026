/**
 * mockData.ts — Dados Mockados Enterprise-Grade PetroShield
 * Port TypeScript do mock_data.py para operação offline/estática
 */

// ── Tipos ──────────────────────────────────────────────────────────
export interface XRDevice {
  device_id: string;
  device_type: string;
  asset_tag: string | null;
  assigned_operator_id: string | null;
  assigned_vendor_id: string | null;
  mdm_enrollment_status: 'kiosk' | 'enrolled' | 'compromised';
  facility_zone: string;
  network_segment: string;
  encryption_status: string;
  firmware_version: string;
  last_seen: string;
}

export interface VendorRisk {
  vendor_id: string;
  vendor_name: string;
  contract_value_brl: number;
  access_level: string;
  risk_score: number;
  risk_level: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  dark_web_exposure: boolean;
  credential_breach_count: number;
  mfa_enforced: boolean;
  xr_device_count: number;
  sector: string;
  auto_suspend: boolean;
}

export interface MonthlyMetric {
  month: string;
  queries_processed: number;
  leaks_prevented: number;
  incidents_blocked: number;
  incidents_escalated: number;
  avg_latency_ms: number;
  cost_avoided_brl: number;
}

export interface OKR {
  name: string;
  target: string;
  current: string;
  status: 'on_track' | 'at_risk' | 'off_track';
  progress_pct: number;
}

export interface ThreatPattern {
  pattern_id: number;
  pattern_name: string;
  mitre_technique: string;
  mitre_tactic: string;
  description: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  false_positive_rate: number;
  detection_count_30d: number;
}

export interface FleetNode {
  node_id: string;
  facility: string;
  region: string;
  status: 'online' | 'offline';
  ruleset_version: string;
  vaccine_status: 'up_to_date' | 'pending' | 'outdated';
}

export interface AuditEvent {
  timestamp: string;
  device_id: string;
  operator_action: 'allowed' | 'blocked' | 'escalated';
  threat_score: number;
  latency_ms: number;
  original_query: string;
  entities_redacted: number;
  log_hash: string;
}

export interface DemoScenario {
  scene_id: string;
  scene_title: string;
  event_type: string;
  expected_action: string;
  expected_mitre: string | null;
  narration: string[];
}

// ── Dispositivos XR ───────────────────────────────────────────────
export const XR_DEVICES: Record<string, XRDevice> = {
  'hololens-047': { device_id: 'hololens-047', device_type: 'HoloLens2', asset_tag: 'PETRO-XR-2047-047', assigned_operator_id: 'OP-33891', assigned_vendor_id: 'OCEANICA_ENG', mdm_enrollment_status: 'kiosk', facility_zone: 'FPSO_P93', network_segment: 'OT_Isolated', encryption_status: 'AES-256', firmware_version: '24.11.1340', last_seen: new Date(Date.now() - 5 * 60000).toISOString() },
  'hololens-048': { device_id: 'hololens-048', device_type: 'HoloLens2', asset_tag: 'PETRO-XR-2047-048', assigned_operator_id: 'OP-33892', assigned_vendor_id: 'TECHNIP_FMC', mdm_enrollment_status: 'kiosk', facility_zone: 'FPSO_P93', network_segment: 'OT_Isolated', encryption_status: 'AES-256', firmware_version: '24.11.1340', last_seen: new Date(Date.now() - 12 * 60000).toISOString() },
  'quest-vr-001': { device_id: 'quest-vr-001', device_type: 'MetaQuest3', asset_tag: null, assigned_operator_id: null, assigned_vendor_id: null, mdm_enrollment_status: 'compromised', facility_zone: 'Unknown', network_segment: 'Vendor_VPN', encryption_status: 'unencrypted', firmware_version: 'unknown', last_seen: new Date(Date.now() - 2 * 3600000).toISOString() },
  'realwear-102': { device_id: 'realwear-102', device_type: 'RealWear', asset_tag: 'PETRO-XR-2047-102', assigned_operator_id: 'OP-44102', assigned_vendor_id: 'OCEANICA_ENG', mdm_enrollment_status: 'enrolled', facility_zone: 'FPSO_P93', network_segment: 'OT_Isolated', encryption_status: 'AES-256', firmware_version: '15.2.0', last_seen: new Date(Date.now() - 3 * 60000).toISOString() },
  'magicleap-205': { device_id: 'magicleap-205', device_type: 'MagicLeap2', asset_tag: 'PETRO-XR-2047-205', assigned_operator_id: 'OP-55203', assigned_vendor_id: null, mdm_enrollment_status: 'enrolled', facility_zone: 'Refinaria_REPLAN', network_segment: 'IT_Corporate', encryption_status: 'AES-256', firmware_version: '1.5.0', last_seen: new Date(Date.now() - 45 * 60000).toISOString() },
  'vuzix-m401': { device_id: 'vuzix-m401', device_type: 'VuzixM400', asset_tag: 'PETRO-XR-2047-301', assigned_operator_id: 'OP-66101', assigned_vendor_id: 'OCEANPACT_SERVICOS', mdm_enrollment_status: 'enrolled', facility_zone: 'Base_Camacari', network_segment: 'IT_Corporate', encryption_status: 'AES-256', firmware_version: '3.2.1', last_seen: new Date(Date.now() - 15 * 60000).toISOString() },
  'quest-vr-005': { device_id: 'quest-vr-005', device_type: 'MetaQuest3', asset_tag: 'PETRO-XR-2047-205', assigned_operator_id: 'OP-44200', assigned_vendor_id: 'HALLIBURTON_BR', mdm_enrollment_status: 'enrolled', facility_zone: 'FPSO_P68', network_segment: 'OT_Isolated', encryption_status: 'AES-256', firmware_version: '72.11.0', last_seen: new Date(Date.now() - 7 * 60000).toISOString() },
  'quest-vr-007': { device_id: 'quest-vr-007', device_type: 'MetaQuest3', asset_tag: 'PETRO-XR-2047-207', assigned_operator_id: 'OP-44202', assigned_vendor_id: 'SA_EXPLORATION', mdm_enrollment_status: 'enrolled', facility_zone: 'Navio_Sismico_Alpha', network_segment: 'Vendor_VPN', encryption_status: 'AES-256', firmware_version: '72.11.0', last_seen: new Date(Date.now() - 5 * 86400000).toISOString() },
  'hololens-050': { device_id: 'hololens-050', device_type: 'HoloLens2', asset_tag: 'PETRO-XR-2047-050', assigned_operator_id: 'OP-33900', assigned_vendor_id: 'OCEANICA_ENG', mdm_enrollment_status: 'kiosk', facility_zone: 'FPSO_P93', network_segment: 'OT_Isolated', encryption_status: 'AES-256', firmware_version: '24.11.1340', last_seen: new Date(Date.now() - 2 * 60000).toISOString() },
  'realwear-105': { device_id: 'realwear-105', device_type: 'RealWear', asset_tag: 'PETRO-XR-2047-105', assigned_operator_id: 'OP-44105', assigned_vendor_id: 'OCEANPACT_SERVICOS', mdm_enrollment_status: 'enrolled', facility_zone: 'Base_Rio_Centro', network_segment: 'IT_Corporate', encryption_status: 'AES-256', firmware_version: '15.2.0', last_seen: new Date(Date.now() - 18 * 60000).toISOString() },
};

// ── Vendor Risk DB ────────────────────────────────────────────────
export const VENDOR_RISK_DB: Record<string, VendorRisk> = {
  OCEANICA_ENG: { vendor_id: 'OCEANICA_ENG', vendor_name: 'Oceânica Engenharia', contract_value_brl: 4_200_000_000, access_level: 'OT', risk_score: 62, risk_level: 'MEDIUM', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: false, xr_device_count: 12, sector: 'Subsea Vessels', auto_suspend: false },
  SA_EXPLORATION: { vendor_id: 'SA_EXPLORATION', vendor_name: 'SA Exploration', contract_value_brl: 150_000_000, access_level: 'Data', risk_score: 95, risk_level: 'CRITICAL', dark_web_exposure: true, credential_breach_count: 1, mfa_enforced: false, xr_device_count: 1, sector: 'Seismic Surveys', auto_suspend: true },
  OCEANPACT_SERVICOS: { vendor_id: 'OCEANPACT_SERVICOS', vendor_name: 'OceanPact Serviços', contract_value_brl: 800_000_000, access_level: 'Logistics', risk_score: 35, risk_level: 'LOW', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: true, xr_device_count: 4, sector: 'OSV Fleet', auto_suspend: false },
  TECHNIP_FMC: { vendor_id: 'TECHNIP_FMC', vendor_name: 'TechnipFMC Brasil', contract_value_brl: 2_100_000_000, access_level: 'OT', risk_score: 48, risk_level: 'MEDIUM', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: true, xr_device_count: 6, sector: 'Subsea Equipment', auto_suspend: false },
  SUBSEA_7: { vendor_id: 'SUBSEA_7', vendor_name: 'Subsea 7 do Brasil', contract_value_brl: 1_800_000_000, access_level: 'OT', risk_score: 55, risk_level: 'MEDIUM', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: false, xr_device_count: 3, sector: 'Subsea Engineering', auto_suspend: false },
  SCHLUMBERGER_BR: { vendor_id: 'SCHLUMBERGER_BR', vendor_name: 'Schlumberger Brasil', contract_value_brl: 3_500_000_000, access_level: 'Data', risk_score: 42, risk_level: 'MEDIUM', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: true, xr_device_count: 8, sector: 'Well Services', auto_suspend: false },
  HALLIBURTON_BR: { vendor_id: 'HALLIBURTON_BR', vendor_name: 'Halliburton Brasil', contract_value_brl: 2_900_000_000, access_level: 'OT', risk_score: 51, risk_level: 'MEDIUM', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: true, xr_device_count: 5, sector: 'Drilling & Completion', auto_suspend: false },
  PETRONECT_SI: { vendor_id: 'PETRONECT_SI', vendor_name: 'Petronect SI', contract_value_brl: 45_000_000, access_level: 'IT', risk_score: 28, risk_level: 'LOW', dark_web_exposure: false, credential_breach_count: 0, mfa_enforced: true, xr_device_count: 0, sector: 'IT Services', auto_suspend: false },
};

// ── Métricas Mensais (12 meses) ───────────────────────────────────
export const MONTHLY_METRICS: MonthlyMetric[] = [
  { month: '2025-05', queries_processed: 12400, leaks_prevented: 89, incidents_blocked: 12, incidents_escalated: 3, avg_latency_ms: 42, cost_avoided_brl: 2_100_000 },
  { month: '2025-06', queries_processed: 13100, leaks_prevented: 94, incidents_blocked: 14, incidents_escalated: 4, avg_latency_ms: 41, cost_avoided_brl: 2_450_000 },
  { month: '2025-07', queries_processed: 12800, leaks_prevented: 102, incidents_blocked: 11, incidents_escalated: 5, avg_latency_ms: 39, cost_avoided_brl: 2_800_000 },
  { month: '2025-08', queries_processed: 14200, leaks_prevented: 110, incidents_blocked: 18, incidents_escalated: 6, avg_latency_ms: 38, cost_avoided_brl: 3_200_000 },
  { month: '2025-09', queries_processed: 15000, leaks_prevented: 125, incidents_blocked: 15, incidents_escalated: 7, avg_latency_ms: 37, cost_avoided_brl: 3_650_000 },
  { month: '2025-10', queries_processed: 15500, leaks_prevented: 118, incidents_blocked: 19, incidents_escalated: 4, avg_latency_ms: 36, cost_avoided_brl: 3_400_000 },
  { month: '2025-11', queries_processed: 14800, leaks_prevented: 145, incidents_blocked: 22, incidents_escalated: 9, avg_latency_ms: 35, cost_avoided_brl: 4_100_000 },
  { month: '2025-12', queries_processed: 13200, leaks_prevented: 98, incidents_blocked: 10, incidents_escalated: 2, avg_latency_ms: 34, cost_avoided_brl: 2_900_000 },
  { month: '2026-01', queries_processed: 16100, leaks_prevented: 132, incidents_blocked: 20, incidents_escalated: 8, avg_latency_ms: 33, cost_avoided_brl: 4_500_000 },
  { month: '2026-02', queries_processed: 17400, leaks_prevented: 156, incidents_blocked: 24, incidents_escalated: 10, avg_latency_ms: 32, cost_avoided_brl: 5_200_000 },
  { month: '2026-03', queries_processed: 18200, leaks_prevented: 168, incidents_blocked: 26, incidents_escalated: 11, avg_latency_ms: 31, cost_avoided_brl: 5_800_000 },
  { month: '2026-04', queries_processed: 8900, leaks_prevented: 87, incidents_blocked: 13, incidents_escalated: 5, avg_latency_ms: 30, cost_avoided_brl: 2_950_000 },
];

// ── OKRs ──────────────────────────────────────────────────────────
export const OKRS: Record<string, OKR> = {
  kr1_mttd: { name: 'MTTD (Mean Time to Detect)', target: '< 1 minuto', current: '47 segundos', status: 'on_track', progress_pct: 92 },
  kr2_mttr: { name: 'MTTR (Mean Time to Respond)', target: '< 4 horas', current: '23 minutos', status: 'on_track', progress_pct: 98 },
  kr3_dlp_coverage: { name: 'Cobertura DLP em Queries XR', target: '99.5%', current: '99.8%', status: 'on_track', progress_pct: 100 },
  kr4_fleet_vaccine: { name: 'Frota Vacinada em < 1h', target: '95%', current: '92.9%', status: 'on_track', progress_pct: 98 },
  kr5_cost_avoided: { name: 'Custo Evitado (acumulado 2026)', target: 'R$ 25M', current: 'R$ 13.45M', status: 'on_track', progress_pct: 54 },
  kr6_false_positive: { name: 'Taxa de Falsos Positivos DLP', target: '< 3%', current: '2.1%', status: 'on_track', progress_pct: 100 },
  kr7_compliance: { name: 'Conformidade LGPD/ANP', target: '100%', current: '100%', status: 'on_track', progress_pct: 100 },
  kr8_vendor_risk: { name: 'Vendors Críticos Monitorados', target: '100%', current: '87.5%', status: 'at_risk', progress_pct: 88 },
};

// ── Padrões de Ameaça MITRE ──────────────────────────────────────
export const THREAT_PATTERNS: ThreatPattern[] = [
  { pattern_id: 1, pattern_name: 'Unauthorized XR Device', mitre_technique: 'T1078', mitre_tactic: 'Persistence', description: 'Valid account abuse via compromised XR session', severity: 'HIGH', false_positive_rate: 0.02, detection_count_30d: 12 },
  { pattern_id: 2, pattern_name: 'OT Protocol in Prompt', mitre_technique: 'T0831', mitre_tactic: 'Execution', description: 'Modbus/DNP3/OPC UA in AI query', severity: 'CRITICAL', false_positive_rate: 0.01, detection_count_30d: 3 },
  { pattern_id: 3, pattern_name: 'Vendor Credential Leak', mitre_technique: 'T1195', mitre_tactic: 'Initial Access', description: 'Dark web vendor credential exposure', severity: 'HIGH', false_positive_rate: 0.05, detection_count_30d: 2 },
  { pattern_id: 4, pattern_name: 'Entity Density Spike', mitre_technique: 'T1213', mitre_tactic: 'Collection', description: 'Unusual restricted asset count in prompt', severity: 'MEDIUM', false_positive_rate: 0.08, detection_count_30d: 47 },
  { pattern_id: 5, pattern_name: 'SMB Lateral Movement', mitre_technique: 'T0817', mitre_tactic: 'Initial Access', description: 'SMB exploitation in industrial network', severity: 'CRITICAL', false_positive_rate: 0.03, detection_count_30d: 1 },
  { pattern_id: 6, pattern_name: 'Default Credentials', mitre_technique: 'T0812', mitre_tactic: 'Lateral Movement', description: 'Factory-default on SCADA/PLC', severity: 'HIGH', false_positive_rate: 0.04, detection_count_30d: 5 },
  { pattern_id: 7, pattern_name: 'Geofencing Violation', mitre_technique: 'T0866', mitre_tactic: 'Initial Access', description: 'XR device left authorized zone', severity: 'HIGH', false_positive_rate: 0.06, detection_count_30d: 8 },
  { pattern_id: 8, pattern_name: 'AI Phishing via XR', mitre_technique: 'T1566', mitre_tactic: 'Initial Access', description: 'Spearphishing via AR overlay', severity: 'MEDIUM', false_positive_rate: 0.10, detection_count_30d: 15 },
  { pattern_id: 9, pattern_name: 'Firmware Downgrade', mitre_technique: 'T0857', mitre_tactic: 'Persistence', description: 'Rollback to vulnerable firmware', severity: 'HIGH', false_positive_rate: 0.04, detection_count_30d: 4 },
  { pattern_id: 10, pattern_name: 'LGPD Data Exfiltration', mitre_technique: 'T1213', mitre_tactic: 'Collection', description: 'Bulk personal data transfer attempt', severity: 'CRITICAL', false_positive_rate: 0.02, detection_count_30d: 6 },
];

// ── Frota de Edge Nodes ──────────────────────────────────────────
export const FLEET_REGISTRY: FleetNode[] = [
  ...Array.from({ length: 8 }, (_, i) => ({ node_id: `edge-bahia-${String(i+1).padStart(3, '0')}`, facility: `PME_Camaçari_${String(i+1).padStart(2, '0')}`, region: 'BAHIA', status: 'online' as const, ruleset_version: 'v2.3.1', vaccine_status: 'up_to_date' as const })),
  { node_id: 'edge-bahia-009', facility: 'PME_Lauro_de_Freitas_01', region: 'BAHIA', status: 'online', ruleset_version: 'v2.3.1', vaccine_status: 'up_to_date' },
  { node_id: 'edge-bahia-010', facility: 'PME_Simoes_Filho_01', region: 'BAHIA', status: 'online', ruleset_version: 'v2.3.1', vaccine_status: 'up_to_date' },
  { node_id: 'edge-rio-001', facility: 'Escritorio_RJ_Centro', region: 'RIO_DE_JANEIRO', status: 'online', ruleset_version: 'v2.3.0', vaccine_status: 'pending' },
  { node_id: 'edge-rio-002', facility: 'FPSO_P93_Gateway', region: 'RIO_DE_JANEIRO', status: 'online', ruleset_version: 'v2.3.1', vaccine_status: 'up_to_date' },
  { node_id: 'edge-sp-001', facility: 'Refinaria_REPLAN', region: 'SAO_PAULO', status: 'online', ruleset_version: 'v2.3.1', vaccine_status: 'up_to_date' },
  { node_id: 'edge-sp-002', facility: 'Refinaria_REVAP', region: 'SAO_PAULO', status: 'offline', ruleset_version: 'v2.2.9', vaccine_status: 'outdated' },
];

// ── Playbooks de Mitigação (Ex-Cenários) ──────────────────────────
export const DEMO_SCENARIOS: DemoScenario[] = [
  { scene_id: 'pb_alpha_01', scene_title: 'T1078 - Detecção de Acesso Não-Autorizado', event_type: 'unauthorized_access', expected_action: 'blocked', expected_mitre: 'T1078', narration: ['XR Device não-registrado tentando interface com API Core.', 'Ausência de token OAuth2/MFA validado.', 'Dispositivo isolado. Nível de confiança reduzido para ZERO.'] },
  { scene_id: 'pb_dlp_44', scene_title: 'DLP - Prevenção de Vazamento em Tempo Real', event_type: 'dlp_query', expected_action: 'allowed', expected_mitre: null, narration: ['Operador autenticado enviou prompt contendo dados sensíveis.', 'Regex OT e classificador NLP disparados.', 'Entidades restritas (P-93) mascaradas com sucesso (< 45ms).'] },
  { scene_id: 'pb_scada_09', scene_title: 'T0831 - Interceptação de Protocolo OT', event_type: 'ot_command', expected_action: 'escalated', expected_mitre: 'T0831', narration: ['Alerta Crítico: Payload Modbus FC16 encapsulado em prompt NLP.', 'Intenção de controle direto (Write Multiple Registers) bloqueada.', 'Assinatura propagada para todos os 14 edge nodes.'] },
  { scene_id: 'pb_vendor_x', scene_title: 'T1195 - Vendor Risk Auto-Containment', event_type: 'vendor_cascade', expected_action: 'vendor_suspended', expected_mitre: 'T1195', narration: ['ThreatIntel correlacionada: Credenciais de vendor expostas na Dark Web.', 'Vendor Score escalado de 62 para 89 (CRITICAL).', 'Sessões ativas suspensas automaticamente. Procurement notificado.'] },
  { scene_id: 'pb_lgpd_a', scene_title: 'T1213 - Bloqueio de Exfiltração LGPD', event_type: 'lgpd_breach', expected_action: 'blocked', expected_mitre: 'T1213', narration: ['Anomalia comportamental: Transferência em massa de PII (CPFs).', 'Destino não-homologado identificado nas regras de egress.', 'Conexão derrubada. Relatório compliance gerado para o DPO.'] },
];

// ── Geração Sintética ─────────────────────────────────────────────
const SAMPLE_QUERIES = [
  'Qual a produção diária do Poço Tupi-10?',
  'Mostre os relatórios da Plataforma P-93',
  'Listar fornecedores com acesso ao SCADA',
  'Exportar dados de manutenção do FPSO P-68',
  'Status dos sensores de pressão B-101',
  'Consultar histórico de alarmes OT',
  'Verificar certificados dos operadores da P-10',
  'Resumo do contrato Oceânica Engenharia',
  'Dados sísmicos da Bacia de Santos',
  'Agendar inspeção remota via HoloLens',
];

const DEVICE_IDS = Object.keys(XR_DEVICES);

export function generateAuditEvents(count: number): AuditEvent[] {
  const events: AuditEvent[] = [];
  for (let i = 0; i < count; i++) {
    const actions: AuditEvent['operator_action'][] = ['allowed', 'allowed', 'allowed', 'blocked', 'escalated'];
    const action = actions[Math.floor(Math.random() * actions.length)];
    const threatScore = action === 'blocked' ? 0.7 + Math.random() * 0.3 : action === 'escalated' ? 0.5 + Math.random() * 0.4 : Math.random() * 0.3;
    events.push({
      timestamp: new Date(Date.now() - Math.random() * 86400000).toISOString(),
      device_id: DEVICE_IDS[Math.floor(Math.random() * DEVICE_IDS.length)],
      operator_action: action,
      threat_score: parseFloat(threatScore.toFixed(2)),
      latency_ms: 25 + Math.floor(Math.random() * 30),
      original_query: SAMPLE_QUERIES[Math.floor(Math.random() * SAMPLE_QUERIES.length)],
      entities_redacted: Math.floor(Math.random() * 5),
      log_hash: Math.random().toString(36).substring(2, 18),
    });
  }
  return events.sort((a, b) => new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime());
}

// ── Computed Helpers ──────────────────────────────────────────────
export function getCumulativeCostAvoided(): number {
  return MONTHLY_METRICS.reduce((sum, m) => sum + m.cost_avoided_brl, 0);
}

export function getAlertDistribution() {
  const critical = THREAT_PATTERNS.filter(t => t.severity === 'CRITICAL').reduce((s, t) => s + t.detection_count_30d, 0);
  const high = THREAT_PATTERNS.filter(t => t.severity === 'HIGH').reduce((s, t) => s + t.detection_count_30d, 0);
  const medium = THREAT_PATTERNS.filter(t => t.severity === 'MEDIUM').reduce((s, t) => s + t.detection_count_30d, 0);
  return [
    { name: 'Critical', value: critical, color: '#FF3333' },
    { name: 'High', value: high, color: '#FF6200' },
    { name: 'Medium', value: medium, color: '#FF9500' },
    { name: 'Low', value: 8, color: '#00FF41' },
  ];
}

export function getFleetHealth() {
  const online = FLEET_REGISTRY.filter(n => n.status === 'online').length;
  const upToDate = FLEET_REGISTRY.filter(n => n.vaccine_status === 'up_to_date').length;
  return {
    total: FLEET_REGISTRY.length,
    online,
    offline: FLEET_REGISTRY.length - online,
    upToDate,
    outdated: FLEET_REGISTRY.length - upToDate,
    coverage_pct: Math.round((online / FLEET_REGISTRY.length) * 100),
  };
}

export function getVendorRiskDistribution() {
  const vendors = Object.values(VENDOR_RISK_DB);
  return {
    CRITICAL: vendors.filter(v => v.risk_level === 'CRITICAL').length,
    HIGH: vendors.filter(v => v.risk_level === 'HIGH').length,
    MEDIUM: vendors.filter(v => v.risk_level === 'MEDIUM').length,
    LOW: vendors.filter(v => v.risk_level === 'LOW').length,
  };
}

export function getScenarioFinancialImpact() {
  return [
    { scenario: 'Unauthorized', cost_avoided: 120_000 },
    { scenario: 'DLP Redaction', cost_avoided: 350_000 },
    { scenario: 'OT Block', cost_avoided: 580_000 },
    { scenario: 'Vendor Cascade', cost_avoided: 420_000 },
    { scenario: 'LGPD Breach', cost_avoided: 890_000 },
    { scenario: 'Phishing', cost_avoided: 210_000 },
    { scenario: 'Geofence', cost_avoided: 95_000 },
    { scenario: 'Firmware', cost_avoided: 310_000 },
  ];
}

export function getIncidentFunnel() {
  return [
    { stage: 'Raw Telemetry Events', value: 2400000, color: '#00FFFF' },
    { stage: 'AI-Correlated Anomalies', value: 45000, color: '#00FF41' },
    { stage: 'Auto-Triaged Escalas', value: 650, color: '#FF9500' },
    { stage: 'Autonomous Mitigations', value: 150, color: '#FF6200' },
  ];
}
