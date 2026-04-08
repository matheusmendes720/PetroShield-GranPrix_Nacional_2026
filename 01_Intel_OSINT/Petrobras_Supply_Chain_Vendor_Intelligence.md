# PETROBRAS SUPPLY CHAIN & VENDOR INTELLIGENCE
## Post-SA Exploration Breach Analysis

---

# EXECUTIVE SUMMARY

The November 2025 Everest ransomware breach through **SA Exploration** exposed catastrophic vulnerabilities in Petrobras' supply chain security. This document provides comprehensive intelligence on Petrobras' vendor ecosystem, risk factors, and strategic opportunities for supply chain security solutions.

**Critical Finding:** Petrobras' vendor ecosystem includes thousands of contractors with varying security postures, creating a massive attack surface that nation-state actors and cybercriminals actively exploit.

---

# PART 1: THE SA EXPLORATION BREACH - CASE STUDY

## 1.1 Incident Timeline

| Date | Event |
|------|-------|
| **Nov 14, 2025** | Everest group compromises SA Exploration systems |
| **Nov 17, 2025** | Countdown timer published on dark web |
| **Nov 17, 2025** | Petrobras announces oil discovery in Campos Basin (coincidence?) |
| **Nov 20, 2025** | Petrobras confirms unauthorized data exposure |
| **Nov 25, 2025** | 190GB of data leaked after ransom non-payment |

## 1.2 Attack Vector Analysis

### How the Breach Occurred:
```
1. CREDENTIAL COMPROMISE
   └─> SA Exploration VPN credentials stolen
   └─> Likely via credential stuffing or phishing

2. LATERAL MOVEMENT
   └─> Access to SA Exploration internal systems
   └─> Compromise of shared resources with Petrobras

3. DATA EXFILTRATION
   └─> 90GB Petrobras data + 176GB SA Exploration data
   └─> Seismic research data from Campos Basin
   └─> Navigation coordinates, equipment specs
```

### Data Compromised:
- Raw seismic navigation data
- Ship coordinates and DGPS positioning
- Ocean Bottom Node (OBN) positions
- Equipment configurations
- Survey quality control parameters
- **Strategic Impact:** Competitors could replicate exploration strategies

## 1.3 Lessons Learned

| Failure Point | Root Cause | Solution Needed |
|--------------|------------|-----------------|
| Vendor credential compromise | Weak password policy + no MFA | Vendor access governance |
| Lack of vendor monitoring | No continuous security assessment | Real-time vendor monitoring |
| Unrestricted data access | Poor data classification | Data loss prevention (DLP) |
| Delayed detection | No anomaly detection | Behavioral analytics |

---

# PART 2: PETROBRAS VENDOR ECOSYSTEM

## 2.1 Major Contract Categories

### **Category A: Critical Infrastructure (>R$1B contracts)**

| Vendor | Service | Contract Value | Risk Level |
|--------|---------|---------------|------------|
| **Oceânica Engenharia** | Subsea vessels | R$ 4.2B (US$736M) | CRITICAL |
| **OceanPact** | Offshore support | R$ 3.2B | CRITICAL |
| **Subsea 7** | Subsea engineering | Multi-billion | HIGH |
| **TechnipFMC** | Subsea equipment | Multi-billion | HIGH |

### **Category B: Technical Services (R$100M-1B)**

| Vendor | Service | Risk Factors |
|--------|---------|--------------|
| **SA Exploration** | Seismic surveys | **BREACHED Nov 2025** |
| **Ambipar** | Environmental services | Financial crisis |
| **Various drilling contractors** | Well operations | OT network access |
| **Engineering consultancies** | Project design | Data processing |

### **Category C: Technology & IT**

| Vendor Type | Examples | Risk Profile |
|-------------|----------|--------------|
| Cloud providers | AWS, Azure, local | Data sovereignty |
| Software vendors | SAP, Oracle, custom | Supply chain |
| Cybersecurity firms | Various | Trusted access |
| System integrators | Multiple | Broad network access |

## 2.2 Vendor Statistics

