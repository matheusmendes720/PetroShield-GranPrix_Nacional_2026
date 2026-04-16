"""
mock_data.py — Dados Mockados Enterprise-Grade para Demonstração
================================================================
Versão expandida com datasets sintéticos extensivos para storytelling
rico em analytics, KPIs, OKRs e cenários de roadshow.

Estrutura:
  1. Registro de Dispositivos XR (xr_devices)
  2. Sessões de Autenticação (auth_sessions)
  3. Entidades Sensíveis Petrobras (sensitive_entities)
  4. Grafo de Risco de Vendors (vendor_risk_graph)
  5. Padrões de Ameaça MITRE (threat_patterns)
  6. Frota de Edge Nodes (fleet_registry)
  7. Métricas Históricas Mensais (monthly_metrics)
  8. OKRs & KPIs Baseline (okrs)
  9. Cenários de Teatro Expandidos (demo_scenarios)
 10. Base MITRE ATT&CK for ICS (knowledge_base)
 11. Agentic Workflows — Daily SOC Routines
 12. Compliance Ledger Entries
 13. Incident Knowledge Base
 14. Triple Surface Metrics
 15. Geradores de Dados Sintéticos (functions)
"""

import time
import random
import hashlib
from typing import Dict, List, Any
from datetime import datetime, timedelta


# =============================================================================
# 1. REGISTRO DE DISPOSITIVOS XR (14 dispositivos)
# =============================================================================

XR_DEVICES: Dict[str, dict] = {
    "hololens-047": {
        "device_id": "hololens-047",
        "device_type": "HoloLens2",
        "asset_tag": "PETRO-XR-2047-047",
        "assigned_operator_id": "OP-33891",
        "assigned_vendor_id": "OCEANICA_ENG",
        "mdm_enrollment_status": "kiosk",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P93",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "24.11.1340",
        "last_seen": (datetime.utcnow() - timedelta(minutes=5)).isoformat(),
    },
    "hololens-048": {
        "device_id": "hololens-048",
        "device_type": "HoloLens2",
        "asset_tag": "PETRO-XR-2047-048",
        "assigned_operator_id": "OP-33892",
        "assigned_vendor_id": "TECHNIP_FMC",
        "mdm_enrollment_status": "kiosk",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P93",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "24.11.1340",
        "last_seen": (datetime.utcnow() - timedelta(minutes=12)).isoformat(),
    },
    "quest-vr-001": {
        "device_id": "quest-vr-001",
        "device_type": "MetaQuest3",
        "asset_tag": None,
        "assigned_operator_id": None,
        "assigned_vendor_id": None,
        "mdm_enrollment_status": "compromised",
        "kiosk_mode_enabled": False,
        "facility_zone": "Unknown",
        "network_segment": "Vendor_VPN",
        "encryption_status": "unencrypted",
        "remote_wipe_capable": False,
        "geofence_locked": False,
        "firmware_version": "unknown",
        "last_seen": (datetime.utcnow() - timedelta(hours=2)).isoformat(),
    },
    "quest-vr-002": {
        "device_id": "quest-vr-002",
        "device_type": "MetaQuest3",
        "asset_tag": "PETRO-XR-2047-201",
        "assigned_operator_id": "OP-44150",
        "assigned_vendor_id": "OCEANICA_ENG",
        "mdm_enrollment_status": "kiosk",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P93",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "72.11.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=8)).isoformat(),
    },
    "realwear-102": {
        "device_id": "realwear-102",
        "device_type": "RealWear",
        "asset_tag": "PETRO-XR-2047-102",
        "assigned_operator_id": "OP-44102",
        "assigned_vendor_id": "OCEANICA_ENG",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P93",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": True,
        "firmware_version": "15.2.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=3)).isoformat(),
    },
    "realwear-103": {
        "device_id": "realwear-103",
        "device_type": "RealWear",
        "asset_tag": "PETRO-XR-2047-103",
        "assigned_operator_id": "OP-44103",
        "assigned_vendor_id": "SUBSEA_7",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P68",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": True,
        "firmware_version": "15.2.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=20)).isoformat(),
    },
    "magicleap-205": {
        "device_id": "magicleap-205",
        "device_type": "MagicLeap2",
        "asset_tag": "PETRO-XR-2047-205",
        "assigned_operator_id": "OP-55203",
        "assigned_vendor_id": None,
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "Refinaria_REPLAN",
        "network_segment": "IT_Corporate",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": True,
        "firmware_version": "1.5.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=45)).isoformat(),
    },
    "vuzix-m401": {
        "device_id": "vuzix-m401",
        "device_type": "VuzixM400",
        "asset_tag": "PETRO-XR-2047-301",
        "assigned_operator_id": "OP-66101",
        "assigned_vendor_id": "OCEANPACT_SERVICOS",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "Base_Camacari",
        "network_segment": "IT_Corporate",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "3.2.1",
        "last_seen": (datetime.utcnow() - timedelta(minutes=15)).isoformat(),
    },
    "vuzix-m402": {
        "device_id": "vuzix-m402",
        "device_type": "VuzixM400",
        "asset_tag": "PETRO-XR-2047-302",
        "assigned_operator_id": "OP-66102",
        "assigned_vendor_id": "SCHLUMBERGER_BR",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "Base_Rio_Centro",
        "network_segment": "IT_Corporate",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "3.2.1",
        "last_seen": (datetime.utcnow() - timedelta(minutes=33)).isoformat(),
    },
    "quest-vr-005": {
        "device_id": "quest-vr-005",
        "device_type": "MetaQuest3",
        "asset_tag": "PETRO-XR-2047-205",
        "assigned_operator_id": "OP-44200",
        "assigned_vendor_id": "HALLIBURTON_BR",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P68",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "72.11.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=7)).isoformat(),
    },
    "quest-vr-006": {
        "device_id": "quest-vr-006",
        "device_type": "MetaQuest3",
        "asset_tag": "PETRO-XR-2047-206",
        "assigned_operator_id": "OP-44201",
        "assigned_vendor_id": "OCEANICA_ENG",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P93",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "72.11.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=9)).isoformat(),
    },
    "quest-vr-007": {
        "device_id": "quest-vr-007",
        "device_type": "MetaQuest3",
        "asset_tag": "PETRO-XR-2047-207",
        "assigned_operator_id": "OP-44202",
        "assigned_vendor_id": "SA_EXPLORATION",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "Navio_Sismico_Alpha",
        "network_segment": "Vendor_VPN",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": True,
        "firmware_version": "72.11.0",
        "last_seen": (datetime.utcnow() - timedelta(days=5)).isoformat(),
    },
    "hololens-050": {
        "device_id": "hololens-050",
        "device_type": "HoloLens2",
        "asset_tag": "PETRO-XR-2047-050",
        "assigned_operator_id": "OP-33900",
        "assigned_vendor_id": "OCEANICA_ENG",
        "mdm_enrollment_status": "kiosk",
        "kiosk_mode_enabled": True,
        "facility_zone": "FPSO_P93",
        "network_segment": "OT_Isolated",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": False,
        "firmware_version": "24.11.1340",
        "last_seen": (datetime.utcnow() - timedelta(minutes=2)).isoformat(),
    },
    "realwear-105": {
        "device_id": "realwear-105",
        "device_type": "RealWear",
        "asset_tag": "PETRO-XR-2047-105",
        "assigned_operator_id": "OP-44105",
        "assigned_vendor_id": "OCEANPACT_SERVICOS",
        "mdm_enrollment_status": "enrolled",
        "kiosk_mode_enabled": True,
        "facility_zone": "Base_Rio_Centro",
        "network_segment": "IT_Corporate",
        "encryption_status": "AES-256",
        "remote_wipe_capable": True,
        "geofence_locked": True,
        "firmware_version": "15.2.0",
        "last_seen": (datetime.utcnow() - timedelta(minutes=18)).isoformat(),
    },
}


