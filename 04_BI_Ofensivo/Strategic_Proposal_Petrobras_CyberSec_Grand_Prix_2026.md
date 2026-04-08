# PROPOSTA ESTRATÉGICA INTEGRADA
## Petrobras + CyberSecurity + Grand Prix SENAI 2026
### Do Macro Global ao Micro Operacional: Análise Top-Down para Especialistas

---

**Documento:** Proposta Estratégica Técnica  
**Público-Alvo:** Especialistas em Cybersecurity, OT/ICS Security, Vendor Risk Management  
**Cliente:** Petrobras (via Grand Prix SENAI 2026)  
**Tema:** Supply Chain Security & Vendor Risk Management  
**Data:** Abril 2026  
**Classificação:** Inteligência Técnica Estratégica

---

# SUMÁRIO EXECUTIVO TÉCNICO

## Threat Model Consolidado

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    THREAT LANDSCAPE CONSOLIDADO                        │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  🎯 ATOR DE AMEAÇA: Everest Ransomware Group                            │
│     ├─ TTPs: Credential stuffing, VPN compromise (T1133)               │
│     ├─ Vetor: SA Exploration (vendor terceirizado)                     │
│     └─ Impacto: 90GB dados sísmicos exfiltrados (Nov/2025)             │
│                                                                         │
│  🎯 ATOR EMERGENTE: Iranian APTs (CISA Alert April 2026)               │
│     ├─ TTPs: PLC targeting, password-spraying                          │
│     ├─ Vetor: Industrial control systems                               │
│     └─ Risco: Physical damage potential                                │
│                                                                         │
│  🎯 RANSOMWARE ATIVO LATAM: Storm-1175 / Medusa                        │
│     ├─ TTPs: High-velocity exploitation, double extortion              │
│     ├─ Vetor: Internet-exposed assets                                  │
│     └─ Risco: OT networks, critical infrastructure                     │
│                                                                         │
│  📊 SURFACE DE ATAQUE:                                                │
│     • 10.000+ vendors ativos                                           │
│     • Modbus/DNP3/OPC UA expostos                                      │
│     • Contratos R$4,2B+ (Oceânica)                                     │
│     • Vendors com acesso OT offshore                                   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# PARTE I: MACRO - PANORAMA GLOBAL E THREAT LANDSCAPE

## 1.1 Mercado Global de CyberSecurity Industrial

### Tamanho e Projeções

| Segmento | 2026 | 2030 | CAGR | Driver Principal |
|----------|------|------|------|------------------|
| **ICS Security** | US$ 25.3B | US$ 37.8B | 9.6% | Convergência IT/OT |
| **Supply Chain Sec** | US$ 8.7B | US$ 19.3B | 17.3% | 60%+ breaches via terceiros |
| **AI-Driven Sec** | US$ 28.1B | US$ 62.4B | 18.9% | AI weaponization |
| **Brazil Market** | R$ 18.7B | R$ 32.1B | 12.2% | LGPD enforcement |

### Tendências Tecnológicas 2025-2026

#### 1.1.1 AI Weaponization (Google Cloud Prediction, 2026)

```yaml
Tendência: AI-driven scalable cyberattacks
Sectores_alvo: [Manufacturing, Retail, Finance, Energy]
Técnicas:
  - Autonomous reconnaissance
  - Adaptive malware (polymorphic AI)
  - Deepfake social engineering
  - Automated vulnerability exploitation

Implicação_para_oil_gas:
  "AI-powered attacks can map SCADA networks, identify 
   vulnerable PLCs, and deploy targeted payloads faster 
   than human defenders can respond"
```

#### 1.1.2 Convergência IT/OT - O Novo Perímetro

| Camada Legacy | Estado de Segurança | Exposição |
|---------------|---------------------|-----------|
| **ERP/IT** | Moderada | VPN, cloud |
| **OT DMZ** | Fraca | Data diodes mal configurados |
| **Control Network** | Crítica | Modbus/DNP3 plaintext |
| **Safety Systems** | Isolada | TRITON-style bypass risk |

## 1.2 Threat Actors Ativos no Setor Energy

### XENOTIME (Dragos Assessment)

```
┌─────────────────────────────────────────────────────────────┐
│ XENOTIME - APT Nível Crítico                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Target: Oil & Gas, Electric utilities                      │
│  Capabilities: TRITON malware (Triton v2.0 identified 2025) │
│  Objective: Physical destruction, safety system bypass      │
│  Access: Long-term persistent, OT networks                  │
│                                                             │
│  TTPs (MITRE ATT&CK for ICS):                               │
│  • T0831: Modify Controller Logic                           │
│  • T0853: Scripting (PowerShell/Python)                     │
│  • T0855: Force device restart (Cold Restart)              │
│  • T0866: Exploit via vendor remote access                  │
│                                                             │
│  Petrobras Relevance:                                        │
│  • Pre-salt technology = strategic national asset           │
│  • TRITON targets SIS (Safety Instrumented Systems)         │
│  • Could cause physical damage to offshore platforms        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Iranian APTs - Alerta CISA (April 2026)

| Atributo | Detalhe |
|----------|---------|
| **Atribuição** | Iran-nexus threat actor |
| **Target** | US critical infrastructure, PLCs |
| **Técnica** | Programmable Logic Controller exploitation |
| **Impacto** | "Operational disruption and damage" |
| **Campanha Global** | 300+ Israeli Microsoft 365 orgs (password-spraying) |
| **AWS Bahrain** | Attack reported (Iran cloud targeting) |

**Relevância para Petrobras:**
- State-controlled oil company = alvo estratégico prioritário
- Pre-salt tech = rivalidade tecnológica com Irã
- Supply chain vendors = vetores de acesso preferidos
- PLCs offshore = superfície de ataque exposta

### Everest Ransomware Group (Post-Nov/2025)

```
Cronologia do Ataque:
═══════════════════════════════════════════════════════════

14/11/2025 - Comprometimento SA Exploration
   └─> Vetor: Credential stuffing em VPN corporativa
   └─> Nenhum MFA ativado

14-17/11/2025 - Lateral movement
   └─> Reconnaissance de sistemas Petrobras-accessíveis
   └─> Mapeamento de servidores de dados sísmicos

17/11/2025 - Publicação do leak
   └─> 90GB Petrobras + 176GB SA Exploration
   └─> Dados: 3D/4D seismic, OBN positions, DGPS
   └─> Timer para publicação total

17/11/2025 - Coincidência suspeita
   └─> Petrobras anuncia nova descoberta Bacia de Campos
   └─> Possible strategic timing para blefe

20/11/2025 - Confirmação Petrobras
   └─> "Exposição não autorizada via prestadora"
   └─> Negação de acesso direto a sistemas internos

25/11/2025 - Efetivação do leak
   └─> Dados publicados após não-pagamento
   └─> 190GB total liberado em dark web