**Scale of Vendor Ecosystem:**
- **Total active vendors:** 10,000+
- **Critical vendors:** ~500
- **High-access vendors:** ~2,000
- **International vendors:** ~30%
- **Local Brazilian vendors:** ~70%

**Recent Vendor Initiatives:**
- Petronect marketplace: 104+ transactions in 2025
- Sebrae partnership: Local supplier development
- ABIMAQ collaboration: Industrial equipment suppliers
- New pre-qualification model: Enhanced vetting

---

# PART 3: SUPPLY CHAIN RISK FRAMEWORK

## 3.1 Risk Taxonomy

### **Tier 1: Direct Vendor Risks**
```
┌─────────────────────────────────────────────────────────────┐
│ 1. CREDENTIAL THEFT                                          │
│    - Compromised VPN accounts                                │
│    - Weak password policies                                  │
│    - No multi-factor authentication                          │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 2. NETWORK ACCESS ABUSE                                      │
│    - Overprivileged vendor accounts                          │
│    - Standing access (not just-in-time)                      │
│    - No session monitoring                                   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 3. DATA EXFILTRATION                                         │
│    - Unmonitored data downloads                              │
│    - USB/removable media                                     │
│    - Cloud storage uploads                                   │
└─────────────────────────────────────────────────────────────┘
```

### **Tier 2: Supply Chain Risks**
```
┌─────────────────────────────────────────────────────────────┐
│ 4. SUBCONTRACTOR VULNERABILITIES (4th PARTY)                 │
│    - Vendor's vendors compromise                             │
│    - Cascading security failures                             │
│    - Lack of visibility downstream                           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 5. SOFTWARE SUPPLY CHAIN                                     │
│    - Compromised updates                                     │
│    - Malicious dependencies                                  │
│    - Open-source vulnerabilities                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 6. HARDWARE SUPPLY CHAIN                                     │
│    - Counterfeit equipment                                   │
│    - Pre-installed malware                                   │
│    - Firmware backdoors                                      │
└─────────────────────────────────────────────────────────────┘
```

## 3.2 Vendor Risk Scoring Model

### Risk Factors (Weighted):
| Factor | Weight | Assessment Criteria |
|--------|--------|---------------------|
| **Data Access Level** | 25% | Volume and sensitivity of data accessed |
| **Network Access Scope** | 20% | OT vs IT, segment access |
| **Security Maturity** | 20% | Certifications, audits, policies |
| **Financial Stability** | 15% | Credit rating, market position |
| **Geopolitical Risk** | 10% | Country of origin, sanctions |
| **Incident History** | 10% | Past breaches, response quality |

### Risk Levels:
| Score | Risk Level | Action Required |
|-------|------------|-----------------|
| 0-30 | Low | Annual review |
| 31-60 | Medium | Quarterly review |
| 61-80 | High | Monthly review + compensating controls |
| 81-100 | Critical | Continuous monitoring + executive reporting |

---

# PART 4: STRATEGIC VENDOR SECURITY SOLUTIONS

## 4.1 Vendor Risk Management Platform

### Core Capabilities:
```python
vendor_risk_platform = {
    "discovery": {
        "automatic_vendor_identification": True,
        "shadow_it_detection": True,
        "subcontractor_mapping": True
    },
    "assessment": {
        "security_questionnaires": "automated",
        "external_scanning": "continuous",
        "certification_tracking": "real_time",
        "financial_monitoring": "integrated"
    },
    "monitoring": {
        "dark_web_monitoring": True,
        "breach_notification": "immediate",
        "behavioral_analytics": True,
        "threat_intelligence": "integrated"
    },
    "response": {
        "automated_alerts": True,
        "access_revocation": "one_click",
        "forensic_collection": "automated",
        "anpd_reporting": "integrated"
    }
}
```

### Key Features for Petrobras:

#### 1. **Continuous Vendor Monitoring**
- Real-time security score updates
- Dark web exposure monitoring
- Credential compromise detection
- Open port and service scanning

#### 2. **Access Governance**
- Just-in-time (JIT) vendor access
- Time-limited credentials
- Session recording and monitoring
- Automated access revocation

