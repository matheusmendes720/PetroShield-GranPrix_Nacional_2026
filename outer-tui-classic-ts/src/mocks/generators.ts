/**
 * Geradores sintéticos para Classic TUI.
 */
import { type LogEntry, type XRDevice, LOGS, XR_DEVICES } from "./data.js";

const SOURCES = ["supervisor", "dlp_edge", "fleet_vaccinator", "intel_cloud", "clevel_reporter", "blocker", "vendor_cascade"];
const LEVELS: LogEntry["level"][] = ["INFO", "WARN", "ALERT", "CRIT"];
const MESSAGES = [
  "Heartbeat check completo",
  "Anomalia de geolocalização detectada",
  "Query suspicious bloqueada",
  "Dispositivo flagged como comprometido",
  "Policy drift em vendor",
  "Exfiltração detectada e contida",
  "Relatório C-Level gerado",
  "Scan de vulnerabilidade completo",
];

function rand<T>(arr: T[]): T {
  return arr[Math.floor(Math.random() * arr.length)];
}

function pad(n: number): string {
  return n.toString().padStart(2, "0");
}

function nowTime(): string {
  const d = new Date();
  return `${pad(d.getHours())}:${pad(d.getMinutes())}:${pad(d.getSeconds())}`;
}

export function generateLogs(count: number): LogEntry[] {
  const out: LogEntry[] = [];
  for (let i = 0; i < count; i++) {
    out.push({
      timestamp: nowTime(),
      level: rand(LEVELS),
      source: rand(SOURCES),
      message: rand(MESSAGES),
    });
  }
  return out;
}

export function generateDevices(count: number): XRDevice[] {
  const types = ["HoloLens2", "MetaQuest3", "RealWear", "MagicLeap2", "VuzixM400"];
  const zones = ["FPSO_P93", "FPSO_P68", "Refinaria_REPLAN", "Base_Camacari", "Base_Rio_Centro"];
  const segs = ["OT_Isolated", "IT_Corporate", "Vendor_VPN"];
  const stats = ["kiosk", "enrolled", "compromised", "unmanaged"];
  const out: XRDevice[] = [];
  for (let i = 0; i < count; i++) {
    out.push({
      device_id: `dev-${1000 + i}`,
      device_type: rand(types),
      facility_zone: rand(zones),
      network_segment: rand(segs),
      mdm_enrollment_status: rand(stats),
      last_seen: `-${Math.floor(Math.random() * 120)}m`,
    });
  }
  return out;
}

export function expandDataset<T>(base: T[], generator: (n: number) => T[], extraCount = 5): T[] {
  return [...base, ...generator(extraCount)];
}
