# TECHNICAL DEEP DIVE
## SCADA Protocols, LGPD Implementation & MITRE ATT&CK for ICS
### Pre-Contest Technical Preparation Guide

---

# PART 1: SCADA/OT PROTOCOLS IN-DEPTH

## 1.1 Critical Protocols for Oil & Gas Operations

### **MODBUS (TCP/RTU)**

**Overview:**
- Created: 1979 by Modicon
- Port: TCP 502 (Modbus TCP)
- Usage: Most widely deployed industrial protocol globally

**Security Issues:**
```
1. NO AUTHENTICATION - Any host can connect
2. NO ENCRYPTION - Plaintext communication
3. NO SESSION MANAGEMENT - No concept of sessions
4. COMMAND REPLAY ATTACKS - Commands can be replayed
5. FUNCTION CODE ABUSE - 127 function codes, most unused
```

**Common Attacks:**
| Attack Type | Description | Impact |
|-------------|-------------|--------|
| **Function Code 8** | Diagnostics abuse | System reconnaissance |
| **Function Code 43** | Encapsulated transport | Malicious payload delivery |
| **Force Coil (FC 5)** | Write single coil | Unauthorized control actions |
| **Preset Registers (FC 16)** | Write multiple registers | Mass configuration changes |
| **Man-in-the-Middle** | Traffic interception | Data exfiltration, command injection |

**Petrobras-Specific Context:**
- Likely used in: Wellhead controllers, pump stations, tank level monitoring
- Risk: Pre-salt offshore platforms use Modbus for sensor networks
- Recent malware: FrostyGoop used Modbus to manipulate industrial devices

**Defensive Measures:**
1. Protocol whitelisting (allow only specific function codes)
2. Network segmentation (dedicated control VLANs)
3. Deep packet inspection (DPI) for Modbus traffic
4. Read-only mode for non-control systems
5. Register address range restrictions

---

### **DNP3 (Distributed Network Protocol 3)**

**Overview:**
- Created: 1993 for electric utilities, now widely adopted
- Port: TCP 20000
- Usage: Power utilities, water systems, oil & gas pipelines

**Key Features:**
- Unsolicited responses (outstations can initiate communication)
- Time synchronization
- Secure DNP3 variant (but often not implemented)

**Security Vulnerabilities:**
```
1. CLEARTEXT BY DEFAULT - No encryption in legacy deployments
2. WEAK AUTHENTICATION - Often disabled or using default keys
3. UNSOLICITED RESPONSES - Can be spoofed
4. TIME SYNC MANIPULATION - Attackers can skew timestamps
5. BROADCAST ABUSE - Broadcast messages can disrupt operations
```

**Attack Vectors:**
| Technique | MITRE ATT&CK ID | Description |
|-----------|-----------------|-------------|
| Spoofing | T0851 | Impersonate master/outstation |
| Replay | T0857 | Replay valid commands |
| Time Manipulation | T0839 | Disturb synchronization |
| Cold Restart | T0855 | Force device restart |

**Defensive Controls:**
1. Deploy Secure DNP3 with authentication
2. Strict key management procedures
3. Monitor for unexpected unsolicited responses
4. Time sync validation against GPS/NTP
5. Master-to-RTU link isolation

---

### **OPC UA (Unified Architecture)**

**Overview:**
- Successor to OPC Classic (DCOM-based)
- Built-in security features (but often misconfigured)
- Modern standard for industrial interoperability

**Security Modes:**
| Mode | Security Level | Risk |
|------|---------------|------|
| **None** | No encryption/signing | CRITICAL |
| **Sign** | Digital signatures only | MEDIUM |
| **SignAndEncrypt** | Full security | LOW |

**Common Misconfigurations:**
1. Security mode set to "None"
2. Anonymous endpoints enabled
3. Self-signed certificates (no PKI)
4. Weak certificate validation
5. Exposed discovery endpoints

**Petrobras Context:**
- Likely used in: Digital twins, historian systems, HMI integration
- Recent: R$151M Libra Rocks project likely uses OPC UA for data integration
- Risk: AI/ML pipelines may use OPC UA for data ingestion

