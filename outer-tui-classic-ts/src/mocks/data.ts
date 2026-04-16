/**
 * Dados mockados para PetroShield Classic TUI (Blessed).
 * Espelhamento reduzido mas compatível com Axeguard.
 */

export interface XRDevice {
  device_id: string;
  device_type: string;
  facility_zone: string;
  network_segment: string;
  mdm_enrollment_status: string;
  last_seen: string;
}

export interface LogEntry {
  timestamp: string;
  level: "INFO" | "WARN" | "ALERT" | "CRIT";
  source: string;
  message: string;
}

export interface Threat {
  id: string;
  tactic: string;
  technique: string;
  target: string;
  severity: string;
}

export const XR_DEVICES: XRDevice[] = [
  { device_id: "hololens-047", device_type: "HoloLens2", facility_zone: "FPSO_P93", network_segment: "OT_Isolated", mdm_enrollment_status: "kiosk", last_seen: "-5m" },
  { device_id: "quest-vr-001", device_type: "MetaQuest3", facility_zone: "Unknown", network_segment: "Vendor_VPN", mdm_enrollment_status: "compromised", last_seen: "-2h" },
  { device_id: "realwear-102", device_type: "RealWear", facility_zone: "FPSO_P93", network_segment: "OT_Isolated", mdm_enrollment_status: "enrolled", last_seen: "-3m" },
  { device_id: "vuzix-m401", device_type: "VuzixM400", facility_zone: "Base_Camacari", network_segment: "IT_Corporate", mdm_enrollment_status: "enrolled", last_seen: "-15m" },
  { device_id: "magicleap-205", device_type: "MagicLeap2", facility_zone: "Refinaria_REPLAN", network_segment: "IT_Corporate", mdm_enrollment_status: "enrolled", last_seen: "-45m" },
];

export const LOGS: LogEntry[] = [
  { timestamp: "08:42:11", level: "INFO", source: "supervisor", message: "Heartbeat check completo — 178 nodes OK" },
  { timestamp: "08:43:02", level: "WARN", source: "dlp_edge", message: "Query suspicious detectada: 'pressão do poço Tupi-10'" },
  { timestamp: "08:43:05", level: "ALERT", source: "blocker", message: "Exfiltração bloqueada — ativo restrito [Tupi-10]" },
  { timestamp: "08:44:19", level: "CRIT", source: "fleet_vaccinator", message: "Dispositivo quest-vr-001 flagged como comprometido" },
  { timestamp: "08:45:33", level: "INFO", source: "clevel_reporter", message: "Relatório de economia projetada gerado: R$ 1.85M" },
  { timestamp: "08:46:01", level: "WARN", source: "vendor_cascade", message: "Vendor SCHLUMBERGER_BR — policy drift detectado" },
];

export const THREATS: Threat[] = [
  { id: "TH-001", tactic: "Initial Access", technique: "T1190", target: "Edge_Proxy_03", severity: "critical" },
  { id: "TH-002", tactic: "Discovery", technique: "T1018", target: "FPSO_P93_SCADA", severity: "high" },
  { id: "TH-003", tactic: "Reconnaissance", technique: "T1040", target: "Vendor_VPN", severity: "medium" },
];

export const COLORS = {
  neonGreen: "green",
  fireOrange: "red", // blessed usa nomes de cor limitados; red/fit
  deepVoid: "black",
  cyan: "cyan",
  alertRed: "red",
  gold: "yellow",
};
