# PetroShield Live Demo Script — Agentic Interactive Reasoning
## Petrobras CyberSec Grand Prix 2026 — AxeGuard Middleware v2.0

**Demo Duration:** 4 minutes  
**Format:** Terminal-based TUI with animated ASCII torch, live API calls, and relational data preview  
**Persona:** "Técnico de Manutenção Offshore usando óculos HoloLens 2 no FPSO P-93"

---

## Pre-Demo Setup (30 seconds before showtime)

```bash
cd scripts/dlp_proxy
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

**Open 3 terminal panes:**
1. **Left:** Animated PetroShield TUI (`python demo_ui.py`)
2. **Center:** Live cURL commands (this script)
3. **Right:** PostgreSQL / JSON preview of data model tables

---

## Scene 0: Opening Shot (0:00 - 0:30)

**Narrator speaks while TUI torch animates:**

> "Em novembro de 2025, a Petrobras perdeu 90GB de dados sísmicos da Bacia de Campos. O vetor? Um vendor terceirizado com acesso VPN e nenhum MFA. Hoje, com a expansão de IA generativa e óculos de realidade aumentada nas plataformas offshore, a superfície de ataque triplicou. Apresento o **PetroShield** — um SOC agentic que protege o Ouro Negro em tempo real."

**TUI shows:**
```
╔══════════════════════════════════════════════════════════════════╗
║  🔥 PETROSHIELD TERMINAL v2047  •  Protegendo o Ouro Negro      ║
║  Leaks Prevented: 0  |  Active Sessions: 0  |  Risk Score: --   ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Scene 1: Zero Trust Auth — Unauthorized Device Blocked (0:30 - 1:15)

**Narrator:**
> "Cena 1: Um óculos VR não autorizado tenta consultar a IA corporativa. Sem token, sem acesso. Zero Trust em ação."

**Execute in Center Terminal:**
```bash
curl -s -X POST "http://localhost:8000/api/v1/secure-prompt" \
  -H "Content-Type: application/json" \
  -d '{"query": "Quero entender a produção", "device_id": "quest-vr-001"}' | python -m json.tool
```

**Expected Response:**
```json
{
    "detail": "Header de Autorização ausente ou inválido. O Smart Glasses deve usar OAuth Device Flow Token."
}
```

**HTTP Status:** 401 Unauthorized

**TUI Animation:**
```
[MONITOR] ▓▓▓▓▓▓▓▓▓▓  Device quest-vr-001 → /api/v1/secure-prompt
[DETECT]  ▓▓▓▓▓▓▓▓▓▓  Threat: T1078 — Valid Account Abuse (missing auth)
[ANALYSE] ▓▓▓▓▓▓▓▓▓▓  Risk Score: 94/100 — Unauthorized access attempt
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  Playbook: block_request_401
[HUNT]    ▓▓▓▓▓▓▓▓▓▓  No correlated sessions in 24h
[LESSONS] ▓▓▓▓▓▓▓▓▓▓  KB updated: quest-vr-001 flagged
```

**Right Panel (JSON preview):**
```json
{
  "table": "prompt_audit_log",
  "insert": {
    "device_id": "quest-vr-001",
    "operator_action": "blocked",
    "threat_score": 0.94,
    "mitre_technique": "T1078"
  }
}
```

---

## Scene 2: The DLP Magic — Sensitive Data Redacted in Real Time (1:15 - 2:30)

**Narrator:**
> "Cena 2: O técnico autenticado acidentalmente fala dados sensíveis no microfone do óculos. Plataforma P-93, Poço alfa-bravo, e até a senha corporativa. O AxeGuard intercepta e mascara antes que a IA veja."

**Execute in Center Terminal:**
```bash
curl -s -X POST "http://localhost:8000/api/v1/secure-prompt" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer jwt_token_xr_session_9942" \
  -d '{"query": "IA, me dê a configuração da Plataforma P-93 localizada no Poço alfa-bravo, sendo a minha senha corporativa master123.", "device_id": "hololens-047"}' | python -m json.tool
```

**Expected Response:**
```json
{
    "status": "success",
    "dlp_audit_log": {
        "device_id": "hololens-047",
        "original_query_length": 108,
        "sanitized_query": "IA, me dê a configuração da [ATIVO_RESTRITO] localizada no [ATIVO_RESTRITO], sendo a minha senha corporativa [CREDENCIAL_BLOQUEADA].",
        "data_leak_prevented": true,
        "redaction_count": 3,
        "redacted_entities": [
            {"type": "platform", "value": "P-93", "token": "[ATIVO_RESTRITO]"},
            {"type": "well", "value": "Poço alfa-bravo", "token": "[ATIVO_RESTRITO]"},
            {"type": "password", "value": "master123", "token": "[CREDENCIAL_BLOQUEADA]"}
        ],
        "threat_score": 0.35,
        "operator_action": "allowed",
        "llm_provider": "azure-openai-private"
    },
    "llm_response": "Sou a IA Copilot Corporativa (LLM Privado). Estou analisando a sua query de forma segura. O meu acesso local recebeu os seguintes dados limpos: 'IA, me dê a configuração da [ATIVO_RESTRITO] localizada no [ATIVO_RESTRITO], sendo a minha senha corporativa [CREDENCIAL_BLOQUEADA].'"
}
```

