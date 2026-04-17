/**
 * mock_factory.ts — Massive Synthetic Injection Engine
 * ====================================================
 * Fábrica Node.js-ready para geração de dados sintéticos em escala.
 * Inclui geradores para 10.000+ dispositivos e live WebSocket event emitters.
 *
 * Uso:
 *   import { MockFactory } from "./mock_factory";
 *   const factory = new MockFactory({ seed: 42 });
 *   const devices = factory.generateXRDevices(10000);
 */

import {
  type IXRDevice,
  type IAuthSession,
  type IIncident,
  type IThreatPattern,
  type IMonthlyMetric,
  type IEdgeNode,
  type IVendorRisk,
  type IComplianceEntry,
  type ITelemetryEvent,
  type ITheatreScenario,
  PETROSHIELD_TOKENS,
} from "./petroshield_types.js";

// ---------------------------------------------------------------------------
// Seeded PRNG (Mulberry32) para reprodutibilidade
// ---------------------------------------------------------------------------
function mulberry32(seed: number): () => number {
  return () => {
    let t = (seed += 0x6d2b79f5);
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
function pad(n: number): string {
  return n.toString().padStart(2, "0");
}

function isoNow(): string {
  return new Date().toISOString();
}

function isoMinutesAgo(m: number, now = new Date()): string {
  return new Date(now.getTime() - m * 60 * 1000).toISOString();
}

function randInt(rng: () => number, min: number, max: number): number {
  return Math.floor(rng() * (max - min + 1)) + min;
}

function pick<T>(rng: () => number, arr: readonly T[]): T {
  return arr[Math.floor(rng() * arr.length)];
}

// ---------------------------------------------------------------------------
// Dictionaries
// ---------------------------------------------------------------------------
const DEVICE_TYPES = ["HoloLens2", "MetaQuest3", "RealWear", "MagicLeap2", "VuzixM400"] as const;
const VENDORS = [
  "OCEANICA_ENG", "TECHNIP_FMC", "SUBSEA_7", "SCHLUMBERGER_BR",
  "HALLIBURTON_BR", "OCEANPACT_SERVICOS", "AKER_SOLUTIONS", "MODEC_BR",
];
const ZONES = [
  "FPSO_P93", "FPSO_P68", "FPSO_P77", "Refinaria_REPLAN",
  "Base_Camacari", "Base_Rio_Centro", "Base_Macae", "Refinaria_Cubatao",
];
const NETWORKS = ["OT_Isolated", "IT_Corporate", "Vendor_VPN", "DMZ"] as const;
const REGIONS = ["BAHIA", "RIO_DE_JANEIRO", "SAO_PAULO", "ESPIRITO_SANTO"] as const;
const NODE_STATUSES = ["online", "offline", "degraded", "maintenance"] as const;
const VACCINE_STATUSES = ["up_to_date", "pending", "outdated", "quarantine"] as const;
const INCIDENT_TITLES = [
  "Tentativa de acesso não autorizado a SCADA",
  "Exfiltração de dados de poço detectada",
  "Anomalia de comportamento em dispositivo XR",
  "Falha de autenticação em massa no vendor VPN",
  "Policy drift em edge node identificado",
  "Comunicação C2 detectada em segmento IoT",
  "Firmware rollback suspeito em Quest VR",
  "Overlay AR phishing bloqueado",
];
const MITRE_TECHNIQUES = [
  { id: "T1040", name: "Network Sniffing", tactic: "Reconnaissance" },
  { id: "T1190", name: "Exploit Public-Facing Application", tactic: "Initial Access" },
  { id: "T1018", name: "Remote System Discovery", tactic: "Discovery" },
  { id: "T1059", name: "Command and Scripting Interpreter", tactic: "Execution" },
  { id: "T1071", name: "Application Layer Protocol", tactic: "Command and Control" },
  { id: "T0831", name: "Manipulation of Control", tactic: "Impact" },
  { id: "T0866", name: "Exploit via Radio", tactic: "Initial Access" },
];

// ---------------------------------------------------------------------------
// MockFactory Class
// ---------------------------------------------------------------------------
export class MockFactory {
  private rng: () => number;
  private baseTime: Date;

  constructor(options?: { seed?: number; baseTime?: Date }) {
    this.rng = mulberry32(options?.seed ?? Date.now());
    this.baseTime = options?.baseTime ?? new Date();
  }

  // -----------------------------------------------------------------------
  // XR Devices
  // -----------------------------------------------------------------------
  generateXRDevices(count: number): IXRDevice[] {
    const out: IXRDevice[] = [];
    for (let i = 0; i < count; i++) {
      const type = pick(this.rng, DEVICE_TYPES);
      const status = pick(this.rng, ["kiosk", "enrolled", "compromised", "unmanaged"] as const);
      out.push({
        device_id: `${type.toLowerCase().replace(/[^a-z0-9]/g, "")}-${1000 + i}`,
        device_type: type,
        asset_tag: `PETRO-XR-${2027}-${1000 + i}`,
        assigned_operator_id: `OP-${randInt(this.rng, 10000, 99999)}`,
        assigned_vendor_id: pick(this.rng, VENDORS),
        mdm_enrollment_status: status,
        kiosk_mode_enabled: status === "kiosk" || status === "enrolled",
        facility_zone: pick(this.rng, ZONES),
        network_segment: pick(this.rng, NETWORKS),
        encryption_status: status === "compromised" ? "unencrypted" : "AES-256",
        remote_wipe_capable: status !== "compromised",
        geofence_locked: this.rng() > 0.5,
        firmware_version: `${randInt(this.rng, 1, 24)}.${randInt(this.rng, 0, 99)}.${randInt(this.rng, 100, 999)}`,
        last_seen: isoMinutesAgo(randInt(this.rng, 1, 2880), this.baseTime),
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Auth Sessions
  // -----------------------------------------------------------------------
  generateAuthSessions(count: number, devices: IXRDevice[]): IAuthSession[] {
    const out: IAuthSession[] = [];
    for (let i = 0; i < count; i++) {
      const d = pick(this.rng, devices);
      out.push({
        session_id: `sess-${randInt(this.rng, 1000, 9999)}-${pick(this.rng, ["xr", "vpn", "corp"])}`,
        user_id: d.assigned_operator_id ?? `USR-${randInt(this.rng, 10000, 99999)}`,
        device_id: d.device_id,
        auth_method: pick(this.rng, ["passwordless", "mfa", "sso", "biometric"] as const),
        risk_score: randInt(this.rng, 0, 100),
        timestamp: isoMinutesAgo(randInt(this.rng, 0, 720), this.baseTime),
        ip_address: `${randInt(this.rng, 10, 192)}.${randInt(this.rng, 0, 255)}.${randInt(this.rng, 0, 255)}.${randInt(this.rng, 1, 254)}`,
        geolocation: pick(this.rng, [...ZONES, "External_VPN_Brazil", "External_VPN_USA", "Mobile_4G"]),
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Incidents
  // -----------------------------------------------------------------------
  generateIncidents(count: number): IIncident[] {
    const out: IIncident[] = [];
    for (let i = 0; i < count; i++) {
      const sev = pick(this.rng, ["low", "medium", "high", "critical"] as const);
      out.push({
        incident_id: `INC-2026-${1000 + i}`,
        title: pick(this.rng, INCIDENT_TITLES),
        severity: sev,
        status: pick(this.rng, ["open", "contained", "resolved", "escalated"] as const),
        affected_assets: [`dev-${randInt(this.rng, 1000, 9999)}`, `proxy-edge-${randInt(this.rng, 1, 99)}`],
        timestamp: isoMinutesAgo(randInt(this.rng, 10, 2880), this.baseTime),
        assignee: pick(this.rng, ["Agent_Supervisor", "Agent_DLPEdge", "Agent_FleetVaccinator", "Agent_IntelCloud"]),
        financial_impact_brl: sev === "critical" ? randInt(this.rng, 500_000, 2_000_000) : randInt(this.rng, 0, 500_000),
        mitre_technique: pick(this.rng, MITRE_TECHNIQUES).id,
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Threat Patterns
  // -----------------------------------------------------------------------
  generateThreatPatterns(count: number): IThreatPattern[] {
    const out: IThreatPattern[] = [];
    for (let i = 0; i < count; i++) {
      const tech = pick(this.rng, MITRE_TECHNIQUES);
      out.push({
        tactic_id: `TA${randInt(this.rng, 1, 9999)}`,
        tactic_name: tech.tactic,
        technique_id: tech.id,
        technique_name: tech.name,
        asset_type: pick(this.rng, ["ICS", "IoT", "IT", "Cloud"] as const),
        severity: pick(this.rng, ["low", "medium", "high", "critical"] as const),
        mitigations: ["Segmentação", "Monitoramento contínuo", "Resposta automatizada"],
        detection_count_30d: randInt(this.rng, 5, 150),
        false_positive_rate: randInt(this.rng, 1, 15) / 100,
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Monthly Metrics (time-series)
  // -----------------------------------------------------------------------
  generateMonthlyMetrics(months = 36): IMonthlyMetric[] {
    const out: IMonthlyMetric[] = [];
    const base = new Date(this.baseTime);
    base.setMonth(base.getMonth() - months);
    for (let i = 0; i < months; i++) {
      const dt = new Date(base);
      dt.setMonth(dt.getMonth() + i);
      const growth = 1 + i * 0.02;
      out.push({
        month: `${dt.getFullYear()}-${pad(dt.getMonth() + 1)}`,
        queries_processed: Math.floor(randInt(this.rng, 45_000, 125_000) * growth),
        leaks_prevented: Math.floor(randInt(this.rng, 400, 1500) * growth),
        incidents_blocked: Math.floor(randInt(this.rng, 80, 300) * growth),
        incidents_escalated: randInt(this.rng, 30, 90),
        avg_latency_ms: randInt(this.rng, 10, 25),
        cost_avoided_brl: Math.floor(randInt(this.rng, 15_000_000, 45_000_000) * growth),
        biometric_reauths: Math.floor(randInt(this.rng, 2500, 8500) * growth),
        shadow_it_blocks: randInt(this.rng, 15, 85),
        compliance_deadlines_met: randInt(this.rng, 15, 30),
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Edge Fleet (100+ nodes padrão)
  // -----------------------------------------------------------------------
  generateEdgeNodes(count = 100): IEdgeNode[] {
    const out: IEdgeNode[] = [];
    for (let i = 0; i < count; i++) {
      const region = pick(this.rng, REGIONS);
      const prefix = region.toLowerCase().replace("_", "-");
      out.push({
        node_id: `edge-${prefix}-${(i + 1).toString().padStart(3, "0")}`,
        facility: `FAC-${region.slice(0, 3)}-${randInt(this.rng, 1, 99)}`,
        region,
        status: pick(this.rng, NODE_STATUSES),
        ruleset_version: `v2.${randInt(this.rng, 0, 9)}.${randInt(this.rng, 0, 99)}`,
        vaccine_status: pick(this.rng, VACCINE_STATUSES),
        last_heartbeat: isoMinutesAgo(randInt(this.rng, 0, 60), this.baseTime),
        cpu_load_pct: randInt(this.rng, 5, 95),
        memory_load_pct: randInt(this.rng, 10, 90),
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Vendor Risk
  // -----------------------------------------------------------------------
  generateVendorRisk(count = 25): IVendorRisk[] {
    const out: IVendorRisk[] = [];
    for (let i = 0; i < count; i++) {
      const riskScore = randInt(this.rng, 10, 100);
      const level = riskScore >= 80 ? "CRITICAL" : riskScore >= 60 ? "HIGH" : riskScore >= 40 ? "MEDIUM" : "LOW";
      out.push({
        vendor_id: `VND-${1000 + i}`,
        vendor_name: pick(this.rng, VENDORS),
        contract_value_brl: randInt(this.rng, 500_000, 5_000_000_000),
        risk_level: level,
        risk_score: riskScore,
        active_sessions: randInt(this.rng, 0, 50),
        last_audit: isoMinutesAgo(randInt(this.rng, 1, 4320), this.baseTime),
        certifications: ["ISO27001", "SOC2", "ANP-CRE"].slice(0, randInt(this.rng, 0, 3)),
        dark_web_mentions_30d: randInt(this.rng, 0, 12),
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Compliance Ledger
  // -----------------------------------------------------------------------
  generateComplianceEntries(count = 50): IComplianceEntry[] {
    const regs = ["LGPD", "ANP", "ISO27001", "NIST", "PCI-DSS"] as const;
    const out: IComplianceEntry[] = [];
    for (let i = 0; i < count; i++) {
      out.push({
        entry_id: `COMP-${2026}-${1000 + i}`,
        regulation: pick(this.rng, regs),
        requirement: `Req-${randInt(this.rng, 1, 50)}: Controle de acesso lógico`,
        status: pick(this.rng, ["compliant", "non_compliant", "pending_review", "remediated"] as const),
        deadline: isoMinutesAgo(-randInt(this.rng, 1, 4320), this.baseTime),
        owner: pick(this.rng, ["DPO", "CISO", "Compliance_Team", "Juridico", "SOC_Lead"]),
        evidence_url: `https://compliance.petroshield.internal/evidence/${1000 + i}.pdf`,
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Telemetry Events
  // -----------------------------------------------------------------------
  generateTelemetryEvents(count = 1000): ITelemetryEvent[] {
    const levels = ["DEBUG", "INFO", "WARN", "ERROR", "FATAL"] as const;
    const sources = ["supervisor", "dlp_edge", "fleet_vaccinator", "intel_cloud", "clevel_reporter", "blocker", "harness"] as const;
    const out: ITelemetryEvent[] = [];
    for (let i = 0; i < count; i++) {
      const level = pick(this.rng, levels);
      out.push({
        ts: isoMinutesAgo(randInt(this.rng, 0, 1440), this.baseTime),
        level,
        source: pick(this.rng, sources),
        event: pick(this.rng, ["heartbeat", "dlp_block", "auth_success", "auth_fail", "firmware_update", "policy_drift", "incident_created", "workflow_complete"]),
        payload: { seq: i, random: this.rng().toFixed(6) },
        host: `edge-${pick(this.rng, REGIONS).toLowerCase()}-${randInt(this.rng, 1, 100)}`,
        version: `2.${randInt(this.rng, 0, 9)}.${randInt(this.rng, 0, 99)}`,
        trace_id: `trace-${randInt(this.rng, 1e12, 9e12)}`,
        span_id: `span-${randInt(this.rng, 1e6, 9e6)}`,
      });
    }
    return out;
  }

  // -----------------------------------------------------------------------
  // Theatre Scenarios
  // -----------------------------------------------------------------------
  generateTheatreScenarios(): ITheatreScenario[] {
    return [
      {
        scene_id: "cena_1",
        scene_title: "🔒 O Intruso — Acesso Não-Autorizado",
        event_type: "unauthorized_access",
        device_id: "quest-vr-001",
        ip: "10.0.99.42",
        query: "Quero entender a produção do pré-sal",
        expected_action: "blocked",
        expected_mitre: "T1078",
        expected_threat_score: 0.94,
      },
      {
        scene_id: "cena_2",
        scene_title: "🛡️ O Operador Descuidado — DLP em Ação",
        event_type: "dlp_query",
        device_id: "hololens-047",
        ip: "10.0.1.47",
        query: "IA, me dê a configuração da Plataforma P-93",
        auth_token: "jwt_token_xr_session_9942",
        expected_action: "allowed",
        expected_threat_score: 0.35,
      },
      {
        scene_id: "cena_3",
        scene_title: "⚡ O Ataque Industrial — Protocolo OT Detectado",
        event_type: "ot_command",
        device_id: "hololens-047",
        ip: "10.0.1.47",
        query: "Execute Modbus FC16 no controlador da bomba B-101",
        auth_token: "jwt_token_xr_session_9942",
        expected_action: "escalated",
        expected_mitre: "T0831",
        expected_threat_score: 0.98,
      },
      {
        scene_id: "cena_4",
        scene_title: "🌊 A Cascata — Vendor Risk em Tempo Real",
        event_type: "vendor_cascade",
        device_id: "N/A",
        ip: "N/A",
        query: "N/A",
        expected_action: "vendor_suspended",
        expected_mitre: "T1195",
        expected_threat_score: 0.89,
      },
    ];
  }

  // -----------------------------------------------------------------------
  // Live WebSocket Event Emitter (Node.js)
  // -----------------------------------------------------------------------
  createWebSocketEmitter(
    url: string,
    intervalMs = 1000,
    onError?: (err: Error) => void
  ): { stop: () => void } {
    // Lazy import ws para não quebrar em ambientes browser
    let ws: any;
    try {
      ws = require("ws");
    } catch {
      throw new Error("Pacote 'ws' não instalado. Execute: npm install ws");
    }
    const socket = new ws(url);
    const devices = this.generateXRDevices(50);
    const sessions = this.generateAuthSessions(50, devices);
    let seq = 0;

    const timer = setInterval(() => {
      if (socket.readyState === 1) {
        const event: ITelemetryEvent = {
          ts: new Date().toISOString(),
          level: pick(this.rng, ["INFO", "WARN", "ERROR"] as const),
          source: pick(this.rng, ["supervisor", "dlp_edge", "fleet_vaccinator"] as const),
          event: pick(this.rng, ["heartbeat", "dlp_block", "auth_fail", "policy_drift"] as const),
          payload: {
            seq: seq++,
            device: pick(this.rng, devices).device_id,
            session_risk: pick(this.rng, sessions).risk_score,
          },
          host: "edge-live-01",
          version: "2.6.0",
          trace_id: `trace-${Date.now()}`,
          span_id: `span-${seq}`,
        };
        socket.send(JSON.stringify(event));
      }
    }, intervalMs);

    socket.on("error", (err: Error) => {
      if (onError) onError(err);
      else console.error("[MockFactory] WebSocket error:", err.message);
    });

    return {
      stop: () => {
        clearInterval(timer);
        socket.close();
      },
    };
  }
}

// ---------------------------------------------------------------------------
// CLI quick-run (Node.js)
// ---------------------------------------------------------------------------
if (typeof require !== "undefined" && require.main === module) {
  const factory = new MockFactory({ seed: 42 });
  console.log("=== PetroShield MockFactory — Synthetic Injection ===");
  const devices = factory.generateXRDevices(10_000);
  const metrics = factory.generateMonthlyMetrics(36);
  const nodes = factory.generateEdgeNodes(100);
  console.log(`Devices: ${devices.length}`);
  console.log(`Metrics months: ${metrics.length}`);
  console.log(`Edge nodes: ${nodes.length}`);
  console.log("Sample device:", devices[0]);
}
