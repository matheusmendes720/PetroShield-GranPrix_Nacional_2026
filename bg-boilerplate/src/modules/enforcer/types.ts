/**
 * @interface ThreatEvent — Evento de ameaça no ecossistema PetroShield.
 */
export interface ThreatEvent {
  id: string;
  timestamp: string;
  source: string;
  type: string;
  severity: 'LOW' | 'MEDIUM' | 'HIGH' | 'CRITICAL';
  description: string;
  payload?: string;
  mitigation?: string;
  mitigationSteps?: string[];
}

export type SOCPhase =
  | 'INITIALIZING' | 'MONITOR' | 'HUNT' | 'DETECT' | 'ANALYSE'
  | 'RESPOND' | 'IR_RECOVERY' | 'LESSONS_LEARNT' | 'STANDBY';

export interface SOCState {
  phase: SOCPhase;
  currentIncident: ThreatEvent | null;
  logs: LogEntry[];
  metrics: SOCMetrics;
  connectedAgents: string[];
}

export interface SOCMetrics {
  threatsBlocked: number;
  uptimeEvaded: number;
  moneySafeguarded: number;
  complianceStatus: number;
  networkHealth?: number;
}

export interface LogEntry {
  id: string;
  timestamp: string;
  agent: string;
  message: string;
  type: 'system' | 'agent' | 'alert' | 'tool' | 'rag';
}