#### 3. **Data Loss Prevention**
- Vendor DLP policies
- Data classification and tagging
- Anomalous download detection
- USB/removable media control

#### 4. **Third-Party Risk Intelligence**
- Vendor breach notifications
- Subcontractor risk cascade
- Geopolitical risk alerts
- Regulatory compliance tracking

## 4.2 Technical Implementation

### Architecture:
```
┌─────────────────────────────────────────────────────────────┐
│              VENDOR RISK MANAGEMENT PLATFORM                │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   External   │  │   Internal   │  │  Third-Party │      │
│  │   Scanning   │  │   Systems    │  │ Intelligence │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         └──────────────────┼──────────────────┘             │
│                            ▼                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              RISK ANALYSIS ENGINE                     │  │
│  │  - Scoring algorithms                                 │  │
│  │  - Anomaly detection                                  │  │
│  │  - Predictive analytics                               │  │
│  └──────────────────────┬───────────────────────────────┘  │
│                         ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           VISUALIZATION & RESPONSE                    │  │
│  │  - Risk dashboards                                     │  │
│  │  - Alert management                                    │  │
│  │  - Automated remediation                               │  │
│  │  - ANPD reporting                                      │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Integration Points:
- **Petronect:** Vendor onboarding integration
- **SAP/ERP:** Financial data integration
- **Active Directory:** Identity management
- **SIEM:** Security event correlation
- **ANP:** Regulatory reporting

## 4.3 ROI Calculation for Petrobras

### Cost of Vendor Breach (SA Exploration case):
| Cost Category | Estimate |
|--------------|----------|
| Data recovery and forensics | R$ 5-10M |
| Regulatory fines (ANPD) | R$ 10-50M |
| Reputational damage | Incalculable |
| Operational disruption | R$ 20-50M |
| **Total Potential Cost** | **R$ 35M-110M+** |

### Solution Investment:
| Component | Annual Cost |
|-----------|-------------|
| Platform license | R$ 2-5M |
| Implementation | R$ 3-5M (one-time) |
| Operations | R$ 1-2M/year |
| **Total (3 years)** | **R$ 10-20M** |

### ROI:
- **Break-even:** Preventing 1 major breach every 3 years
- **Conservative ROI:** 200-500% over 3 years
- **Risk reduction:** 80%+ reduction in vendor-related incidents

---

# PART 5: HACKATHON SOLUTION FRAMEWORK

## 5.1 Problem Statement Template

```markdown
**Problem:** Petrobras' vendor ecosystem of 10,000+ suppliers creates
an unmanageable attack surface. The November 2025 SA Exploration breach
exposed seismic research data through a compromised vendor, demonstrating
the critical need for continuous vendor risk monitoring.

**Current State:**
- Manual vendor assessments (annual)
- No real-time monitoring
- No automated breach detection
- Reactive incident response

