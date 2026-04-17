# Telemetry & Serverless Web Architecture

> **Projeto:** PetroShield AxeGuard v2.6  
> **Foco:** Observabilidade, telemetria estruturada e funções serverless para ingestão e alertas.

---

## 1. Filosofia de Observabilidade

> *"Se não está instrumentado, não existe."*

O ecossistema PetroShield adota **OpenTelemetry** como padrão único para traces, metrics e logs, com exportação para backends serverless sempre que possível.

### Pilares
| Pilar | Ferramenta | Destino |
|-------|-----------|---------|
| **Traces** | OpenTelemetry JS/Python | Jaeger Cloud / Honeycomb |
| **Metrics** | OpenTelemetry + Prometheus | Grafana Cloud / Netlify Analytics |
| **Logs** | JSON Lines (structured) | Netlify Function → S3 → Athena |
| **Alertas** | OpenTelemetry + PagerDuty | Slack / Email / SMS |

---

## 2. Formato de Telemetria (JSON Lines)

Cada evento é uma linha JSON compacta, pronta para ingestão em batch:

```json
{"ts":"2026-04-17T06:00:00Z","level":"INFO","source":"dlp_edge","event":"dlp_block","payload":{"device":"hololens-047","entities":3,"latency_ms":42},"host":"edge-bahia-001","version":"2.6.0","trace_id":"trace-123...","span_id":"span-456..."}
```

### Schema Garantido
- `ts` — ISO-8601 UTC (obrigatório)
- `level` — DEBUG | INFO | WARN | ERROR | FATAL
- `source` — Identificador do componente
- `event` — Nome semântico do evento (snake_case)
- `payload` — Objeto livre (evite aninhamento > 3 níveis)
- `host` — Node ou instância que emitiu
- `version` — SemVer do componente
- `trace_id` / `span_id` — OpenTelemetry correlation (opcional)

---

## 3. Pipeline Serverless: Netlify Functions

### 3.1 Ingestor de Telemetria
**Arquivo:** `netlify/functions/telemetry-ingest.ts`

```typescript
import type { Config } from "@netlify/functions";

export default async (req: Request) => {
  if (req.method !== "POST") return new Response("Method Not Allowed", { status: 405 });
  
  const events = await req.json();
  // Validação básica
  const valid = events.filter((e: any) => e.ts && e.event && e.level);
  
  // Batch write para S3 (via presigned URL) ou DynamoDB
  await writeToS3Batch(valid);
  
  return Response.json({ ingested: valid.length });
};

export const config: Config = { path: "/api/v1/telemetry" };
```

### 3.2 WebSocket Bridge (Edge Function)
**Arquivo:** `netlify/edge-functions/ws-bridge.ts`

```typescript
export default async (request: Request, context: any) => {
  const upgrade = request.headers.get("upgrade");
  if (upgrade !== "websocket") return new Response("Expected websocket", { status: 400 });
  
  const [client, server] = Object.values(new WebSocketPair());
  context.waitUntil(handleSession(server));
  return new Response(null, { status: 101, webSocket: client });
};

async function handleSession(ws: WebSocket) {
  ws.accept();
  ws.addEventListener("message", (msg) => {
    const data = JSON.parse(msg.data as string);
    // Broadcast para subscribers do mesmo trace_id
    broadcastToChannel(data.trace_id, data);
  });
}
```

### 3.3 Alert Dispatcher
**Arquivo:** `netlify/functions/alert-dispatch.ts`

- Regra: Se `level === "CRITICAL"` ou `event === "dlp_block"` com `entities > 5`
- Ação: POST para Slack Webhook + PagerDuty Event API

---

## 4. Dashboard de Observabilidade (Web)

### 4.1 Live Telemetry Viewer
- **Fonte:** SSE stream de `/api/v1/telemetry/stream`
- **UI:** Tabela virtualizada com filtros por level, source, host
- **Highlight:** Vermelho para ERROR/FATAL, Âmbar para WARN

### 4.2 SLA Monitor
```ts
interface SLAMonitor {
  metric: "MTTD" | "MTTR" | "DLP_Latency";
  target: number;
  current: number;
  breachCount24h: number;
}
```

### 4.3 Cost Avoided Real-Time
- **Fonte:** Agregação de `cost_avoided_brl` nos eventos
- **Visual:** Contador animado + sparkline de 24h

---

## 5. Armazenamento & Analytics

### Opção A: S3 + Athena (Custo-baixo)
1. Netlify Function escreve em batch para S3 (`s3://petroshield-telemetry/YYYY/MM/DD/HH.jsonl`)
2. Athena table partitioning por `year/month/day/hour`
3. Queries SQL ad-hoc para auditoria

### Opção B: Upstash Kafka + ClickHouse (Real-time)
1. Edge Function publica em Kafka topic `telemetry.raw`
2. ClickHouse consumidor com materialized views
3. Grafana dashboards em sub-segundo

### Opção C: Netlify Blobs (Simplicidade)
1. `netlify-blobs` package para write direto
2. Limitado a 5MB/objeto, ideal para snapshots

---

## 6. Segurança & Compliance

- **Sanitização:** Nunca logar CPFs, senhas ou tokens JWT em `payload`
- **LGPD:** Campo `data_subject_id` opcional para anonimização
- **Retention:** 90 dias hot (S3 Standard), 2 anos cold (S3 Glacier)
- **CORS:** `Access-Control-Allow-Origin` restrito aos domínios PetroShield

---

*Documento gerado como parte da Fase de Observabilidade Serverless — PetroShield AxeGuard v2.6*
