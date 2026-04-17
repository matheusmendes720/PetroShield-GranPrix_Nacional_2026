/**
 * petroshield_types.ts — Data Contracts & Type System
 * ===================================================
 * Contratos de dados fortemente tipados que padronizam o "Genetic Code"
 * da aplicação PetroShield AxeGuard entre Python (Backend) e TypeScript (Web/BFF).
 *
 * Uso:
 *   import { IXRDevice, IVendorRisk, IMonthlyMetric } from "./petroshield_types";
 */

// ---------------------------------------------------------------------------
// Semantic Tokens — PetroShield Palette
// ---------------------------------------------------------------------------
export const PETROSHIELD_TOKENS = {
  neonGreen: "#00FF41",
  fireOrange: "#FF6200",
  deepVoid: "#0A0A0A",
  cyan: "#00FFFF",
  amber: "#FF9500",
  alertRed: "#FF3333",
  purple: "#BF00FF",
} as const;

export type PetroColor = typeof PETROSHIELD_TOKENS[keyof typeof PETROSHIELD_TOKENS];

// ---------------------------------------------------------------------------
// Core Entity: XR Device
// ---------------------------------------------------------------------------
export interface IXRDevice {
  device_id: string;
  device_type: "HoloLens2" | "MetaQuest3" | "RealWear" | "MagicLeap2" | "VuzixM400";
  asset_tag: string | null;
  assigned_operator_id: string | null;
  assigned_vendor_id: string | null;
  mdm_enrollment_status: "kiosk" | "enrolled" | "compromised" | "unmanaged";
  kiosk_mode_enabled: boolean;
  facility_zone: string;
  network_segment: "OT_Isolated" | "IT_Corporate" | "Vendor_VPN" | "DMZ";
  encryption_status: "AES-256" | "unencrypted" | "ChaCha20";
  remote_wipe_capable: boolean;
  geofence_locked: boolean;
  firmware_version: string;
  last_seen: string; // ISO-8601
}

// ---------------------------------------------------------------------------
// Auth & Sessions
// ---------------------------------------------------------------------------
export interface IAuthSession {
  session_id: string;
  user_id: string;
  device_id: string;
  auth_method: "passwordless" | "mfa" | "sso" | "biometric";
  risk_score: number; // 0-100
  timestamp: string;
  ip_address: string;
  geolocation: string;
}

// ---------------------------------------------------------------------------
// Vendor Risk
// ---------------------------------------------------------------------------
export interface IVendorRisk {
  vendor_id: string;
  vendor_name: string;
  contract_value_brl: number;
  risk_level: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL";
  risk_score: number;
  active_sessions: number;
  last_audit: string;
  certifications: string[];
  dark_web_mentions_30d: number;
}

// ---------------------------------------------------------------------------
// Threat Patterns (MITRE ATT&CK for ICS)
// ---------------------------------------------------------------------------
export interface IThreatPattern {
  tactic_id: string;       // e.g. TA0043
  tactic_name: string;
  technique_id: string;    // e.g. T1040
  technique_name: string;
  asset_type: "ICS" | "IoT" | "IT" | "Cloud";
  severity: "low" | "medium" | "high" | "critical";
  mitigations: string[];
  detection_count_30d?: number;
  false_positive_rate?: number;
}

// ---------------------------------------------------------------------------
// Incident Knowledge Base
// ---------------------------------------------------------------------------
export interface IIncident {
  incident_id: string;
  title: string;
  severity: "low" | "medium" | "high" | "critical";
  status: "open" | "contained" | "resolved" | "escalated";
  affected_assets: string[];
  timestamp: string;
  assignee: string;
  financial_impact_brl: number;
  mitre_technique?: string;
  narration?: string[];
}

// ---------------------------------------------------------------------------
// Monthly Metrics (Time-series)
// ---------------------------------------------------------------------------
export interface IMonthlyMetric {
  month: string; // YYYY-MM
  queries_processed: number;
  leaks_prevented: number;
  incidents_blocked: number;
  incidents_escalated: number;
  avg_latency_ms: number;
  cost_avoided_brl: number;
  biometric_reauths: number;
  shadow_it_blocks: number;
  compliance_deadlines_met: number;
}

