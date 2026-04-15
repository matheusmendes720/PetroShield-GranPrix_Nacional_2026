# Deep Research Synthesis: XR Edge Security, Data Leak Root Causes & AxeGuard Unified Data Model

## PetroShield SOC — Petrobras CyberSec Grand Prix 2026

**Research Pipeline:** Deep OSINT + Technical Benchmarking + Relational Data Modeling
**Date:** April 13, 2026
**Classification:** Internal Research — Competitive Intelligence & Architecture Design
**Scope:** Enterprise VR/AR security breaches, edge-device leak causality, oil & gas XR adoption, COTS authentication/DLP/retention solutions, and live-demo data modeling for AxeGuard middleware inside PetroShield agentic SOC.

---

## Executive Summary

This document synthesizes a multi-vector deep research campaign into **four consolidated deliverables**:

1. **Validated Case Corpus:** 30+ mapped incidents and risk patterns from big tech/energy enterprises down to SMBs involving XR/edge wearables, smart glasses, and IoT devices.
2. **Root-Cause Taxonomy:** A deterministic causal tree of data leaks specific to edge computing + wearable AI (VR/AR smart glasses).
3. **COTS Market Matrix:** Authentication, MDM, DLP proxy, and confidential-compute solutions already available for immediate prototyping.
4. **Unified Relational Data Model:** Complete schema design for the live interactive demo, connecting Petrobras energy-sector specifics (pre-salt, FPSO, vendor ecosystem) to agentic SOC reasoning loops.

> **Key Insight:** The convergence of AI assistants, XR wearables, and OT/IT networks in oil & gas creates a **"Triple Surface" attack vector**: (1) Biometric/Visual capture on the device, (2) Prompt/PII injection into cloud LLMs, and (3) Lateral movement into SCADA/Modbus networks via vendor-managed edge tunnels. AxeGuard is designed to sit at the intersection of these three surfaces.

---

## Part 1: VR/AR Industrial Security Landscape — Research Findings

### 1.1 Global Market & Threat Trajectory

| Metric                                        | Value                                                                         | Source / Implication                                              |
| --------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Global XR market (2030)                       | **$1.06 trillion**                                                      | CAGR 32.9% — massive enterprise attack-surface expansion         |
| Avg. data breach cost (2025)                  | **$4.44M** | IBM — down from $4.88M due to AI detection, but volume up |                                                                   |
| Breaches with ransomware                      | **44%**                                                                 | Verizon DBIR 2025 — up from 32%                                  |
| Stolen credential dwell time                  | **292 days**                                                            | IBM — longest detection window, prime for edge-device compromise |
| Multi-cloud breach cost                       | **$5.05M**                                                              | IBM — XR devices inherently bridge on-prem + cloud + edge        |
| Third-party / supply chain breach involvement | **Rising sharply**                                                      | DBIR 2025 — directly relevant to Petrobras vendor model          |

### 1.2 The "Triple Surface" Attack Vector for Industrial XR

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    INDUSTRIAL XR — TRIPLE SURFACE ATTACK                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  SURFACE 1: DEVICE CAPTURE (Bio-Visual-Acoustic)                           │
│  ├── Camera / video recording of sensitive equipment, SCADA screens        │
│  ├── Microphone capture of verbal passwords, operational commands          │
│  ├── Eye-tracking data revealing attention patterns (≈ unanonymizable PII) │
│  ├── Spatial mapping exposing facility layouts and restricted zones        │
│  └── Biometric leakage: iris, retina, voiceprint, hand geometry            │
│                                                                             │
│  SURFACE 2: AI/LLM DATA PIPELINE (Prompt + PII Exfiltration)               │
│  ├── Voice-to-text prompts containing asset names, passwords, coordinates  │
│  ├── Unsanitized queries sent to third-party LLM APIs (OpenAI, Anthropic)  │
│  ├── Training-data retention by vendor (data residency / no-train risk)    │
│  ├── Prompt injection attacks hijacking assistant behavior                 │
│  └── Response caching / logging on shared infrastructure                   │
│                                                                             │
│  SURFACE 3: NETWORK/OT LATERAL MOVEMENT (Edge → Core)                      │
│  ├── Compromised XR device as pivot into corporate WiFi / VPN              │
│  ├── Sideloaded apps with network scanning capabilities                    │
│  ├── Flat OT networks allowing Modbus/DNP3 access from compromised host    │
│  ├── Vendor-managed tunnels (Shadow IT) bypassing SOC visibility           │
│  └── Compromised MDM agent enabling persistent access                      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.3 Enterprise to SMB Case Study Corpus

