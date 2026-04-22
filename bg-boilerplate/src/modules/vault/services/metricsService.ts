/**
 * @fileoverview High-Fidelity Security Metrics Engine (Client-Side BFF)
 * Simulador completo do SOC em memória para deploy estático.
 */

export type ThreatLevel = 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
export type AgentStatus = 'POLLING' | 'ANALYZING' | 'MITIGATING' | 'IDLE';
export type SOCLifecyclePhase = 'MONITOR' | 'DETECT' | 'TRIAGE_L1' | 'ANALYSIS_L2' | 'RESPONSE_L3' | 'RECOVERY' | 'HUNT' | 'LESSONS_LEARNT';

export interface SecurityAgent {
  id: string;
  name: string;
  type: 'DLP' | 'NETWORK' | 'ENDPOINT' | 'HEURISTIC';
  status: AgentStatus;
  load: number;
  lastDetection: string | null;
  neuralHealth: number;
}

export interface SecurityIncident {
  id: string;
  timestamp: string;
  type: 'SQL_INJECTION' | 'BRUTE_FORCE' | 'DLP_LEAK' | 'MALWARE_PHONING' | 'UNAUTHORIZED_ACCESS';
  severity: ThreatLevel;
  source: string;
  status: 'OPEN' | 'INVESTIGATING' | 'RESOLVED';
  summary: string;
}

export interface SecurityKPI {
  label: string;
  value: number | string;
  trend: 'up' | 'down' | 'stable';
  color: 'matrix' | 'orange' | 'cyan' | 'red';
  subValue?: string;
}

export interface ThreatEvent {
  id: string;
  type: string;
  source: string;
  severity: ThreatLevel;
  timestamp: string;
  meta?: string;
}

export interface ReportLog {
  date: string;
  title: string;
  content: string;
  status: 'DRAFT' | 'FINALIZED';
}

export interface MetricSnapshot {
  timestamp: number;
  cpu: number;
  memory: { total: number; used: number; percentage: number; swap: number; cachePressure: number };
  network: { rx: number; tx: number; activeConnections: number; threatScore: number; jitter: number; packetLoss: number };
  disk: { read: number; write: number; iowait: number; entropy: number };
  agents: SecurityAgent[];
  incidents: SecurityIncident[];
  kpis: SecurityKPI[];
  threatsHistory: { time: string; count: number }[];
  currentPhase: SOCLifecyclePhase;
  threatStream: ThreatEvent[];
  reportingAgent: ReportLog[];
  axeGuardStatus: 'ACTIVE' | 'ISOLATED' | 'BYPASS';
  langGraphNodes: { id: string; status: 'ACTIVE' | 'WAITING' | 'ERROR' }[];
}

export interface MetricsConfig {
  sensitivity: number;
  threshold: number;
  agentCount: number;
  realTimeMode: boolean;
  lifecycleSpeed: number;
}

class MetricsEngine {
  private history: MetricSnapshot[] = [];
  private maxHistory = 60;
  private lastSnap: MetricSnapshot | null = null;
  private config: MetricsConfig = { sensitivity: 45, threshold: 75, agentCount: 4, realTimeMode: true, lifecycleSpeed: 3 };
  private phases: SOCLifecyclePhase[] = ['MONITOR', 'DETECT', 'TRIAGE_L1', 'ANALYSIS_L2', 'RESPONSE_L3', 'RECOVERY', 'HUNT', 'LESSONS_LEARNT'];
  private currentPhaseIdx = 0;
  private phaseTicks = 0;
  private rawThreats: ThreatEvent[] = [];
  private reportHistory: ReportLog[] = [
    { date: '2026-04-17', title: 'INCIDENT_RPT_#AS-124', content: '# AXE-GUARD INCIDENT REPORT\n\n## STATUS: RESOLVED\nDetected unusual L7 egress pattern from secure enclave.\n\n### MITIGATION\nIsolated node #720 and flushed VNet caches.\n\n### LESSONS\nUpdate heuristics to detect fragment-level entropy shifts.', status: 'FINALIZED' }
  ];

  constructor() { this.initialize(); }

  private initialize() {
    const now = Date.now();
    for (let i = 0; i < this.maxHistory; i++) {
      this.history.push(this.generateSnapshot(now - (this.maxHistory - i) * 60000));
    }
  }

  public setConfig(newConfig: Partial<MetricsConfig>) { this.config = { ...this.config, ...newConfig }; }
  public getConfig() { return { ...this.config }; }

  private smooth(target: number, current: number, factor = 0.3) {
    return (current * factor) + (target * (1 - factor));
  }