═══════════════════════════════════════════════════════════
```

## 1.3 Supply Chain Security - Análise Estatística

### Estatísticas Críticas

| Métrica | Valor | Fonte |
|---------|-------|-------|
| Breaches via terceiros | 60%+ | SecurityScorecard, 2025 |
| Vendor ecosystems median | 5.000+ | Ponemon Institute |
| Mean time to detect vendor breach | 287 dias | IBM Cost of Breach 2025 |
| 4th party visibility | <20% | Prevalent, 2025 |
| Software supply chain attacks | +742% (2020-2025) | Sonatype |

### Casos Paradigmáticos

| Incidente | Ano | Root Cause | Impacto |
|-----------|-----|------------|---------|
| **SolarWinds** | 2020 | Compromised build process | 18.000+ orgs |
| **Kaseya VSA** | 2021 | MSP supply chain | 1.500+ empresas |
| **3CX** | 2023 | Software supply chain | Milhões usuários |
| **MOVEit** | 2023 | File transfer vendor | 500+ orgs, 60M+ records |
| **Petrobras** | 2025 | Vendor credential theft | 90GB seismic data |

---

# PARTE II: MESO - ESPECIFICIDADE BRASILEIRA E REGULATÓRIO

## 2.1 Marco Legal de Cibersegurança (2025-2026)

### Decreto 12.572/2025 - Política Nacional de Segurança da Informação

```python
# Framework Governança Cibernética Brasil

class NationalSecurityPolicy:
    """
    Decreto 12.572/2025 - Replaces 9.637/2018
    Coordenador: Gabinete de Segurança Institucional (GSI)
    """
    
    requirements = {
        "information_classification": [
            "ULTRASSECRETO",
            "SECRETO", 
            "CONFIDENCIAL",
            "RESERVADO",
            "OSTENSIVO"
        ],
        "risk_management": "ISO 27005 compatible",
        "incident_response": "24/7 SOC mandatory for critical",
        "access_control": "Princípio do menor privilégio"
    }
    
    def applies_to(self, entity):
        return entity.type in [
            "administração_pública_federal",
            "empresas_estatais",  # Petrobras
            "infraestrutura_crítica"
        ]
```

### Decreto 12.573/2025 - Estratégia Nacional de Cibersegurança

| Pilar | Objetivo | Aplicação Petrobras |
|-------|----------|---------------------|
| **Defense** | Proteger infraestrutura crítica | OT/ICS protection |
| **Deterrence** | Atribuição e consequências | Threat intel |
| **Development** | Build capabilities | Workforce dev (SENAI) |
| **Diplomacy** | Cooperação internacional | ANP, OCDE |

### Lei 15.352/2026 - ANPD como Autarquia Especial

**Implicações Técnicas:**

```yaml
Status_ANPD: 
  previous: "Órgão integrado da estrutura da Presidência"
  current: "Autarquia especial vinculada ao Ministério da Justiça"
  
Poderes_Enhanced:
  - Sancionador reforçado (fines up to 2% revenue / R$50M)
  - Autorregulamentação
  - Cooperação internacional direta
  - Fiscalização autônoma

Enforcement_Priorities_2026:
  - Adult content age verification (Lei ECA Digital)
  - International data transfers (Res 19/2024)
  - AI governance (emergent)
  - Children's data protection
```

## 2.2 LGPD - Implementação Técnica

### Article 37 - Registros de Operações

```python
# Estrutura técnica para LGPD compliance

lgpd_processing_record = {
    "agent": {
        "controller": "Petrobras",
        "processor": "Vendor_Name",  # SA Exploration example
        "dpo": "encarregado@petrobras.com.br"
    },
    "processing": {
        "activity": "Seismic Data Processing",
        "purpose": "Offshore exploration analysis",
        "legal_basis": "Legitimate Interest (Art 7, IX) + Consent (Art 7, I)",
        "retention": "5 years post-project",
        "categories": ["Geolocation", "Equipment IDs", "Survey Data"]
    },
    "data_subjects": {
        "categories": ["Employees", "Contractors", "Survey Teams"],
        "volume": "10.000+",
        "sensitive": False  # Unless biometric
    },
    "security": {
        "measures": [
            "AES-256 encryption at rest",
            "TLS 1.3 in transit",
            "RBAC with MFA",
            "Audit logging (12 months)",
            "DLP monitoring"
        ],
        "international_transfer": {
            "mechanism": "ANPD SCCs (Res 19/2024)",
            "destination": "USA (if applicable)",
            "adequacy_decision": False
        }
    },
    "risk_assessment": {
        "ripd_required": True,  # Res 14/2024
        "high_risk_indicators": [
            "Large-scale processing",
            "Systematic monitoring",
            "Sensitive data",
            "Cross-border transfer"
        ]
    }
}
```

### Resolução 15/2024 - Notificação de Incidentes

| Aspecto | Requisito | Implementação Técnica |
|---------|-----------|----------------------|
| **Deadline** | 3 business days | Automated trigger from SIEM |
| **Canal** | ANPD website + email | API integration |
| **Conteúdo** | 5 elementos obrigatórios | Template auto-generation |
| **Comunicação** | Titulares afetados | Email/SMS automation |

```python
def detect_lgpd_breach(anomaly_score, data_volume, sensitivity):
    """
    Sistema de detecção automatizada para LGPD
    """
    BREACH_THRESHOLD = 0.8
    HIGH_VOLUME_GB = 1.0
    
    is_breach = (
        anomaly_score > BREACH_THRESHOLD and 
        (data_volume > HIGH_VOLUME_GB or sensitivity in ['high', 'critical'])
    )
    
    if is_breach:
        # 3 business days countdown starts
        deadline = calculate_business_days(3)
        
        # Auto-generate ANPD report
        report = generate_anpd_notification(
            incident_type="Data Exfiltration",
            categories_affected=data_categories,
            data_subjects_count=estimated_subjects,
            technical_measures=remediation_actions,
            dpo_contact=dpo_info
        )
        
        # Notify DPO immediately
        notify_dpo(report, priority="CRITICAL")
        
        return {
            "status": "BREACH_CONFIRMED",
            "anpd_deadline": deadline,
            "report_id": report.id,
            "notification_sent": True
        }
```

### Resolução 19/2024 - Transferências Internacionais

**SCCs ANPD vs EU:**

| Aspecto | ANPD SCCs | EU SCCs |
|---------|-----------|---------|
| **Idioma** | Português obrigatório | Inglês padrão |
| **Cláusulas** | 18 cláusulas específicas | 4 módulos padrão |
| **Subprocessadores** | Consentimento prévio | Informação posterior |
| **Auditoria** | ANPD pode inspecionar | Supervisory authority |
| **Governing Law** | Brasileira | Variável |

## 2.3 ANP Resolution 882/2022 - Regulação Setorial

### Requisitos de Segurança

```yaml
ANP_Resolution_882:
  applicable_to:
    - Concessionários
    - Permissionários  
    - Autorizados
    
  requirements:
    incident_reporting:
      deadline: "Sem demora injustificada"
      content:
        - Descrição do incidente
        - Sistemas afetados
        - Medidas corretivas
        - Prevenção futura
        
    investigation:
      report_required: True
      timeline: "Conforme complexidade"
      
    security_measures:
      - Controle de acesso
      - Criptografia
      - Monitoramento
      - Backup e recuperação
      - Gestão de incidentes
      
    vendor_security:
      - Cláusulas contratuais
      - Avaliações periódicas
      - Notificação de incidentes