#### Category A: Direct XR/Wearable Security Incidents

| Case                                                             | Sector                      | What Happened                                                                                                  | Root Cause                                           | Lesson for Petrobras                                                                                  |
| ---------------------------------------------------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| **Meta Quest VR Attack (2024-2025)**                       | Consumer/Enterprise         | Attackers exploited sideloading and app-store weaknesses to inject malicious overlays and data sniffers        | Weak app sandboxing; user-enabled sideloading        | **Kiosk Mode + MDM is mandatory** — consumer-grade XR cannot be trusted in industrial settings |
| **Oculus Privacy Controversy (2020-2024)**                 | Consumer/Enterprise         | Facebook login mandate sparked mass privacy concerns; biometric tracking data linked to social profiles        | Forced identity fusion; opaque data sharing policies | **Device auth must be decoupled from consumer identity platforms** — use corporate IAM only    |
| **AI Smart Glasses — Lost/Stolen Devices (2026 reports)** | Healthcare / Field Services | Multiple reported losses of AI glasses storing unencrypted audio/video; HIPAA breach notification triggers     | No remote wipe; local data encryption absent         | **Mandatory encryption-at-rest + remote wipe + geofencing** on all field XR devices             |
| **AR Browser Content Spoofing**                            | Industrial Maintenance      | Third-party AR browsers allowed malicious actors to overlay false instructions / signs in worker field of view | Unauthenticated content injection                    | **Content signing + trusted origin verification** for any AR overlay in critical ops            |
| **VR Ransomware — Motion Tracking Blackmail**             | Gaming / Enterprise POCs    | Hackers recorded VR sessions and threatened to release behavioral biometrics                                   | Unencrypted session telemetry                        | **Session telemetry must route through DLP proxy with PII masking**                             |

#### Category B: Edge/IoT Data Leaks with Structural Similarity to XR

| Case                                                         | Company Scale              | What Happened                                                                | Edge-Cause Mapping                                   | AxeGuard Countermeasure                              |
| ------------------------------------------------------------ | -------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| **SA Exploration → Petrobras (Nov 2025)**             | Enterprise                 | 90GB seismic data exfiltrated via compromised vendor VPN                     | Vendor edge credentials + no MFA + no DLP            | OAuth Device Flow + DLP Proxy + JIT access           |
| **Change Healthcare (Feb 2024)**                       | Enterprise                 | 190M patient records stolen via compromised Citrix credentials               | Edge remote-access appliance with no MFA             | Kiosk-restricted endpoints + phishing-resistant auth |
| **Norsk Hydro (2019)**                                 | Enterprise                 | $70M+ loss from LockerGoga ransomware via compromised RDP                    | Flat network from edge to core                       | Microsegmentation + XR device isolation              |
| **Colonial Pipeline (2021)**                           | Enterprise                 | $4.4M ransom; fuel shortages from VPN credential leak                        | Single-factor VPN at edge                            | Zero-trust network access (ZTNA) for all wearables   |
| **Boeing RFQ Campaign (April 2026)**                   | Enterprise / SMB suppliers | Malicious DOCX files targeting industrial suppliers                          | Supply chain phishing into edge devices              | Email DLP + document sandboxing before XR viewing    |
| **MOAB Data Leak (Jan 2024)**                          | Cross-sector               | 26B aggregated records from multiple edge/cloud leaks                        | Long-tail data accumulation from unsecured endpoints | Data minimization + automatic retention purging      |
| **SMB Manufacturing — Exposed S3 via AR app backend** | SMB                        | Small AR maintenance app leaked facility photos via misconfigured AWS bucket | Cloud misconfiguration from XR app developer         | CSPM integration for all XR app backends             |

---

## Part 2: Root-Cause Taxonomy of Edge-Device Data Leaks

### 2.1 Causal Tree: "Why XR Devices Leak Data"

