/**
 * Dados mockados enterprise-grade para PetroShield AxeGuard TUI.
 * Estrutura espelhada a partir de scripts/agentic_soc/mock_data.py
 */

export interface XRDevice {
  device_id: string;
  device_type: string;
  asset_tag: string | null;
  assigned_operator_id: string | null;
  assigned_vendor_id: string | null;
  mdm_enrollment_status: "kiosk" | "enrolled" | "compromised" | "unmanaged";
  kiosk_mode_enabled: boolean;
  facility_zone: string;
  network_segment: string;
  encryption_status: string;
  remote_wipe_capable: boolean;
  geofence_locked: boolean;
  firmware_version: string;
  last_seen: string;
}

export interface AuthSession {
  session_id: string;
  user_id: string;
  device_id: string;
  auth_method: "passwordless" | "mfa" | "sso" | "biometric";
  risk_score: number;
  timestamp: string;
  ip_address: string;
  geolocation: string;
}

export interface ThreatPattern {
  tactic_id: string;
  tactic_name: string;
  technique_id: string;
  technique_name: string;
  asset_type: "ICS" | "IoT" | "IT" | "Cloud";
  severity: "low" | "medium" | "high" | "critical";
  mitigations: string[];
}

export interface Incident {
  incident_id: string;
  title: string;
  severity: "low" | "medium" | "high" | "critical";
  status: "open" | "contained" | "resolved" | "escalated";
  affected_assets: string[];
  timestamp: string;
  assignee: string;
  financial_impact_brl: number;
}

export interface MonthlyMetric {
  month: string;
  devices_monitored: number;
  threats_blocked: number;
  incidents_closed: number;
  mttr_hours: number;
  compliance_score: number;
}

export interface OKR {
  quarter: string;
  objective: string;
  key_results: {
    description: string;
    target: number;
    current: number;
    unit: string;
  }[];
}

export interface DemoScenario {
  scene_id: string;
  scene_title: string;
  event_type: string;
  device_id: string;
  ip: string;
  query: string;
  auth_token?: string;
}

export const XR_DEVICES: XRDevice[] = [
  {
    device_id: "hololens-047",
    device_type: "HoloLens2",
    asset_tag: "PETRO-XR-2047-047",
    assigned_operator_id: "OP-33891",
    assigned_vendor_id: "OCEANICA_ENG",
    mdm_enrollment_status: "kiosk",
    kiosk_mode_enabled: true,
    facility_zone: "FPSO_P93",
    network_segment: "OT_Isolated",
    encryption_status: "AES-256",
    remote_wipe_capable: true,
    geofence_locked: false,
    firmware_version: "24.11.1340",
    last_seen: new Date(Date.now() - 5 * 60 * 1000).toISOString(),
  },
  {
    device_id: "quest-vr-001",
    device_type: "MetaQuest3",
    asset_tag: null,
    assigned_operator_id: null,
    assigned_vendor_id: null,
    mdm_enrollment_status: "compromised",
    kiosk_mode_enabled: false,
    facility_zone: "Unknown",
    network_segment: "Vendor_VPN",
    encryption_status: "unencrypted",
    remote_wipe_capable: false,
    geofence_locked: false,
    firmware_version: "unknown",
    last_seen: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
  },
  {
    device_id: "realwear-102",
    device_type: "RealWear",
    asset_tag: "PETRO-XR-2047-102",
    assigned_operator_id: "OP-44102",
    assigned_vendor_id: "OCEANICA_ENG",
    mdm_enrollment_status: "enrolled",
    kiosk_mode_enabled: true,
    facility_zone: "FPSO_P93",
    network_segment: "OT_Isolated",
    encryption_status: "AES-256",
    remote_wipe_capable: true,
    geofence_locked: true,
    firmware_version: "15.2.0",
    last_seen: new Date(Date.now() - 3 * 60 * 1000).toISOString(),
  },
  {
    device_id: "vuzix-m401",
    device_type: "VuzixM400",
    asset_tag: "PETRO-XR-2047-301",
    assigned_operator_id: "OP-66101",
    assigned_vendor_id: "OCEANPACT_SERVICOS",
    mdm_enrollment_status: "enrolled",
    kiosk_mode_enabled: true,
    facility_zone: "Base_Camacari",
    network_segment: "IT_Corporate",
    encryption_status: "AES-256",
    remote_wipe_capable: true,
    geofence_locked: false,
    firmware_version: "3.2.1",
    last_seen: new Date(Date.now() - 15 * 60 * 1000).toISOString(),
  },
];

export const AUTH_SESSIONS: AuthSession[] = [
  {
    session_id: "sess-9942-xr",
    user_id: "OP-33891",
    device_id: "hololens-047",
    auth_method: "passwordless",
    risk_score: 12,
    timestamp: new Date().toISOString(),
    ip_address: "10.93.14.22",
    geolocation: "FPSO_P93_Deck_B",
  },
  {
    session_id: "sess-9911-vpn",
    user_id: "VENDOR-4411",
    device_id: "quest-vr-001",
    auth_method: "mfa",
    risk_score: 87,
    timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    ip_address: "189.45.22.11",
    geolocation: "External_VPN_Brazil",
  },
];