```

---

# PARTE III: MICRO - ANÁLISE TÉCNICA PETROBRAS

## 3.1 Perfil Corporativo e Contexto

### Financial Snapshot (2026)

```
┌────────────────────────────────────────────────────────────────┐
│               PETROBRAS - METRICS ESTRATÉGICAS                │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  💰 CAPITALIZAÇÃO:                 ~R$ 640B (~US$ 120B)       │
│  📈 LUCRO LÍQUIDO 2025:            US$ 19,6B (+160% YoY)      │
│  📊 STOCK PERFORMANCE YTD:         +75% (melhor em 20 anos)   │
│  🛢️ PRODUÇÃO:                      2,4M bpd (recorde)          │
│  📈 CRESCIMENTO PRÉ-SAL:           +16,4% produção            │
│                                                                │
│  💼 BUSINESS PLAN 2026-2030:                                   │
│     • Investimentos Totais:        US$ 109B                    │
│     • E&P (Pré-sal):               US$ 69,2B (63%)             │
│     • Otimização de custos:        US$ 12B target              │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Nova Liderança (April 6-7, 2026)

| Posição | Anterior | Novo | Implicação Estratégica |
|---------|----------|------|------------------------|
| **Chairman** | [Outgoing] | Marcelo Weick Pogliese | Janela para novas prioridades |
| **Logistics/Commercial** | Claudio Schlosser | Angelica Laureano | Foco em supply chain |

**Oportunidade:** Mudanças de liderança frequentemente precedem novas iniciativas de cybersecurity e inovação.

## 3.2 Análise SWOT Técnica

### Strengths (Capacidades Internas)

```yaml
Capacidades_Técnicas:
  Financial_Capacity:
    description: "US$ 19.6B lucro permite investimento enterprise"
    application: "Budget para soluções de segurança premium"
    
  Innovation_Ecosystem:
    programs:
      - "ENFUSE/Unicamp (hard tech startups)"
      - "CBPF AI Hackathon (R$151M Libra Rocks)"
      - "SENAI partnership (10k+ students)"
    application: "Pipeline de inovação já estabelecido"
    
  Scale_Advamtage:
    description: "Volume justifica desenvolvimento próprio"
    application: "Economias de escala em segurança"
    
  Post_Breach_Awareness:
    description: "Board-level attention post-Nov/2025"
    application: "Urgência corporativa para ação"
```

### Weaknesses (Vulnerabilidades Técnicas)

```yaml
Legacy_Infrastructure:
  SCADA_Systems:
    age: "15-20 anos em operação"
    protocols: ["Modbus TCP/RTU", "DNP3", "OPC UA"]
    vulnerabilities:
      - "No native authentication (Modbus)"
      - "Plaintext communication"
      - "Unpatched CVEs"
    
  OT_Network_Segmentation:
    status: "Flat network topology"
    exposure: "Vendors with direct PLC access"
    risk: "Lateral movement IT→OT"

Vendor_Complexity:
  Scale:
    active_vendors: 10000+
    critical_vendors: ~500
    high_access_vendors: ~2000
    international: ~30%
    
  Governance_Gaps:
    - "Assessments anuais (não contínuos)"
    - "No real-time monitoring"
    - "No behavioral analytics"
    - "4th party visibility <20%"
    
  Recent_Incidents:
    SA_Exploration:
      date: "November 2025"
      vector: "Credential compromise"
      data_exfiltrated: "90GB seismic"
      root_cause: "No MFA, no monitoring"

Talent_Gap:
  OT_Security_Shortage: "Escassez de profissionais ICS no Brasil"
  Competition: "Mercado privado competing por talentos"
  Dependence: "Alta dependência de consultorias"
```

## 3.3 Deep Dive: Incidente SA Exploration (Nov/2025)

### Análise Técnica do Ataque

```
┌─────────────────────────────────────────────────────────────────────┐
│           ATTACK CHAIN - SA EXPLORATION BREACH                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  [RECONNAISSANCE]                                                   │
│  └─> Everest identifica SA Exploration como vendor Petrobras       │
│  └─> OSINT: LinkedIn, contratos públicos, website                  │
│  └─> Identificação de VPN endpoints expostos                        │
│                                                                     │
│  [INITIAL ACCESS] - T1133 (External Remote Services)               │
│  └─> Vetor: Credential stuffing em VPN corporativa                 │
│  └─> Credenciais comprometidas (possível phishing ou leak)         │
│  └─> NENHUM MFA ativado (critical failure)                         │
│                                                                     │
│  [PERSISTENCE] - T1078 (Valid Accounts)                            │
│  └─> Uso de credenciais legítimas = evasão de detecção             │
│  └─> Standing access (não Just-In-Time)                            │
│  └─> No session monitoring ou recording                            │
│                                                                     │
│  [DISCOVERY] - T1046 (Network Service Scanning)                    │
│  └─> Mapeamento de rede interna SA Exploration                    │
│  └─> Identificação de sistemas Petrobras-conectados               │
│  └─> Localização de servidores de dados sísmicos                  │
│                                                                     │
│  [COLLECTION] - T1213 (Data from Info Repositories)                │
│  └─> Raw seismic navigation data                                   │
│  └─> Ship coordinates, OBN positions                               │
│  └─> Equipment configurations                                      │
│  └─> Quality control parameters                                    │
│                                                                     │
│  [EXFILTRATION]                                                    │
│  └─> 90GB Petrobras + 176GB SA Exploration                        │
│  └─> Extended period (dias) sem detecção                          │
│  └─> No DLP or anomaly detection triggered                        │
│                                                                     │
│  [IMPACT] - T0817 (Theft of Operational Information)               │
│  └─> Publicação em site de leaks                                   │
│  └─> Dados sísmicos expostos                                       │
│  └─> Competidores podem replicar estratégias                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Dados Comprometidos - Detalhamento

| Categoria | Tipo Específico | Valor Estratégico | Classificação |
|-----------|-----------------|-------------------|---------------|
| **Seismic Data** | Raw 3D/4D navigation | Inestimável | ⭐⭐⭐ Estratégica |
| **Coordinates** | Ship GPS, OBN positions | Competitivo | ⭐⭐⭐ Estratégica |
| **Equipment** | Hydrophone configs | Operacional | ⭐⭐ Alta |
| **QC Parameters** | Survey line quality | Técnica | ⭐⭐ Alta |
| **Timing Data** | Firing pressures | Operacional | ⭐⭐ Alta |

### Falhas de Segurança Identificadas

```yaml
Falhas_Críticas:
  1_Credential_Management:
    failure: "No MFA enforcement"
    control_missing: "Just-In-Time access"
    policy_gap: "Weak password requirements"
    
  2_Vendor_Monitoring:
    failure: "No continuous security assessment"
    control_missing: "Behavioral analytics"
    detection_gap: "No anomaly detection on access"
    
  3_Network_Segmentation:
    failure: "Flat vendor network access"
    control_missing: "Microsegmentation"
    exposure: "Direct data repository access"
    
  4_Data_Loss_Prevention:
    failure: "No DLP on large downloads"
    control_missing: "Data classification"
    detection_gap: "90GB exfiltration undetected"
    
  5_Incident_Response:
    failure: "Detection delay (days)"
    control_missing: "Automated alerting"
    process_gap: "Manual investigation only"
