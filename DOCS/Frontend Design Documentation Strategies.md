# PetroShield AxeGuard — Frontend Design Document (FDD) v2.6

> **Projeto:** PetroShield AxeGuard SOC Agentic Dashboard  
> **Versão:** 2.6.0-harness  
> **Escopo:** Especificação completa de frontend: backend functions, data structures, BFF composition, widgets, charts, values e metrics por tab.  
> **Stack Alvo:** React 18 + TypeScript + Vite + Bun + Netlify  
> **Idioma:** Português (Brasil)

---

## 📑 Índice

1. [Visão Geral & Arquitetura](#1-visão-geral--arquitetura)
2. [Backend Functions & API Contracts](#2-backend-functions--api-contracts)
3. [Data Structures — Domain Model](#3-data-structures--domain-model)
4. [BFF Composition Layer](#4-bff-composition-layer)
5. [Tab 1: Dashboard](#5-tab-1-dashboard)
6. [Tab 2: Operations](#6-tab-2-operations)
7. [Tab 3: Theatre](#7-tab-3-theatre)
8. [Tab 4: Analytics](#8-tab-4-analytics)
9. [Atomic Component Library](#9-atomic-component-library)
10. [Chart Types & Visualization](#10-chart-types--visualization)
11. [Metrics, Values & Business KPIs](#11-metrics-values--business-kpis)
12. [State Management & Data Flow](#12-state-management--data-flow)
13. [Appendix: TypeScript Contracts](#13-appendix-typescript-contracts)

---

## 1. Visão Geral & Arquitetura

### 1.1 Propósito
O frontend do PetroShield AxeGuard é um **Operational Dashboard** de alta densidade projetado para:
- **Analistas SOC:** Monitoramento em tempo real de dispositivos XR, sessões e ameaças
- **Engenheiros OT:** Visualização de protocolos industriais e anomalias de controle
- **C-Level / Jurídico:** Compliance LGPD, custo evitado e métricas de negócio
- **Avaliadores SENAI:** Demonstração cinematográfica do Theatre Engine

### 1.2 Arquitetura de Camadas

```
┌──────────────────────────────────────────────┐
│  React 18 + Vite + Bun (Browser)             │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │ Dashboard│ │Operations│ │ Theatre │ ...   │
│  └────┬────┘ └────┬────┘ └────┬────┘        │
│       └─────────────┬─────────────┘          │
│              Zustand Store                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │TanStack │ │ WebSocket│ │Netlify │        │
│  │ Query   │ │ Client   │ │Function│        │
│  └────┬────┘ └────┬────┘ └────┬────┘        │
└───────┼───────────┼───────────┼──────────────┘
        │           │           │
┌───────┼───────────┼───────────┼──────────────┐
│       │           │           │              │
│  ┌────┴────┐ ┌────┴────┐ ┌────┴────┐        │
│  │REST API │ │SSE/WS   │ │Telemetry│        │
│  │FastAPI  │ │Bridge   │ │Ingest   │        │
│  └────┬────┘ └────┬────┘ └────┬────┘        │
│       └───────────┼───────────┘              │
│              BFF Layer (Python/TS)           │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐        │
│  │Theatre  │ │ DLP     │ │ Fleet   │        │
│  │Engine   │ │ Engine  │ │ Vaccinator      │
│  └─────────┘ └─────────┘ └─────────┘        │
└──────────────────────────────────────────────┘
```

### 1.3 Design Tokens — PetroShield Palette

| Token | Hex | Uso |
|-------|-----|-----|
| `neonGreen` | `#00FF41` | Online, Success, Primary Action |
| `fireOrange` | `#FF6200` | Warning, Active, Energy |
| `deepVoid` | `#0A0A0A` | Background base |
| `cyan` | `#00FFFF` | Info, Secondary, Links |
| `amber` | `#FF9500` | Caution, Attention |
| `alertRed` | `#FF3333` | Critical, Error, Offline |
| `purple` | `#BF00FF` | Telemetry, Trace, AI |
| `gold` | `#FFD700` | Achievement, Milestone |

### 1.4 Tipografia

| Função | Fonte | Tamanho | Peso |
|--------|-------|---------|------|
| Display / Banner | VT323 | 40px | 400 |
| Títulos de Seção | VT323 | 24px | 400 |
| Métricas / Números | JetBrains Mono | 28px | 700 |
| Corpo / Tabelas | JetBrains Mono | 14px | 400 |
| Labels / Tags | JetBrains Mono | 12px | 500 |

---

## 2. Backend Functions & API Contracts

### 2.1 REST Endpoints (FastAPI)

```typescript
// Base URL: /api/v1
interface APIEndpoints {
  // Auth & Sessions
  "GET /auth/sessions": { params: { active?: boolean }; response: IAuthSession[] };
  "GET /auth/sessions/:id": { response: IAuthSession };
  "POST /auth/refresh": { body: { device_id: string }; response: { token: string } };

  // Devices XR
  "GET /devices": { params: { status?: string; zone?: string; vendor?: string; limit?: number; offset?: number }; response: Paginated<IXRDevice> };
  "GET /devices/:id": { response: IXRDevice };
  "POST /devices/:id/wipe": { response: { success: boolean; job_id: string } };
  "POST /devices/:id/quarantine": { response: { success: boolean } };

  // DLP Pipeline
  "POST /dlp/analyze": { body: { query: string; device_id: string; session_id: string }; response: IDLPResult };
  "GET /dlp/blocks": { params: { from?: string; to?: string }; response: IDLPBlock[] };

  // Threat Intelligence
  "GET /threats": { params: { severity?: string; tactic?: string }; response: IThreatPattern[] };
  "GET /threats/mitre": { response: IMITREEntry[] };

  // Incidents
  "GET /incidents": { params: { status?: string; severity?: string; assignee?: string }; response: Paginated<IIncident> };
  "POST /incidents": { body: Partial<IIncident>; response: IIncident };
  "PATCH /incidents/:id": { body: Partial<IIncident>; response: IIncident };

  // Fleet / Edge Nodes
  "GET /fleet": { response: IEdgeNode[] };
  "GET /fleet/health": { response: IFleetHealth };
  "POST /fleet/vaccinate": { body: { node_ids: string[]; ruleset: string }; response: { vaccinated: number } };

  // Vendor Risk
  "GET /vendors": { response: IVendorRisk[] };
  "GET /vendors/:id/risk": { response: IVendorRisk };
  "POST /vendors/:id/suspend": { response: { suspended_sessions: number } };

  // Compliance
  "GET /compliance": { response: IComplianceEntry[] };
  "GET /compliance/summary": { response: IComplianceSummary };

  // Metrics & OKRs
  "GET /metrics/monthly": { params: { months?: number }; response: IMonthlyMetric[] };
  "GET /metrics/okrs": { response: IOKRSet[] };
  "GET /metrics/triple-surface": { response: ITripleSurfaceMetric[] };

  // Theatre Engine
  "POST /theatre/run": { body: { scene_id: string; mode: "mock" | "live" | "hybrid" }; response: ITheatreResult };
  "GET /theatre/scenarios": { response: ITheatreScenario[] };
  "GET /theatre/status": { response: { running: boolean; current_scene?: string; progress_pct: number } };

  // Telemetry (Serverless)
  "POST /telemetry": { body: ITelemetryEvent[]; response: { ingested: number } };
  "GET /telemetry/stream": { response: EventStream<ITelemetryEvent> };
}
```

### 2.2 WebSocket Events (Real-time)

```typescript
interface WSEvents {
  // Server → Client
  "device.heartbeat": { device_id: string; status: string; timestamp: string };
  "dlp.block": { session_id: string; query: string; entities: string[]; action: string };
  "incident.new": IIncident;
  "threat.detected": IThreatPattern;
  "theatre.transition": { node_name: string; state: object; timestamp: string };
  "theatre.complete": { scene_id: string; result: ITheatreResult };
  "fleet.vaccine.progress": { node_id: string; status: string; progress_pct: number };
  "compliance.alert": { entry_id: string; regulation: string; deadline: string };

  // Client → Server
  "subscribe": { channels: string[] };
  "unsubscribe": { channels: string[] };
  "ping": { timestamp: number };
}
```

### 2.3 Netlify Edge Functions (BFF)

```typescript
// netlify/edge-functions/bff-aggregator.ts
// Agrega múltiplos endpoints em uma única chamada para reduzir waterfall

interface BFFDashboardPayload {
  devices: IXRDevice[];
  sessions: IAuthSession[];
  incidents: IIncident[];
  metrics: IMonthlyMetric[];
  okrs: IOKRSet[];
  tripleSurface: ITripleSurfaceMetric[];
  fleetHealth: IFleetHealth;
  complianceSummary: IComplianceSummary;
}

// Route: GET /api/v1/bff/dashboard?refresh=live
// TTL: 5s para dados live, 60s para dados estáticos
```

---

## 3. Data Structures — Domain Model

### 3.1 Core Entities

```typescript
// Dispositivo XR
interface IXRDevice {
  device_id: string;           // "hololens-047"
  device_type: "HoloLens2" | "MetaQuest3" | "RealWear" | "MagicLeap2" | "VuzixM400";
  asset_tag: string | null;    // "PETRO-XR-2047-047"
  assigned_operator_id: string | null;
  assigned_vendor_id: string | null;
  mdm_enrollment_status: "kiosk" | "enrolled" | "compromised" | "unmanaged";
  kiosk_mode_enabled: boolean;
  facility_zone: string;       // "FPSO_P93"
  network_segment: "OT_Isolated" | "IT_Corporate" | "Vendor_VPN" | "DMZ";
  encryption_status: "AES-256" | "unencrypted" | "ChaCha20";
  remote_wipe_capable: boolean;
  geofence_locked: boolean;
  firmware_version: string;    // "24.11.1340"
  last_seen: string;           // ISO-8601
}

// Sessão de Autenticação
interface IAuthSession {
  session_id: string;          // "sess-9942-xr"
  user_id: string;
  device_id: string;
  auth_method: "passwordless" | "mfa" | "sso" | "biometric";
  risk_score: number;          // 0-100
  timestamp: string;
  ip_address: string;
  geolocation: string;
}

// Vendor Risk
interface IVendorRisk {
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

// Padrão de Ameaça MITRE
interface IThreatPattern {
  tactic_id: string;           // "TA0043"
  tactic_name: string;
  technique_id: string;        // "T1040"
  technique_name: string;
  asset_type: "ICS" | "IoT" | "IT" | "Cloud";
  severity: "low" | "medium" | "high" | "critical";
  mitigations: string[];
  detection_count_30d?: number;
  false_positive_rate?: number;
}

// Incidente
interface IIncident {
  incident_id: string;         // "INC-2026-0042"
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

// Métrica Mensal (Time-series)
interface IMonthlyMetric {
  month: string;               // "2026-04"
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

// OKR
interface IKeyResult {
  name: string;
  target: string;
  current: string;
  status: "on_track" | "at_risk" | "behind";
  progress_pct: number;
}

interface IOKRSet {
  quarter: string;             // "Q2-2026"
  objective: string;
  key_results: IKeyResult[];
}

// Edge Node
interface IEdgeNode {
  node_id: string;             // "edge-bahia-001"
  facility: string;
  region: "BAHIA" | "RIO_DE_JANEIRO" | "SAO_PAULO" | "ESPIRITO_SANTO";
  status: "online" | "offline" | "degraded" | "maintenance";
  ruleset_version: string;     // "v2.3.1"
  vaccine_status: "up_to_date" | "pending" | "outdated" | "quarantine";
  last_heartbeat?: string;
  cpu_load_pct?: number;
  memory_load_pct?: number;
}

// Triple Surface
interface ITripleSurfaceMetric {
  surface: "OT_Perimeter" | "IT_Corporate" | "Cloud_SaaS";
  label: string;
  blocks_30d: number;
  active_alerts: number;
  trend: "up" | "down" | "stable";
}

// Theatre Scenario
interface ITheatreScenario {
  scene_id: string;            // "cena_1"
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

// Telemetry
interface ITelemetryEvent {
  ts: string;
  level: "DEBUG" | "INFO" | "WARN" | "ERROR" | "FATAL";
  source: string;
  event: string;
  payload: Record<string, unknown>;
  host: string;
  version: string;
  trace_id?: string;
  span_id?: string;
}
```

### 3.2 DLP Specific Types

```typescript
interface IDLPResult {
  action: "allowed" | "blocked" | "escalated" | "sanitized";
  original_query: string;
  sanitized_query: string;
  entities_found: IDLPEntity[];
  threat_score: number;
  latency_ms: number;
  pipeline_stages: IDLPStage[];
}

interface IDLPEntity {
  type: "ativo_restrito" | "poco" | "credencial" | "cpf" | "coordenada" | "senha";
  value: string;
  redacted: string;
  classification: "public" | "internal" | "restricted" | "critical";
  position: [number, number]; // start, end na query
}

interface IDLPStage {
  stage: "regex" | "heuristic" | "ml_classifier" | "decision";
  status: "pass" | "block" | "flag";
  latency_ms: number;
  details?: object;
}
```

---

## 4. BFF Composition Layer

### 4.1 Propósito
O BFF (Backend for Frontend) agrega dados de múltiplos microserviços Python em payloads otimizados para cada tab do dashboard, eliminando waterfalls de rede no cliente.

### 4.2 Endpoints BFF por Tab

```typescript
// BFF Dashboard — Tab 1
GET /bff/dashboard
Response: {
  summary: {
    active_sessions: number;
    devices_online: number;
    devices_compromised: number;
    incidents_open_critical: number;
    cumulative_cost_avoided_brl: number;
    compliance_rate_pct: number;
    mttr_minutes: number;
    mttr_target_minutes: number;
  };
  sparklines: {
    queries_24h: number[];      // 24 pontos, 1 por hora
    blocks_24h: number[];
    latency_24h: number[];
  };
  cards: IMetricCard[];
  recent_incidents: IIncident[];
  top_threats: IThreatPattern[];
}

// BFF Operations — Tab 2
GET /bff/operations
Response: {
  workflows: IAgenticWorkflow[];
  playbook_runs: IPlaybookRun[];
  fleet_grid: IEdgeNode[];
  vendor_risk_top5: IVendorRisk[];
  compliance_alerts: IComplianceAlert[];
  live_logs: ILogEntry[];
}

// BFF Theatre — Tab 3
GET /bff/theatre
Response: {
  scenes: ITheatreScenario[];
  current_scene?: ITheatreScenario;
  graph_nodes: IGraphNode[];
  graph_edges: IGraphEdge[];
  live_log: ITheatreLogEntry[];
  metrics: {
    avg_scene_duration_ms: number;
    success_rate_pct: number;
    nodes_executed_total: number;
  };
}

// BFF Analytics — Tab 4
GET /bff/analytics?range=30d&group_by=week
Response: {
  financial: {
    cost_avoided_series: ITimeSeriesPoint[];
    roi_series: ITimeSeriesPoint[];
    downtime_hours_avoided: number;
  };
  operational: {
    incidents_by_severity: IPieSlice[];
    incidents_by_status: IPieSlice[];
    mttr_trend: ITimeSeriesPoint[];
    mttd_trend: ITimeSeriesPoint[];
  };
  fleet: {
    health_radar: IRadarPoint[];
    vaccine_coverage_pct: number;
    nodes_by_region: IBarSegment[];
  };
  compliance: {
    audits_by_regulation: IBarSegment[];
    overdue_trend: ITimeSeriesPoint[];
  };
}
```

### 4.3 Aggregation Strategy

| Fonte | Dado | TTL Cache | Refresh |
|-------|------|-----------|---------|
| FastAPI | Devices, Sessions | 5s | WebSocket push |
| TheatreEngine | Scenes, Graph | 0s (real-time) | SSE stream |
| MockFactory | Synthetic bulk | 60s | Manual / Cron |
| Netlify Function | Telemetry ingest | — | Event-driven |

---

## 5. Tab 1: Dashboard

### 5.1 Layout Template

```
┌──────────────────────────────────────────────────────────────┐
│ Header: PetroShield AxeGuard v2.6 │ Status: OPERATIONAL       │
├──────────┬──────────────────────────┬────────────────────────┤
│          │  Metric Cards (6x grid)  │                        │
│  Torch   │  [M1][M2][M3][M4][M5][M6]│  Mini-Stats            │
│  Widget  │                          │  [S1][S2][S3]          │
│          ├──────────────────────────┼────────────────────────┤
│          │ Agentic Loop Stepper     │ Triple Surface Radar   │
├──────────┼──────────────────────────┼────────────────────────┤
│ Compliance Heartbeat │ Vendor Spotlight │ Event Stream (Live) │
├──────────────────────┴──────────────────┴────────────────────┤
│ Live Event Stream — Agentic Daily Routines                   │
└──────────────────────────────────────────────────────────────┘
```

### 5.2 Widgets & Components

#### Torch Widget (`<TorchAnimation />`)
- **Tipo:** Atom / Molecule
- **Props:** `size: "sm" | "md" | "lg"; animated: boolean`
- **Visual:** ASCII art animado com keyframes CSS (fallback) ou WebGL particles
- **Cores:** Laranja (`#FF6200`) + Ciano (`#00FFFF`) para o banner PetroShield
- **Ações:** Click → expande para fullscreen; Double-click → pause animation

#### Metric Cards (`<MetricCard />`)
- **Tipo:** Molecule
- **Props:**
```typescript
interface MetricCardProps {
  title: string;
  value: string | number;
  delta?: string;               // "+12% vs mês passado"
  deltaType?: "positive" | "negative" | "neutral";
  icon?: LucideIconName;
  color?: PetroColor;
  sparkline?: number[];         // últimos 30 pontos
  alertThreshold?: number;      // dispara pulse animation se valor > threshold
  onClick?: () => void;
}
```
- **Layout:**
```
┌─────────────────────┐
│ [icon] Title        │
│                     │
│ [Value]             │
│ ▁▂▄▆█ sparkline     │
│ [Delta]             │
└─────────────────────┘
```

**6 Cards do Dashboard:**
| ID | Título | Valor | Delta | Cor |
|----|--------|-------|-------|-----|
| M1 | Sessões Ativas | `devices.filter(d => d.status !== "compromised").length` | — | `neonGreen` |
| M2 | Vazamentos Evitados (MoM) | `latestMetric.leaks_prevented` | "+12% vs mês passado" | `neonGreen` |
| M3 | Re-Auths Biométricas | `latestMetric.biometric_reauths` | "Gaze liveness OK" | `cyan` |
| M4 | Bloqueios Shadow IT | `latestMetric.shadow_it_blocks` | "Túneis isolados" | `alertRed` |
| M5 | Custo Evitado YTD | `R$ ${cumulativeCost / 1_000_000}M` | "ROI > 1200%" | `amber` |
| M6 | Cobertura Frota | `${fleetHealth.coverage_pct}%` | `${online}/${total} nodes` | `neonGreen` |

#### Agentic Loop Stepper (`<AgenticStepper />`)
- **Tipo:** Organism
- **Props:** `phases: string[]; activeIndex: number; completedColor?: string`
- **Fases:** `["MONITOR", "DETECT", "ANALYSE", "RESPOND", "HUNT", "LESSONS"]`
- **Visual:** Timeline horizontal com dots conectados por linha
- **Estados:** `pending` (dim), `active` (pulse + cyan), `completed` (neonGreen + check)
- **Animação:** Transição suave entre fases com `framer-motion` layoutId

#### Triple Surface Radar (`<TripleSurfaceRadar />`)
- **Tipo:** Organism
- **Dados:** `ITripleSurfaceMetric[]`
- **Visual:** Radar/Spider chart (Recharts `RadarChart`) com 3 eixos
- **Cores:**
  - OT_Perimeter: `fireOrange`
  - IT_Corporate: `cyan`
  - Cloud_SaaS: `purple`
- **Interação:** Hover em vértice → tooltip com `blocks_30d`, `active_alerts`, `trend`

#### Compliance Heartbeat (`<ComplianceHeartbeat />`)
- **Tipo:** Organism
- **Props:** `summary: IComplianceSummary`
- **Visual:**
  - Progress ring para `compliance_rate_pct`
  - Lista de 3 itens: Total | Pendentes | Atrasados
  - Cor dos itens: Verde (0) → Âmbar (1-2) → Vermelho (>2)
- **Ação:** Click em "Pendentes" → navega para Operations tab filtrado

#### Vendor Spotlight (`<VendorSpotlight />`)
- **Tipo:** Organism
- **Props:** `vendors: IVendorRisk[]; maxItems?: number`
- **Visual:** Cards compactos dos vendors CRITICAL / HIGH
- **Dados:** `vendor_name`, `risk_score`, `contract_value_brl`, `dark_web_mentions_30d`
- **Alerta:** Se `dark_web_mentions_30d > 0`, badge pulsante vermelho

#### Live Event Stream (`<EventStream />`)
- **Tipo:** Organism
- **Props:**
```typescript
interface EventStreamProps {
  events: ILogEntry[];
  maxRows?: number;
  highlightPatterns?: RegExp[];
  autoScroll?: boolean;
  filter?: { level?: string[]; source?: string[] };
}
```
- **Visual:** Tabela virtualizada (`react-window`) com scroll auto
- **Colunas:** Timestamp | Level | Source | Event | Payload (collapsed)
- **Highlight:** Regex para CPF, Poço, Credencial → cores DLP
- **Cores de Level:** DEBUG (dim), INFO (cyan), WARN (amber), ERROR (red), FATAL (red bg)

### 5.3 Charts & Visualization

| Chart | Biblioteca | Dados | Propósito |
|-------|-----------|-------|-----------|
| Sparkline (MetricCard) | Custom SVG | `number[]` | Tendência 30 dias em micro-escala |
| Radar (Triple Surface) | Recharts | `ITripleSurfaceMetric[]` | Distribuição de bloqueios por superfície |
| Progress Ring (Compliance) | Custom SVG | `number` (0-100) | Taxa de conformidade visual |

---

## 6. Tab 2: Operations

### 6.1 Layout Template

```
┌──────────────────────────────────────────────────────────────┐
│ Header: Operações Agentic                                    │
├──────────────┬────────────────────────┬──────────────────────┤
│              │                        │                      │
│  Playbook    │  Workflow Inspector    │  Live Log + Run      │
│  Table       │  (State JSON / Graph)  │  Controls            │
│  (40%)       │  (35%)                 │  (25%)               │
│              │                        │                      │
├──────────────┼────────────────────────┼──────────────────────┤
│ Fleet Grid   │ Vendor Risk Matrix     │ Compliance Alerts    │
│ (50%)        │ (25%)                  │ (25%)                │
└──────────────┴────────────────────────┴──────────────────────┘
```

### 6.2 Widgets & Components

#### Playbook Table (`<PlaybookTable />`)
- **Tipo:** Organism
- **Props:**
```typescript
interface PlaybookTableProps {
  workflows: IAgenticWorkflow[];
  onSelect: (id: string) => void;
  onRun: (id: string) => void;
  onClone?: (id: string) => void;
  onExport?: (id: string) => void;
  filter?: { type?: string; status?: string };
}
```
- **Colunas:**
| Coluna | Chave | Tipo | Ações |
|--------|-------|------|-------|
| ID | `workflow_id` | string | — |
| Nome | `workflow_name` | string | Truncado 40 chars |
| Trigger | `trigger_event` | badge | Cor por categoria |
| SLA | `sla_breach_threshold_sec` | progress | Verde (<50%), Âmbar (50-80%), Vermelho (>80%) |
| Última Execução | `last_run_at` | relative time | "2m atrás" |
| Ações | — | button group | Run ▶, Clone, Export JSON |

- **Virtualização:** `@tanstack/react-table` + `react-window` para >100 workflows
- **Row Actions:**
  - **Run:** Dispara `POST /workflows/:id/run`, abre modal de confirmação
  - **Clone:** Cópia com `_clone` suffix no ID
  - **Export:** Download JSON com schema completo

#### Workflow Inspector (`<WorkflowInspector />`)
- **Tipo:** Organism
- **Estados:**
  - `idle`: Placeholder "Selecione um playbook"
  - `selected`: Visualização do grafo agentic + estado atual
  - `running`: Animação de progresso + logs em tempo real
  - `completed`: Resultado final + métricas
- **Sub-components:**
  - `<WorkflowGraph />`: React Flow com nós (supervisor, dlp_edge, intel_cloud, fleet_vaccinator, clevel_reporter, blocker, vendor_cascade)
  - `<StateJSON />`: Visualizador JSON collapsible com syntax highlighting
  - `<OutcomePanel />`: Cards de resultado financeiro e operacional

#### Live Log + Run Controls (`<OperationsConsole />`)
- **Tipo:** Organism
- **Controles:**
  - **Run Selected:** Botão primário (neonGreen) — executa playbook selecionado
  - **Stop All:** Botão de perigo (alertRed) — kill switch para todas as execuções
  - **Filter:** Toggle por level (DEBUG, INFO, WARN, ERROR)
  - **Search:** Fuzzy search em tempo real nos logs

#### Fleet Grid (`<FleetGrid />`)
- **Tipo:** Organism
- **Props:**
```typescript
interface FleetGridProps {
  nodes: IEdgeNode[];
  groupBy?: "region" | "status" | "vaccine_status";
  onNodeClick?: (node: IEdgeNode) => void;
  selectionMode?: "single" | "multi";
  onSelectionChange?: (ids: string[]) => void;
}
```
- **Visual:** CSS Grid com cards de node
- **Card de Node:**
```
┌─────────────────────┐
│ [status-dot] edge-bahia-001
│ Region: BAHIA       │
│ CPU: 45%  MEM: 62%  │
│ [vaccine badge]     │
└─────────────────────┘
```
- **Cores de Status:**
  - online: `neonGreen`
  - offline: `alertRed`
  - degraded: `amber`
  - maintenance: `cyan`
- **Bulk Actions:** Seleção múltipla → "Vaccinate Selected", "Remote Wipe", "Restart Ruleset"

#### Vendor Risk Matrix (`<VendorRiskMatrix />`)
- **Tipo:** Organism
- **Visual:** Scatter plot (Recharts `ScatterChart`)
- **Eixos:**
  - X: `risk_score` (0-100)
  - Y: `contract_value_brl` (log scale)
  - Size: `active_sessions`
  - Color: `risk_level`
- **Threshold Lines:**
  - Vertical em score=80 (CRITICAL threshold)
  - Horizontal em R$ 1B (high-value contract)
- **Quadrantes:**
  - Q1 (alto score, alto valor): **PERIGO MÁXIMO** — badge pulsante
  - Q2 (baixo score, alto valor): Monitorar
  - Q3 (alto score, baixo valor): Suspender
  - Q4 (baixo score, baixo valor): OK

#### Compliance Alerts (`<ComplianceAlerts />`)
- **Tipo:** Molecule
- **Visual:** Lista de cards com countdown para deadline
- **Dados:** `IComplianceEntry[]`
- **Estados:**
  - `compliant`: Card verde com check
  - `pending_review`: Card âmbar com relógio + countdown
  - `non_compliant`: Card vermelho com alerta
  - `remediated`: Card cinza (strikethrough)
- **Ação:** Click → expande evidência (`evidence_url`)

### 6.3 Charts & Visualization

| Chart | Biblioteca | Dados | Propósito |
|-------|-----------|-------|-----------|
| Workflow Graph | React Flow | `IGraphNode[], IGraphEdge[]` | Grafo agentic interativo |
| Fleet Grid | CSS Grid + Custom | `IEdgeNode[]` | Status visual da frota |
| Vendor Scatter | Recharts Scatter | `IVendorRisk[]` | Matrix risco x valor |
| SLA Progress | Custom SVG | `number` | Progresso do playbook |

---

## 7. Tab 3: Theatre

### 7.1 Layout Template

```
┌──────────────────────────────────────────────────────────────┐
│ Header: Theatre Engine — Cenários Determinísticos            │
├──────────────┬───────────────────────────────────────────────┤
│              │                                               │
│  Scene       │  Stage — Narração + Visualização              │
│  Selector    │                                               │
│  (20%)       │  [Typewriter Text]                            │
│              │  [Agent Graph Animation]                      │
│              │                                               │
├──────────────┼───────────────────────────────────────────────┤
│  Controls    │  Timeline + Metrics ao Vivo                   │
│  (Play/Pause)│                                               │
├──────────────┴───────────────────────────────────────────────┤
│ Live Log do Theatre + KPIs da Sessão                         │
└──────────────────────────────────────────────────────────────┘
```

### 7.2 Widgets & Components

#### Scene Selector (`<SceneSelector />`)
- **Tipo:** Molecule
- **Props:** `scenes: ITheatreScenario[]; activeSceneId?: string; onSelect: (id) => void`
- **Visual:** Lista vertical com cards de cena
- **Card de Cena:**
```
┌─────────────────────────────┐
│ 🔒 Cena 1: O Intruso        │
│ Evento: unauthorized_access │
│ Device: quest-vr-001        │
│ MITRE: T1078                │
└─────────────────────────────┘
```
- **Estados:** `active` (borda neonGreen), `completed` (check + dim), `pending` (default)

#### Stage (`<TheatreStage />`)
- **Tipo:** Organism
- **Modos:**
  - `narration`: Typewriter effect com o texto da narração
  - `graph`: Animação do grafo agentic com transições de nó
  - `split`: Narration em 60% + Graph em 40%
- **Typewriter Config:**
  - Speed: 30ms/char para narração, 10ms/char para diálogos
  - Pause em pontuação: 300ms para `.`, 150ms para `,`
  - Cursor: Blinking block (`▮`) em `fireOrange`

#### Agent Graph Animation (`<AgentGraphAnimation />`)
- **Tipo:** Organism
- **Biblioteca:** React Flow ou Cytoscape.js
- **Nós:**
```typescript
interface IGraphNode {
  id: string;                  // "supervisor", "dlp_edge", etc.
  type: "start" | "agent" | "decision" | "end";
  label: string;
  status: "idle" | "active" | "completed" | "error";
  duration_ms?: number;
  payload_preview?: string;
}
```
- **Arestas:**
```typescript
interface IGraphEdge {
  id: string;
  source: string;
  target: string;
  label?: string;              // "allowed", "blocked", "escalated"
  animated: boolean;
  color: string;
}
```
- **Animação:**
  - Nó ativo: Pulse + glow em `cyan`
  - Aresta ativa: Partículas fluindo na direção
  - Nó completed: NeonGreen fill
  - Nó error: AlertRed + shake animation

#### Theatre Controls (`<TheatreControls />`)
- **Tipo:** Molecule
- **Botões:**
  - **Play ▶:** Inicia cena selecionada
  - **Pause ⏸:** Pausa na transição atual
  - **Step →:** Avança um nó manualmente
  - **Reset ↺:** Volta ao estado inicial
  - **Speed:** Toggle 1x / 2x / 4x

#### Theatre Metrics (`<TheatreMetrics />`)
- **Tipo:** Molecule
- **Métricas em tempo real:**
| Métrica | Fonte | Formato |
|---------|-------|---------|
| Nodes Executed | Contador | `X / Y` |
| Latency Acumulada | Soma | `XXX ms` |
| Threat Score | Último nó DLP | `0.XX` |
| Custo Evitado | C-Level Reporter | `R$ X.XM` |
| SLA Status | Comparativo | `✓ On Time` / `⚠ Breach` |

### 7.3 Charts & Visualization

| Chart | Biblioteca | Dados | Propósito |
|-------|-----------|-------|-----------|
| Agent Graph | React Flow | `IGraphNode[], IGraphEdge[]` | Fluxo agentic animado |
| Timeline | Custom SVG | `ITheatreLogEntry[]` | Timeline horizontal de eventos |
| Metrics Gauge | Recharts Gauge | `number` | Threat score radial |

---

## 8. Tab 4: Analytics

### 8.1 Layout Template

```
┌──────────────────────────────────────────────────────────────┐
│ Header: Analytics & Intelligence                             │
│ [Date Range Picker] [Export CSV] [Export PDF] [Refresh]      │
├──────────────┬────────────────────────┬──────────────────────┤
│              │                        │                      │
│  Financial   │  Trend Lines +         │  Fleet Health        │
│  Charts      │  Anomaly Detection     │  Radar               │
│  (30%)       │  (40%)                 │  (30%)               │
│              │                        │                      │
├──────────────┼────────────────────────┼──────────────────────┤
│ Incidents    │ Compliance             │ OKR Tracker          │
│ by Category  │ Heatmap                │ Progress Grid        │
│ (30%)        │ (40%)                  │ (30%)                │
└──────────────┴────────────────────────┴──────────────────────┘
```

### 8.2 Widgets & Components

#### Financial Charts (`<FinancialCharts />`)
- **Tipo:** Organism
- **Sub-charts:**
  - **Custo Evitado (Area Chart):** `IMonthlyMetric[].cost_avoided_brl` — últimos 36 meses
  - **ROI (Line Chart):** `roi_percentage` calculado por mês
  - **Downtime Evitado (Bar Chart):** Horas de downtime evitado por incidente
- **Anomaly Detection:** Ponto fora da banda Bollinger → badge "ANOMALY"

#### Trend Lines + Anomaly Detection (`<TrendAnalytics />`)
- **Tipo:** Organism
- **Métricas:**
  - Queries Processed (trend line)
  - Leaks Prevented (trend line)
  - Avg Latency (trend line com threshold de 50ms)
- **Bandas:** Média móvel 3 meses ± 2 desvios padrão
- **Highlight:**Âmbar para valores próximos ao threshold, vermelho para breach

#### Fleet Health Radar (`<FleetHealthRadar />`)
- **Tipo:** Organism
- **Eixos (6):**
  - Online Rate
  - Vaccine Coverage
  - CPU Load Médio
  - Memory Load Médio
  - Ruleset Compliance
  - Heartbeat Freshness
- **Comparativo:** Mês atual vs Mês anterior (2 séries sobrepostas)

#### Incidents by Category (`<IncidentBreakdown />`)
- **Tipo:** Organism
- **Visualização:**
  - Treemap: `incidents_by_type` (DLP, OT, Vendor, Phishing, Geofencing, etc.)
  - Pie Chart: `incidents_by_severity`
  - Horizontal Bar: Top 10 assignees por volume

#### Compliance Heatmap (`<ComplianceHeatmap />`)
- **Tipo:** Organism
- **Eixos:**
  - X: Regulações (LGPD, ANP, ISO27001, NIST, PCI-DSS)
  - Y: Meses (últimos 12)
  - Valor: `compliance_rate_pct`
- **Cores:**
  - 100%: `neonGreen`
  - 80-99%: `amber`
  - <80%: `alertRed`
- **Interação:** Click em célula → drill-down para lista de itens não conformes

#### OKR Tracker (`<OKRTracker />`)
- **Tipo:** Organism
- **Visualização:**
  - Grid de cards por quarter
  - Cada OKR: Progress bar segmentada por KR
  - Cores de status: Verde (on_track), Âmbar (at_risk), Vermelho (behind)
  - Detalhe: Expandable panel com descrição de cada KR

### 8.3 Charts & Visualization

| Chart | Biblioteca | Dados | Propósito |
|-------|-----------|-------|-----------|
| Area (Custo) | Recharts | `IMonthlyMetric[]` | Evolução financeira |
| Line (Trends) | Recharts | `IMonthlyMetric[]` | Tendências operacionais |
| Radar (Fleet) | Recharts | `IFleetHealth` | Saúde multidimensional |
| Treemap (Incidents) | Recharts | `IIncident[]` | Densidade por categoria |
| Heatmap (Compliance) | Custom SVG | `IComplianceEntry[]` | Matriz temporal de conformidade |
| Bar (OKRs) | Custom SVG | `IOKRSet[]` | Progresso de objetivos |

---

## 9. Atomic Component Library

### 9.1 Atoms

| Componente | Props | Descrição |
|------------|-------|-----------|
| `<StatusDot />` | `level: string; pulse?: boolean` | Indicador circular de status |
| `<Badge />` | `label: string; variant: string` | Tag colorida semântica |
| `<Sparkline />` | `data: number[]; color: string` | Linha SVG minimalista |
| `<ProgressRing />` | `value: number; max: number` | Anel de progresso SVG |
| `<IconButton />` | `icon: string; onClick; variant` | Botão quadrado com ícone |
| `<Token />` | `label: string; value: string` | Par label-valor inline |

### 9.2 Molecules

| Componente | Props | Descrição |
|------------|-------|-----------|
| `<MetricCard />` | `MetricCardProps` | Card de métrica com sparkline |
| `<SearchBar />` | `value; onChange; placeholder` | Input com ícone de busca |
| `<FilterChip />` | `label; active; onToggle` | Chip toggleable para filtros |
| `<TimelineItem />` | `time; title; description; status` | Item de timeline vertical |
| `<LogEntry />` | `entry: ILogEntry` | Linha de log colorida por level |

### 9.3 Organisms

| Componente | Props | Descrição |
|------------|-------|-----------|
| `<EventStream />` | `EventStreamProps` | Stream de logs virtualizado |
| `<PlaybookTable />` | `PlaybookTableProps` | Tabela de workflows com ações |
| `<FleetGrid />` | `FleetGridProps` | Grid de cards de edge nodes |
| `<VendorRiskMatrix />` | `vendors: IVendorRisk[]` | Scatter plot interativo |
| `<ComplianceHeatmap />` | `entries: IComplianceEntry[]` | Heatmap mensal |
| `<TheatreStage />` | `scene: ITheatreScenario` | Stage com narração + grafo |
| `<AgentGraphAnimation />` | `nodes; edges; activeNodeId` | Grafo agentic animado |

---

## 10. Chart Types & Visualization

### 10.1 Decision Matrix: Qual Chart Usar?

| Dado | Objetivo | Chart Recomendado | Biblioteca |
|------|----------|-------------------|------------|
| Time-series (métricas mensais) | Tendência ao longo do tempo | Area / Line | Recharts |
| Categorias (incidentes por tipo) | Composição / Part-to-whole | Treemap / Donut | Recharts |
| Correlação (risco x valor) | Relação entre variáveis | Scatter | Recharts |
| Performance multidimensional | Comparar múltiplos eixos | Radar | Recharts |
| Distribuição temporal | Padrões sazonais | Heatmap | Custom SVG |
| Progresso (OKRs) | Avanço percentual | Segmented Bar | Custom SVG |
| Status discreto | Estado atual | Status Dot / Badge | Custom |
| Hierarquia (grafo agentic) | Fluxo de processos | Node Graph | React Flow |

### 10.2 Configurações Visuais Padrão

```typescript
const CHART_THEME = {
  colors: {
    primary: PETROSHIELD_TOKENS.neonGreen,
    secondary: PETROSHIELD_TOKENS.cyan,
    warning: PETROSHIELD_TOKENS.amber,
    danger: PETROSHIELD_TOKENS.alertRed,
    info: PETROSHIELD_TOKENS.purple,
    grid: "#1A1A1A",
    text: "#E0E0E0",
    textMuted: "#666666",
  },
  grid: {
    strokeDasharray: "3 3",
    stroke: "#1A1A1A",
    vertical: false,
  },
  tooltip: {
    backgroundColor: "#0A0A0A",
    borderColor: "#FF6200",
    borderWidth: 1,
    style: { fontFamily: "JetBrains Mono", fontSize: 12 },
  },
  legend: {
    style: { fontFamily: "JetBrains Mono", fontSize: 12, color: "#E0E0E0" },
  },
};
```

### 10.3 Animações

| Elemento | Tipo | Duração | Easing |
|----------|------|---------|--------|
| MetricCard value | Count-up | 800ms | easeOutExpo |
| Sparkline draw | SVG stroke-dashoffset | 600ms | easeOutCubic |
| Graph node activate | Scale + glow | 300ms | spring(1, 100, 10) |
| Toast / Alert | Slide-in + fade | 200ms | easeOutQuart |
| Tab switch | Fade cross | 150ms | linear |
| Modal open | Scale + backdrop fade | 250ms | easeOutCubic |

---

## 11. Metrics, Values & Business KPIs

### 11.1 Métricas Técnicas (SRE Golden Signals)

| Métrica | Fonte | Target | Alerta |
|---------|-------|--------|--------|
| **Latency (p99)** | DLP Pipeline | < 50ms | > 100ms |
| **Throughput** | Queries / min | > 1000 | < 500 |
| **Error Rate** | 5xx / total | < 0.1% | > 1% |
| **Saturation** | Edge Node CPU | < 80% | > 90% |

### 11.2 Métricas de Negócio (C-Level)

| Métrica | Fórmula | Target 2026 | Atual |
|---------|---------|-------------|-------|
| **Custo Evitado YTD** | `SUM(cost_avoided_brl)` | R$ 25M | R$ 13.45M |
| **ROI** | `(Custo Evitado / Investimento) * 100` | > 1200% | > 1200% |
| **MTTD** | Mean Time to Detect | < 1 min | 47s |
| **MTTR** | Mean Time to Respond | < 4h | 23 min |
| **DLP Coverage** | Queries bloqueadas / total | 99.5% | 99.8% |
| **Fleet Vaccine** | Nodes up_to_date / total | 95% | 92.9% |
| **Compliance Rate** | Itens compliant / total | 100% | 100% |
| **Vendor Critical** | Vendors monitorados / total | 100% | 87.5% |

### 11.3 Métricas de Segurança (SOC)

| Métrica | Fonte | Janela |
|---------|-------|--------|
| Threats Blocked (30d) | Triple Surface | Rolling 30d |
| Active Alerts | DLP + OT + Vendor | Real-time |
| Incidents by Severity | Incident KB | MTD / QTD / YTD |
| Biometric Reauths | Auth Sessions | 24h |
| Shadow IT Tunnels | Network Scan | 24h |
| Dark Web Mentions | Vendor Risk | 30d |

### 11.4 Valores Financeiros Projetados

| Cenário | Proteção | Valor |
|---------|----------|-------|
| Vazamento de dados sísmicos | DLP + Vendor Risk | R$ 35M evitados |
| Ataque OT via IA | Protocol Sentinel | R$ 580k em downtime evitado |
| Multa LGPD | Compliance Auto | R$ 50M em multas evitadas |
| Sideloading RAT | Kiosk + Geofencing | R$ 890k em incidentes evitados |

---

## 12. State Management & Data Flow

### 12.1 Zustand Store Structure

```typescript
interface AppStore {
  // Tab state
  activeTab: "dashboard" | "operations" | "theatre" | "analytics";
  setActiveTab: (tab: string) => void;

  // Data caches
  devices: IXRDevice[];
  sessions: IAuthSession[];
  incidents: IIncident[];
  metrics: IMonthlyMetric[];
  okrs: IOKRSet[];
  workflows: IAgenticWorkflow[];
  fleet: IEdgeNode[];
  vendors: IVendorRisk[];
  compliance: IComplianceEntry[];
  scenes: ITheatreScenario[];

  // Live state (WebSocket)
  liveEvents: ILogEntry[];
  theatreState: {
    running: boolean;
    currentScene?: string;
    currentNode?: string;
    progress: number;
  };

  // UI state
  selectedDeviceId?: string;
  selectedWorkflowId?: string;
  selectedSceneId?: string;
  dateRange: [Date, Date];
  filters: {
    severity?: string[];
    status?: string[];
    region?: string[];
  };

  // Actions
  fetchDashboard: () => Promise<void>;
  fetchOperations: () => Promise<void>;
  runTheatreScene: (id: string) => Promise<void>;
  injectSynthetic: (count: number) => Promise<void>;
  appendLiveEvent: (event: ILogEntry) => void;
}
```

### 12.2 Data Flow Diagram

```
User Action → Zustand Action → TanStack Query / WebSocket
     ↑                                              ↓
  UI Re-render ←── Zustand State Update ←── API Response / WS Message
```

### 12.3 Caching Strategy

| Dado | Cache | Stale Time | Background Refetch |
|------|-------|------------|-------------------|
| Devices | 30s | 10s | Every 30s |
| Sessions | 10s | 5s | Every 10s |
| Incidents | 60s | 30s | Every 60s |
| Metrics | 5min | 1min | Every 5min |
| OKRs | 1h | 15min | Manual |
| Theatre | 0s | 0s | Real-time (WS) |

---

## 13. Appendix: TypeScript Contracts

### 13.1 Utility Types

```typescript
type PetroColor = "#00FF41" | "#FF6200" | "#0A0A0A" | "#00FFFF" | "#FF9500" | "#FF3333" | "#BF00FF" | "#FFD700";

interface Paginated<T> {
  data: T[];
  total: number;
  page: number;
  pageSize: number;
  hasNext: boolean;
}

interface TimeSeriesPoint {
  timestamp: string;
  value: number;
  label?: string;
}

interface PieSlice {
  name: string;
  value: number;
  color: string;
}

interface BarSegment {
  label: string;
  value: number;
  color: string;
  subLabel?: string;
}

interface RadarPoint {
  axis: string;
  value: number;
  fullMark: number;
}
```

### 13.2 API Error Contract

```typescript
interface APIError {
  status: number;
  code: string;           // "DLP_BLOCK_FAILED", "DEVICE_NOT_FOUND"
  message: string;
  details?: object;
  trace_id: string;
  timestamp: string;
}
```

### 13.3 WebSocket Message Contract

```typescript
interface WSMessage<T = unknown> {
  id: string;             // UUID v4
  channel: string;        // "dlp", "incidents", "theatre", "fleet"
  event: string;          // "block", "new", "transition", "heartbeat"
  payload: T;
  ts: string;             // ISO-8601
}
```

---

*Documento gerado como parte da Fase de Frontend Design Documentation — PetroShield AxeGuard v2.6*  
*Última atualização: 2026-04-17*