**Security Recommendations:**
1. Enforce SignAndEncrypt mode
2. Disable anonymous access
3. Implement certificate PKI
4. Endpoint access restrictions
5. Regular certificate rotation

---

### **IEC 61850**

**Overview:**
- Power utility communication standard
- Components: GOOSE (Generic Object Oriented Substation Events), MMS, SV
- Usage: Substation automation, smart grids

**Security Challenges:**
- GOOSE messages use multicast (can flood network)
- Time-sensitive (hard to add crypto overhead)
- Many implementations lack security configurations

**Attacks:**
- GOOSE spoofing (trip circuit breakers)
- MMS manipulation (modify settings)
- Denial of service via multicast flooding

---

## 1.2 Brazilian-Specific Considerations

### **ScadaBR**
- Open-source SCADA platform widely used in Brazil
- **CRITICAL:** CISA added CVE-2021-26829 to KEV catalog (Dec 2025)
- Vulnerability: XSS allowing remote code execution
- **Action:** Check if Petrobras or vendors use ScadaBR

### **Protocol Prevalence in Brazil Energy Sector:**
| Protocol | Usage % | Security Maturity |
|----------|---------|-------------------|
| Modbus | 70% | Low |
| DNP3 | 15% | Medium |
| OPC UA | 10% | High (when configured) |
| Proprietary | 5% | Unknown |

---

# PART 2: LGPD - TECHNICAL IMPLEMENTATION

## 2.1 Core Technical Requirements

### **Data Mapping & Inventory (Article 37)**
```python
# Example data structure for LGPD compliance
lgpd_record = {
    "processing_activity": "Employee Payroll",
    "data_categories": ["CPF", "RG", "bank_account", "salary"],
    "data_subjects": "Employees",
    "legal_basis": "Legal Obligation (Art 7, II)",
    "retention_period": "5 years after termination",
    "recipients": ["Payroll_system", "Tax_authority"],
    "security_measures": ["Encryption", "Access_control", "Audit_logs"],
    "international_transfer": False,
    "dpo_contact": "encarregado@company.com"
}
```

### **Breach Notification (Resolution 15/2024)**
- **Deadline:** 3 business days to ANPD
- **Content Requirements:**
  1. Description of incident
  2. Data categories affected
  3. Number of data subjects
  4. Technical measures taken
  5. Contact information

**Technical Implementation:**
```python
def detect_breach(anomaly_score, data_classification):
    """
    Auto-detection system for LGPD breach notification
    """
    if anomaly_score > 0.8 and data_classification in ['sensitive', 'high_volume']:
        trigger_notification()
        generate_report()
        notify_dpo()
        
def trigger_notification():
    # 3-business-day countdown starts
    notification_deadline = business_days_from_now(3)
    create_anpd_report()
    notify_affected_subjects()
```

### **International Data Transfers (Resolution 19/2024)**

**SCC Requirements:**
- Controller-to-Controller SCCs
- Controller-to-Processor SCCs
- Must be in Portuguese
- ANPD-specific clauses required

**Technical Controls:**
1. Data residency enforcement (geo-fencing)
2. Encryption in transit (TLS 1.3)
3. Access logging for cross-border flows
4. Automated SCC compliance checking

---

## 2.2 LGPD vs GDPR - Technical Differences

| Aspect | LGPD | GDPR | Technical Impact |
|--------|------|------|------------------|
| **DPO Required** | All controllers | Threshold-based | Must appoint Encarregado |
| **Sensitive Data Basis** | No legitimate interest | Some flexibility | Stricter consent management |
| **Breach Deadline** | 3 business days | 72 hours | Weekend/holiday handling |
| **Transfer SCCs** | ANPD-specific | EU SCCs | Separate legal frameworks |
| **Biometric Data** | Explicit consent | Context-dependent | Strict deletion policies |

---

## 2.3 ANPD Enforcement (2024-2026)

**Recent Sanctions:**
- First fine: Telekall Infoservice (BRL 14,400) - 2023
- Trend: Graduated enforcement, higher fines expected for large companies

**Technical Compliance Priorities:**
1. **Data Mapping** - Most common gap
2. **Legal Basis Documentation** - Required for all processing
3. **DPA with Vendors** - Article 46 requirement
4. **Breach Response** - 3-day notification procedure

---

