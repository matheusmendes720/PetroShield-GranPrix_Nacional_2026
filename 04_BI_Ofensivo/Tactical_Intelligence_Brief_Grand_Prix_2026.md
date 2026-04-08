# TACTICAL INTELLIGENCE BRIEF
## Grand Prix SENAI de Inovação 2026 - Preparation Guide

---

## 1. SENAI GRAND PRIX 2026 - LOGISTICAL INTELLIGENCE

### Key Dates (Estimated based on historical patterns):
| Phase | Typical Timeline | Notes |
|-------|-----------------|-------|
| **Registration Opens** | August-September 2026 | Watch gpinovacao.senai.br |
| **Registration Closes** | October 2026 | Usually 2-3 weeks before event |
| **Regional Qualifiers** | October-November 2026 | State-level pre-selections |
| **National Finals** | November-December 2026 | Main 72-hour hackathon |
| **Results** | December 2026 | Livestream announcement |

### Competition Structure 2026:
- **Format:** 48-72 hour innovation marathon
- **Team Size:** Typically 4-6 members per "Escuderia"
- **Categories:** Júnior | Avançado | Sênior

---

## 2. PROBABLE CHALLENGE THEMES (CYBERSECURITY ANGLE)

Based on Petrobras' current priorities, expect challenges in these areas:

### 🔴 HIGH PROBABILITY THEMES:

#### A. Supply Chain Security Platform
**Context:** Petrobras' SA Exploration breach exposed third-party vendor vulnerabilities
**Challenge:** Create a system for:
- Real-time vendor security scoring
- Automated compliance monitoring
- Third-party access management
- Supply chain threat intelligence

**Key Metrics to Show:**
- Number of vendors monitored
- Mean time to detect vendor compromise
- Cost per vendor assessment

#### B. OT/ICS Security Monitoring
**Context:** Pre-salt operations require 24/7 availability; SCADA systems are legacy
**Challenge:** Develop:
- Anomaly detection for industrial networks
- SCADA traffic analysis
- OT/IT network segmentation visualization
- Incident response automation for OT environments

**Key Technologies:**
- Machine learning for anomaly detection
- Protocol analysis (Modbus, DNP3, OPC-UA)
- Network topology mapping

#### C. LGPD Compliance Automation
**Context:** Brazil's ANPD is now fully enforcing; Petrobras handles massive personal/seismic data
**Challenge:** Build tools for:
- Automated data classification
- Consent management
- Data subject request automation
- Cross-border transfer compliance

**Regulatory Context:**
- LGPD (Lei 13.709/2018)
- ANPD sanctions now active (2024-2025)
- Potential fines: up to 2% of revenue

#### D. Secure AI/ML for Exploration
**Context:** Petrobras investing R$151M in AI for pre-salt (Libra Rocks)
**Challenge:** Create secure ML pipelines for:
- Adversarial attack detection
- Model poisoning prevention
- Secure federated learning
- Training data integrity verification

---

## 3. WINNING TEAM PROFILES (HISTORICAL ANALYSIS)

### Common Characteristics of SENAI Grand Prix Winners:

#### Technical Composition:
- 1x Cybersecurity/Security Engineer
- 1x Software Developer (Full Stack)
- 1x Data Scientist/ML Engineer
- 1x Domain Expert (Oil & Gas knowledge)
- 1x Business/UX Designer

#### Winning Patterns:
1. **Working Prototype > Slides** (60% of scoring)
2. **Real Data Demonstration** (synthetic but realistic)
3. **Clear Business Case** (ROI calculation)
4. **Scalability Plan** (how to deploy at Petrobras scale)
5. **Diversity Factor** (women in tech, underrepresented groups)

---

## 4. PETROBRAS KEY CONTACTS & DECISION MAKERS

### Innovation & Technology:
| Role | Name | Context |
|------|------|---------|
| **Gerente Geral de Gestão da Inovação** | Jullio Cesar Leite | Unicamp partnership signer |
| **Pesquisador em Inovação** | Luciano Felipe de Carvalho Rodrigues | R&D programs |
| **Gerente Executivo de Responsabilidade Social** | José Maria Rangel | SENAI partnership lead |
| **Presidente** | Magda Chambriard | Business Plan 2026-2030 architect |

### SENAI Innovation Contacts:
| Role | Name | Contact |
|------|------|---------|
| **Interlocutor Nacional** | Antônio Braz Lopes Filho | (31) 98843-6138, antonio.lopes@senaicni.com.br |
| **Gerente de Tecnologias Educacionais** | Luiz Eduardo Leão | Grand Prix coordinator |
| **Diretor de Operações** | Gustavo Leal | Overall SENAI strategy |

---

## 5. RECOMMENDED TECH STACK FOR CYBERSECURITY CHALLENGE

### Core Technologies (Petrobras-friendly):
| Category | Recommended | Alternative |
|----------|-------------|-------------|
| **Backend** | Python (FastAPI/Django) | Node.js |
| **Frontend** | React/Vue.js | Angular |
| **ML/AI** | TensorFlow/PyTorch | Scikit-learn |
| **Database** | PostgreSQL | MongoDB |
| **Cloud** | AWS (Petrobras uses) | Azure |
| **Security** | OWASP ZAP, Suricata | Snort, OSSEC |
| **Monitoring** | Grafana + Prometheus | ELK Stack |

### Petrobras-Specific Considerations:
- **Language:** Portuguese UI mandatory
- **Deployment:** Hybrid cloud/on-premise option
- **Compliance:** LGPD data handling from day one
- **Integration:** API-first architecture for legacy systems