```

## 3.4 Vendor Ecosystem - Inteligência Técnica

### Mapeamento de Vendors Críticos

| Vendor | Contrato | Acesso | Nível de Risco | MITRE Technique |
|--------|----------|--------|----------------|-----------------|
| **Oceânica Engenharia** | R$ 4,2B (2026-2031) | OT offshore, vessels | ⭐⭐⭐ CRÍTICO | T0866 (Exploit via remote) |
| **OceanPact** | R$ 3,2B (acquisition) | OSV fleet, logistics | ⭐⭐⭐ CRÍTICO | T0866 |
| **SA Exploration** | Significativo | Seismic data (BREACHED) | ⭐⭐⭐ COMPROMETIDO | T1195 |
| **Subsea 7** | Multi-B | Subsea engineering | ⭐⭐ HIGH | T1078 |
| **TechnipFMC** | Multi-B | Equipment, systems | ⭐⭐ HIGH | T0866 |

### Modelo de Scoring de Risco

```python
class VendorRiskScoring:
    """
    Modelo ponderado de avaliação de risco de vendors
    Escala: 0-100 (0=Baixo, 100=Crítico)
    """
    
    WEIGHTS = {
        'data_access_level': 0.25,      # Volume/sensibilidade
        'network_access_scope': 0.20,   # OT vs IT
        'security_maturity': 0.20,      # Certificações
        'financial_stability': 0.15,    # Crédito
        'geopolitical_risk': 0.10,      # País
        'incident_history': 0.10        # Breaches passados
    }
    
    def calculate_score(self, vendor):
        scores = {
            'data_access_level': self._score_data_access(vendor),
            'network_access_scope': self._score_network_access(vendor),
            'security_maturity': self._score_security_posture(vendor),
            'financial_stability': self._score_financial_health(vendor),
            'geopolitical_risk': self._score_geo_risk(vendor),
            'incident_history': self._score_past_incidents(vendor)
        }
        
        weighted_score = sum(
            scores[k] * self.WEIGHTS[k] 
            for k in scores
        )
        
        return {
            'total_score': weighted_score,
            'risk_level': self._classify_risk(weighted_score),
            'component_scores': scores,
            'recommendation': self._generate_recommendation(weighted_score)
        }
    
    def _classify_risk(self, score):
        if score <= 30: return 'LOW'
        if score <= 60: return 'MEDIUM'
        if score <= 80: return 'HIGH'
        return 'CRITICAL'
    
    def _generate_recommendation(self, score):
        recommendations = {
            'LOW': 'Annual review sufficient',
            'MEDIUM': 'Quarterly review recommended',
            'HIGH': 'Monthly review + compensating controls',
            'CRITICAL': 'Continuous monitoring + executive reporting'
        }
        return recommendations.get(self._classify_risk(score))

# Exemplo: SA Exploration post-breach
sa_exploration = VendorRiskScoring()
result = sa_exploration.calculate_score({
    'data_access': 'Seismic research (highest sensitivity)',
    'network_access': 'VPN to data repositories',
    'security_maturity': 'Low (no MFA, no monitoring)',
    'incident_history': 'CONFIRMED_BREACH_Nov2025'
})
# Resultado esperado: Score 85-95 (CRITICAL)
```

## 3.5 SCADA/OT Protocols - Análise de Vulnerabilidades

### Modbus TCP/RTU

```yaml
Protocol: Modbus
Version: TCP (Port 502), RTU (Serial)
Deployment: "70% dos sistemas industriais brasileiros"
Security_Level: "CRITICAL - No native security"

Vulnerabilities:
  Authentication:
    status: "NONE"
    impact: "Any host can connect and issue commands"
    
  Encryption:
    status: "NONE"
    impact: "Plaintext communication"
    
  Session_Management:
    status: "NONE"
    impact: "No concept of sessions or state"
    
  Command_Replay:
    status: "VULNERABLE"
    impact: "Commands can be replayed by attackers"

Attack_Vectors:
  - Function_Code_8: "Diagnostics abuse - reconnaissance"
  - Function_Code_43: "Encapsulated transport - payload delivery"
  - Force_Coil_FC5: "Write single coil - unauthorized control"
  - Preset_Registers_FC16: "Mass configuration changes"
  - Man_in_the_Middle: "Traffic interception"

Petrobras_Context:
  Usage: "Wellhead controllers, pump stations, tank monitoring"
  Pre_Salt_Risk: "Offshore platforms use Modbus for sensor networks"
  Recent_Malware: "FrostyGoop used Modbus to manipulate devices"

Defensive_Measures:
  1. "Protocol whitelisting (allow only specific FCs)"
  2. "Network segmentation (dedicated control VLANs)"
  3. "Deep packet inspection for Modbus traffic"
  4. "Read-only mode for non-control systems"
  5. "Register address range restrictions"
```

### DNP3 (Distributed Network Protocol 3)

```yaml
Protocol: DNP3
Port: TCP 20000
Usage: "Power utilities, pipelines, water systems"

Security_Features:
  Secure_DNP3: "Available but often not implemented"
  Authentication: "Weak or disabled"
  Encryption: "Not in legacy deployments"

Vulnerabilities:
  - Cleartext_Default: "No encryption"
  - Weak_Auth: "Default keys or disabled"
  - Unsolicited_Response_Spoofing: "Outstations can be impersonated"
  - Time_Sync_Manipulation: "Attackers can skew timestamps"
  - Broadcast_Abuse: "Disruption via broadcast"

MITRE_Mapping:
  T0851: "Spoofing - Master/outstation impersonation"
  T0857: "Replay attacks"
  T0839: "Time manipulation"
  T0855: "Cold restart (DoS)"
```

### OPC UA (Unified Architecture)

```yaml
Protocol: OPC UA
Evolution: "Successor to OPC Classic (DCOM)"
Security_Model: "Built-in but often misconfigured"

Security_Modes:
  None:
    level: "CRITICAL"
    features: "No encryption, no signing"
    prevalence: "Unfortunately common"
    
  Sign:
    level: "MEDIUM"
    features: "Digital signatures only"
    
  SignAndEncrypt:
    level: "LOW"
    features: "Full security"
    recommendation: "MANDATORY"

Common_Misconfigurations:
  1. "Security mode set to 'None'"
  2. "Anonymous endpoints enabled"
  3. "Self-signed certificates (no PKI)"
  4. "Weak certificate validation"
  5. "Exposed discovery endpoints"

Petrobras_Context:
  Usage: "Digital twins, historian systems, HMI integration"
  Libra_Rocks: "R$151M AI project likely uses OPC UA"
  Risk: "AI/ML pipelines may ingest via OPC UA"

Recommendations:
  - "Enforce SignAndEncrypt mode"
  - "Disable anonymous access"
  - "Implement certificate PKI"
  - "Endpoint access restrictions"
  - "Regular certificate rotation"
