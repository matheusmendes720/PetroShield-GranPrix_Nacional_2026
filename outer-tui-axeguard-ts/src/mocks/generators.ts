/**
 * Geradores de dados sintéticos expansíveis para PetroShield TUI.
 * Permite aumentar datasets em runtime para stress-test visual.
 */

import {
  type XRDevice,
  type AuthSession,
  type Incident,
  type ThreatPattern,
  XR_DEVICES,
  AUTH_SESSIONS,
  INCIDENTS,
  THREAT_PATTERNS,
} from "./data.js";

const VENDORS = ["OCEANICA_ENG", "TECHNIP_FMC", "SUBSEA_7", "SCHLUMBERGER_BR", "HALLIBURTON_BR", "OCEANPACT_SERVICOS"];
const ZONES = ["FPSO_P93", "FPSO_P68", "Refinaria_REPLAN", "Base_Camacari", "Base_Rio_Centro"];
const DEVICE_TYPES = ["HoloLens2", "MetaQuest3", "RealWear", "MagicLeap2", "VuzixM400"];
const TECHNIQUES = [
  { id: "T1040", name: "Network Sniffing" },
  { id: "T1190", name: "Exploit Public-Facing Application" },
  { id: "T1018", name: "Remote System Discovery" },
  { id: "T1059", name: "Command and Scripting Interpreter" },
  { id: "T1071", name: "Application Layer Protocol" },
];

function rand<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)];
}

function randInt(min: number, max: number): number {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function isoMinutesAgo(m: number): string {
  return new Date(Date.now() - m * 60 * 1000).toISOString();
}

export function generateXRDevices(count: number): XRDevice[] {
  const out: XRDevice[] = [];
  const base = XR_DEVICES.length;
  for (let i = 0; i < count; i++) {
    const idx = base + i;
    const type = rand(DEVICE_TYPES);
    const statusPool: XRDevice["mdm_enrollment_status"][] = ["kiosk", "enrolled", "compromised", "unmanaged"];
    const status = rand(statusPool);
    out.push({
      device_id: `${type.toLowerCase().replace(/[^a-z0-9]/g, "")}-${100 + idx}`,
      device_type: type,
      asset_tag: `PETRO-XR-2047-${100 + idx}`,
      assigned_operator_id: `OP-${randInt(10000, 99999)}`,
      assigned_vendor_id: rand(VENDORS),
      mdm_enrollment_status: status,
      kiosk_mode_enabled: status === "kiosk" || status === "enrolled",
      facility_zone: rand(ZONES),
      network_segment: rand(["OT_Isolated", "IT_Corporate", "Vendor_VPN"]),
      encryption_status: status === "compromised" ? "unencrypted" : "AES-256",
      remote_wipe_capable: status !== "compromised",
      geofence_locked: rand([true, false]),
      firmware_version: `${randInt(1, 24)}.${randInt(0, 99)}.${randInt(100, 999)}`,
      last_seen: isoMinutesAgo(randInt(1, 1440)),
    });
  }
  return out;
}

export function generateAuthSessions(count: number): AuthSession[] {
  const out: AuthSession[] = [];
  const devices = [...XR_DEVICES, ...generateXRDevices(10)];
  for (let i = 0; i < count; i++) {
    const device = rand(devices);
    out.push({
      session_id: `sess-${randInt(1000, 9999)}-${rand(["xr", "vpn", "corp"])}`,
      user_id: device.assigned_operator_id ?? `USR-${randInt(10000, 99999)}`,
      device_id: device.device_id,
      auth_method: rand(["passwordless", "mfa", "sso", "biometric"]),
      risk_score: randInt(0, 100),
      timestamp: isoMinutesAgo(randInt(0, 720)),
      ip_address: `${randInt(10, 192)}.${randInt(0, 255)}.${randInt(0, 255)}.${randInt(1, 254)}`,
      geolocation: rand([...ZONES, "External_VPN_Brazil", "External_VPN_USA", "Mobile_4G"]),
    });
  }
  return out;
}

export function generateIncidents(count: number): Incident[] {
  const titles = [
    "Tentativa de acesso não autorizado a SCADA",
    "Exfiltração de dados de poço detectada",
    "Anomalia de comportamento em dispositivo XR",
    "Falha de autenticação em massa no vendor VPN",
    "Policy drift em edge node identificado",
    "Comunicação C2 detectada em segmento IoT",
  ];
  const out: Incident[] = [];
  const base = INCIDENTS.length;
  for (let i = 0; i < count; i++) {
    const idx = base + i;
    const sev = rand(["low", "medium", "high", "critical"] as const);
    out.push({
      incident_id: `INC-2026-${1000 + idx}`,
      title: rand(titles),
      severity: sev,
      status: rand(["open", "contained", "resolved", "escalated"] as const),
      affected_assets: [rand(XR_DEVICES).device_id, `proxy-edge-${randInt(1, 9)}`],
      timestamp: isoMinutesAgo(randInt(10, 2880)),
      assignee: rand(["Agent_Supervisor", "Agent_DLPEdge", "Agent_FleetVaccinator", "Agent_IntelCloud"]),
      financial_impact_brl: sev === "critical" ? randInt(500000, 2000000) : randInt(0, 500000),
    });
  }
  return out;
}

export function generateThreatPatterns(count: number): ThreatPattern[] {
  const tactics = [
    { id: "TA0043", name: "Reconnaissance" },
    { id: "TA0001", name: "Initial Access" },
    { id: "TA0007", name: "Discovery" },
    { id: "TA0002", name: "Execution" },
    { id: "TA0011", name: "Command and Control" },
  ];
  const out: ThreatPattern[] = [];
  const base = THREAT_PATTERNS.length;
  for (let i = 0; i < count; i++) {
    const tech = rand(TECHNIQUES);
    const tac = rand(tactics);
    out.push({
      tactic_id: tac.id,
      tactic_name: tac.name,
      technique_id: tech.id,
      technique_name: tech.name,
      asset_type: rand(["ICS", "IoT", "IT", "Cloud"]),
      severity: rand(["low", "medium", "high", "critical"]),
      mitigations: ["Segmentação", "Monitoramento contínuo", "Resposta automatizada"],
    });
  }
  return out;
}

/** Expande qualquer dataset base com dados sintéticos. */
export function expandDataset<T>(
  base: T[],
  generator: (n: number) => T[],
  extraCount = 10
): T[] {
  return [...base, ...generator(extraCount)];
}
