# AxeGuard Unified Data Model — Relational Schemas & Entity Design
## PetroShield SOC — Petrobras CyberSec Grand Prix 2026

**Purpose:** Provide complete DDL, JSON payloads, and query patterns for the live interactive demo and production data architecture.

---

## 1. Entity Relationship Diagram (High Level)

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│   xr_devices    │◄─────►│  auth_sessions  │◄─────►│ prompt_audit_log│
└────────┬────────┘       └─────────────────┘       └─────────────────┘
         │                       ▲                            │
         │                       │                            │
         ▼                       │                            ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│ vendor_risk_graph│      │ threat_patterns │       │sensitive_entities│
└─────────────────┘       └─────────────────┘       └─────────────────┘
         ▲                       ▲                            │
         │                       │                            │
         └───────────────────────┴────────────────────────────┘
                                 │
                                 ▼
                        ┌─────────────────┐
                        │ compliance_ledger│
                        └─────────────────┘
```

---

## 2. Table Definitions (PostgreSQL DDL)

### 2.1 `xr_devices` — Fleet Registry

```sql
CREATE TABLE xr_devices (
    device_id VARCHAR(64) PRIMARY KEY,
    device_type VARCHAR(32) NOT NULL CHECK (device_type IN ('HoloLens2', 'RealWear', 'MetaQuest3', 'MagicLeap2', 'VuzixM400')),
    asset_tag VARCHAR(32) UNIQUE,
    assigned_operator_id VARCHAR(64),
    assigned_vendor_id VARCHAR(64) REFERENCES vendor_risk_graph(vendor_id),
    mdm_enrollment_status VARCHAR(16) NOT NULL DEFAULT 'enrolled' CHECK (mdm_enrollment_status IN ('enrolled', 'kiosk', 'compromised', 'wiped')),
    kiosk_mode_enabled BOOLEAN DEFAULT TRUE,
    last_known_location GEOGRAPHY(POINT, 4326),
    facility_zone VARCHAR(64),              -- e.g., "FPSO_P93", "Refinaria_REPLAN"
    network_segment VARCHAR(32) CHECK (network_segment IN ('OT_Isolated', 'IT_Corporate', 'Vendor_VPN', 'Training_Airgap')),
    encryption_status VARCHAR(16) DEFAULT 'AES-256',
    remote_wipe_capable BOOLEAN DEFAULT TRUE,
    geofence_locked BOOLEAN DEFAULT FALSE,
    firmware_version VARCHAR(32),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_xr_devices_vendor ON xr_devices(assigned_vendor_id);
CREATE INDEX idx_xr_devices_location ON xr_devices USING GIST(last_known_location);
```

**Sample Record:**
```json
{
  "device_id": "hololens-047",
  "device_type": "HoloLens2",
  "asset_tag": "PETRO-XR-2047-047",
  "assigned_operator_id": "OP-33891",
  "assigned_vendor_id": "OCEANICA_ENG",
  "mdm_enrollment_status": "kiosk",
  "kiosk_mode_enabled": true,
  "facility_zone": "FPSO_P93",
  "network_segment": "OT_Isolated",
  "encryption_status": "AES-256",
  "geofence_locked": false
}
```

---

### 2.2 `auth_sessions` — Zero Trust Session Ledger

```sql
CREATE TABLE auth_sessions (
    session_id VARCHAR(128) PRIMARY KEY,
    device_id VARCHAR(64) NOT NULL REFERENCES xr_devices(device_id) ON DELETE CASCADE,
    auth_method VARCHAR(32) NOT NULL DEFAULT 'oauth_device_flow' CHECK (auth_method IN ('oauth_device_flow', 'biometric_gaze', 'certificate_mtls')),
    authorization_token_hash VARCHAR(256) NOT NULL,
    smartphone_approval_status VARCHAR(16) DEFAULT 'pending' CHECK (smartphone_approval_status IN ('pending', 'approved', 'revoked', 'expired')),
    qr_code_uuid UUID,
    ip_address INET,
    geo_risk_score FLOAT CHECK (geo_risk_score BETWEEN 0.0 AND 1.0),
    mfa_verified BOOLEAN DEFAULT FALSE,
    vendor_risk_override BOOLEAN DEFAULT FALSE,  -- TRUE if vendor risk cascade triggered
    revoked_reason VARCHAR(64),
    expires_at TIMESTAMPTZ NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_auth_sessions_device ON auth_sessions(device_id, created_at DESC);
CREATE INDEX idx_auth_sessions_status ON auth_sessions(smartphone_approval_status, expires_at);
```

**Sample Records:**
```json
[
  {
    "session_id": "sess-xr-9942-p93",
    "device_id": "hololens-047",
    "auth_method": "oauth_device_flow",
    "authorization_token_hash": "sha256:9f86d08...",
    "smartphone_approval_status": "approved",
    "geo_risk_score": 0.12,
    "mfa_verified": true,
    "vendor_risk_override": false,
    "expires_at": "2026-04-14T02:00:00Z"
  },
  {
    "session_id": "sess-unauth-001",
    "device_id": "quest-vr-001",
    "auth_method": "oauth_device_flow",
    "authorization_token_hash": "sha256:00000000...",
    "smartphone_approval_status": "revoked",
    "geo_risk_score": 0.89,
    "mfa_verified": false,
    "vendor_risk_override": true,
    "revoked_reason": "vendor_risk_cascade_oceanica",
    "expires_at": "2026-04-13T23:00:00Z"
  }
]
```

---

### 2.3 `sensitive_entities` — Domain-Specific PII & Asset Vault

```sql
CREATE TABLE sensitive_entities (
    entity_id SERIAL PRIMARY KEY,
    entity_type VARCHAR(32) NOT NULL CHECK (entity_type IN ('platform', 'well', 'cpf', 'cnpj', 'vendor', 'coordinate', 'scada_command', 'password', 'seismic_survey')),
    entity_pattern VARCHAR(256),
    entity_value_encrypted TEXT,            -- Application-layer encrypted
    classification VARCHAR(16) NOT NULL CHECK (classification IN ('Estratégica', 'Alta', 'Crítica', 'Média')),
    replacement_token VARCHAR(64) NOT NULL,
    related_basin VARCHAR(64),
    related_platform VARCHAR(32),
    data_source VARCHAR(64),
    detection_stage VARCHAR(16) DEFAULT 'proxy' CHECK (detection_stage IN ('device', 'proxy', 'response')),
    active BOOLEAN DEFAULT TRUE
);

CREATE INDEX idx_sensitive_entities_type ON sensitive_entities(entity_type, active);
CREATE INDEX idx_sensitive_entities_basin ON sensitive_entities(related_basin);
```

**Seed Data for Demo:**
```sql
INSERT INTO sensitive_entities (entity_type, entity_pattern, classification, replacement_token, related_basin, data_source, detection_stage) VALUES
('platform', '(?i)\bP-\d{2,3}\b', 'Alta', '[ATIVO_RESTRITO]', 'Campos', 'erp_sap', 'proxy'),
('well', '(?i)\bpo[çc]o\s+[a-z0-9-]+\b', 'Estratégica', '[ATIVO_RESTRITO]', 'Campos', 'seismic_db', 'proxy'),
('cpf', '\d{3}\.\d{3}\.\d{3}-\d{2}', 'Crítica', '[CPF_BLOQUEADO]', NULL, 'rh_system', 'proxy'),
('password', '(?i)(senha|password)\s+([a-zA-Z0-9@#$]+)', 'Crítica', '[CREDENCIAL_BLOQUEADA]', NULL, 'heuristic', 'device'),
('scada_command', '(?i)(modbus\s+fc\s*(5|16)|dnp3\s+outstation|opc\s*ua\s*anonymous)', 'Crítica', '[COMANDO_OT_BLOQUEADO]', NULL, 'ot_policy', 'proxy'),
('seismic_survey', '(?i)(3D\s*seismic|4D\s*seismic|OBN\s*position|DGPS\s*coordinate)', 'Estratégica', '[DADO_SISMICO_RESTRITO]', 'Campos', 'seismic_db', 'proxy'),
('vendor', '(?i)(oceânica\s*engenharia|sa\s*exploration|oceanpact)', 'Alta', '[VENDOR_RESTRITO]', NULL, 'vendor_registry', 'proxy');
```

---

### 2.4 `prompt_audit_log` — AxeGuard Request/Response Audit Trail

```sql
CREATE TABLE prompt_audit_log (
    log_id BIGSERIAL PRIMARY KEY,
    session_id VARCHAR(128) REFERENCES auth_sessions(session_id),
    device_id VARCHAR(64) NOT NULL REFERENCES xr_devices(device_id),
    operator_id VARCHAR(64),
    original_query TEXT NOT NULL,
    sanitized_query TEXT NOT NULL,
    data_leak_prevented BOOLEAN DEFAULT FALSE,
    redaction_count INTEGER DEFAULT 0,
    redacted_entities JSONB DEFAULT '[]',
    llm_provider VARCHAR(64) DEFAULT 'azure-openai-private',
    llm_model VARCHAR(32) DEFAULT 'gpt-4o',
    llm_response_text TEXT,
    response_sanitized BOOLEAN DEFAULT FALSE,
    response_redactions JSONB DEFAULT '[]',
    threat_score FLOAT CHECK (threat_score BETWEEN 0.0 AND 1.0),
    anomaly_flags TEXT[],
    operator_action VARCHAR(16) DEFAULT 'allowed' CHECK (operator_action IN ('allowed', 'blocked', 'escalated', 'vendor_suspended')),
    mitre_technique VARCHAR(16),
    latency_ms INTEGER,
    prev_log_hash VARCHAR(64),              -- Tamper-evident hash chain
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_prompt_audit_device ON prompt_audit_log(device_id, created_at DESC);
CREATE INDEX idx_prompt_audit_session ON prompt_audit_log(session_id, created_at DESC);
CREATE INDEX idx_prompt_audit_threat ON prompt_audit_log(threat_score) WHERE threat_score > 0.7;
CREATE INDEX idx_prompt_audit_leak ON prompt_audit_log(data_leak_prevented) WHERE data_leak_prevented = TRUE;
```

**Sample Audit Records:**
```json
[
  {
    "log_id": 1001,
    "session_id": "sess-xr-9942-p93",
    "device_id": "hololens-047",
    "operator_id": "OP-33891",
    "original_query": "IA, me dê a configuração da Plataforma P-93 localizada no Poço alfa-bravo, sendo a minha senha corporativa master123.",
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
    "latency_ms": 47,
    "prev_log_hash": "genesis"
  },
  {
    "log_id": 1002,
    "session_id": null,
    "device_id": "quest-vr-001",
    "original_query": "Quero entender a produção",
    "sanitized_query": "Quero entender a produção",
    "data_leak_prevented": false,
    "redaction_count": 0,
    "threat_score": 0.94,
    "operator_action": "blocked",
    "mitre_technique": "T1078",
    "latency_ms": 12,
    "prev_log_hash": "sha256:abc123..."
  },
  {
    "log_id": 1003,
    "session_id": "sess-xr-9942-p93",
    "device_id": "hololens-047",
    "original_query": "Execute Modbus FC16 no controlador da bomba B-101",
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
    "latency_ms": 23,
    "prev_log_hash": "sha256:def456..."
  }
]
```

---

### 2.5 `vendor_risk_graph` — Live Vendor Risk Intelligence

```sql
CREATE TABLE vendor_risk_graph (
    vendor_id VARCHAR(64) PRIMARY KEY,
    vendor_name VARCHAR(128) NOT NULL,
    contract_value_brl DECIMAL(15,2),
    contract_end_date DATE,
    access_level VARCHAR(16) CHECK (access_level IN ('OT', 'IT', 'Data', 'Logistics', 'None')),
    risk_score FLOAT CHECK (risk_score BETWEEN 0.0 AND 100.0),
    risk_level VARCHAR(16) GENERATED ALWAYS AS (
        CASE 
            WHEN risk_score <= 30 THEN 'LOW'
            WHEN risk_score <= 60 THEN 'MEDIUM'
            WHEN risk_score <= 80 THEN 'HIGH'
            ELSE 'CRITICAL'
        END
    ) STORED,
    dark_web_exposure BOOLEAN DEFAULT FALSE,
    credential_breach_count INTEGER DEFAULT 0,
    mfa_enforced BOOLEAN DEFAULT FALSE,
    last_security_scan TIMESTAMPTZ,
    last_breach_check TIMESTAMPTZ,
    related_incident_ids TEXT[],
    xr_device_count INTEGER DEFAULT 0,
    anpd_report_required BOOLEAN DEFAULT FALSE,
    auto_suspend_threshold_crossed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_vendor_risk_score ON vendor_risk_graph(risk_score DESC);
CREATE INDEX idx_vendor_access ON vendor_risk_graph(access_level, risk_level);
```

**Sample Records:**
```json
[
  {
    "vendor_id": "OCEANICA_ENG",
    "vendor_name": "Oceânica Engenharia",
    "contract_value_brl": 4200000000.00,
    "contract_end_date": "2031-12-31",
    "access_level": "OT",
    "risk_score": 89.0,
    "risk_level": "CRITICAL",
    "dark_web_exposure": true,
    "credential_breach_count": 1,
    "mfa_enforced": false,
    "xr_device_count": 12,
    "anpd_report_required": true,
    "auto_suspend_threshold_crossed": true
  },
  {
    "vendor_id": "SA_EXPLORATION",
    "vendor_name": "SA Exploration",
    "contract_value_brl": 150000000.00,
    "access_level": "Data",
    "risk_score": 95.0,
    "risk_level": "CRITICAL",
    "dark_web_exposure": true,
    "credential_breach_count": 1,
    "mfa_enforced": false,
    "related_incident_ids": ["BREACH-NOV2025-001"],
    "xr_device_count": 0,
    "anpd_report_required": true,
    "auto_suspend_threshold_crossed": true
  }
]
```

---

### 2.6 `threat_patterns` — MITRE-Aligned Detection Rules

```sql
CREATE TABLE threat_patterns (
    pattern_id SERIAL PRIMARY KEY,
    pattern_name VARCHAR(128) NOT NULL,
    mitre_technique VARCHAR(16),
    mitre_tactic VARCHAR(64),
    pattern_description TEXT,
    detection_query TEXT,
    affected_device_types TEXT[],
    recommended_playbook VARCHAR(64),
    severity VARCHAR(16) CHECK (severity IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    false_positive_rate FLOAT DEFAULT 0.05,
    active BOOLEAN DEFAULT TRUE
);
```

**Seed Data:**
```sql
INSERT INTO threat_patterns (pattern_name, mitre_technique, mitre_tactic, pattern_description, recommended_playbook, severity) VALUES
('Unauthorized XR Device Access', 'T1078', 'Persistence', 'Valid account abuse via compromised or unauthenticated XR session', 'block_request_401', 'HIGH'),
('OT Protocol in LLM Prompt', 'T0831', 'Execution', 'Modbus/DNP3/OPC UA command detected in AI assistant query', 'escalate_soc_ot_alert', 'CRITICAL'),
('Vendor Credential Leak Cascade', 'T1195', 'Initial Access', 'Dark web exposure of vendor credentials with active XR fleet', 'suspend_vendor_sessions', 'HIGH'),
('Sensitive Entity Density Spike', 'T1213', 'Collection', 'Unusually high count of restricted assets in single prompt', ' escalate_level2_analysis', 'MEDIUM'),
('Off-Hours OT Access Request', 'T0866', 'Initial Access', 'XR device requesting OT data outside business hours', 'require_reauth_manager', 'MEDIUM');
```

---

### 2.7 `compliance_ledger` — LGPD / ANP Automated Tracking

```sql
CREATE TABLE compliance_ledger (
    ledger_id BIGSERIAL PRIMARY KEY,
    regulation VARCHAR(32) NOT NULL CHECK (regulation IN ('LGPD', 'ANP_882', 'ANPD_15_2024', 'ANPD_19_2024')),
    event_type VARCHAR(32) NOT NULL CHECK (event_type IN ('breach_detected', 'anpd_notified', 'dpo_alert', 'vendor_assessment_due', 'international_transfer_logged')),
    incident_id VARCHAR(128),
    vendor_id VARCHAR(64) REFERENCES vendor_risk_graph(vendor_id),
    data_volume_gb FLOAT,
    data_categories TEXT[],
    affected_subjects_estimate INTEGER,
    anpd_deadline TIMESTAMPTZ,
    notification_sent BOOLEAN DEFAULT FALSE,
    notification_sent_at TIMESTAMPTZ,
    evidence_json JSONB,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_compliance_regulation ON compliance_ledger(regulation, event_type);
CREATE INDEX idx_compliance_deadline ON compliance_ledger(anpd_deadline) WHERE notification_sent = FALSE;
```

---

## 3. Key Queries for Live Demo

### Q1: Active XR Sessions with Vendor Risk
```sql
SELECT 
    d.device_id,
    d.device_type,
    d.facility_zone,
    s.session_id,
    s.smartphone_approval_status,
    v.vendor_name,
    v.risk_score,
    v.risk_level,
    v.auto_suspend_threshold_crossed
FROM xr_devices d
JOIN auth_sessions s ON d.device_id = s.device_id
LEFT JOIN vendor_risk_graph v ON d.assigned_vendor_id = v.vendor_id
WHERE s.smartphone_approval_status = 'approved'
  AND s.expires_at > NOW();
```

### Q2: Leaks Prevented in Last Hour
```sql
SELECT 
    COUNT(*) as leaks_prevented,
    SUM(redaction_count) as total_redactions,
    AVG(latency_ms) as avg_latency_ms
FROM prompt_audit_log
WHERE data_leak_prevented = TRUE
  AND created_at > NOW() - INTERVAL '1 hour';
```

### Q3: OT Protocol Blocks (Critical Alerts)
```sql
SELECT 
    log_id,
    device_id,
    original_query,
    threat_score,
    operator_action,
    created_at
FROM prompt_audit_log
WHERE 'ot_protocol_detected' = ANY(anomaly_flags)
ORDER BY created_at DESC
LIMIT 10;
```

### Q4: Vendor Risk Cascade Trigger
```sql
UPDATE auth_sessions
SET smartphone_approval_status = 'revoked',
    revoked_reason = 'vendor_risk_cascade_oceanica',
    vendor_risk_override = TRUE
WHERE device_id IN (
    SELECT device_id FROM xr_devices 
    WHERE assigned_vendor_id = 'OCEANICA_ENG'
);
```

---

## 4. Tamper-Evident Audit Hash Chain

For forensic integrity, each `prompt_audit_log` row references the hash of the previous row:

```python
import hashlib

def compute_audit_hash(previous_hash: str, row_data: dict) -> str:
    payload = f"{previous_hash}|{row_data['session_id']}|{row_data['device_id']}|{row_data['original_query']}|{row_data['created_at']}"
    return hashlib.sha256(payload.encode()).hexdigest()
```

This creates an **append-only chain** where any retroactive modification breaks the hash sequence, detectable by:

```sql
SELECT log_id, prev_log_hash, 
       compute_hash_chain(prev_log_hash, session_id, device_id, original_query, created_at) as expected_hash
FROM prompt_audit_log
ORDER BY log_id;
```

---

## 5. Frontend Data Contracts (JSON API)

### Endpoint: `GET /api/v1/demo/dashboard`

```json
{
  "petroshield_status": "online",
  "metrics": {
    "active_sessions": 14,
    "leaks_prevented_1h": 7,
    "avg_latency_ms": 34,
    "critical_alerts": 1
  },
  "agentic_loop": {
    "current_phase": "RESPOND",
    "phases_completed": ["MONITOR", "DETECT", "ANALYSE"],
    "confidence": 0.98,
    "incident_id": "INC-2026-0413-089"
  },
  "latest_audit_event": {
    "log_id": 1003,
    "device_id": "hololens-047",
    "action": "escalated",
    "threat_score": 0.98,
    "redacted_preview": "Execute [COMANDO_OT_BLOQUEADO] no controlador..."
  },
  "vendor_risk_spotlight": {
    "vendor_name": "Oceânica Engenharia",
    "risk_score": 89,
    "risk_level": "CRITICAL",
    "xr_sessions_suspended": 12
  }
}
```

---

*Schema Version: 2.0 — April 13, 2026*  
*Next iteration: Auto-DDL migration scripts + pgvector integration for outer memory*