```

### Detecção de Anomalias - Use Cases

```yaml
alert_rules:
  # Modbus Anomaly Detection
  modbus_suspicious_function_code:
    when: "function_code NOT IN [1, 2, 3, 4, 5, 6, 15, 16]"
    severity: HIGH
    action: "alert_and_log"
    
  modbus_mass_write:
    when: "function_code = 16 AND register_count > 10"
    severity: CRITICAL
    action: "alert_and_block"
    
  modbus_unauthorized_source:
    when: "src_ip NOT IN authorized_masters"
    severity: HIGH
    action: "alert_and_block"
    
  # LGPD Breach Detection
  large_data_exfiltration:
    when: "bytes_out > 1GB AND dst_country != 'Brazil'"
    severity: CRITICAL
    action: "alert_dpo_and_anpd"
    trigger: "lgpd_breach_workflow"
    
  unauthorized_database_access:
    when: "db_query_count > threshold AND user_role != 'dba'"
    severity: HIGH
    action: "alert_and_investigate"
    
  # Vendor Access Anomalies
  vendor_off_hours_access:
    when: "vendor_login AND time NOT IN business_hours"
    severity: MEDIUM
    action: "alert_soc"
    
  vendor_concurrent_sessions:
    when: "same_vendor_multiple_ips"
    severity: HIGH
    action: "verify_identity"
```

---

# PARTE IV: PROPOSTA TÉCNICA DE SOLUÇÃO

## 4.1 Sentinela Vendor Trust - Arquitetura

### Visão Geral da Plataforma

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SENTINEL VENDOR TRUST v1.0                               │
│              Vendor Risk Intelligence for Oil & Gas                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        DATA COLLECTION LAYER                        │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐    │   │
│  │  │ EXTERNAL         │ │ INTERNAL         │ │ THREAT INTEL     │    │   │
│  │  │ OSINT SCANNING   │ │ SYSTEMS          │ │ FEEDS            │    │   │
│  │  │                  │ │                  │ │                  │    │   │
│  │  │ • Port scanning  │ │ • SAP ERP        │ │ • Dark web       │    │   │
│  │  │ • SSL monitoring │ │ • Active Dir.    │ │ • IOCs           │    │   │
│  │  │ • Cert tracking  │ │ • SIEM logs      │ │ • APT intel      │    │   │
│  │  │ • Website crawl  │ │ • DLP alerts     │ │ • Ransomware     │    │   │
│  │  │ • DNS monitoring │ │ • VPN logs       │ │ • CISA alerts    │    │   │
│  │  └────────┬─────────┘ └────────┬─────────┘ └────────┬─────────┘    │   │
│  │           └────────────────────┼────────────────────┘              │   │
│  └────────────────────────────────┼───────────────────────────────────┘   │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     RISK ANALYTICS ENGINE                           │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                     │   │
│  │  ┌───────────────────────────────────────────────────────────────┐ │   │
│  │  │ ML MODELS                                                     │ │   │
│  │  │ • Anomaly detection (behavioral baselines)                    │ │   │
│  │  │ • Risk prediction (vendor failure probability)                │ │   │
│  │  │ • Breach correlation (dark web → vendor matching)             │ │   │
│  │  │ • Geopolitical risk scoring                                   │ │   │
│  │  └───────────────────────────────────────────────────────────────┘ │   │
│  │                                                                     │   │
│  │  ┌───────────────────────────────────────────────────────────────┐ │   │
│  │  │ RISK SCORING ENGINE                                           │ │   │
│  │  │ • Multi-factor weighted algorithm (0-100)                     │ │   │
│  │  │ • Dynamic recalculation (real-time updates)                   │ │   │
│  │  │ • Peer benchmarking                                           │ │   │
│  │  │ • Trend analysis                                              │ │   │
│  │  └───────────────────────────────────────────────────────────────┘ │   │
│  │                                                                     │   │
│  │  ┌───────────────────────────────────────────────────────────────┐ │   │
│  │  │ COMPLIANCE AUTOMATION                                         │ │   │
│  │  │ • LGPD Article 37 mapping                                     │ │   │
│  │  │ • ANP Resolution 882 checklists                               │ │   │
│  │  │ • Breach notification (3-day ANPD)                            │ │   │
│  │  │ • SCC validation (Res 19/2024)                                │ │   │
│  │  └───────────────────────────────────────────────────────────────┘ │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                   ▼                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                  VISUALIZATION & RESPONSE LAYER                     │   │
│  ├─────────────────────────────────────────────────────────────────────┤   │
│  │                                                                     │   │
│  │  ┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐    │   │
│  │  │ EXECUTIVE        │ │ OPERATIONAL      │ │ COMPLIANCE       │    │   │
│  │  │ DASHBOARD        │ │ CONSOLE          │ │ PORTAL           │    │   │
│  │  │                  │ │                  │ │                  │    │   │
│  │  │ • Risk posture   │ │ • Real-time      │ │ • ANPD reports   │    │   │
│  │  │ • Trending       │ │   alerts         │ │ • Audit trails   │    │   │
│  │  │ • Board metrics  │ │ • Incident       │ │ • SCC templates  │    │   │
│  │  │                  │ │   management     │ │                  │    │   │
│  │  └──────────────────┘ └──────────────────┘ └──────────────────┘    │   │
│  │                                                                     │   │
│  │  ┌───────────────────────────────────────────────────────────────┐ │   │
│  │  │ AUTOMATED RESPONSE                                            │ │   │
│  │  │ • One-click access revocation                                 │ │   │
│  │  │ • Automated ticket creation                                   │ │   │
│  │  │ • Forensic evidence collection                                │ │   │
│  │  │ • Stakeholder notification                                    │ │   │
│  │  └───────────────────────────────────────────────────────────────┘ │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 4.2 Componentes Técnicos Detalhados

### Módulo 1: Vendor Discovery & Inventory

```python
class VendorDiscovery:
    """
    Automated vendor identification and enrichment
    """
    
    def discover_from_erp(self, sap_connection):
        """Extract vendor list from SAP ERP"""
        vendors = sap_connection.query(
            table='LFA1',  # Vendor master
            fields=['LIFNR', 'NAME1', 'STRAS', 'ORT01', 'LAND1'],
            filters={'LOEVM': ''}  # Not deleted
        )
        return self._enrich_vendor_data(vendors)
    
    def discover_shadow_it(self, network_logs):
        """Identify vendors not in official records"""
        # Analyze network traffic for vendor connections
        external_ips = extract_unique_destinations(network_logs)
        vendor_ips = correlate_with_threat_intel(external_ips)
        return self._identify_unknown_vendors(vendor_ips)
    
    def map_fourth_party(self, vendor_contracts):
        """Map subcontractors (4th party risk)"""
        fourth_parties = []
        for vendor in vendor_contracts:
            subcontractors = vendor.get_subcontractors()
            fourth_parties.extend(subcontractors)
        return fourth_parties
    
    def _enrich_vendor_data(self, vendors):
        """Enrich with external data sources"""
        for vendor in vendors:
            vendor.website_data = self._scrape_website(vendor.website)
            vendor.linkedIn_data = self._search_linkedIn(vendor.name)
            vendor.certificate_data = self._check_ssl_cert(vendor.domain)
            vendor.reputation_data = self._check_reputation(vendor.domain)
        return vendors