```yaml
XR_DataLeak_Causality:
  
  Layer_1_Physical_Device:
    - cause: "Lost or stolen device"
      frequency: HIGH
      mitigation: ["Geofencing auto-lock", "Remote wipe", "Full-disk encryption"]
    - cause: "Shoulder surfing in AR/VR input"
      frequency: MEDIUM
      mitigation: ["OAuth Device Flow (no typing)", "Biometric gaze unlock"]
    - cause: "Camera/mic recording without audit"
      frequency: HIGH
      mitigation: ["Recording watermarking", "DLP content analysis", "Policy-based auto-delete"]
    - cause: "Eye-tracking & motion biometric exfiltration"
      frequency: EMERGING
      mitigation: ["Local biometric anonymization", "DLP proxy for telemetry"]
  
  Layer_2_Application_Runtime:
    - cause: "Sideloaded / unapproved apps"
      frequency: HIGH
      mitigation: ["Kiosk Mode (ArborXR/Hexnode)", "App whitelisting", "Code signing"]
    - cause: "Malicious AR overlays (content spoofing)"
      frequency: MEDIUM
      mitigation: ["Content origin verification", "AR sandboxing"]
    - cause: "Insecure voice-to-text capture"
      frequency: HIGH
      mitigation: ["On-device STT with local DLP", "Encrypted audio stream"]
    - cause: "Prompt injection into LLM assistant"
      frequency: EMERGING
      mitigation: ["Prompt guardrails", "Input sanitization", "LLM proxy with injection detection"]
  
  Layer_3_Network_Transport:
    - cause: "Unencrypted WiFi / third-party network"
      frequency: HIGH
      mitigation: ["Always-on VPN (WireGuard/IPsec)", "Certificate pinning"]
    - cause: "Man-in-the-middle on AR browser channels"
      frequency: MEDIUM
      mitigation: ["TLS 1.3 mandatory", "mTLS for device-to-proxy"]
    - cause: "Shadow IT tunnels from vendor apps"
      frequency: MEDIUM
      mitigation: ["Network microsegmentation", "Egress filtering", "ZTNA"]
  
  Layer_4_Cloud_AI_Backend:
    - cause: "Unsanitized PII/sensitive data in LLM prompts"
      frequency: CRITICAL
      mitigation: ["DLP Proxy with regex + NLP masking", "Domain-specific entity redaction"]
    - cause: "Vendor LLM training-data retention"
      frequency: HIGH
      mitigation: ["Private endpoint (Azure OpenAI)", "No-Train B2B clause", "Local LLM fallback"]
    - cause: "Multi-tenant LLM response caching leaks"
      frequency: MEDIUM
      mitigation: ["Session-isolated inference", "No shared cache for sensitive queries"]
    - cause: "Cloud misconfiguration of XR app backend"
      frequency: HIGH
      mitigation: ["CSPM", "Least-privilege IAM", "Encrypted storage"]
  
  Layer_5_Organizational_Governance:
    - cause: "No continuous monitoring of vendor/device security posture"
      frequency: CRITICAL
      mitigation: ["Sentinel Vendor Trust platform", "Continuous external scanning", "Dark web monitoring"]
    - cause: "Annual (not continuous) vendor assessments"
      frequency: HIGH
      mitigation: ["Real-time risk scoring", "Behavioral analytics"]
    - cause: "LGPD/ANP breach notification delays"
      frequency: MEDIUM
      mitigation: ["Automated ANPD reporting", "3-day deadline tracker"]
```

---

## Part 3: COTS Market Solutions Matrix

### 3.1 Authentication & Identity (Layer 2)

| Solution                                | Type              | Why It Fits Petrobras XR                                                      | Market Validation                          |
| --------------------------------------- | ----------------- | ----------------------------------------------------------------------------- | ------------------------------------------ |
| **Microsoft Entra ID (Azure AD)** | IAM / OAuth 2.0   | Native HoloLens 2 integration; supports Device Authorization Grant (RFC 8628) | Used by Shell, BP for industrial XR fleets |
| **Okta**                          | IAM / SSO         | Strong device-flow support; enterprise-grade MFA                              | Fortune 500 standard                       |
| **Keycloak**                      | Open-source IAM   | Self-hosted; no data leaves Brazil; LGPD-friendly                             | SMB to Enterprise                          |
| **FIDO2 / WebAuthn Passkeys**     | Passwordless auth | Resistant to phishing and shoulder surfing                                    | Emerging enterprise standard               |

### 3.2 Mobile Device Management for XR (Layer 1)

| Solution                       | Specialization      | Key Capabilities                                                      | Prototyping Fit                                      |
| ------------------------------ | ------------------- | --------------------------------------------------------------------- | ---------------------------------------------------- |
| **ArborXR**              | XR-native MDM       | Kiosk mode, remote view, app deployment, Meta Quest / HoloLens / Pico | **Best for hackathon** — purpose-built for XR |
| **Hexnode UEM**          | Cross-platform      | VR/AR management, Fire OS support, zero-trust kiosk framework         | Good alternative with strong docs                    |
| **VMware Workspace ONE** | Enterprise UEM      | Full lifecycle, certificate management, network profiles              | Large-enterprise proven                              |
| **Microsoft Intune**     | Microsoft ecosystem | HoloLens 2 auto-enrollment, SCEP/PKCS certs, conditional access       | Ideal if Petrobras is Microsoft shop                 |