# PART 3: MITRE ATT&CK FOR ICS

## 3.1 Framework Overview

MITRE ATT&CK for ICS is a knowledge base of adversary tactics and techniques specific to industrial control systems.

**Tactics (12):**
1. Initial Access
2. Execution
3. Persistence
4. Evasion
5. Discovery
6. Collection
7. Command and Control
8. Inhibit Response Function
9. Impair Process Control
10. Impact

## 3.2 Key Techniques for Oil & Gas

### **Initial Access**
| Technique | ID | Description | Mitigation |
|-----------|-----|-------------|------------|
| **External Remote Services** | T1133 | VPN, RDP exploitation | MFA, JIT access |
| **Internet-Accessible Device** | T0819 | Exposed PLCs, HMIs | Network segmentation |
| **Spearphishing** | T1566 | Targeted phishing | Email security |
| **Supply Chain Compromise** | T1195 | Vendor compromise | Vendor security assessments |

### **Execution**
| Technique | ID | Description | Mitigation |
|-----------|-----|-------------|------------|
| **Modify Controller Logic** | T0831 | PLC code injection | Code signing, version control |
| **Native API** | T0834 | Use native protocols | Protocol monitoring |
| **Scripting** | T0853 | PowerShell, Python | Application whitelisting |

### **Impair Process Control**
| Technique | ID | Description | Mitigation |
|-----------|-----|-------------|------------|
| **Denial of Control** | T0813 | Block control commands | Redundant control paths |
| **Manipulation of Control** | T0835 | Alter setpoints | Change detection |
| **Denial of View** | T0815 | Block monitoring | Redundant sensors |

## 3.3 Threat Groups Targeting Energy

### **XENOTIME (Dragos)**
- **Target:** Oil & gas, electric
- **Capability:** TRITON malware (safety system targeting)
- **Interest:** Physical destruction, safety system bypass

### **ELECTRUM / Sandworm**
- **Target:** Electric utilities
- **Capability:** CRASHOVERRIDE (power grid disruption)
- **Interest:** Widespread outages

### **MAGNUM TEMPUS**
- **Target:** Oil & gas
- **Capability:** Living off the land, credential theft
- **Interest:** Espionage, long-term access

## 3.4 Mapping to Petrobras Context

**Petrobras-Specific Attack Scenario:**
```
1. INITIAL ACCESS: Compromise SA Exploration (vendor) - T1195
   └─> Vendor VPN credentials stolen

2. PERSISTENCE: Valid Accounts - T1078
   └─> Maintain access via legitimate credentials

3. DISCOVERY: Network Service Scanning - T1046
   └─> Map seismic data servers

4. COLLECTION: Data from Information Repositories - T1213
   └─> Exfiltrate 90GB seismic research data

5. IMPACT: Theft of Operational Information - T0817
   └─> Publish data on dark web
```

---

# PART 4: NATIONAL CYBERSECURITY POLICY (BRAZIL)

## 4.1 Decree 12.572/2025 - National Information Security Policy

**Key Points:**
- Replaces Decree 9.637/2018
- Governs federal public administration
- Establishes GSI (Institutional Security Cabinet) as coordinator

**Technical Requirements:**
1. Information classification system
2. Risk management framework
3. Incident response procedures
4. Access control policies

## 4.2 Decree 12.573/2025 - National Cybersecurity Strategy

**Strategic Pillars:**
1. **Defense** - Protect critical infrastructure
2. **Deterrence** - Attribution and consequences
3. **Development** - Build capabilities
4. **Diplomacy** - International cooperation

## 4.3 ANP Resolution 882/2022

**Incident Reporting Requirements:**
- Operators must report security incidents
- Investigation reports required
- ANP may conduct inspections

**Technical Implications:**
- Automated incident detection
- Standardized reporting formats
- Integration with ANP systems

---

# PART 5: GEOPOLITICAL THREATS TO BRAZILIAN ENERGY

## 5.1 China-Brazil Energy Relations

**Current Status:**
- China is largest buyer of Brazilian oil
- Petrobras has partnerships with Chinese NOCs
- Technology transfer concerns

**Cyber Espionage Risk:**
- Pre-salt technology is strategic asset
- Industrial espionage targeting seismic data
- Supply chain infiltration