**Impact:**
- 90GB of confidential data exfiltrated
- Strategic exploration data compromised
- Regulatory scrutiny from ANPD
- Reputational damage
```

## 5.2 Solution Components for Hackathon

### MVP Scope (72-hour sprint):

#### **Component 1: Vendor Discovery**
- Import vendor list from CSV/ERP
- Automatic enrichment (website, social media)
- Basic risk scoring

#### **Component 2: External Monitoring**
- Open port scanning
- SSL certificate monitoring
- Dark web credential monitoring
- Breach notification tracking

#### **Component 3: Risk Dashboard**
- Vendor risk score visualization
- Alert management
- Risk trend analysis
- PDF reporting

#### **Component 4: Integration Demo**
- Mock Petrobras ERP integration
- Sample ANPD report generation
- Automated email alerts

## 5.3 Technical Stack Recommendation

| Component | Technology | Justification |
|-----------|------------|---------------|
| **Frontend** | React + Tailwind | Fast prototyping, responsive |
| **Backend** | Python/FastAPI | Async scanning, ML ready |
| **Database** | PostgreSQL + TimescaleDB | Time-series risk data |
| **Scanning** | Nmap (Python) + APIs | Proven security tools |
| **Queue** | Redis + Celery | Async task processing |
| **Visualization** | Chart.js / D3.js | Interactive dashboards |
| **Reports** | WeasyPrint | PDF generation |

## 5.4 Demo Scenarios

### Scenario 1: New Vendor Onboarding
```
1. User adds vendor "Test Engineering Ltda"
2. System automatically enriches data
3. External scan reveals open RDP port
4. Risk score calculated: 75 (HIGH)
5. Alert generated for security team
```

### Scenario 2: Breach Detection
```
1. Dark web monitoring detects vendor credentials
2. System automatically cross-references with Petrobras vendor list
3. Match found: "SA Exploration"
4. Immediate alert with recommended actions
5. One-click access revocation
```

### Scenario 3: Executive Reporting
```
1. Dashboard shows vendor risk distribution
2. Drill-down to high-risk vendors
3. Trend analysis (risk improving/declining)
4. One-click ANPD compliance report
5. Export to PDF for board presentation
```

---

# PART 6: VENDOR-SPECIFIC INTELLIGENCE

## 6.1 High-Risk Vendor Profiles

### **SA Exploration (Post-Breach)**
- **Status:** Confirmed compromised
- **Services:** Seismic data acquisition
- **Access Level:** HIGH (seismic data)
- **Post-Breach Actions:** Enhanced monitoring required
- **Lesson:** Seismic contractors need highest security tier

### **Oceânica Engenharia**
- **Contract:** R$ 4.2B (US$736M) through 2031
- **Services:** Subsea vessels, ROV operations
- **Risk Factors:** 
  - Real-time data connectivity to offshore units
  - Multiple vessel operations
  - International partnerships
- **Mitigation:** Vessel network isolation, strict access controls

### **OceanPact**
- **Contract:** R$ 3.2B (vessel acquisition + services)
- **Services:** Offshore support vessels
- **Recent:** Merged with CBO (2nd largest Brazilian fleet)
- **Risk Factors:**
  - Largest OSV fleet in Brazil
  - Critical logistics provider
  - Merger integration risks
- **Mitigation:** Fleet-wide security standardization

## 6.2 Emerging Vendor Risks

### **AI/ML Service Providers**
- New vendors for Libra Rocks project
- Access to geological data
- Model training data exposure risks
- **Recommendation:** Data anonymization, secure enclaves

### **Cloud Migration Partners**
- Petrobras' digital transformation
- Multi-cloud strategy
- Data sovereignty concerns
- **Recommendation:** Brazilian cloud regions, encryption

---

# PART 7: REGULATORY COMPLIANCE

## 7.1 ANP Requirements

### **Resolution 882/2022:**
- Incident reporting to ANP
- Investigation report submission
- Security measures documentation

### **Vendor-Specific Requirements:**
- Vendor security clauses in contracts
- Periodic security assessments
- Incident notification obligations

## 7.2 LGPD Implications

### **Vendor as Data Processor:**
- Data Processing Agreements (DPA) required
- International transfer mechanisms (if applicable)
- Subcontractor liability

### **Breach Notification:**
- 3 business days to ANPD
- Data subject notification
- Vendor breach cascade reporting

---

# APPENDIX: VENDOR SECURITY ASSESSMENT CHECKLIST

## Pre-Contract Assessment
- [ ] Security policies review
- [ ] Incident history check
- [ ] Financial stability verification
- [ ] Reference checks
- [ ] Compliance certifications (ISO 27001, etc.)
- [ ] Data handling procedures
- [ ] Subcontractor management
- [ ] Insurance coverage

## Ongoing Monitoring
- [ ] Quarterly security reviews
- [ ] Annual penetration testing
- [ ] Continuous external monitoring
- [ ] Dark web monitoring
- [ ] Financial health checks
- [ ] Regulatory compliance updates

## Incident Response
- [ ] 24/7 contact information
- [ ] Incident notification SLA
- [ ] Forensic cooperation agreement
- [ ] Business continuity plans
- [ ] Data recovery procedures

---

*Document Classification: OSINT - Open Source Intelligence*  
*Compiled: April 2026*  
*For: Grand Prix SENAI 2026 Preparation*