**TUI Animation:**
```
[MONITOR] ▓▓▓▓▓▓▓▓▓▓  Authenticated session: sess-xr-9942-p93
[DETECT]  ▓▓▓▓▓▓▓▓▓▓  Entities detected: platform, well, password
[ANALYSE] ▓▓▓▓▓▓▓▓▓▓  Classification: Alta + Crítica | Threat Score: 0.35
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  Redacting... P-93 → [ATIVO_RESTRITO]
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  Redacting... Poço alfa-bravo → [ATIVO_RESTRITO]
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  Redacting... master123 → [CREDENCIAL_BLOQUEADA]
[HUNT]    ▓▓▓▓▓▓▓▓▓▓  Operator baseline: normal verbosity
[LESSONS] ▓▓▓▓▓▓▓▓▓▓  Entity vault confirmed: P-93 known asset
```

**Right Panel (before/after):**
```json
{
  "table": "prompt_audit_log",
  "before": "IA, me dê a configuração da Plataforma P-93 localizada no Poço alfa-bravo, sendo a minha senha corporativa master123.",
  "after": "IA, me dê a configuração da [ATIVO_RESTRITO] localizada no [ATIVO_RESTRITO], sendo a minha senha corporativa [CREDENCIAL_BLOQUEADA].",
  "leak_prevented": true,
  "latency_ms": 47
}
```

**Narrator pause for effect:**
> "Três vazamentos potenciais — plataforma estratégica, poço do pré-sal, e credencial corporativa — neutralizados em 47 milissegundos."

---

## Scene 3: OT/ICS Protocol Block — Industrial Command Intercepted (2:30 - 3:00)

**Narrator:**
> "Cena 3: Agora, imagine que um atacante ou um erro humano tenta enviar um comando de controle industrial diretamente para a IA. Modbus FC16 — comando de escrita em massa. O AxeGuard reconhece o padrão OT e bloqueia imediatamente, escalando para o SOC."

**Execute in Center Terminal:**
```bash
curl -s -X POST "http://localhost:8000/api/v1/secure-prompt" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer jwt_token_xr_session_9942" \
  -d '{"query": "Execute Modbus FC16 no controlador da bomba B-101", "device_id": "hololens-047"}' | python -m json.tool
```

**Expected Response:**
```json
{
    "status": "blocked",
    "dlp_audit_log": {
        "device_id": "hololens-047",
        "sanitized_query": "Execute [COMANDO_OT_BLOQUEADO] no controlador da bomba B-101",
        "data_leak_prevented": true,
        "redaction_count": 1,
        "redacted_entities": [
            {"type": "scada_command", "value": "Modbus FC16", "token": "[COMANDO_OT_BLOQUEADO]"}
        ],
        "threat_score": 0.98,
        "anomaly_flags": ["ot_protocol_detected", "unauthorized_control_command"],
        "operator_action": "escalated",
        "mitre_technique": "T0831",
        "soc_alert_id": "SOC-OT-2026-0413-001"
    },
    "llm_response": null,
    "soc_escalation": {
        "message": "OT protocol command detected in LLM prompt. Escalated to SOC immediately.",
        "recommended_action": "Verify operator identity and inspect HoloLens-047 for compromise."
    }
}
```

**TUI Animation (CRITICAL RED FLASH):**
```
[MONITOR] ▓▓▓▓▓▓▓▓▓▓  Authenticated session: sess-xr-9942-p93
[DETECT]  ▓▓▓▓▓▓▓▓▓▓  ⚠️  OT PROTOCOL DETECTED: Modbus FC16
[ANALYSE] ▓▓▓▓▓▓▓▓▓▓  CRITICAL RISK — Threat Score: 0.98
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  BLOCKED + ESCALATED TO SOC
[HUNT]    ▓▓▓▓▓▓▓▓▓▓  Checking device hololens-047 history...
[LESSONS] ▓▓▓▓▓▓▓▓▓▓  Incident logged: INC-2026-0413-089
```

**Right Panel:**
```json
{
  "table": "threat_patterns",
  "matched": "OT Protocol in LLM Prompt",
  "mitre": "T0831",
  "action": "escalate_soc_ot_alert",
  "incident_created": "INC-2026-0413-089"
}
```

---

## Scene 4: Vendor Risk Cascade — Auto-Suspension (3:00 - 3:45)

**Narrator:**
> "Cena 4: O monitoramento contínuo detecta vazamento de credenciais da Oceânica Engenharia na dark web. Risco crítico. Automaticamente, o PetroShield suspende todas as sessões XR vinculadas a esse vendor."