  private generateSnapshot(timestamp: number): MetricSnapshot {
    const { sensitivity, threshold, lifecycleSpeed } = this.config;
    const isBurst = Math.random() * 100 < sensitivity;

    this.phaseTicks++;
    if (this.phaseTicks > (30 / (lifecycleSpeed || 1))) {
      this.currentPhaseIdx = (this.currentPhaseIdx + 1) % this.phases.length;
      this.phaseTicks = 0;
    }
    const currentPhase = this.phases[this.currentPhaseIdx];

    if (isBurst || Math.random() > 0.8) {
      const threatEvent: ThreatEvent = {
        id: 'EVT-' + Math.random().toString(36).substr(2, 5).toUpperCase(),
        type: currentPhase === 'DETECT' ? 'SIGNATURE_MATCH' : 'HEURISTIC_ANOMALY',
        source: `172.24.${Math.floor(Math.random() * 10)}.${Math.floor(Math.random() * 255)}`,
        severity: isBurst ? 'CRITICAL' : 'MEDIUM',
        timestamp: new Date().toISOString(),
        meta: `SHA256: 0x${Math.random().toString(16).substr(2, 12)}`
      };
      if (this.rawThreats.length > 20) this.rawThreats.shift();
      this.rawThreats.push(threatEvent);
    }

    const agents: SecurityAgent[] = [
      { id: 'AXE-G', name: 'Axe-Guard-DLP', type: 'DLP', status: isBurst ? 'MITIGATING' : 'POLLING', load: 45 + Math.random() * 20, lastDetection: isBurst ? 'CORP-PII-EXFIL' : null, neuralHealth: 98.4 },
      { id: 'LGS-1', name: 'LangGraph-Orchestrator', type: 'HEURISTIC', status: 'ANALYZING', load: 60, lastDetection: null, neuralHealth: 99.9 },
      { id: 'PROM-V', name: 'Prometheus-Observer', type: 'NETWORK', status: 'POLLING', load: 20, lastDetection: null, neuralHealth: 88.2 },
    ];

    const targetCpu = (isBurst ? 85 : 20) + Math.random() * 10;
    const cpu = this.lastSnap ? this.smooth(targetCpu, this.lastSnap.cpu) : targetCpu;
    const targetRx = 100 + Math.random() * 1000 + (isBurst ? 5000 : 0);
    const rx = this.lastSnap ? this.smooth(targetRx, this.lastSnap.network.rx) : targetRx;
    const targetTx = 50 + Math.random() * 500 + (isBurst ? 2000 : 0);
    const tx = this.lastSnap ? this.smooth(targetTx, this.lastSnap.network.tx) : targetTx;
    const targetEntropy = 0.2 + (Math.random() * 0.1) + (isBurst ? 0.3 : 0);
    const entropy = this.lastSnap ? this.smooth(targetEntropy, this.lastSnap.disk.entropy, 0.9) : targetEntropy;
    const targetMemPercentage = 40 + (isBurst ? 30 : 0) + Math.random() * 5;
    const usedMem = (32 * targetMemPercentage) / 100;

    const snap: MetricSnapshot = {
      timestamp, cpu: Math.floor(cpu),
      memory: { total: 32, used: parseFloat(usedMem.toFixed(2)), percentage: Math.floor(targetMemPercentage), swap: isBurst ? 2.4 : 0.8, cachePressure: 15 + Math.random() * 10 },
      network: { rx: Math.floor(rx), tx: Math.floor(tx), activeConnections: 1200 + Math.floor(Math.random() * 200) + (isBurst ? 800 : 0), threatScore: isBurst ? 92 : 12, jitter: isBurst ? 12.4 : 1.2, packetLoss: isBurst ? 0.04 : 0 },
      disk: { read: 10, write: 5, iowait: 0.1, entropy },
      agents, incidents: isBurst ? [{ id: 'INC-' + Math.random().toString(36).substr(2, 4).toUpperCase(), timestamp: new Date().toISOString(), type: 'DLP_LEAK', severity: 'CRITICAL', source: 'INTERNAL_NODE_7_ZETA', status: 'OPEN', summary: 'Agentic LangGraph clusters identified PII leakage signatures in egress tunnel 0x42-B.' }] : [],
      kpis: [
        { label: 'SOC_PHASE', value: currentPhase, trend: 'stable', color: 'cyan', subValue: `Step ${this.phaseTicks}` },
        { label: 'AXE_SHIELD', value: (99.8 + Math.random() * 0.1).toFixed(2), trend: 'stable', color: 'matrix', subValue: 'Active Agents: 3' },
        { label: 'LLM_GUARD', value: 100, trend: 'up', color: 'matrix', subValue: 'Verified' },
      ],
      threatsHistory: Array.from({ length: 12 }, (_, j) => ({ time: `${12 - j}h`, count: Math.floor(Math.random() * threshold) + (isBurst ? 40 : 0) })),
      currentPhase, threatStream: [...this.rawThreats], reportingAgent: this.reportHistory,
      axeGuardStatus: isBurst ? 'ISOLATED' : 'ACTIVE',
      langGraphNodes: [
        { id: 'L1_TRIAGE', status: 'ACTIVE' },
        { id: 'L2_ANALYSIS', status: currentPhase.includes('ANALYSIS') ? 'ACTIVE' : 'WAITING' },
        { id: 'L3_RESPONSE', status: currentPhase.includes('RESPONSE') ? 'ACTIVE' : 'WAITING' },
      ],
    };
    this.lastSnap = snap;
    return snap;
  }

  public tick(): MetricSnapshot {
    const next = this.generateSnapshot(Date.now());
    this.history.push(next);
    if (this.history.length > this.maxHistory) this.history.shift();
    return next;
  }

  public getHistory() { return [...this.history]; }
}

export const metricsService = new MetricsEngine();