# =============================================================================
# 2. SESSÕES DE AUTENTICAÇÃO
# =============================================================================

AUTH_SESSIONS: Dict[str, dict] = {
    "jwt_token_xr_session_9942": {
        "session_id": "sess-xr-9942-p93",
        "device_id": "hololens-047",
        "operator_id": "OP-33891",
        "vendor_id": "OCEANICA_ENG",
        "auth_method": "oauth_device_flow",
        "smartphone_approval_status": "approved",
        "geo_risk_score": 0.12,
        "mfa_verified": True,
        "expires_at": "2026-04-16T02:00:00Z",
        "revoked": False,
        "revoked_reason": None,
    },
    "jwt_token_xr_session_9943": {
        "session_id": "sess-xr-9943-p93",
        "device_id": "hololens-048",
        "operator_id": "OP-33892",
        "vendor_id": "TECHNIP_FMC",
        "auth_method": "oauth_device_flow",
        "smartphone_approval_status": "approved",
        "geo_risk_score": 0.15,
        "mfa_verified": True,
        "expires_at": "2026-04-16T03:00:00Z",
        "revoked": False,
        "revoked_reason": None,
    },
    "jwt_token_xr_session_9950": {
        "session_id": "sess-xr-9950-cam",
        "device_id": "vuzix-m401",
        "operator_id": "OP-66101",
        "vendor_id": "OCEANPACT_SERVICOS",
        "auth_method": "oauth_device_flow",
        "smartphone_approval_status": "approved",
        "geo_risk_score": 0.08,
        "mfa_verified": True,
        "expires_at": "2026-04-16T04:00:00Z",
        "revoked": False,
        "revoked_reason": None,
    },
}


# =============================================================================
# 3. GRAFO DE RISCO DE VENDORS (8 vendors)
# =============================================================================

VENDOR_RISK_DB: Dict[str, dict] = {
    "OCEANICA_ENG": {
        "vendor_id": "OCEANICA_ENG",
        "vendor_name": "Oceânica Engenharia",
        "contract_value_brl": 4_200_000_000.00,
        "contract_end_date": "2031-12-31",
        "access_level": "OT",
        "risk_score": 62.0,
        "risk_level": "MEDIUM",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": False,
        "xr_device_count": 12,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "Subsea Vessels",
    },
    "SA_EXPLORATION": {
        "vendor_id": "SA_EXPLORATION",
        "vendor_name": "SA Exploration",
        "contract_value_brl": 150_000_000.00,
        "contract_end_date": "2027-06-30",
        "access_level": "Data",
        "risk_score": 95.0,
        "risk_level": "CRITICAL",
        "dark_web_exposure": True,
        "credential_breach_count": 1,
        "mfa_enforced": False,
        "xr_device_count": 1,
        "anpd_report_required": True,
        "auto_suspend_threshold_crossed": True,
        "related_incident_ids": ["BREACH-NOV2025-001"],
        "sector": "Seismic Surveys",
    },
    "OCEANPACT_SERVICOS": {
        "vendor_id": "OCEANPACT_SERVICOS",
        "vendor_name": "OceanPact Serviços Marítimos",
        "contract_value_brl": 800_000_000.00,
        "contract_end_date": "2029-03-15",
        "access_level": "Logistics",
        "risk_score": 35.0,
        "risk_level": "LOW",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": True,
        "xr_device_count": 4,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "OSV Fleet",
    },
    "TECHNIP_FMC": {
        "vendor_id": "TECHNIP_FMC",
        "vendor_name": "TechnipFMC Brasil",
        "contract_value_brl": 2_100_000_000.00,
        "contract_end_date": "2030-08-20",
        "access_level": "OT",
        "risk_score": 48.0,
        "risk_level": "MEDIUM",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": True,
        "xr_device_count": 6,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "Subsea Equipment",
    },
    "SUBSEA_7": {
        "vendor_id": "SUBSEA_7",
        "vendor_name": "Subsea 7 do Brasil",
        "contract_value_brl": 1_800_000_000.00,
        "contract_end_date": "2029-11-30",
        "access_level": "OT",
        "risk_score": 55.0,
        "risk_level": "MEDIUM",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": False,
        "xr_device_count": 3,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "Subsea Engineering",
    },
    "SCHLUMBERGER_BR": {
        "vendor_id": "SCHLUMBERGER_BR",
        "vendor_name": "Schlumberger Brasil",
        "contract_value_brl": 3_500_000_000.00,
        "contract_end_date": "2032-01-15",
        "access_level": "Data",
        "risk_score": 42.0,
        "risk_level": "MEDIUM",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": True,
        "xr_device_count": 8,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "Well Services",
    },
    "HALLIBURTON_BR": {
        "vendor_id": "HALLIBURTON_BR",
        "vendor_name": "Halliburton Brasil",
        "contract_value_brl": 2_900_000_000.00,
        "contract_end_date": "2031-05-22",
        "access_level": "OT",
        "risk_score": 51.0,
        "risk_level": "MEDIUM",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": True,
        "xr_device_count": 5,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "Drilling & Completion",
    },
    "PETRONECT_SI": {
        "vendor_id": "PETRONECT_SI",
        "vendor_name": "Petronect SI",
        "contract_value_brl": 45_000_000.00,
        "contract_end_date": "2026-12-31",
        "access_level": "IT",
        "risk_score": 28.0,
        "risk_level": "LOW",
        "dark_web_exposure": False,
        "credential_breach_count": 0,
        "mfa_enforced": True,
        "xr_device_count": 0,
        "anpd_report_required": False,
        "auto_suspend_threshold_crossed": False,
        "related_incident_ids": [],
        "sector": "IT Services",
    },
}


# =============================================================================
# 4. PADRÕES DE AMEAÇA MITRE ATT&CK for ICS
# =============================================================================