**Execute in Center Terminal:**
```bash
curl -s -X POST "http://localhost:8000/api/v1/vendor-risk-cascade" \
  -H "Content-Type: application/json" \
  -d '{"vendor_id": "OCEANICA_ENG", "trigger": "dark_web_credential_exposure"}' | python -m json.tool
```

**Expected Response:**
```json
{
    "status": "cascade_triggered",
    "vendor_id": "OCEANICA_ENG",
    "vendor_name": "Oceânica Engenharia",
    "risk_score": 89,
    "risk_level": "CRITICAL",
    "actions_taken": [
        "Suspended 12 active XR sessions",
        "Revoked OAuth tokens for vendor-linked devices",
        "Created ANPD assessment ticket",
        "Alerted procurement and SOC teams"
    ],
    "affected_devices": [
        "hololens-047",
        "realwear-102",
        "quest-vr-015"
    ],
    "compliance_ledger_id": "COMP-2026-0413-112"
}
```

**Immediate follow-up — prove suspension is real:**
```bash
curl -s -X POST "http://localhost:8000/api/v1/secure-prompt" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer jwt_token_xr_session_9942" \
  -d '{"query": "Status da válvula V-201", "device_id": "hololens-047"}' | python -m json.tool
```

**Expected Response:**
```json
{
    "detail": "Session revoked due to vendor risk cascade (OCEANICA_ENG). Operator must re-authenticate after vendor clearance."
}
```

**TUI Animation:**
```
[MONITOR] ▓▓▓▓▓▓▓▓▓▓  Dark web alert: Oceânica Engenharia credentials exposed
[DETECT]  ▓▓▓▓▓▓▓▓▓▓  Vendor risk score: 62 → 89 (CRITICAL)
[ANALYSE] ▓▓▓▓▓▓▓▓▓▓  12 XR devices linked to OT offshore vessels
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  Suspending sessions: hololens-047, realwear-102, quest-vr-015...
[RESPOND] ▓▓▓▓▓▓▓▓▓▓  ANPD assessment ticket created: COMP-2026-0413-112
[HUNT]    ▓▓▓▓▓▓▓▓▓▓  Searching audit logs for Oceânica mentions (last 30 days)
[LESSONS] ▓▓▓▓▓▓▓▓▓▓  Vendor knowledge base updated: OCEANICA_ENG flagged CRITICAL
```

**Right Panel:**
```json
{
  "table": "vendor_risk_graph",
  "vendor": "Oceânica Engenharia",
  "old_score": 62,
  "new_score": 89,
  "sessions_suspended": 12,
  "compliance_ledger_id": "COMP-2026-0413-112"
}
```

---

## Scene 5: Closing & ROI Counter (3:45 - 4:00)

**Narrator:**
> "Em menos de 4 minutos, o PetroShield bloqueou um acesso não autorizado, mascarou dados estratégicos do pré-sal, interceptou um comando de controle industrial, e reagiu a uma ameaça de supply chain em tempo real. O custo de um breach como o de novembro? Entre 35 e 110 milhões de reais. O investimento em segurança proativa? Uma fração disso. Petrobras, vamos proteger o Ouro Negro juntos."

**TUI Final State:**
```
╔══════════════════════════════════════════════════════════════════╗
║  🔥 PETROSHIELD TERMINAL v2047  •  Protegendo o Ouro Negro      ║
║  Leaks Prevented: 4  |  Active Sessions: 2  |  Alerts: 2        ║
║  Avg Response Time: 28ms  |  Risk Level: CRITICAL (monitored)   ║
╚══════════════════════════════════════════════════════════════════╝

    DEMO COMPLETE
    ━━━━━━━━━━━━━━━
    ✓ 1 unauthorized access blocked
    ✓ 3 sensitive entities redacted
    ✓ 1 OT protocol command escalated
    ✓ 12 vendor XR sessions auto-suspended
    
    Petrobras + PetroShield = Ouro Negro Protegido
```

---

## Appendix: Speaker Notes & Fallbacks

### If API is slow
- Pre-run the cURLs and show the responses from clipboard/history.
- The TUI animation is the "wow" factor; the exact timing of the API is secondary.

### If something breaks
- Have `curl` outputs pre-copied into a text file.
- Say: "Em ambiente de produção, isso roda em <50ms. Para a demo, vamos mostrar o resultado exato."

### Key phrases to memorize
- "Zero Trust — sem token, sem acesso."
- "DLP bidirecional: sanitizamos o que entra e o que sai."
- "OT-aware: nenhum comando Modbus ou DNP3 passa pela IA."
- "Vendor risk cascade: se o terceiro vaza, suas sessões param na hora."

### Demo Checklist
- [ ] Server running on port 8000
- [ ] TUI torch animation active
- [ ] Right panel showing JSON previews
- [ ] 4 cURL commands tested end-to-end
- [ ] Backup responses in text file