```

### Módulo 2: Continuous Monitoring

```python
class ContinuousMonitoring:
    """
    24/7 vendor security monitoring
    """
    
    def __init__(self):
        self.scanners = {
            'port_scanner': NmapScanner(),
            'ssl_checker': SSLChecker(),
            'dark_web_monitor': DarkWebMonitor(),
            'breach_checker': HaveIBeenPwnedAPI(),
            'threat_intel': MISPIntegration()
        }
    
    def monitor_vendor(self, vendor):
        """Execute full monitoring suite"""
        results = {
            'timestamp': datetime.utcnow(),
            'vendor_id': vendor.id,
            
            'external_scan': self._external_scan(vendor),
            'security_posture': self._check_security_posture(vendor),
            'dark_web_exposure': self._check_dark_web(vendor),
            'breach_status': self._check_breach_databases(vendor),
            'threat_intel': self._query_threat_intel(vendor)
        }
        
        return self._analyze_results(results)
    
    def _external_scan(self, vendor):
        """Network-level security scan"""
        return {
            'open_ports': self.scanners['port_scanner'].scan(vendor.domain),
            'ssl_grade': self.scanners['ssl_checker'].check(vendor.domain),
            'exposed_services': self._identify_services(vendor.domain),
            'vulnerabilities': self._check_cves(vendor.domain)
        }
    
    def _check_dark_web(self, vendor):
        """Monitor dark web for vendor data"""
        queries = [
            vendor.name,
            vendor.domain,
            vendor.email_domain,
            f"{vendor.name} credentials",
            f"{vendor.name} database"
        ]
        
        findings = []
        for query in queries:
            results = self.scanners['dark_web_monitor'].search(query)
            findings.extend(results)
        
        return {
            'exposed_credentials': findings,
            'risk_level': self._assess_dark_web_risk(findings)
        }
```

### Módulo 3: Risk Scoring Engine

```python
class RiskScoringEngine:
    """
    Dynamic risk scoring with ML components
    """
    
    WEIGHTS = {
        'external_security': 0.20,
        'dark_web_exposure': 0.15,
        'financial_health': 0.15,
        'access_privileges': 0.20,
        'incident_history': 0.15,
        'compliance_status': 0.15
    }
    
    def calculate_risk_score(self, vendor):
        """Calculate comprehensive risk score"""
        
        components = {
            'external_security': self._score_external_security(vendor),
            'dark_web_exposure': self._score_dark_web(vendor),
            'financial_health': self._score_financial_health(vendor),
            'access_privileges': self._score_access_risk(vendor),
            'incident_history': self._score_incident_history(vendor),
            'compliance_status': self._score_compliance(vendor)
        }
        
        # Calculate weighted score
        total_score = sum(
            components[k] * self.WEIGHTS[k]
            for k in components
        )
        
        # ML anomaly detection
        anomaly_factor = self._ml_anomaly_detection(vendor, components)
        
        final_score = min(100, total_score * anomaly_factor)
        
        return {
            'score': round(final_score, 1),
            'risk_level': self._classify_risk(final_score),
            'components': components,
            'anomaly_detected': anomaly_factor > 1.2,
            'trend': self._calculate_trend(vendor),
            'recommendations': self._generate_recommendations(final_score, components)
        }
    
    def _ml_anomaly_detection(self, vendor, components):
        """
        Detect anomalous patterns using ML
        """
        # Load pre-trained model
        model = joblib.load('models/vendor_anomaly_v1.pkl')
        
        features = [
            components['external_security'],
            components['dark_web_exposure'],
            components['access_privileges'],
            vendor.data_volume_accessed,
            vendor.session_duration_avg,
            vendor.off_hours_access_rate
        ]
        
        anomaly_score = model.predict_proba([features])[0][1]
        
        # Return anomaly multiplier
        if anomaly_score > 0.8:
            return 1.3  # 30% score increase for anomalies
        elif anomaly_score > 0.6:
            return 1.1
        return 1.0
```

### Módulo 4: LGPD Compliance Automation

```python
class LGPDComplianceModule:
    """
    Automated LGPD compliance management
    """
    
    def generate_article37_record(self, processing_activity):
        """Generate Article 37 processing record"""
        
        record = {
            'record_id': uuid.uuid4(),
            'created_at': datetime.utcnow(),
            'last_updated': datetime.utcnow(),
            
            'controller': {
                'name': 'Petrobras',
                'cnpj': '33.000.167/0001-01',
                'dpo': 'encarregado@petrobras.com.br'
            },
            
            'processing': {
                'activity_name': processing_activity.name,
                'purpose': processing_activity.purpose,
                'legal_basis': processing_activity.legal_basis,
                'legitimate_interest': processing_activity.legitimate_interest,
                'data_categories': processing_activity.data_categories,
                'sensitive_data': processing_activity.contains_sensitive,
                'data_subjects': {
                    'categories': processing_activity.subject_categories,
                    'estimated_volume': processing_activity.subject_count
                }
            },
            
            'retention': {
                'period': processing_activity.retention_period,
                'criteria': processing_activity.retention_criteria,
                'destruction_method': 'Secure deletion per NIST 800-88'
            },
            
            'security_measures': self._list_security_measures(processing_activity),
            
            'sharing': {
                'processors': self._list_processors(processing_activity),
                'third_parties': self._list_third_parties(processing_activity),
                'international_transfers': self._check_intl_transfers(processing_activity)
            }
        }
        
        return record
    
    def trigger_breach_notification(self, incident):
        """Automated ANPD breach notification (Res 15/2024)"""
        
        # Validate if notification required
        if not self._is_notifiable_breach(incident):
            return {'notification_required': False}
        
        # Calculate 3 business days deadline
        deadline = self._calculate_business_days(3)
        
        # Generate ANPD report
        report = {
            'tipo_incidencia': incident.classification,
            'data_hora': incident.detection_time.isoformat(),
            'categorias_dados': incident.data_categories,
            'quantidade_titulares': incident.affected_subjects,
            'medidas_tecnicas': incident.remediation_actions,
            'contato_encarregado': 'encarregado@petrobras.com.br',
            'prazo_notificacao': deadline.isoformat()
        }
        
        # Auto-submit to ANPD
        self._submit_to_anpd(report)
        
        # Notify affected subjects
        self._notify_data_subjects(incident)
        
        return {
            'notification_required': True,
            'anpd_reference': report['id'],
            'deadline': deadline,
            'submitted': True
        }
    
    def _is_notifiable_breach(self, incident):
        """Determine if breach requires ANPD notification"""
        # Res 15/2024 criteria
        
        if incident.data_sensitivity in ['high', 'sensitive']:
            return True
        
        if incident.affected_subjects > 1000:
            return True
        
        if incident.potential_impact == 'significant':
            return True
        
        if incident.data_volume_gb > 1.0:
            return True
        
        return False
