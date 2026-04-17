# Logging & Observability Guide

> **Projeto:** PetroShield AxeGuard v2.6  
> **Escopo:** Padrões de logging estruturado, níveis de severidade, tracing distribuído e dashboards de saúde.

---

## 1. Níveis de Log

| Nível | Uso | Cor Rich | Exemplo |
|-------|-----|----------|---------|
| **DEBUG** | Desenvolvimento local apenas | `dim` | `advance_frame: idx=2` |
| **INFO** | Eventos de negócio normais | `cyan` | `DLP block: 3 entities` |
| **WARN** | Anomalias recuperáveis | `yellow` | `Vendor risk score > 60` |
| **ERROR** | Falhas operacionais | `red bold` | `WebSocket connection failed` |
| **FATAL** | Parada do sistema | `red on white` | `Database corruption` |

### Regra de Ouro
> Em produção (`NODE_ENV=production` ou `PYTHON_ENV=production`), **DEBUG é silenciado** e **INFO é amostrado** (1% se volume > 1000/s).

---

## 2. Estrutura de Log JSON

Todo log deve ser um objeto JSON com campos padronizados:

```json
{
  "timestamp": "2026-04-17T06:00:00.000Z",
  "severity": "INFO",
  "service": "dlp_edge",
  "trace_id": "abc123",
  "span_id": "def456",
  "message": "Query sanitizada com sucesso",
  "attributes": {
    "device_id": "hololens-047",
    "query_length": 120,
    "entities_found": 3,
    "latency_ms": 42
  }
}
```

### Convenções
- **message:** Frase completa em português ou inglês, sem templates crus
- **attributes:** Dados estruturados para queries (nunca coloque PII direto em `message`)
- **trace_id:** UUID v4, propagado via headers HTTP (`x-petroshield-trace-id`)

---

## 3. Logging no Python (scripts/)

### Padrão
```python
import logging
import structlog

structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)

logger = structlog.get_logger("dlp_edge")
logger.info("dlp_block", device_id="hololens-047", entities=3, latency_ms=42)
```

### Log de Métricas de Negócio
```python
logger.info(
    "business_metric",
    metric_name="cost_avoided_brl",
    value=1_500_000,
    period="2026-Q2",
)
```

---

## 4. Logging no TypeScript / Node

### Padrão
```typescript
import { logger } from "./telemetry";

logger.info({
  event: "dlp_block",
  deviceId: "hololens-047",
  entities: 3,
  latencyMs: 42,
});
```

### Implementação Recomendada (pino)
```typescript
import pino from "pino";

export const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  base: { service: "axeguard-web" },
  timestamp: pino.stdTimeFunctions.isoTime,
  formatters: {
    level: (label) => ({ severity: label.toUpperCase() }),
  },
});
```

---

## 5. Tracing Distribuído (OpenTelemetry)

### Propagação de Contexto
```
[Browser] --trace_id--> [Netlify Edge] --trace_id--> [FastAPI] --trace_id--> [TheatreEngine]
```

### Headers
- `traceparent`: `00-{trace_id}-{span_id}-01`
- `tracestate`: `petroshield=edge-bahia-001`

### Spans Principais
| Span | Duração Esperada | Atributos |
|------|-----------------|-----------|
| `http_request` | < 50ms | method, route, status |
| `dlp_pipeline` | < 10ms | entities_found, action |
| `theatre_scene` | 500ms-5s | scene_id, nodes_executed |
| `ws_event` | < 5ms | event_type, payload_bytes |

---

## 6. Dashboards de Saúde

### 6.1 SRE Golden Signals
```markdown
- **Latency:** p50, p95, p99 de todas as APIs
- **Traffic:** RPS por endpoint
- **Errors:** Taxa 5xx / 4xx por serviço
- **Saturation:** CPU/Memória dos edge nodes
```

### 6.2 Business Health
```markdown
- Devices online / compromised / offline
- Incidentes abertos por severidade
- Custo evitado acumulado (YTD)
- Compliance rate (% auditorias aprovadas)
```

### 6.3 Alertas
| Condição | Canal | SLA de Resposta |
|----------|-------|----------------|
| `p99_latency > 100ms` | Slack #ops | 15 min |
| `error_rate > 1%` | PagerDuty | 5 min |
| `critical_incident_open > 0` | SMS + Slack | 2 min |
| `compliance_rate < 95%` | Email C-Level | 24h |

---

## 7. Ferramentas Recomendadas

| Propósito | Dev / Local | Produção |
|-----------|-------------|----------|
| Log Viewer | Rich Console + `jq` | Grafana Loki / Datadog |
| Traces | Jaeger Docker | Honeycomb / Tempo |
| Metrics | Prometheus local | Grafana Cloud / Mimir |
| APM | OpenTelemetry Collector | New Relic / Dynatrace |
| Alerting | — | PagerDuty + Slack |

---

## 8. Checklist de Code Review

- [ ] Todo `logger.info` tem `event` semanticamente nomeado
- [ ] Nenhum CPF, senha ou token aparece em logs
- [ ] `trace_id` é propagado entre todas as chamadas
- [ ] Logs de erro incluem stack trace em `attributes.error.stack`
- [ ] Métricas de negócio usam `business_metric` event type

---

*Documento gerado como parte da Fase de Observabilidade — PetroShield AxeGuard v2.6*