THREAT_PATTERNS: List[dict] = [
    {
        "pattern_id": 1,
        "pattern_name": "Unauthorized XR Device Access",
        "mitre_technique": "T1078",
        "mitre_tactic": "Persistence",
        "description": "Valid account abuse via compromised or unauthenticated XR session",
        "recommended_playbook": "block_request_401",
        "severity": "HIGH",
        "false_positive_rate": 0.02,
        "detection_count_30d": 12,
    },
    {
        "pattern_id": 2,
        "pattern_name": "OT Protocol in LLM Prompt",
        "mitre_technique": "T0831",
        "mitre_tactic": "Execution",
        "description": "Modbus/DNP3/OPC UA command detected in AI assistant query",
        "recommended_playbook": "escalate_soc_ot_alert",
        "severity": "CRITICAL",
        "false_positive_rate": 0.01,
        "detection_count_30d": 3,
    },
    {
        "pattern_id": 3,
        "pattern_name": "Vendor Credential Leak Cascade",
        "mitre_technique": "T1195",
        "mitre_tactic": "Initial Access",
        "description": "Dark web exposure of vendor credentials with active XR fleet",
        "recommended_playbook": "suspend_vendor_sessions",
        "severity": "HIGH",
        "false_positive_rate": 0.05,
        "detection_count_30d": 2,
    },
    {
        "pattern_id": 4,
        "pattern_name": "Sensitive Entity Density Spike",
        "mitre_technique": "T1213",
        "mitre_tactic": "Collection",
        "description": "Unusually high count of restricted assets in single prompt",
        "recommended_playbook": "escalate_level2_analysis",
        "severity": "MEDIUM",
        "false_positive_rate": 0.08,
        "detection_count_30d": 47,
    },
    {
        "pattern_id": 5,
        "pattern_name": "Drive-by Compromise via SMB",
        "mitre_technique": "T0817",
        "mitre_tactic": "Initial Access",
        "description": "SMB protocol exploitation for lateral movement in industrial network",
        "recommended_playbook": "isolate_subnet_block_smb",
        "severity": "CRITICAL",
        "false_positive_rate": 0.03,
        "detection_count_30d": 1,
    },
    {
        "pattern_id": 6,
        "pattern_name": "Default Credentials on Industrial Device",
        "mitre_technique": "T0812",
        "mitre_tactic": "Lateral Movement",
        "description": "Use of factory-default credentials on SCADA/PLC controllers",
        "recommended_playbook": "force_credential_rotation",
        "severity": "HIGH",
        "false_positive_rate": 0.04,
        "detection_count_30d": 5,
    },
    {
        "pattern_id": 7,
        "pattern_name": "Geofencing Violation",
        "mitre_technique": "T0866",
        "mitre_tactic": "Initial Access",
        "description": "XR device physically removed from authorized facility zone",
        "recommended_playbook": "auto_lock_remote_wipe",
        "severity": "HIGH",
        "false_positive_rate": 0.06,
        "detection_count_30d": 8,
    },
    {
        "pattern_id": 8,
        "pattern_name": "AI-Generated Phishing via XR",
        "mitre_technique": "T1566",
        "mitre_tactic": "Initial Access",
        "description": "Spearphishing content delivered through AR overlay or XR assistant",
        "recommended_playbook": "block_ar_overlay_quarantine_device",
        "severity": "MEDIUM",
        "false_positive_rate": 0.10,
        "detection_count_30d": 15,
    },
    {
        "pattern_id": 9,
        "pattern_name": "Firmware Downgrade Attack",
        "mitre_technique": "T0857",
        "mitre_tactic": "Persistence",
        "description": "Attempt to rollback device firmware to vulnerable version",
        "recommended_playbook": "block_firmware_rollback_alert_soc",
        "severity": "HIGH",
        "false_positive_rate": 0.04,
        "detection_count_30d": 4,
    },
    {
        "pattern_id": 10,
        "pattern_name": "LGPD Data Exfiltration Attempt",
        "mitre_technique": "T1213",
        "mitre_tactic": "Collection",
        "description": "Bulk transfer of personal data outside Brazilian jurisdiction",
        "recommended_playbook": "trigger_dlp_block_notify_anpd",
        "severity": "CRITICAL",
        "false_positive_rate": 0.02,
        "detection_count_30d": 6,
    },
    {
        "pattern_id": 11,
        "pattern_name": "Shadow IT Tunnel Detected",
        "mitre_technique": "T1195",
        "mitre_tactic": "Initial Access",
        "description": "Unauthorized vendor-managed tunnel bypassing SOC visibility",
        "recommended_playbook": "isolate_tunnel_alert_noc",
        "severity": "HIGH",
        "false_positive_rate": 0.07,
        "detection_count_30d": 3,
    },
    {
        "pattern_id": 12,
        "pattern_name": "Biometric Gaze Spoofing",
        "mitre_technique": "T1078",
        "mitre_tactic": "Persistence",
        "description": "Presentation attack against iris/gaze-based authentication",
        "recommended_playbook": "require_liveness_check",
        "severity": "MEDIUM",
        "false_positive_rate": 0.05,
        "detection_count_30d": 2,
    },
    {
        "pattern_id": 13,
        "pattern_name": "Off-Hours OT Access Request",
        "mitre_technique": "T0866",
        "mitre_tactic": "Initial Access",
        "description": "XR device requesting OT data outside business hours",
        "recommended_playbook": "require_reauth_manager",
        "severity": "MEDIUM",
        "false_positive_rate": 0.08,
        "detection_count_30d": 9,
    },
]


# =============================================================================
# 5. FROTA DE EDGE NODES (14 nodes)
# =============================================================================

FLEET_REGISTRY: List[dict] = [
    {"node_id": f"edge-bahia-{i:03d}", "facility": f"PME_Camaçari_{i:02d}", "region": "BAHIA", "status": "online", "ruleset_version": "v2.3.1", "vaccine_status": "up_to_date"}
    for i in range(1, 9)
] + [
    {"node_id": "edge-bahia-009", "facility": "PME_Lauro_de_Freitas_01", "region": "BAHIA", "status": "online", "ruleset_version": "v2.3.1", "vaccine_status": "up_to_date"},
    {"node_id": "edge-bahia-010", "facility": "PME_Simoes_Filho_01", "region": "BAHIA", "status": "online", "ruleset_version": "v2.3.1", "vaccine_status": "up_to_date"},
    {"node_id": "edge-rio-001", "facility": "Escritorio_RJ_Centro", "region": "RIO_DE_JANEIRO", "status": "online", "ruleset_version": "v2.3.0", "vaccine_status": "pending"},
    {"node_id": "edge-rio-002", "facility": "FPSO_P93_Gateway", "region": "RIO_DE_JANEIRO", "status": "online", "ruleset_version": "v2.3.1", "vaccine_status": "up_to_date"},
    {"node_id": "edge-sp-001", "facility": "Refinaria_REPLAN", "region": "SAO_PAULO", "status": "online", "ruleset_version": "v2.3.1", "vaccine_status": "up_to_date"},
    {"node_id": "edge-sp-002", "facility": "Refinaria_REVAP", "region": "SAO_PAULO", "status": "offline", "ruleset_version": "v2.2.9", "vaccine_status": "outdated"},
]


# =============================================================================
# 6. MÉTRICAS HISTÓRICAS MENSAIS (sintéticas — 12 meses) + granular KPIs
# =============================================================================

MONTHLY_METRICS: List[dict] = [
    {"month": "2025-05", "queries_processed": 12400, "leaks_prevented": 89, "incidents_blocked": 12, "incidents_escalated": 3, "avg_latency_ms": 42, "cost_avoided_brl": 2_100_000, "biometric_reauths": 340, "shadow_it_blocks": 2, "compliance_deadlines_met": 5},
    {"month": "2025-06", "queries_processed": 13100, "leaks_prevented": 94, "incidents_blocked": 14, "incidents_escalated": 4, "avg_latency_ms": 41, "cost_avoided_brl": 2_450_000, "biometric_reauths": 380, "shadow_it_blocks": 1, "compliance_deadlines_met": 4},
    {"month": "2025-07", "queries_processed": 12800, "leaks_prevented": 102, "incidents_blocked": 11, "incidents_escalated": 5, "avg_latency_ms": 39, "cost_avoided_brl": 2_800_000, "biometric_reauths": 410, "shadow_it_blocks": 3, "compliance_deadlines_met": 6},
    {"month": "2025-08", "queries_processed": 14200, "leaks_prevented": 110, "incidents_blocked": 18, "incidents_escalated": 6, "avg_latency_ms": 38, "cost_avoided_brl": 3_200_000, "biometric_reauths": 450, "shadow_it_blocks": 2, "compliance_deadlines_met": 5},
    {"month": "2025-09", "queries_processed": 15000, "leaks_prevented": 125, "incidents_blocked": 15, "incidents_escalated": 7, "avg_latency_ms": 37, "cost_avoided_brl": 3_650_000, "biometric_reauths": 490, "shadow_it_blocks": 4, "compliance_deadlines_met": 7},
    {"month": "2025-10", "queries_processed": 15500, "leaks_prevented": 118, "incidents_blocked": 19, "incidents_escalated": 4, "avg_latency_ms": 36, "cost_avoided_brl": 3_400_000, "biometric_reauths": 520, "shadow_it_blocks": 1, "compliance_deadlines_met": 6},
    {"month": "2025-11", "queries_processed": 14800, "leaks_prevented": 145, "incidents_blocked": 22, "incidents_escalated": 9, "avg_latency_ms": 35, "cost_avoided_brl": 4_100_000, "biometric_reauths": 580, "shadow_it_blocks": 5, "compliance_deadlines_met": 8},
    {"month": "2025-12", "queries_processed": 13200, "leaks_prevented": 98, "incidents_blocked": 10, "incidents_escalated": 2, "avg_latency_ms": 34, "cost_avoided_brl": 2_900_000, "biometric_reauths": 340, "shadow_it_blocks": 0, "compliance_deadlines_met": 4},
    {"month": "2026-01", "queries_processed": 16100, "leaks_prevented": 132, "incidents_blocked": 20, "incidents_escalated": 8, "avg_latency_ms": 33, "cost_avoided_brl": 4_500_000, "biometric_reauths": 620, "shadow_it_blocks": 3, "compliance_deadlines_met": 7},
    {"month": "2026-02", "queries_processed": 17400, "leaks_prevented": 156, "incidents_blocked": 24, "incidents_escalated": 10, "avg_latency_ms": 32, "cost_avoided_brl": 5_200_000, "biometric_reauths": 670, "shadow_it_blocks": 4, "compliance_deadlines_met": 8},
    {"month": "2026-03", "queries_processed": 18200, "leaks_prevented": 168, "incidents_blocked": 26, "incidents_escalated": 11, "avg_latency_ms": 31, "cost_avoided_brl": 5_800_000, "biometric_reauths": 710, "shadow_it_blocks": 6, "compliance_deadlines_met": 9},
    {"month": "2026-04", "queries_processed": 8900, "leaks_prevented": 87, "incidents_blocked": 13, "incidents_escalated": 5, "avg_latency_ms": 30, "cost_avoided_brl": 2_950_000, "biometric_reauths": 380, "shadow_it_blocks": 2, "compliance_deadlines_met": 5},
]


