/**
 * PetroShield AxeGuard - TypeScript Data Contracts
 * Central source of truth for Web TUI and BFF communications.
 */

export type RiskLevel = "LOW" | "MEDIUM" | "HIGH" | "CRITICAL";

export type DeviceType = 
  | "HoloLens2" 
  | "MetaQuest3" 
  | "RealWear" 
  | "VuzixM400" 
  | "NrealAir" 
  | "VisionProEE";

export type NetworkSegment = "OT_Isolated" | "IT_Corporate" | "Vendor_VPN";

export type MDMStatus = "enrolled" | "kiosk" | "compromised";

export interface IXRDevice {
  device_id: string;
  device_type: DeviceType;
  asset_tag: string | null;
  assigned_operator_id: string | null;
  assigned_vendor_id: string | null;
  mdm_enrollment_status: MDMStatus;
  kiosk_mode_enabled: boolean;
  facility_zone: string;
  network_segment: NetworkSegment;
  encryption_status: "AES-256" | "unencrypted";
  remote_wipe_capable: boolean;
  geofence_locked: boolean;
  firmware_version: string;
  last_seen: string; // ISO DateTime
}

export interface IVendorRisk {
  vendor_id: string;
  vendor_name: string;
  contract_value_brl: number;
  contract_end_date: string;
  access_level: string;
  risk_score: number;
  risk_level: RiskLevel;
  dark_web_exposure: boolean;
  credential_breach_count: number;
  mfa_enforced: boolean;
  xr_device_count: number;
  anpd_report_required: boolean;
  auto_suspend_threshold_crossed: boolean;
  related_incident_ids: string[];
  sector: string;
}

export interface IMonthlyMetric {
  month: string;
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

export interface IOKR {
  name: string;
  target: string;
  current: string;
  status: "on_track" | "at_risk" | "behind";
  progress_pct: number;
}

export interface IAgenticWorkflow {
  workflow_id: string;
  workflow_name: string;
  workflow_type: string;
  event_type: string;
  description: string;
  affected_devices: string[];
  expected_action: "allowed" | "blocked" | "escalated" | "vendor_suspended";
  expected_mitre: string | null;
  daily_frequency: string;
  business_value: string;
  kpi: string;
}

export interface IComplianceLedgerEntry {
  ledger_id: number;
  regulation: string;
  event_type: string;
  incident_id: string | null;
  vendor_id: string | null;
  data_volume_gb: number;
  data_categories: string[];
  affected_subjects_estimate: number;
  anpd_deadline: string | null;
  notification_sent: boolean;
  notification_sent_at?: string;
  evidence_json: Record<string, any>;
}

export interface ITheatreLogEntry {
  agent: string;
  type: "THOUGHT" | "ACTION" | "OBSERVATION" | "SYSTEM" | "ERROR" | "METRIC" | "PHASE" | "NARRATION" | "GRAPH";
  content: string;
  timestamp?: string;
}

export interface IWorkflowResult {
  scene_id: string;
  final_state: {
    dlp_action: string;
    dlp_threat_score: number;
    dlp_entities: string[];
    financial?: {
      downtime_hours_avoided: number;
      downtime_cost_avoided_brl: number;
      roi_percentage: number;
    };
  };
}