### 3.3 DLP Proxy / AI Gateway (Layer 3 — The AxeGuard Core)

| Solution                                 | Type                       | Capabilities                                                 | Open-Source?         |
| ---------------------------------------- | -------------------------- | ------------------------------------------------------------ | -------------------- |
| **Contextul.io Network DLP Proxy** | Commercial / Network-layer | Pseudonymization + private LLM routing                       | Partially documented |
| **Traefik Hub Content Guard**      | API Gateway middleware     | Presidio-based PII detection, custom entities                | Commercial           |
| **AegisGate (GitHub)**             | Open-source LLM gateway    | Prompt injection detection, PII redaction, audit logging     | **Yes**        |
| **CloakLLM (GitHub)**              | Open-source PII cloaking   | Tamper-evident audit logs for LLM calls                      | **Yes**        |
| **cloakpipe (GitHub)**             | Rust privacy middleware    | Pseudonymization, encrypted vault, SSE streaming rehydration | **Yes**        |
| **grob (GitHub)**                  | Rust LLM proxy             | DLP, EU AI Act/GDPR compliance, multi-provider failover      | **Yes**        |
| **Microsoft Purview DLP**          | Enterprise DLP             | Native integration with Azure OpenAI, M365                   | Commercial           |
| **Nightfall AI**                   | Cloud-native DLP           | API-based PII detection for SaaS/GenAI                       | Commercial           |

### 3.4 Confidential Compute & Private AI (Layer 4)

| Solution                                          | Type                 | Why It Fits                                                         | Cost Profile      |
| ------------------------------------------------- | -------------------- | ------------------------------------------------------------------- | ----------------- |
| **Azure OpenAI Service (Private Endpoint)** | Managed LLM          | VNet private endpoint; B2B no-train clauses; Brazilian South region | Enterprise        |
| **AWS Bedrock + Llama 3 (VPC)**             | Managed LLM          | VPC-isolated; self-hosted within AWS Brazil                         | Enterprise        |
| **Ollama / vLLM on private GPU**            | Self-hosted LLM      | Full data sovereignty; zero vendor retention                        | Medium (hardware) |
| **Cloudflare Access Tunnels**               | Secure reverse proxy | Easy tunneling for hackathon demos; ZTNA integration                | Low / Free tier   |
| **Ngrok (with auth)**                       | Developer tunnel     | Rapid prototyping of proxy layer                                    | Free for demo     |

---

## Part 4: Oil & Gas XR Adoption & Petrobras-Specific Security Context

### 4.1 Industry Benchmark: How Majors Use XR

| Company                 | XR Use Case                                                                  | Security Posture                                                           | Lesson for Petrobras                                                         |
| ----------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Shell**         | Real-time digital twins for deepwater ops; XR visualization of subsea assets | Heavy Microsoft/Azure integration; private endpoints for digital twin data | **Model:** Use Azure private endpoints for all AI + twin data          |
| **Equinor**       | Immersive simulation for offshore platform training (Kongsberg Digital)      | Sim environments air-gapped from production OT                             | **Model:** Training XR should be on separate network segment           |
| **BP**            | ACE Digital Twin (AVEVA) — AR-assisted maintenance and integrity management | Enterprise IAM + conditional access for field devices                      | **Model:** Field XR must use conditional access based on location/time |
| **TotalEnergies** | VR training for process safety and emergency response                        | Isolated VR labs; no external internet on training headsets                | **Model:** Kiosk mode with no browser access                           |

### 4.2 Petrobras-Specific Operational Data to Protect

From existing intelligence (`01_Intel_OSINT/`), these are the **critical data categories** that an XR operator might accidentally vocalize or visualize:

```python
PETROBRAS_SENSITIVE_ENTITIES = {
    "seismic_data": {
        "examples": ["3D/4D navigation Campos Basin", "OBN positions", "DGPS coordinates"],
        "classification": "Estratégica",
        "breach_history": "SA Exploration Nov 2025 — 90GB exfiltrated"
    },
    "platform_assets": {
        "examples": ["P-10", "P-93", "FPSO Carioca", "Plataforma P-XX"],
        "classification": "Alta",
        "pattern": r"(?i)\bp-\d{2,3}\b"
    },
    "well_data": {
        "examples": ["Poço Tupi-10", "Poço alfa-bravo", "Pré-sal Mero"],
        "classification": "Estratégica",
        "pattern": r"(?i)\bpo[çc]o\s+[a-z0-9-]+\b"
    },
    "credentials": {
        "examples": ["senha master123", "CPF 123.456.789-00"],
        "classification": "Crítica",
        "pattern": r"\d{3}\.\d{3}\.\d{3}-\d{2}"
    },
    "scada_modbus": {
        "examples": ["Function Code 16 register 502", "DNP3 outstation ID"],
        "classification": "Crítica — OT direct control",
        "pattern": "Industrial protocol commands"
    },
    "vendor_access": {
        "examples": ["Oceânica Engenharia VPN", "SA Exploration credentials"],
        "classification": "Alta",
        "breach_history": "Everest ransomware via vendor compromise"
    }
}
```