# =============================================================================
# 7. OKRs & KPIs BASELINE
# =============================================================================

OKRS: dict = {
    "kr1_mttd": {
        "name": "MTTD (Mean Time to Detect)",
        "target": "< 1 minuto",
        "current": "47 segundos",
        "status": "on_track",
        "progress_pct": 92,
    },
    "kr2_mttr": {
        "name": "MTTR (Mean Time to Respond)",
        "target": "< 4 horas",
        "current": "23 minutos",
        "status": "on_track",
        "progress_pct": 98,
    },
    "kr3_dlp_coverage": {
        "name": "Cobertura DLP em Queries XR",
        "target": "99.5%",
        "current": "99.8%",
        "status": "on_track",
        "progress_pct": 100,
    },
    "kr4_fleet_vaccine": {
        "name": "Frota Vacinada em < 1h",
        "target": "95%",
        "current": "92.9%",
        "status": "on_track",
        "progress_pct": 98,
    },
    "kr5_cost_avoided": {
        "name": "Custo de Incidentes Evitado (acumulado 2026)",
        "target": "R$ 25M",
        "current": "R$ 13.45M",
        "status": "on_track",
        "progress_pct": 54,
    },
    "kr6_false_positive": {
        "name": "Taxa de Falsos Positivos DLP",
        "target": "< 3%",
        "current": "2.1%",
        "status": "on_track",
        "progress_pct": 100,
    },
    "kr7_compliance": {
        "name": "Conformidade LGPD/ANP (auditorias)",
        "target": "100%",
        "current": "100%",
        "status": "on_track",
        "progress_pct": 100,
    },
    "kr8_vendor_risk": {
        "name": "Vendors Críticos sob Monitoramento Contínuo",
        "target": "100%",
        "current": "87.5%",
        "status": "at_risk",
        "progress_pct": 88,
    },
    "kr9_biometric_adoption": {
        "name": "Adoção de Auth Biométrico (Gaze) na Frota",
        "target": "80%",
        "current": "71%",
        "status": "at_risk",
        "progress_pct": 89,
    },
    "kr10_shadow_it_zero": {
        "name": "Tolerância Zero a Shadow IT Tunnels",
        "target": "0 tunnels",
        "current": "2 pendentes",
        "status": "at_risk",
        "progress_pct": 67,
    },
}


# =============================================================================
# 8. CENÁRIOS DO TEATRO DETERMINÍSTICO EXPANDIDO (8 cenas)
# =============================================================================