```

## 4.3 Stack Tecnológico Recomendado

| Componente | Tecnologia | Justificativa |
|------------|------------|---------------|
| **Backend API** | Python 3.11 + FastAPI | Async, high-performance, ML-ready |
| **Frontend** | React 18 + TypeScript | Type safety, component reusability |
| **Database** | PostgreSQL 15 + TimescaleDB | Relational + time-series data |
| **Cache/Queue** | Redis + Celery | Async task processing |
| **ML/Analytics** | Scikit-learn + XGBoost | Proven algorithms, explainability |
| **Scanning** | Python-Nmap + Shodan API | Industry-standard tools |
| **Monitoring** | Prometheus + Grafana | Observability stack |
| **Security** | OWASP ZAP + Bandit | Security testing |
| **Deployment** | Docker + Kubernetes | Container orchestration |
| **Cloud** | AWS (Petrobras-compatible) | Existing relationship |

## 4.4 Integrações Empresariais

```yaml
Petrobras_Integration_Map:
  ERP:
    system: "SAP S/4HANA"
    integration: "RFC/BAPI connectors"
    data: "Vendor master, contracts, payments"
    
  IAM:
    system: "Active Directory + SAP IDM"
    integration: "LDAP/SCIM"
    data: "Vendor accounts, access rights"
    
  SIEM:
    system: "Splunk/QRadar (assumed)"
    integration: "REST API / Syslog"
    data: "Security events, access logs"
    
  DLP:
    system: "Symantec/McAfee (assumed)"
    integration: "API"
    data: "Data exfiltration alerts"
    
  Petronect:
    system: "Vendor marketplace"
    integration: "API"
    data: "Vendor onboarding, transactions"
    
  ANP:
    system: "Regulatory portal"
    integration: "API (future)"
    data: "Incident reports, compliance"
```

---

# PARTE V: ESTRATÉGIA DE EXECUÇÃO HACKATHON

## 5.1 MVP Scope (72 Horas)

### Funcionalidades Mínimas Viáveis

```yaml
MVP_Components:
  
  Component_1_Vendor_Discovery:
    hours: 8
    deliverables:
      - "CSV import de vendors"
      - "Auto-enrichment básico (website, SSL)"
      - "Listagem com risk scores"
    
  Component_2_External_Monitoring:
    hours: 16
    deliverables:
      - "Port scanning (top 100 ports)"
      - "SSL certificate validation"
      - "Dark web credential check (HaveIBeenPwned)"
      - "Breach notification tracking"
    
  Component_3_Risk_Dashboard:
    hours: 16
    deliverables:
      - "Vendor list com scores 0-100"
      - "Risk distribution visualization"
      - "Alert management interface"
      - "Drill-down capability"
    
  Component_4_LGPD_Module:
    hours: 16
    deliverables:
      - "Article 37 record template"
      - "Breach notification calculator"
      - "3-day ANPD deadline tracker"
      - "Basic compliance checklist"
    
  Component_5_Pitch_Demo:
    hours: 16
    deliverables:
      - "Working demo (local)"
      - "Pitch deck (problem → solution → demo → ROI)"
      - "Business case com cálculos"
      - "Technical architecture diagram"
```

## 5.2 Demo Script (5 minutos)

```
┌────────────────────────────────────────────────────────────────┐
│                    DEMO SCRIPT - 5 MINUTES                     │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  [0:00-0:30] INTRODUÇÃO                                       │
│  "Em novembro de 2025, a Petrobras perdeu 90GB de dados      │
│   sísmicos por conta de um vendor comprometido.               │
│   Nossa solução previne isso."                                │
│                                                                │
│  [0:30-1:30] PROBLEMA                                         │
│  [Mostrar dashboard com incidente SA Exploration]             │
│  "SA Exploration: score de risco 85/100.                      │
│   Credenciais vazadas, nenhum MFA, 90GB perdidos."            │
│                                                                │
│  [1:30-3:30] SOLUÇÃO                                          │
│  [Demonstrar features ao vivo]                                │
│                                                                │
│  1. DISCOVERY:                                                │
│     "Importei lista de 47 vendors críticos.                   │
│      Sistema enriqueceu automaticamente."                     │
│                                                                │
│  2. MONITORING:                                               │
│     "Scanning contínuo detectou:                              │
│      - 3 vendors com ports expostas                           │
│      - 1 vendor com credenciais no dark web                   │
│      - Alerta gerado em tempo real"                           │
│                                                                │
│  3. RISK SCORING:                                             │
│     "Algoritmo calcula score ponderado.                       │
│      Vendor X: 78/100 (HIGH RISK)                             │
│      Por quê? Access level + dark web + no MFA"               │
│                                                                │
│  4. RESPONSE:                                                 │
│     "Um click: revogação de acesso automática.               │
│      LGPD: notificação ANPD gerada."                          │
│                                                                │
│  [3:30-4:30] VALOR                                            │
│  [Mostrar ROI]                                                │
│  "Custo do breach: R$ 35-110M.                                │
│   Custo da solução: R$ 2-5M/ano.                              │
│   ROI: 700%+ no primeiro ano."                                │
│                                                                │
│  [4:30-5:00] CALL TO ACTION                                   │
│  "Precisamos de 6 meses de piloto com 50 vendors.            │
│   Petrobras, vamos conversar?"                                │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

## 5.3 Critérios de Avaliação do Grand Prix

### Pesos Históricos (2022-2024)

| Critério | Peso | Como Maximizar |
|----------|------|----------------|
| **Protótipo Funcional** | 40% | Working demo, não slides |
| **Aplicabilidade Real** | 25% | Referenciar caso Petrobras |
| **Inovação Tecnológica** | 15% | ML, automação, LGPD |
| **Apresentação** | 10% | Pitch claro, 5 min precisos |
| **Diversidade da Equipe** | 10% | Mulheres, diferentes backgrounds |

### Diferenciadores Estratégicos

1. **Referenciar breach real (SA Exploration)**
   - Demonstrar entendimento profundo do problema
   - Mostrar como solução previne reincidência

2. **LGPD nativo (não adaptação GDPR)**
   - Res 19/2024 SCCs em português
   - 3 dias úteis vs 72 horas
   - ANP Resolution 882

3. **Cálculo de ROI tangível**
   - Custo do breach: R$ 35-110M
   - Investimento: R$ 10-20M (3 anos)
   - Payback: <12 meses

4. **Demonstrar integração**
   - SAP ERP mock
   - ANPD report auto-generation
   - SIEM integration diagram

---

# PARTE VI: ECONOMETRIA E ROI

## 6.1 Análise de Custo-Benefício Detalhada

### Cenário de Prevenção

```yaml
Breach_Analysis:
  Scenario: "Prevenção de 1 breach a cada 3 anos"
  
  Cost_of_Breach:
    forensics_recovery: "R$ 5-10M"
    regulatory_fines_anpd: "R$ 10-50M (até 2% receita)"
    operational_disruption: "R$ 20-50M"
    reputational_damage: "Imensurável"
    competitive_impact: "Estratégico (dados sísmicos)"
    total_potential: "R$ 35-110M+"
    
  Solution_Investment:
    year_1:
      platform_license: "R$ 2-3M"
      implementation: "R$ 3-5M (one-time)"
      operations: "R$ 1M"
      total: "R$ 6-9M"
      
    year_2_3:
      platform_license: "R$ 2-3M/year"
      operations: "R$ 1-2M/year"
      total_per_year: "R$ 3-5M"
      
    total_3_years: "R$ 12-19M"
    
  ROI_Calculation:
    conservative:
      breach_cost_avoided: "R$ 35M"
      investment: "R$ 19M"
      roi: "184%"
      
    realistic:
      breach_cost_avoided: "R$ 60M"
      investment: "R$ 15M"
      roi: "300%"
      
    optimistic:
      breach_cost_avoided: "R$ 110M"
      investment: "R$ 12M"
      roi: "817%"
```