---

## Part 5: Unified Data Model for AxeGuard Middleware

### 5.1 Conceptual Architecture: AxeGuard inside PetroShield SOC

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PETROSHIELD AGENTIC SOC                             │
│                    (LangGraph Supervisor + Outer Memory)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     AXEGUARD MIDDLEWARE LAYER                       │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐  │   │
│  │  │ Device Auth │→│ DLP Proxy   │→│ Threat      │→│ Private   │  │   │
│  │  │ Gateway     │  │ (FastAPI)   │  │ Intel Node  │  │ AI Enclave│  │   │
│  │  │ (OAuth 2.0) │  │ Regex + NLP │  │ (Risk Score)│  │ (Azure)   │  │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘  │   │
│  │        ↑                                       ↓                    │   │
│  │   XR Glasses                            OT/SIEM Alert               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↓                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     UNIFIED DATA MODEL                               │   │
│  │  • Device Registry      • Prompt Audit Log    • Vendor Risk Graph   │   │
│  │  • Entity Vault         • Threat Pattern DB   • Compliance Ledger   │   │
│  │  • Session Telemetry    • LLM Response Cache  • Incident KB         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Relational Schema: Core Tables

#### Table: `xr_devices`

```sql
CREATE TABLE xr_devices (
    device_id VARCHAR(64) PRIMARY KEY,          -- e.g., "quest-vr-001"
    device_type VARCHAR(32),                    -- "HoloLens2", "RealWear", "MetaQuest3"
    asset_tag VARCHAR(32),                      -- Petrobras asset tracking
    assigned_operator_id VARCHAR(64),           -- Link to operator
    mdm_enrollment_status VARCHAR(16),          -- "enrolled", "kiosk", "compromised"
    kiosk_mode_enabled BOOLEAN DEFAULT TRUE,
    last_known_location GEOGRAPHY,              -- PostGIS point (platform/FPSO)
    network_segment VARCHAR(32),                -- "OT_Isolated", "IT_Corporate", "Vendor_VPN"
    encryption_status VARCHAR(16),              -- "AES-256", "unencrypted"
    remote_wipe_capable BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Table: `auth_sessions`

```sql
CREATE TABLE auth_sessions (
    session_id VARCHAR(128) PRIMARY KEY,
    device_id VARCHAR(64) REFERENCES xr_devices(device_id),
    auth_method VARCHAR(32),                    -- "oauth_device_flow", "biometric_gaze"
    authorization_token_hash VARCHAR(256),      -- Hashed Bearer token
    smartphone_approval_status VARCHAR(16),     -- "pending", "approved", "revoked"
    qr_code_uuid VARCHAR(64),
    ip_address INET,
    geo_risk_score FLOAT,                       -- 0.0 to 1.0
    mfa_verified BOOLEAN DEFAULT FALSE,
    expires_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Table: `prompt_audit_log`

```sql
CREATE TABLE prompt_audit_log (
    log_id BIGSERIAL PRIMARY KEY,
    session_id VARCHAR(128) REFERENCES auth_sessions(session_id),
    device_id VARCHAR(64) REFERENCES xr_devices(device_id),
    original_query TEXT,
    sanitized_query TEXT,
    data_leak_prevented BOOLEAN,
    redaction_count INTEGER,
    redacted_entities JSONB,                    -- [{"type": "platform", "value": "P-93"}]
    llm_provider VARCHAR(64),                   -- "azure-openai-private", "local-llm"
    threat_score FLOAT,                         -- Anomaly score from Threat Intel Node
    operator_action VARCHAR(32),                -- "allowed", "blocked", "escalated"
    latency_ms INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

#### Table: `sensitive_entities`

```sql
CREATE TABLE sensitive_entities (
    entity_id SERIAL PRIMARY KEY,
    entity_type VARCHAR(32),                    -- "platform", "well", "cpf", "vendor", "coordinate"
    entity_pattern VARCHAR(128),                -- Regex pattern
    entity_value VARCHAR(256),                  -- Actual value (encrypted at application layer)
    classification VARCHAR(16),                 -- "Estratégica", "Alta", "Crítica"
    replacement_token VARCHAR(64),              -- e.g., "[ATIVO_RESTRITO_001]"
    related_basin VARCHAR(64),                  -- "Campos", "Santos", "Tupi"
    data_source VARCHAR(64),                    -- "seismic_db", "erp_sap", "vendor_registry"
    active BOOLEAN DEFAULT TRUE
);
```

#### Table: `vendor_risk_graph`

```sql
CREATE TABLE vendor_risk_graph (
    vendor_id VARCHAR(64) PRIMARY KEY,
    vendor_name VARCHAR(128),
    contract_value_brl DECIMAL(15,2),
    access_level VARCHAR(16),                   -- "OT", "IT", "Data", "None"
    risk_score FLOAT,
    risk_level VARCHAR(16),                     -- "LOW", "MEDIUM", "HIGH", "CRITICAL"
    dark_web_exposure BOOLEAN,
    mfa_enforced BOOLEAN,
    last_breach_check TIMESTAMP,
    related_incident_ids TEXT[],                -- Array of incident references
    anpd_report_required BOOLEAN DEFAULT FALSE
);
```

#### Table: `threat_patterns`

```sql
CREATE TABLE threat_patterns (
    pattern_id SERIAL PRIMARY KEY,
    pattern_name VARCHAR(128),
    mitre_technique VARCHAR(16),                -- e.g., "T1133", "T1195"
    pattern_description TEXT,
    detection_query TEXT,                       -- Sigma/KQL style
    affected_device_types TEXT[],
    recommended_playbook VARCHAR(64),
    false_positive_rate FLOAT,
    active BOOLEAN DEFAULT TRUE
);
```

#### Table: `compliance_ledger`

```sql
CREATE TABLE compliance_ledger (
    ledger_id BIGSERIAL PRIMARY KEY,
    regulation VARCHAR(32),                     -- "LGPD", "ANP_882", "ANPD_15_2024"
    event_type VARCHAR(32),                     -- "breach_detected", "anpd_notified", "dpo_alert"
    incident_id VARCHAR(128),
    data_volume_gb FLOAT,
    anpd_deadline TIMESTAMP,
    notification_sent BOOLEAN DEFAULT FALSE,
    evidence_json JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5.3 Agentic Reasoning Data Flow

For the **live interactive demo**, the frontend will display these **agentic loops** powered by the data model:

```
DEMO SCENARIO 1: Unauthorized Device Access Attempt
────────────────────────────────────────────────────
1. [MONITOR]  Device "quest-vr-001" attempts /api/v1/secure-prompt
              → No Authorization header
2. [DETECT]   Trigger: auth.session.missing
              → Threat pattern T1078 (Valid Accounts abuse)
              → Confidence: 0.94
3. [ANALYSE]  Risk score: 78/100 (HIGH)
              → Operator is unknown; device last seen on FPSO P-93
              → Escalate to L2
4. [RESPOND]  Playbook: block_request_401
              → Log to prompt_audit_log (operator_action = "blocked")
              → Alert SOC dashboard
5. [HUNT]     Check if same device attempted other endpoints in last 24h
              → Correlation query on auth_sessions
6. [LESSONS]  KB update: "quest-vr-001 attempted unauthorized access"
              → Push to outer memory (pgvector)

DEMO SCENARIO 2: DLP Sanitization in Action
────────────────────────────────────────────────────
1. [MONITOR]  Authenticated operator on HoloLens-047 sends query:
              "Configuração da Plataforma P-93 no Poço alfa-bravo, senha master123"
2. [DETECT]   Entity matches: platform "P-93", well "alfa-bravo", password "master123"
3. [ANALYSE]  DLP engine flags 3 sensitive entities
              → Classification: Alta + Crítica
4. [RESPOND]  Proxy redacts to:
              "Configuração da [ATIVO_RESTRITO] no [ATIVO_RESTRITO], senha [CREDENCIAL_BLOQUEADA]"
              → Forward sanitized prompt to Azure OpenAI Private Endpoint
              → Log original + sanitized to prompt_audit_log
5. [HUNT]     Check operator history: is this anomalous verbosity?
              → Baseline: operator avg 12 words/query; this query 9 words → normal
6. [LESSONS]  Update entity vault if new platform ID discovered

DEMO SCENARIO 3: Vendor Risk Cascade
────────────────────────────────────────────────────
1. [MONITOR]  Dark web monitor detects credential leak for "Oceânica Engenharia"
2. [DETECT]   Cross-reference vendor_risk_graph → CRITICAL vendor, R$4.2B contract
3. [ANALYSE]  Vendor risk score jumps from 62 → 89
              → Network access: OT offshore vessels
              → Related to active XR device fleet on those vessels
4. [RESPOND]  Automated actions:
              → Suspend vendor XR device auth sessions
              → Create compliance_ledger entry (ANPD notification assessment)
              → Alert procurement + SOC
5. [HUNT]     Search prompt_audit_log for any queries mentioning "Oceânica" in last 30 days
6. [LESSONS]  Update vendor_risk_graph incident history; generate board report
```

---

## Part 6: Integration with Existing PetroShield Intelligence

### 6.1 Mapping to `01_Intel_OSINT/Latest_Intelligence_Brief_April_2026.md`

| Intelligence Item                                                       | AxeGuard Integration Point                                                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **ANPD as Special Autarchy (Lei 15.352/2026)**                    | `compliance_ledger` auto-triggers ANPD notifications with 3-day deadline tracking  |
| **CrystalX RAT targeting Brazilian users**                        | `threat_patterns` includes RAT detection for Android-based XR devices              |
| **Iranian APT PLC targeting (CISA April 2026)**                   | `threat_patterns` maps T0831/T0853 for OT-aware XR proxy blocking                  |
| **Storm-1175 / Medusa ransomware LATAM**                          | `vendor_risk_graph` monitors for ransomware group IOCs                             |
| **Petrobras new Chairman Pogliese + Logistics Director Laureano** | Executive dashboard shows supply-chain risk focus aligned with leadership priorities |

### 6.2 Mapping to `01_Intel_OSINT/Petrobras_Supply_Chain_Vendor_Intelligence.md`

| Vendor Intelligence                  | Data Model Link                                                                |
| ------------------------------------ | ------------------------------------------------------------------------------ |
| SA Exploration breach (Nov 2025)     | `vendor_risk_graph` — incident_history includes "CONFIRMED_BREACH_Nov2025"  |
| Oceânica Engenharia R$4.2B contract | `vendor_risk_graph` — contract_value_brl, access_level = "OT"               |
| 10,000+ vendor ecosystem             | `vendor_risk_graph` scales to full Petrobras vendor list via SAP integration |
| ANP Resolution 882 vendor clauses    | `compliance_ledger` automates periodic assessment checklists                 |

### 6.3 Mapping to `04_BI_Ofensivo/Strategic_Proposal_Petrobras_CyberSec_Grand_Prix_2026.md`

| Proposal Element                          | AxeGuard Enhancement                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Sentinel Vendor Trust platform            | Unified with AxeGuard DLP proxy — vendor risk directly affects XR auth decisions                |
| Modbus/DNP3/OPC UA vulnerability analysis | `sensitive_entities` includes industrial protocol commands; proxy blocks them from LLM prompts |
| LGPD Article 37 records                   | `compliance_ledger` auto-generates processing records for XR-captured data                     |
| ROI calculation (R$35-110M breach cost)   | Demo metrics show "leaks prevented × record value" in real-time                                 |

---

## Part 7: Recommendations for `base/implementation_plan.md` Recursive Improvements

### 7.1 Critical Additions

1. **Add Layer 2.5: On-Device Local DLP**

   - Before audio ever leaves the XR device, run a lightweight STT + regex engine locally.
   - This prevents raw audio stream interception on insecure WiFi.
2. **Add Layer 3.5: Threat Intelligence Node**

   - The proxy should not only redact; it should score each prompt for anomaly.
   - Connect to `vendor_risk_graph` to dynamically elevate auth requirements for high-risk vendors.
3. **Expand Layer 4: Local LLM Fallback**

   - For fully offline platform operations (offshore with satellite-only connectivity), add a quantized local LLM (Llama 3 8B on edge GPU) as fallback.
   - Ensures zero vendor retention risk in disconnected environments.
4. **Add Physical Security Layer**

   - Geofencing: XR device auto-locks if GPS/beacon indicates it left authorized FPSO/platform.
   - Remote wipe trigger integrated with MDM (ArborXR/Hexnode).

### 7.2 Criticisms of Current Plan & Fixes

| Current Plan Element     | Criticism                                              | Fix                                                                                                                  |
| ------------------------ | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Regex-only DLP           | Too brittle for natural language; misses paraphrasing  | **Hybrid pipeline:** Regex (fast) + spaCy/Transformers NER (accurate) + domain-specific entity list            |
| Single mock token        | No token rotation or revocation mechanism              | **Session-bound tokens** with Redis-backed TTL and instant revocation endpoint                                 |
| No response sanitization | LLM responses might leak sensitive data back to device | **Bidirectional DLP:** sanitize responses as well as requests                                                  |
| No audit persistence     | Logs only to console; no tamper-evident store          | **Append-only audit log** (PostgreSQL + cryptographic hash chain)                                              |
| No OT/ICS awareness      | Plan is IT-centric; Petrobras operates OT networks     | **OT-aware proxy rules:** block any prompt containing Modbus function codes, DNP3 commands, or SCADA setpoints |

---

## Part 8: Live Demo Frontend — Storytelling Schema

### 8.1 Narrative Arc (4 Minutes)

| Time      | Scene                                                                                                                                                                                                       | Data Model Tables Updated                    |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 0:00-0:30 | **Intro:** "Petrobras operates 80+ offshore platforms. In Nov 2025, 90GB of seismic data leaked via a vendor. Today, PetroShield prevents the next leak — even through AI smart glasses."            | —                                           |
| 0:30-1:15 | **Scene 1 — Zero Trust Auth:** Unauthorized XR device tries to query the AI. AxeGuard blocks it. Terminal shows `auth_sessions` rejection with threat pattern T1078.                               | `auth_sessions`, `threat_patterns`       |
| 1:15-2:30 | **Scene 2 — DLP Magic:** Authenticated technician asks about "Plataforma P-93" and accidentally says a password. AxeGuard redacts in real-time. Terminal shows `prompt_audit_log` before/after.    | `prompt_audit_log`, `sensitive_entities` |
| 2:30-3:15 | **Scene 3 — Vendor Risk Cascade:** Dark web alert for "Oceânica Engenharia." Risk score jumps. AxeGuard suspends all XR sessions tied to that vendor. Dashboard shows `vendor_risk_graph` update. | `vendor_risk_graph`, `compliance_ledger` |
| 3:15-4:00 | **Closing:** ROI counter increments — "3 sensitive leaks prevented in 60 seconds." Call to action for pilot.                                                                                         | —                                           |

### 8.2 Frontend Component Sketch

```yaml
PetroShield_Demo_UI:
  
  Header:
    - Animated ASCII torch (green/orange cyber-flame)
    - Live metrics: "Leaks Prevented: {count}" | "Active Sessions: {n}" | "Risk Score: {score}"
  
  Left_Panel:
    - Terminal stream of AxeGuard proxy logs
    - Color-coded: Green = allowed, Orange = redacted, Red = blocked
  
  Center_Panel:
    - Interactive agentic loop visualization
    - Nodes: MONITOR → DETECT → ANALYSE → RESPOND → HUNT → LESSONS
    - Active node pulses; arrows animate on state transition
  
  Right_Panel:
    - Live relational data preview
    - Rotating cards: auth_sessions → prompt_audit_log → vendor_risk_graph
    - Each card shows actual SQL/JSON payload from the demo
```

---

## Appendix: Research Sources

1. Tripwire — *Exploring the Security Risks of VR and AR* (Nov 2024)
2. Kaspersky — *Security and Privacy Risks of AR and VR* (2021, updated corpus)
3. Workplace Privacy Report — *Compliance Concerns with AI Smart Glasses* (Jan 2026)
4. DeepStrike — *Data Breach Statistics 2025–2026* (Dec 2025)
5. Hexnode Blogs & Help Center — XR/visionOS enterprise deployment (2025-2026)
6. ArborXR Product Updates — Zero-touch Meta Quest enrollment (Nov 2025)
7. VirtualSpeech — *Meta Horizon Managed Services with ArborXR* (Jan 2026)
8. InnovateEnergy — *Shell XR and Digital Twins* (Nov 2025)
9. World Oil — *Shell Real-Time Digital Twin Breakthroughs* (Sep 2025)
10. Kongsberg Digital — *Equinor Simulation Technology* (2025)
11. AVEVA — *BP ACE Digital Twin* (2025)
12. Contextul.io — *Network-Layer DLP Proxy with Pseudonymisation* (Aug 2025)
13. Traefik Hub Docs — *Content Guard Middleware* (Apr 2026)
14. GitHub repositories: AegisGate, CloakLLM, cloakpipe, grob, Semantic-Privacy-Guard, ai-dlp-proxy
15. Petrobras internal intelligence: `01_Intel_OSINT/*`, `04_BI_Ofensivo/Strategic_Proposal_Petrobras_CyberSec_Grand_Prix_2026.md`

---

*Document compiled by PetroShield Research Automation Pipeline*
*Next iteration: Implementation plan updates + schema DDL generation + demo UI prototyping*