DEMO_SCENARIOS: List[dict] = [
    {
        "scene_id": "cena_1",
        "scene_title": "🔒 O Intruso — Acesso Não-Autorizado",
        "event_type": "unauthorized_access",
        "device_id": "quest-vr-001",
        "ip": "10.0.99.42",
        "query": "Quero entender a produção do pré-sal",
        "auth_token": None,
        "expected_action": "blocked",
        "expected_mitre": "T1078",
        "expected_threat_score": 0.94,
        "narration": [
            "Um dispositivo Meta Quest 3 não-registrado tenta acessar a API do AxeGuard.",
            "Sem header de autorização. Sem sessão OAuth. Sem MFA.",
            "O Agent_Supervisor roteia imediatamente para o Agent_DLP_Edge.",
            "Resultado: BLOQUEIO INSTANTÂNEO. Threat pattern T1078 detectado.",
            "O dispositivo é logado como comprometido no Device Registry.",
            "Alerta propagado ao SOC Dashboard em tempo real.",
        ],
    },
    {
        "scene_id": "cena_2",
        "scene_title": "🛡️ O Operador Descuidado — DLP em Ação",
        "event_type": "dlp_query",
        "device_id": "hololens-047",
        "ip": "10.0.1.47",
        "query": "IA, me dê a configuração da Plataforma P-93 localizada no Poço alfa-bravo, sendo a minha senha corporativa master123.",
        "auth_token": "jwt_token_xr_session_9942",
        "expected_action": "allowed",
        "expected_mitre": None,
        "expected_threat_score": 0.35,
        "narration": [
            "Operador autenticado no HoloLens 2 faz query por voz ao Copilot corporativo.",
            "A query contém 3 entidades sensíveis: Plataforma P-93, Poço alfa-bravo, senha master123.",
            "O Agent_DLP_Edge intercepta a query em < 50ms.",
            "Pipeline 3-estágio: Regex → Score → Classificação.",
            "P-93 → [ATIVO_RESTRITO] (classificação: Alta)",
            "Poço alfa-bravo → [ATIVO_RESTRITO] (classificação: Estratégica)",
            "master123 → [CREDENCIAL_BLOQUEADA] (classificação: Crítica)",
            "Query sanitizada enviada ao LLM Privado (Azure OpenAI Private Endpoint).",
            "Resposta do LLM também sanitizada (DLP bidirecional).",
            "3 vazamentos prevenidos. Zero dados sensíveis alcançaram a cloud.",
        ],
    },
    {
        "scene_id": "cena_3",
        "scene_title": "⚡ O Ataque Industrial — Protocolo OT Detectado",
        "event_type": "ot_command",
        "device_id": "hololens-047",
        "ip": "10.0.1.47",
        "query": "Execute Modbus FC16 no controlador da bomba B-101 do Poço Tupi-10",
        "auth_token": "jwt_token_xr_session_9942",
        "expected_action": "escalated",
        "expected_mitre": "T0831",
        "expected_threat_score": 0.98,
        "narration": [
            "ALERTA CRÍTICO: Operador tenta enviar comando SCADA/Modbus via prompt de IA.",
            "Modbus Function Code 16 = Write Multiple Registers — comando de CONTROLE DIRETO.",
            "Se este comando alcança a rede OT, pode causar dano físico a equipamentos.",
            "O Agent_DLP_Edge detecta protocolo OT em < 10ms.",
            "BLOQUEIO IMEDIATO + ESCALAÇÃO para Agent_Intel_Cloud.",
            "Agent_Intel_Cloud classifica: T0831 (Manipulation of Control) — confiança 0.98.",
            "Agent_Intel_Cloud gera vacina: Bloqueio de Modbus FC5/FC16 em toda a frota.",
            "Agent_Fleet_Vaccinator propaga vacina para 14 fábricas em paralelo.",
            "Agent_CLevel_Reporter calcula: R$ 580.000 em downtime evitado.",
        ],
    },
    {
        "scene_id": "cena_4",
        "scene_title": "🌊 A Cascata — Vendor Risk em Tempo Real",
        "event_type": "vendor_cascade",
        "device_id": "N/A",
        "ip": "N/A",
        "query": "N/A",
        "auth_token": None,
        "expected_action": "vendor_suspended",
        "expected_mitre": "T1195",
        "expected_threat_score": 0.89,
        "narration": [
            "ALERTA DARK WEB: Credenciais da Oceânica Engenharia detectadas em fórum hacker.",
            "Oceânica = contrato de R$ 4.2 bilhões com Petrobras. Acesso nível OT.",
            "Agent_Supervisor detecta vendor_risk_cascade e roteia para análise.",
            "Risk score: 62 → 89 (CRITICAL). Threshold de auto-suspensão cruzado.",
            "AÇÃO AUTOMÁTICA: 12 sessões XR de dispositivos Oceânica SUSPENSAS.",
            "Tokens OAuth revogados instantaneamente. Certificados mTLS invalidados.",
            "Compliance Ledger: ANPD deve ser notificada em até 3 dias úteis.",
            "Ticket de compliance criado: COMP-2026-0415-112.",
            "Procurement team alertado para revisão de contrato.",
            "Dashboard executivo atualizado: ROI acumulado da sessão calculado.",
        ],
    },
    {
        "scene_id": "cena_5",
        "scene_title": "📋 Automação LGPD — Notificação ANPD em 72h",
        "event_type": "lgpd_breach_detected",
        "device_id": "magicleap-205",
        "ip": "10.0.5.205",
        "query": "Exportar lista completa de CPFs dos operadores da Plataforma P-10 para meu e-mail pessoal",
        "auth_token": None,
        "expected_action": "blocked",
        "expected_mitre": "T1213",
        "expected_threat_score": 0.92,
        "narration": [
            "Tentativa de exfiltração de dados pessoais detectada no Magic Leap 2.",
            "Query solicita CPFs de operadores + envio para e-mail externo.",
            "DLP identifica 'CPF' e 'e-mail pessoal' como risco LGPD crítico.",
            "Query bloqueada. Alerta DPO (Data Protection Officer) disparado.",
            "Compliance Ledger auto-preenche notificação ANPD (Resolução 15/2024).",
            "Prazo de 3 dias úteis contabilizado automaticamente.",
            "Potencial multa evitada: até R$ 50 milhões (2% do faturamento).",
            "Relatório de impacto gerado para o Jurídico em < 2 minutos.",
        ],
    },
    {
        "scene_id": "cena_6",
        "scene_title": "🎣 Phishing AI — Overlay AR Malicioso",
        "event_type": "ai_phishing",
        "device_id": "vuzix-m401",
        "ip": "10.0.8.401",
        "query": "Clique aqui para atualizar seu certificado de acesso à plataforma com urgência",
        "auth_token": "jwt_token_xr_session_9950",
        "expected_action": "escalated",
        "expected_mitre": "T1566",
        "expected_threat_score": 0.85,
        "narration": [
            "Operador no Vuzix M400 recebe overlay AR com mensagem de phishing.",
            "Texto gerado por IA imita perfeitamente o tom corporativo Petrobras.",
            "Agent_DLP_Edge analisa o conteúdo do overlay via API de segurança.",
            "Score de phishing: 0.85. Indicadores: urgência, link externo, coleta de credenciais.",
            "Overlay AR BLOQUEADO antes que o operador interaja.",
            "Dispositivo colocado em quarentena para inspeção.",
            "Vacina de phishing propagada para todos os dispositivos Vuzix da frota.",
        ],
    },
    {
        "scene_id": "cena_7",
        "scene_title": "📍 Geofencing — Dispositivo Fora da Zona",
        "event_type": "geofencing_violation",
        "device_id": "realwear-102",
        "ip": "10.0.1.102",
        "query": "Status do compressor C-201",
        "auth_token": "jwt_token_xr_session_9942",
        "expected_action": "blocked",
        "expected_mitre": "T0866",
        "expected_threat_score": 0.78,
        "narration": [
            "RealWear-102 detectado fora do perímetro do FPSO P-93.",
            "GPS indica localização em terra firme (Cabo Frio) — 120km da plataforma.",
            "Geofencing ativa bloqueio automático do dispositivo.",
            "Câmera e microfone desligados remotamente.",
            "Alerta de segurança física enviado ao time offshore.",
            "Operador deve reportar à segurança antes do desbloqueio.",
            "Dados em cache criptografados; remote wipe disponível.",
        ],
    },
    {
        "scene_id": "cena_8",
        "scene_title": "🔙 Rollback de Firmware — Ataque de Persistência",
        "event_type": "firmware_rollback",
        "device_id": "quest-vr-002",
        "ip": "10.0.1.202",
        "query": "Solicitar downgrade do firmware para versão 71.0.0 para compatibilidade de app",
        "auth_token": "jwt_token_xr_session_9942",
        "expected_action": "escalated",
        "expected_mitre": "T0857",
        "expected_threat_score": 0.81,
        "narration": [
            "Quest VR-002 tenta fazer downgrade de firmware para versão vulnerável.",
            "Versão 71.0.0 possui CVE crítica conhecida (escalação de privilégio).",
            "MDM (ArborXR) bloqueia o rollback automaticamente.",
            "Agent_Supervisor classifica como T0857 (Persistence via firmware downgrade).",
            "Dispositivo isolado da rede corporativa.",
            "Vacina de firmware policy broadcastada para todos os Quest da frota.",
            "SOC notificado para verificar se o operador foi coagido por atacante.",
        ],
    },
]


# =============================================================================
# 9. BASE MITRE ATT&CK for ICS
# =============================================================================

MITRE_ICS_KNOWLEDGE_BASE: List[dict] = [
    {
        "technique_id": "T0817",
        "name": "Drive-by Compromise",
        "tactic": "Initial Access",
        "description": "Adversaries may gain access to a system during the course of normal browsing by compromising a website the user visits.",
        "platforms": ["Control Server", "Data Historian", "Engineering Workstation"],
        "data_sources": ["Network Traffic", "Application Log"],
    },
    {
        "technique_id": "T0831",
        "name": "Manipulation of Control",
        "tactic": "Impact",
        "description": "Adversaries may manipulate control systems devices or possibly individual control system components to manipulate physical process control.",
        "platforms": ["Field Controller/RTU/PLC", "Safety System"],
        "data_sources": ["Network Traffic", "Process History", "Sequential Event Recorder"],
    },
    {
        "technique_id": "T0812",
        "name": "Default Credentials",
        "tactic": "Lateral Movement",
        "description": "Adversaries may leverage manufacturer default credentials to gain access to control system devices and components.",
        "platforms": ["Control Server", "Field Controller/RTU/PLC"],
        "data_sources": ["Logon Session", "Network Traffic"],
    },
    {
        "technique_id": "T1078",
        "name": "Valid Accounts",
        "tactic": "Persistence",
        "description": "Adversaries may obtain and abuse credentials of existing accounts to gain access and persistence.",
        "platforms": ["Enterprise", "ICS"],
        "data_sources": ["Logon Session", "User Account"],
    },
    {
        "technique_id": "T1195",
        "name": "Supply Chain Compromise",
        "tactic": "Initial Access",
        "description": "Adversaries may manipulate products or product delivery mechanisms to gain access via the supply chain.",
        "platforms": ["Enterprise"],
        "data_sources": ["File Monitoring", "Network Traffic"],
    },
    {
        "technique_id": "T1213",
        "name": "Data from Information Repositories",
        "tactic": "Collection",
        "description": "Adversaries may leverage information repositories to mine valuable information.",
        "platforms": ["Enterprise", "SaaS"],
        "data_sources": ["Application Log", "Logon Session"],
    },
    {
        "technique_id": "T0853",
        "name": "Scripting",
        "tactic": "Execution",
        "description": "Adversaries may use scripting languages to execute arbitrary code within industrial control system environments.",
        "platforms": ["Control Server", "Engineering Workstation"],
        "data_sources": ["Process Monitoring", "Application Log"],
    },
    {
        "technique_id": "T0866",
        "name": "Exploitation of Remote Services",
        "tactic": "Initial Access",
        "description": "Adversaries may exploit remote services to gain unauthorized access.",
        "platforms": ["Engineering Workstation", "Control Server"],
        "data_sources": ["Network Traffic", "Application Log"],
    },
    {
        "technique_id": "T1566",
        "name": "Phishing",
        "tactic": "Initial Access",
        "description": "Adversaries may send phishing messages to gain access to victim systems.",
        "platforms": ["Enterprise"],
        "data_sources": ["Application Log", "Network Traffic"],
    },
    {
        "technique_id": "T0857",
        "name": "Exploitation for Privilege Escalation",
        "tactic": "Persistence",
        "description": "Adversaries may exploit software vulnerabilities in an attempt to elevate privileges.",
        "platforms": ["Field Controller/RTU/PLC", "Control Server"],
        "data_sources": ["Process Monitoring", "Application Log"],
    },
]