// ---------------------------------------------------------------------------
// OKRs & KPIs
// ---------------------------------------------------------------------------
export interface IKeyResult {
  name: string;
  target: string;
  current: string;
  status: "on_track" | "at_risk" | "behind";
  progress_pct: number;
}

export interface IOKRSet {
  quarter: string;
  objective: string;
  key_results: IKeyResult[];
}

// ---------------------------------------------------------------------------
// Edge Fleet
// ---------------------------------------------------------------------------
export interface IEdgeNode {
  node_id: string;
  facility: string;
  region: "BAHIA" | "RIO_DE_JANEIRO" | "SAO_PAULO" | "ESPIRITO_SANTO";
  status: "online" | "offline" | "degraded" | "maintenance";
  ruleset_version: string;
  vaccine_status: "up_to_date" | "pending" | "outdated" | "quarantine";
  last_heartbeat?: string;
  cpu_load_pct?: number;
  memory_load_pct?: number;
}

// ---------------------------------------------------------------------------
// Compliance Ledger
// ---------------------------------------------------------------------------
export interface IComplianceEntry {
  entry_id: string;
  regulation: "LGPD" | "ANP" | "ISO27001" | "NIST" | "PCI-DSS";
  requirement: string;
  status: "compliant" | "non_compliant" | "pending_review" | "remediated";
  deadline: string;
  owner: string;
  evidence_url?: string;
}

// ---------------------------------------------------------------------------
// Triple Surface Metrics
// ---------------------------------------------------------------------------
export interface ITripleSurfaceMetric {
  surface: "OT_Perimeter" | "IT_Corporate" | "Cloud_SaaS";
  label: string;
  blocks_30d: number;
  active_alerts: number;
  trend: "up" | "down" | "stable";
}

// ---------------------------------------------------------------------------
// Agentic Workflow
// ---------------------------------------------------------------------------
export interface IAgenticWorkflow {
  workflow_id: string;
  name: string;
  agent_chain: string[];
  trigger_event: string;
  estimated_duration_sec: number;
  sla_breach_threshold_sec: number;
}

// ---------------------------------------------------------------------------
// Theatre Scenario
// ---------------------------------------------------------------------------
export interface ITheatreScenario {
  scene_id: string;
  scene_title: string;
  event_type: string;
  device_id: string;
  ip: string;
  query: string;
  auth_token?: string;
  expected_action?: string;
  expected_mitre?: string;
  expected_threat_score?: number;
  narration?: string[];
}

// ---------------------------------------------------------------------------
// Telemetry Event (Serverless-ready)
// ---------------------------------------------------------------------------
export interface ITelemetryEvent {
  ts: string; // ISO-8601 UTC
  level: "DEBUG" | "INFO" | "WARN" | "ERROR" | "FATAL";
  source: string;
  event: string;
  payload: Record<string, unknown>;
  host: string;
  version: string;
  trace_id?: string;
  span_id?: string;
}

// ---------------------------------------------------------------------------
// Web TUI Props (React / Vue agnostic)
// ---------------------------------------------------------------------------
export interface IDashboardProps {
  devices: IXRDevice[];
  sessions: IAuthSession[];
  incidents: IIncident[];
  metrics: IMonthlyMetric[];
  okrs: IOKRSet[];
  tripleSurface: ITripleSurfaceMetric[];
  refreshIntervalMs?: number;
}

export interface IOperationsProps {
  workflows: IAgenticWorkflow[];
  fleet: IEdgeNode[];
  vendors: IVendorRisk[];
  onRunWorkflow?: (id: string) => void;
}

export interface ITheatreProps {
  scenarios: ITheatreScenario[];
  onRunScene?: (id: string) => void;
  liveLog?: string[];
}