## 5.2 US-China Competition

**Impact on Petrobras:**
- Caught between competing powers
- Technology export restrictions
- Pressure to choose sides

**Cybersecurity Implications:**
- Increased targeting of energy infrastructure
- State-sponsored APT activity
- Critical infrastructure protection priorities

## 5.3 Venezuela Instability

**Regional Impact:**
- Refugee flows
- Border security concerns
- Potential cyber spillover

---

# PART 6: SUPPLY CHAIN VULNERABILITY ANALYSIS

## 6.1 Petrobras Vendor Ecosystem

**Major Suppliers:**
| Vendor | Service Type | Cyber Risk Level |
|--------|-------------|------------------|
| **Oceânica Engenharia** | Subsea vessels | High |
| **OceanPact** | Offshore support | High |
| **SA Exploration** | Seismic services | CRITICAL (breached) |
| **TechnipFMC** | Subsea equipment | Medium |
| **Subsea 7** | Engineering | Medium |
| **Ambipar** | Environmental | Medium |

## 6.2 Vendor Risk Factors

**High-Risk Indicators:**
1. Remote access to Petrobras networks
2. Processing of sensitive data
3. IT/OT system integration
4. Subcontractor chains (4th party risk)
5. International operations (data transfer)

**Technical Controls Needed:**
1. Vendor security assessments
2. Continuous monitoring
3. Credential lifecycle management
4. Network segmentation for vendor access
5. Data loss prevention (DLP)

---

# PART 7: PRACTICAL IMPLEMENTATION GUIDE

## 7.1 Security Architecture for Oil & Gas

### **Defense in Depth Model:**
```
┌─────────────────────────────────────────────────────────────┐
│  PERIMETER - Firewalls, IDS/IPS, VPN                        │
├─────────────────────────────────────────────────────────────┤
│  DMZ - Jump servers, proxy services                         │
├─────────────────────────────────────────────────────────────┤
│  CORPORATE IT - Business systems                            │
├─────────────────────────────────────────────────────────────┤
│  OT DMZ - Data diodes, historians                           │
├─────────────────────────────────────────────────────────────┤
│  CONTROL NETWORK - PLC, RTU, SCADA servers                  │
├─────────────────────────────────────────────────────────────┤
│  SAFETY SYSTEMS - SIS, protection relays                    │
└─────────────────────────────────────────────────────────────┘
```

## 7.2 Detection Use Cases

### **Modbus Anomaly Detection:**
```yaml
alert: Modbus_Suspicious_Function_Code
when: function_code NOT IN [1, 2, 3, 4, 5, 6, 15, 16]
severity: HIGH
action: alert_and_log

alert: Modbus_Mass_Write
when: function_code = 16 AND register_count > 10
severity: CRITICAL
action: alert_and_block

alert: Modbus_Unauthorized_Source
when: src_ip NOT IN authorized_masters
severity: HIGH
action: alert_and_block
```

### **LGPD Breach Detection:**
```yaml
alert: Large_Data_Exfiltration
when: bytes_out > 1GB AND dst_country != "Brazil"
severity: CRITICAL
action: alert_dpo_and_anpd

alert: Unauthorized_Database_Access
when: database_query_count > threshold AND user_role != "dba"
severity: HIGH
action: alert_and_investigate
```

---

# APPENDIX: QUICK REFERENCE

## Common Port Numbers
| Protocol | Port | Security Risk |
|----------|------|---------------|
| Modbus TCP | 502 | High |
| DNP3 | 20000 | High |
| OPC UA Discovery | 4840 | Medium |
| OPC UA Binary | 4840 | Medium |
| IEC 61850 MMS | 102 | High |
| EtherNet/IP | 44818 | Medium |
| Siemens S7 | 102 | High |

## LGPD Checklist
- [ ] Data mapping complete
- [ ] Legal basis documented
- [ ] DPO appointed
- [ ] Privacy notices published
- [ ] DPAs with vendors
- [ ] Breach response plan
- [ ] International transfer mechanisms
- [ ] Security measures implemented

---

*Document Version: 1.0*  
*Classification: Technical Reference*  
*For: Grand Prix SENAI 2026 Preparation*