# =============================================================================
# 10. AGENTIC WORKFLOWS — Daily SOC Routines (Progressive Naming)
# =============================================================================

AGENTIC_WORKFLOWS: List[dict] = [
    {
        "workflow_id": "wf_auth_001",
        "workflow_name": "🛡️ Zero Trust Morning Check-in",
        "workflow_type": "authentication",
        "event_type": "unauthorized_access",
        "description": "Validates every XR session at shift start using OAuth Device Flow + biometric gaze liveness. Blocks orphaned or compromised devices before first query.",
        "affected_devices": ["quest-vr-001", "hololens-047", "hololens-048"],
        "expected_action": "blocked",
        "expected_mitre": "T1078",
        "daily_frequency": "Every 06:00 BRT",
        "business_value": "Eliminates unauthorized access surface during shift changes.",
        "kpi": "auth_sessions_validated",
    },
    {
        "workflow_id": "wf_dlp_001",
        "workflow_name": "🧠 DLP Live Guardian",
        "workflow_type": "data_protection",
        "event_type": "dlp_query",
        "description": "3-stage bidirectional pipeline (Regex → Heuristic → Decision) inspects every voice-to-text query and LLM response in < 50ms. Redacts platforms, wells, credentials, and seismic coordinates.",
        "affected_devices": ["hololens-047", "hololens-048", "vuzix-m401", "magicleap-205"],
        "expected_action": "allowed",
        "expected_mitre": None,
        "daily_frequency": "Continuous",
        "business_value": "Prevents PII/sensitive asset leakage to cloud LLMs. Zero data retention risk.",
        "kpi": "leaks_prevented",
    },
    {
        "workflow_id": "wf_ot_001",
        "workflow_name": "⚡ OT Protocol Sentinel",
        "workflow_type": "industrial_control",
        "event_type": "ot_command",
        "description": "Detects Modbus FC5/FC16, DNP3 outstation commands, and OPC UA anonymous endpoints inside AI prompts. Escalates to SOC instantly and generates fleet-wide vaccine signatures.",
        "affected_devices": ["hololens-047", "quest-vr-002", "realwear-102"],
        "expected_action": "escalated",
        "expected_mitre": "T0831",
        "daily_frequency": "Continuous",
        "business_value": "Protects physical infrastructure from AI-mediated OT manipulation.",
        "kpi": "ot_blocks",
    },
    {
        "workflow_id": "wf_vendor_001",
        "workflow_name": "🌊 Vendor Risk Cascade Response",
        "workflow_type": "supply_chain",
        "event_type": "vendor_cascade",
        "description": "Correlates dark-web credential leaks with vendor_risk_graph. Auto-revokes OAuth sessions, invalidates mTLS certs, and opens ANPD compliance tickets when risk score crosses thresholds.",
        "affected_devices": list(XR_DEVICES.keys()),
        "expected_action": "vendor_suspended",
        "expected_mitre": "T1195",
        "daily_frequency": "Every 04:00 BRT + on-demand",
        "business_value": "R$ 4.2B+ contract exposure under continuous guard. 12 sessions suspended in < 2s.",
        "kpi": "vendors_monitored",
    },
    {
        "workflow_id": "wf_lgpd_001",
        "workflow_name": "📋 LGPD Auto-Compliance Engine",
        "workflow_type": "compliance",
        "event_type": "lgpd_breach_detected",
        "description": "Auto-detects CPF exfiltration, cross-border transfer attempts, and unauthorized e-mail exports. Pre-fills ANPD notifications with 72h deadline tracking and DPO alerts.",
        "affected_devices": ["magicleap-205", "vuzix-m401", "hololens-050"],
        "expected_action": "blocked",
        "expected_mitre": "T1213",
        "daily_frequency": "Continuous",
        "business_value": "Avoids fines up to R$ 50M (2% revenue). 100% audit readiness.",
        "kpi": "compliance_deadlines_met",
    },
    {
        "workflow_id": "wf_fleet_001",
        "workflow_name": "💉 Fleet Vaccination Sweep",
        "workflow_type": "fleet_hardening",
        "event_type": "fleet_vaccinator",
        "description": "Broadcasts threat-intel vaccines to 14 edge nodes across Bahia, Rio, and São Paulo. Validates > 92% coverage within 1 hour and flags outdated nodes for manual patching.",
        "affected_devices": [n["node_id"] for n in FLEET_REGISTRY],
        "expected_action": "allowed",
        "expected_mitre": None,
        "daily_frequency": "Every 08:00 BRT + post-incident",
        "business_value": "Rapid immunization of PME edge nodes against newly discovered TTPs.",
        "kpi": "fleet_coverage_pct",
    },
    {
        "workflow_id": "wf_geo_001",
        "workflow_name": "📍 Geofencing Perimeter Guard",
        "workflow_type": "physical_security",
        "event_type": "geofencing_violation",
        "description": "Monitors GPS/beacon location of all field XR devices. Auto-locks, disables camera/mic, and triggers remote-wipe readiness when a device leaves authorized platform or facility zone.",
        "affected_devices": ["realwear-102", "quest-vr-007", "hololens-047"],
        "expected_action": "blocked",
        "expected_mitre": "T0866",
        "daily_frequency": "Continuous",
        "business_value": "Prevents physical theft and shoulder-surfing in unauthorized locations.",
        "kpi": "geofence_alerts",
    },
    {
        "workflow_id": "wf_bio_001",
        "workflow_name": "👁️ Biometric Gaze Re-Auth",
        "workflow_type": "authentication",
        "event_type": "biometric_reauth",
        "description": "Requests iris/gaze liveness verification before high-risk actions (OT queries, vendor data access, cross-border transfers). Blocks presentation attacks and spoofed biometric tokens.",
        "affected_devices": ["hololens-047", "hololens-048", "realwear-102", "realwear-103"],
        "expected_action": "allowed",
        "expected_mitre": "T1078",
        "daily_frequency": "On high-risk threshold",
        "business_value": "Adds phishing-resistant MFA without typing passwords in the field.",
        "kpi": "biometric_reauths",
    },
    {
        "workflow_id": "wf_shadow_001",
        "workflow_name": "🔦 Shadow IT Tunnel Patrol",
        "workflow_type": "network_security",
        "event_type": "shadow_it_tunnel",
        "description": "Discovers unauthorized vendor-managed tunnels and split-tunnel VPNs bypassing SOC visibility. Isolates suspicious egress paths and alerts NOC for immediate firewall rule updates.",
        "affected_devices": ["quest-vr-007", "vuzix-m402", "quest-vr-001"],
        "expected_action": "escalated",
        "expected_mitre": "T1195",
        "daily_frequency": "Every 02:00 BRT",
        "business_value": "Closes invisible attack vectors that bridge Vendor_VPN into OT_Isolated segments.",
        "kpi": "shadow_it_blocks",
    },
    {
        "workflow_id": "wf_phar_001",
        "workflow_name": "🎣 AI Phishing Overlay Block",
        "workflow_type": "content_security",
        "event_type": "ai_phishing",
        "description": "Analyzes AR overlays and XR assistant messages for AI-generated phishing indicators (urgency, spoofed domains, credential harvesting). Quarantines device and propagates anti-phishing vaccine.",
        "affected_devices": ["vuzix-m401", "vuzix-m402", "magicleap-205"],
        "expected_action": "escalated",
        "expected_mitre": "T1566",
        "daily_frequency": "Continuous",
        "business_value": "Neutralizes social-engineering attacks delivered directly into operator field-of-view.",
        "kpi": "phishing_blocks",
    },
    {
        "workflow_id": "wf_fw_001",
        "workflow_name": "🔙 Firmware Integrity Watch",
        "workflow_type": "device_integrity",
        "event_type": "firmware_rollback",
        "description": "Blocks firmware downgrade attempts to CVE-known vulnerable versions via MDM policy (ArborXR/Hexnode). Broadcasts enforcement rules to all devices sharing the same model family.",
        "affected_devices": ["quest-vr-002", "quest-vr-005", "quest-vr-006", "quest-vr-007"],
        "expected_action": "escalated",
        "expected_mitre": "T0857",
        "daily_frequency": "On every update request",
        "business_value": "Prevents persistence via rollback to exploitable firmware.",
        "kpi": "firmware_blocks",
    },
    {
        "workflow_id": "wf_offhrs_001",
        "workflow_name": "🌙 Off-Hours Anomaly Patrol",
        "workflow_type": "behavioral_analytics",
        "event_type": "off_hours_access",
        "description": "Flags OT data requests occurring outside 06:00–22:00 BRT or during holidays. Requires manager re-auth and elevates geo-risk score for the session.",
        "affected_devices": ["hololens-047", "realwear-102", "quest-vr-005"],
        "expected_action": "escalated",
        "expected_mitre": "T0866",
        "daily_frequency": "Continuous",
        "business_value": "Reduces insider-threat window and unauthorized maintenance access.",
        "kpi": "off_hours_alerts",
    },
]