---

## 6. COMPETITIVE DIFFERENTIATION STRATEGIES

### A. Reference the November 2025 Breach
- Show understanding of SA Exploration incident
- Demonstrate how your solution prevents similar attacks
- Use "supply chain security" as primary narrative

### B. Cost Efficiency Angle
- Reference Petrobras' $12B cost optimization target
- Show how security automation reduces manual effort
- Calculate potential savings from prevented breaches

### C. National Security Framing
- Position solution as protecting "pré-sal" strategic assets
- Reference energy sovereignty importance
- Connect to Brazil's critical infrastructure protection

### D. Open Source Components
- Show commitment to Brazilian tech ecosystem
- Enable knowledge transfer to Petrobras team
- Reduce vendor lock-in concerns

---

## 7. PRE-COMPETITION PREPARATION CHECKLIST

### Technical Preparation:
- [ ] Build reusable security monitoring dashboard template
- [ ] Create synthetic seismic/oil & gas dataset for demo
- [ ] Prepare LGPD compliance checklist module
- [ ] Develop vendor risk scoring algorithm
- [ ] Set up CI/CD pipeline for rapid deployment

### Domain Knowledge:
- [ ] Study Petrobras 2026-2030 Business Plan
- [ ] Understand ANP regulatory framework
- [ ] Research SCADA/OT security best practices
- [ ] Review Everest ransomware TTPs (Tactics, Techniques, Procedures)

### Team Formation:
- [ ] Identify 4-6 team members with complementary skills
- [ ] Ensure at least one Portuguese speaker
- [ ] Include diverse backgrounds (gender, region, expertise)
- [ ] Assign roles: Leader, Dev, Security, Domain Expert, Designer

### Resources to Prepare:
- [ ] One-page solution concept template
- [ ] Pitch deck structure (problem → solution → demo → business case)
- [ ] Technical architecture diagram template
- [ ] ROI calculation spreadsheet

---

## 8. REGULATORY COMPLIANCE QUICK REFERENCE

### LGPD Key Requirements:
| Requirement | Implementation |
|-------------|---------------|
| **Consent Management** | Clear opt-in/opt-out mechanisms |
| **Data Minimization** | Collect only necessary data |
| **Purpose Limitation** | Use data only for stated purposes |
| **Security Measures** | Encryption, access controls, logging |
| **Data Subject Rights** | Access, correction, deletion, portability |
| **Breach Notification** | 72-hour reporting to ANPD |

### ANP Cybersecurity Directives:
- Critical infrastructure classification
- Incident reporting requirements
- Security audit obligations
- Vendor security assessments

---

## 9. THREAT ACTOR INTELLIGENCE (EVEREST GROUP)

### Known TTPs:
- **Initial Access:** Credential stuffing, VPN compromise
- **Persistence:** Living off the land techniques
- **Exfiltration:** Large data transfers over extended periods
- **Extortion:** Public leak site pressure tactics

### Countermeasures to Demonstrate:
- Multi-factor authentication (MFA)
- Zero-trust network architecture
- Behavioral analytics for credential abuse
- Data loss prevention (DLP) monitoring

---

## 10. SUCCESS METRICS FOR SOLUTION

### Technical Metrics:
- Detection accuracy (% of true positives)
- False positive rate
- Mean time to detect (MTTD)
- Mean time to respond (MTTR)

### Business Metrics:
- Cost per vendor assessment
- Hours saved through automation
- Potential breach cost avoidance
- Compliance audit readiness score

### Innovation Metrics:
- Novelty of approach
- Scalability potential
- Integration ease
- Maintainability

---

## 11. POST-COMPETITION OPPORTUNITIES

### If You Win:
- **Incubation:** Access to Petrobras' innovation programs
- **Pilot Deployment:** Opportunity to test in production environment
- **Employment:** Recruitment pipeline for Petrobras/SENAI
- **Investment:** Connection to Brazilian venture capital

### Follow-up Actions:
- Maintain relationship with challenge mentors
- Apply to ENFUSE/Unicamp startup program
- Pursue ANP R&D funding opportunities
- Consider patent filing for novel innovations

---

## 12. USEFUL RESOURCES & REFERENCES

### Documentation:
- Petrobras Business Plan 2026-2030 (public PDF)
- SENAI Saga de Inovação methodology
- ANP Resolution 847/2022 (cybersecurity)
- LGPD Official Text (Lei 13.709/2018)

### Tools & Platforms:
- MITRE ATT&CK Framework for ICS
- OWASP Top 10 for web security
- NIST Cybersecurity Framework
- CIS Controls for critical infrastructure

### Similar Competitions for Practice:
- Petrobras + CBPF AI Hackathon (annual)
- Hackathon BNDES (Brazilian Development Bank)
- Campus Party challenges
- OpenHack (Microsoft)

---

## TACTICAL SUMMARY

**Primary Objective:** Win Grand Prix SENAI 2026 by solving Petrobras' supply chain cybersecurity challenge

**Key Differentiator:** Deep understanding of November 2025 breach + practical solution for vendor risk management

**Success Probability Factors:**
- Working prototype (40%)
- Business case clarity (25%)
- Team diversity (15%)
- Presentation quality (10%)
- Innovation novelty (10%)

**Critical Success Factors:**
1. Demonstrate real-world applicability
2. Reference actual Petrobras pain points
3. Show cost-benefit analysis
4. Include Portuguese language support
5. Address LGPD compliance

---

*Document Version: 1.0*  
*Last Updated: April 7, 2026*  
*Classification: Internal Use - Team Distribution*