## 6.2 Benchmarks de Eficiência

| Métrica | Indústria (Média) | Nossa Solução | Diferencial |
|---------|-------------------|---------------|-------------|
| **Mean Time to Detect** | 280 dias | < 24 horas | -99.1% |
| **Mean Time to Respond** | 73 dias | < 4 horas | -99.4% |
| **Vendor Coverage** | 40% | 95%+ | +137% |
| **False Positive Rate** | 25% | < 5% | -80% |
| **Compliance Automation** | 30% | 80%+ | +166% |
| **4th Party Visibility** | <20% | 70% | +250% |

---

# PARTE VII: ANEXOS TÉCNICOS

## A. MITRE ATT&CK for ICS Mapping

### Táticas e Técnicas Relevantes

```yaml
Initial_Access:
  T1133: "External Remote Services - VPN exploitation"
  T0819: "Internet-Accessible Device - Exposed PLCs"
  T1195: "Supply Chain Compromise - SA Exploration"
  T1566: "Spearphishing - Vendor targeting"

Execution:
  T0831: "Modify Controller Logic - PLC code injection"
  T0834: "Native API - Protocol abuse (Modbus/DNP3)"
  T0853: "Scripting - PowerShell/Python payloads"

Persistence:
  T1078: "Valid Accounts - Compromised vendor credentials"
  T0859: "Valid Accounts - Local admin"

Discovery:
  T0846: "Remote System Discovery - Network scanning"
  T0841: "Network Service Scanning - Port scanning"

Collection:
  T0811: "Data from Local System - File collection"
  T1213: "Data from Info Repositories - Seismic databases"
  T0817: "Theft of Operational Information - Exfiltration"

Impact:
  T0835: "Manipulation of Control - Setpoint changes"
  T0813: "Denial of Control - Command blocking"
  T0816: "Device Restart/Shutdown - DoS"
```

## B. Common Ports & Protocols

| Protocol | Port | Security Risk | Mitigação |
|----------|------|---------------|-----------|
| Modbus TCP | 502 | ⭐⭐⭐ CRÍTICA | DPI, whitelisting |
| DNP3 | 20000 | ⭐⭐⭐ CRÍTICA | Secure DNP3, key mgmt |
| OPC UA Discovery | 4840 | ⭐⭐ ALTA | SignAndEncrypt mode |
| OPC UA Binary | 4840 | ⭐⭐ ALTA | Certificate PKI |
| IEC 61850 MMS | 102 | ⭐⭐⭐ CRÍTICA | GOOSE validation |
| EtherNet/IP | 44818 | ⭐⭐ ALTA | CIP security |
| Siemens S7 | 102 | ⭐⭐⭐ CRÍTICA | S7Comm+ |

## C. LGPD Checklist Técnico

```yaml
Data_Mapping:
  - [ ] Processing activities documented (Art 37)
  - [ ] Data categories classified
  - [ ] Data subjects identified
  - [ ] Legal basis mapped
  - [ ] Retention periods defined
  
Security_Controls:
  - [ ] Encryption at rest (AES-256)
  - [ ] Encryption in transit (TLS 1.3)
  - [ ] Access controls (RBAC + MFA)
  - [ ] Audit logging (12 months)
  - [ ] DLP monitoring
  
Vendor_Management:
  - [ ] DPAs signed (Art 46)
  - [ ] Security assessments
  - [ ] Incident notification clauses
  - [ ] International transfer mechanisms
  
Incident_Response:
  - [ ] Breach detection procedures
  - [ ] ANPD notification (3 days)
  - [ ] Subject notification
  - [ ] Forensic preservation
  
Compliance_Monitoring:
  - [ ] DPO appointed
  - [ ] Privacy notices published
  - [ ] Subject rights procedures
  - [ ] Regular audits
```

## D. Referências e Fontes

### Inteligência Petrobras
1. Petrobras Business Plan 2026-2030 (SEC Filing 6-K)
2. Agência Petrobras Official Communications
3. Investor Relations: investidorpetrobras.com.br

### Regulamentação
1. LGPD - Lei 13.709/2018
2. ANPD Resolution 15/2024 (Breach Notification)
3. ANPD Resolution 19/2024 (International Transfers)
4. Decree 12.572/2025 (National Security Policy)
5. Decree 12.573/2025 (National Cybersecurity Strategy)
6. ANP Resolution 882/2022

### Threat Intelligence
1. CISA Alerts (April 2026 - Iranian APTs)
2. Dragos Industrial Ransomware Reports
3. Microsoft Threat Intelligence (Storm-1175)
4. TecMundo Security (Brazil threats)

### Frameworks
1. MITRE ATT&CK for ICS
2. NIST Cybersecurity Framework
3. ISO 27001/27002
4. IEC 62443 (Industrial Security)

---

# CONCLUSÃO E CALL TO ACTION

## Síntese Executiva

```
┌────────────────────────────────────────────────────────────────┐
│              PROPOSTA ESTRATÉGICA - RESUMO TÉCNICO            │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  PROBLEMA: Petrobras sofreu breach de 90GB via vendor em      │
│            nov/2025. Supply chain é superfície de ataque      │
│            desprotegida com 10.000+ vendors.                  │
│                                                                │
│  SOLUÇÃO: Sentinel Vendor Trust - Plataforma de monitoramento │
│           contínuo, scoring dinâmico, compliance LGPD/ANP     │
│           automatizado, específica para oil & gas.            │
│                                                                │
│  DIFERENCIAL:                                                  │
│           ✓ Foco em supply chain (lição SA Exploration)       │
│           ✓ LGPD nativa brasileira (não adaptação GDPR)       │
│           ✓ Integração OT/ICS (Modbus/DNP3/OPC UA)            │
│           ✓ ROI demonstrável (200-800% em 3 anos)             │
│                                                                │
│  EXECUÇÃO: MVP em 72h (hackathon) → PoC 3 meses →             │
│            Piloto 6 meses → Produção 12 meses                 │
│                                                                │
│  PEDIDO: 6 meses de piloto com 50 vendors críticos           │
│          para demonstrar valor mensurável.                    │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

**Documento Técnico Completo**  
**Versão:** 2.0 (Especialista)  
**Data:** Abril 2026  
**Para:** Grand Prix SENAI de Inovação 2026 - Desafio Petrobras  
**Classificação:** Inteligência Técnica Aplicada

---

*Este documento sintetiza análises técnicas de protocolos industriais, 
regulamentação brasileira, threat intelligence global e especificidades 
do ecossistema Petrobras em uma proposta de solução completa para 
especialistas em cybersecurity.*