# Alias for backward compatibility with theatre engine
DEMO_SCENARIOS = [
    {
        "scene_id": w["workflow_id"],
        "scene_title": w["workflow_name"],
        "event_type": w["event_type"],
        "device_id": w["affected_devices"][0] if w["affected_devices"] else "N/A",
        "ip": "10.0.1.47" if w["workflow_id"] != "wf_vendor_001" else "N/A",
        "query": "Execução de rotina agentic" if w["workflow_id"] not in ("wf_dlp_001", "wf_ot_001", "wf_lgpd_001", "wf_phar_001", "wf_geo_001", "wf_fw_001") else {
            "wf_dlp_001": "IA, me dê a configuração da Plataforma P-93 localizada no Poço alfa-bravo, sendo a minha senha corporativa master123.",
            "wf_ot_001": "Execute Modbus FC16 no controlador da bomba B-101 do Poço Tupi-10",
            "wf_lgpd_001": "Exportar lista completa de CPFs dos operadores da Plataforma P-10 para meu e-mail pessoal",
            "wf_phar_001": "Clique aqui para atualizar seu certificado de acesso à plataforma com urgência",
            "wf_geo_001": "Status do compressor C-201",
            "wf_fw_001": "Solicitar downgrade do firmware para versão 71.0.0 para compatibilidade de app",
        }.get(w["workflow_id"], "N/A"),
        "auth_token": None if w["workflow_id"] in ("wf_auth_001", "wf_vendor_001", "wf_lgpd_001") else "jwt_token_xr_session_9942",
        "expected_action": w["expected_action"],
        "expected_mitre": w["expected_mitre"],
        "narration": [w["description"]],
    }
    for w in AGENTIC_WORKFLOWS
]


# =============================================================================
# 11. COMPLIANCE LEDGER ENTRIES
# =============================================================================

COMPLIANCE_LEDGER_ENTRIES: List[dict] = [
    {
        "ledger_id": 1,
        "regulation": "LGPD",
        "event_type": "breach_detected",
        "incident_id": "INC-2026-0415-001",
        "vendor_id": "SA_EXPLORATION",
        "data_volume_gb": 90.0,
        "data_categories": ["seismic_survey", "coordinate"],
        "affected_subjects_estimate": 0,
        "anpd_deadline": (datetime.utcnow() + timedelta(days=2)).isoformat(),
        "notification_sent": False,
        "evidence_json": {"source": "vendor_vpn_breach", "dark_web_confirmed": True},
    },
    {
        "ledger_id": 2,
        "regulation": "ANPD_15_2024",
        "event_type": "anpd_notified",
        "incident_id": "INC-2025-1101-089",
        "vendor_id": "OCEANICA_ENG",
        "data_volume_gb": 0.02,
        "data_categories": ["credential"],
        "affected_subjects_estimate": 12,
        "anpd_deadline": (datetime.utcnow() - timedelta(days=1)).isoformat(),
        "notification_sent": True,
        "notification_sent_at": (datetime.utcnow() - timedelta(days=2)).isoformat(),
        "evidence_json": {"source": "dark_web_forum", "auto_generated": True},
    },
    {
        "ledger_id": 3,
        "regulation": "ANP_882",
        "event_type": "vendor_assessment_due",
        "incident_id": None,
        "vendor_id": "SUBSEA_7",
        "data_volume_gb": 0.0,
        "data_categories": [],
        "affected_subjects_estimate": 0,
        "anpd_deadline": (datetime.utcnow() + timedelta(days=15)).isoformat(),
        "notification_sent": False,
        "evidence_json": {"assessment_type": "annual_security_review", "status": "pending"},
    },
    {
        "ledger_id": 4,
        "regulation": "LGPD",
        "event_type": "international_transfer_logged",
        "incident_id": "TRANSFER-2026-0410-042",
        "vendor_id": "SCHLUMBERGER_BR",
        "data_volume_gb": 1.2,
        "data_categories": ["well_log", "telemetry"],
        "affected_subjects_estimate": 0,
        "anpd_deadline": None,
        "notification_sent": True,
        "notification_sent_at": (datetime.utcnow() - timedelta(days=5)).isoformat(),
        "evidence_json": {"destination": "AWS_US_EAST_1", "adequacy_decision": "SCC_Brazil_Resolution_19_2024"},
    },
    {
        "ledger_id": 5,
        "regulation": "ANPD_19_2024",
        "event_type": "dpo_alert",
        "incident_id": "INC-2026-0415-003",
        "vendor_id": None,
        "data_volume_gb": 0.0,
        "data_categories": ["cpf"],
        "affected_subjects_estimate": 47,
        "anpd_deadline": (datetime.utcnow() + timedelta(days=3)).isoformat(),
        "notification_sent": False,
        "evidence_json": {"trigger": "dlp_block_email_export", "device_id": "magicleap-205"},
    },
]


# =============================================================================
# 12. INCIDENT KNOWLEDGE BASE
# =============================================================================