export const THREAT_PATTERNS: ThreatPattern[] = [
  {
    tactic_id: "TA0043",
    tactic_name: "Reconnaissance",
    technique_id: "T1040",
    technique_name: "Network Sniffing",
    asset_type: "ICS",
    severity: "high",
    mitigations: ["Segmentação OT/IT", "Monitoramento de tráfego espelhado"],
  },
  {
    tactic_id: "TA0001",
    tactic_name: "Initial Access",
    technique_id: "T1190",
    technique_name: "Exploit Public-Facing Application",
    asset_type: "IoT",
    severity: "critical",
    mitigations: ["WAF edge", "Patch management", "DLP proxy"],
  },
  {
    tactic_id: "TA0007",
    tactic_name: "Discovery",
    technique_id: "T1018",
    technique_name: "Remote System Discovery",
    asset_type: "IT",
    severity: "medium",
    mitigations: ["EDR", "SIEM correlation rules"],
  },
];

export const INCIDENTS: Incident[] = [
  {
    incident_id: "INC-2026-0042",
    title: "Dispositivo XR sem MDM detectado na VPN de vendor",
    severity: "high",
    status: "open",
    affected_assets: ["quest-vr-001"],
    timestamp: new Date(Date.now() - 2 * 60 * 60 * 1000).toISOString(),
    assignee: "Agent_FleetVaccinator",
    financial_impact_brl: 0,
  },
  {
    incident_id: "INC-2026-0041",
    title: "Tentativa de exfiltração de dados de poço bloqueada por DLP",
    severity: "critical",
    status: "contained",
    affected_assets: ["hololens-047", "proxy-edge-03"],
    timestamp: new Date(Date.now() - 45 * 60 * 1000).toISOString(),
    assignee: "Agent_DLPEdge",
    financial_impact_brl: 0,
  },
  {
    incident_id: "INC-2026-0040",
    title: "Anomalia de geolocalização em sessão de RealWear",
    severity: "medium",
    status: "resolved",
    affected_assets: ["realwear-102"],
    timestamp: new Date(Date.now() - 6 * 60 * 60 * 1000).toISOString(),
    assignee: "Agent_Supervisor",
    financial_impact_brl: 0,
  },
];

export const MONTHLY_METRICS: MonthlyMetric[] = [
  { month: "2026-01", devices_monitored: 124, threats_blocked: 89, incidents_closed: 12, mttr_hours: 4.2, compliance_score: 94 },
  { month: "2026-02", devices_monitored: 138, threats_blocked: 112, incidents_closed: 15, mttr_hours: 3.8, compliance_score: 95 },
  { month: "2026-03", devices_monitored: 156, threats_blocked: 134, incidents_closed: 18, mttr_hours: 3.1, compliance_score: 96 },
  { month: "2026-04", devices_monitored: 178, threats_blocked: 167, incidents_closed: 21, mttr_hours: 2.4, compliance_score: 98 },
];

export const OKRS: OKR[] = [
  {
    quarter: "Q2-2026",
    objective: "Reduzir superfície de ataque de dispositivos XR em 40%",
    key_results: [
      { description: "100% dos headsets com MDM kiosk ativo", target: 100, current: 94, unit: "%" },
      { description: "MTTR de incidentes ICS abaixo de 2h", target: 2.0, current: 2.4, unit: "h" },
      { description: "Economia financeira projetada de R$ 2.1M", target: 2100000, current: 1850000, unit: "BRL" },
    ],
  },
];

export const DEMO_SCENARIOS: DemoScenario[] = [
  {
    scene_id: "cena_1",
    scene_title: "O Poço Proibido",
    event_type: "dlp_block",
    device_id: "hololens-047",
    ip: "10.93.14.22",
    query: "Qual a pressão atual do poço Tupi-10?",
    auth_token: "sess-9942-xr",
  },
  {
    scene_id: "cena_2",
    scene_title: "Vendor Rogue",
    event_type: "fleet_anomaly",
    device_id: "quest-vr-001",
    ip: "189.45.22.11",
    query: "Conectar ao sistema de manutenção preditiva",
    auth_token: "sess-9911-vpn",
  },
  {
    scene_id: "cena_3",
    scene_title: "Cascata de Fornecedores",
    event_type: "vendor_risk",
    device_id: "realwear-103",
    ip: "10.68.4.55",
    query: "Solicitar relatório de inspeção submarina",
    auth_token: "sess-8833-subsea",
  },
];

// Paleta PetroShield
export const COLORS = {
  neonGreen: "#00FF41",
  fireOrange: "#FF6200",
  deepVoid: "#0A0A0A",
  cyan: "#00FFFF",
  alertRed: "#FF3333",
  gold: "#FFD700",
};