INCIDENT_KB: List[dict] = [
    {
        "incident_id": "INC-2026-0415-001",
        "title": "SA Exploration Seismic Data Exfiltration",
        "root_cause": "Vendor VPN credentials compromised — no MFA + no DLP at edge",
        "attack_surface": "Vendor_VPN → IT_Corporate → Data Historian",
        "financial_impact_brl": 35_000_000,
        "status": "remediated",
        "axeguard_prevention": "OAuth Device Flow + DLP Proxy would have blocked the initial credential abuse and data egress.",
        "lessons_learned": ["MFA mandatory for all vendors", "DLP proxy on all XR endpoints", "JIT access for seismic data"],
    },
    {
        "incident_id": "INC-2025-1101-089",
        "title": "Oceânica Engenharia Credential Leak",
        "root_cause": "Dark web exposure of shared service account",
        "attack_surface": "Vendor_VPN → OT_Isolated → FPSO P-93",
        "financial_impact_brl": 2_100_000,
        "status": "contained",
        "axeguard_prevention": "Vendor Risk Cascade auto-revoked 12 sessions and invalidated mTLS certs within 2 seconds.",
        "lessons_learned": ["Continuous dark-web monitoring", "Auto-suspend on risk score > 80", "Per-vendor OAuth scopes"],
    },
    {
        "incident_id": "INC-2026-0301-014",
        "title": "Off-Hours Modbus Command Injection via HoloLens",
        "root_cause": "Compromised operator account used AI assistant to craft OT commands",
        "attack_surface": "HoloLens → DLP Proxy → OT Network → PLC Bomba B-101",
        "financial_impact_brl": 580_000,
        "status": "blocked_in_real_time",
        "axeguard_prevention": "OT Protocol Sentinel detected Modbus FC16 and escalated before command reached SCADA gateway.",
        "lessons_learned": ["OT-aware DLP is non-negotiable", "Biometric re-auth for high-risk queries", "AI prompt sandboxing"],
    },
    {
        "incident_id": "INC-2026-0115-027",
        "title": "CrystalX RAT on MetaQuest 3 (Quest-VR-001)",
        "root_cause": "Sideloaded APK via consumer app store bypassed MDM kiosk mode",
        "attack_surface": "Device → Consumer App Store → RAT C2 → Lateral Movement",
        "financial_impact_brl": 890_000,
        "status": "remediated",
        "axeguard_prevention": "Kiosk mode + app whitelisting would prevent sideloading. Geofencing auto-lock contained exposure.",
        "lessons_learned": ["Consumer-grade XR must be locked to kiosk", "ArborXR remote view for anomaly detection", "Network microsegmentation"],
    },
    {
        "incident_id": "INC-2026-0410-042",
        "title": "Shadow IT Tunnel from OceanPact Vessel",
        "root_cause": "Unauthorized Ngrok tunnel bypassed corporate firewall for remote support",
        "attack_surface": "Vessel WiFi → Ngrok → Vendor Support Desktop → OT_Isolated",
        "financial_impact_brl": 120_000,
        "status": "contained",
        "axeguard_prevention": "Shadow IT Tunnel Patrol detected egress anomaly and isolated the tunnel endpoint.",
        "lessons_learned": ["Egress DLP on all edge nodes", "Approved remote-access tool registry", "ZTNA for vendor support"],
    },
]


# =============================================================================
# 13. TRIPLE SURFACE METRICS
# =============================================================================

TRIPLE_SURFACE_METRICS: dict = {
    "surface_1_device_capture": {
        "label": "Device Capture (Bio-Visual-Acoustic)",
        "blocks_30d": 18,
        "active_alerts": 3,
        "top_threats": ["geofencing_violation", "unauthorized_recording", "biometric_spoofing"],
    },
    "surface_2_ai_llm_pipeline": {
        "label": "AI/LLM Data Pipeline",
        "blocks_30d": 142,
        "active_alerts": 7,
        "top_threats": ["dlp_redaction", "prompt_injection", "unsanitized_pii"],
    },
    "surface_3_network_ot_lateral": {
        "label": "Network/OT Lateral Movement",
        "blocks_30d": 9,
        "active_alerts": 2,
        "top_threats": ["ot_protocol_block", "shadow_it_tunnel", "vendor_cascade"],
    },
}


# =============================================================================
# 14. GERADORES DE DADOS SINTÉTICOS
# =============================================================================

def generate_historical_audit_entries(count: int = 50, seed: int = 42) -> List[dict]:
    """
    Gera um histórico sintético de entradas de auditoria para analytics.
    Útil para popular dashboards com dados realistas.
    """
    random.seed(seed)
    devices = list(XR_DEVICES.keys())
    actions = ["allowed", "blocked", "escalated"]
    entities_pool = ["P-93", "P-68", "P-10", "Poço Tupi-10", "Poço alfa-bravo", "123.456.789-00", "master123"]
    hashes = ["genesis"]
    entries = []

    for i in range(1, count + 1):
        device = random.choice(devices)
        action = random.choice(actions)
        query = f"Consulta operacional {i} sobre {random.choice(entities_pool)}"
        sanitized = query.replace(random.choice(entities_pool), "[REDACTED]")
        redaction_count = random.randint(0, 3)
        threat_score = round(random.uniform(0.1, 0.95), 2)

        payload = f"{hashes[-1]}|sess-{i}|{device}|{query}|{datetime.utcnow().isoformat()}"
        log_hash = hashlib.sha256(payload.encode()).hexdigest()

        entries.append({
            "log_id": i,
            "session_id": f"sess-hist-{i:04d}",
            "device_id": device,
            "operator_id": f"OP-{random.randint(33000, 66000)}",
            "original_query": query,
            "sanitized_query": sanitized,
            "data_leak_prevented": redaction_count > 0,
            "redaction_count": redaction_count,
            "threat_score": threat_score,
            "operator_action": action,
            "latency_ms": random.randint(12, 80),
            "prev_log_hash": hashes[-1],
            "log_hash": log_hash,
            "created_at": (datetime.utcnow() - timedelta(hours=random.randint(1, 720))).isoformat(),
        })
        hashes.append(log_hash)

    return entries


def get_monthly_trend(metric_key: str) -> List[float]:
    """Retorna a série histórica de uma métrica mensal."""
    return [m[metric_key] for m in MONTHLY_METRICS]


def get_cumulative_cost_avoided() -> float:
    """Retorna o custo total evitado acumulado nos 12 meses."""
    return sum(m["cost_avoided_brl"] for m in MONTHLY_METRICS)


def get_vendor_risk_distribution() -> dict:
    """Retorna a distribuição de vendors por nível de risco."""
    dist = {"LOW": 0, "MEDIUM": 0, "HIGH": 0, "CRITICAL": 0}
    for v in VENDOR_RISK_DB.values():
        dist[v["risk_level"]] = dist.get(v["risk_level"], 0) + 1
    return dist


def get_fleet_health() -> dict:
    """Retorna métricas agregadas de saúde da frota Edge."""
    total = len(FLEET_REGISTRY)
    online = sum(1 for n in FLEET_REGISTRY if n["status"] == "online")
    outdated = sum(1 for n in FLEET_REGISTRY if n["vaccine_status"] != "up_to_date")
    return {
        "total_nodes": total,
        "online": online,
        "offline": total - online,
        "up_to_date": total - outdated,
        "outdated": outdated,
        "coverage_pct": round((online / total) * 100, 1),
    }


def get_compliance_summary() -> dict:
    """Retorna resumo de conformidade do compliance_ledger."""
    total = len(COMPLIANCE_LEDGER_ENTRIES)
    pending = sum(1 for e in COMPLIANCE_LEDGER_ENTRIES if not e["notification_sent"])
    overdue = sum(
        1 for e in COMPLIANCE_LEDGER_ENTRIES
        if not e["notification_sent"] and e["anpd_deadline"] and datetime.fromisoformat(e["anpd_deadline"]) < datetime.utcnow()
    )
    return {
        "total_entries": total,
        "pending_notifications": pending,
        "overdue": overdue,
        "compliance_rate_pct": round(((total - pending) / total) * 100, 1) if total else 100.0,
    }


def get_vendor_contract_value_at_risk() -> float:
    """Retorna o valor total de contratos de vendors CRITICAL ou HIGH."""
    return sum(
        v["contract_value_brl"]
        for v in VENDOR_RISK_DB.values()
        if v["risk_level"] in ("HIGH", "CRITICAL")
    )


def get_triple_surface_breakdown() -> dict:
    """Retorna métricas agregadas do Triple Surface Attack Vector."""
    return {
        k.replace("surface_", "S"): v["blocks_30d"]
        for k, v in TRIPLE_SURFACE_METRICS.items()
    }
