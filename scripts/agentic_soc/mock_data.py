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
        "pattern_name": "Acesso Não Autorizado a Dispositivo XR",
        "mitre_technique": "T1078",
        "mitre_tactic": "Persistence",
        "description": "Abuso de conta válida via sessão XR comprometida ou não autenticada",
        "recommended_playbook": "bloquear_requisicao_401",
        "severity": "HIGH",
        "false_positive_rate": 0.02,
        "detection_count_30d": 12,
    },
    {
        "pattern_id": 2,
        "pattern_name": "Protocolo OT em Prompt de LLM",
        "mitre_technique": "T0831",
        "mitre_tactic": "Execution",
        "description": "Comando Modbus/DNP3/OPC UA detectado em query do assistente de IA",
        "recommended_playbook": "escalar_alerta_soc_ot",
        "severity": "CRITICAL",
        "false_positive_rate": 0.01,
        "detection_count_30d": 3,
    },
    {
        "pattern_id": 3,
        "pattern_name": "Cascata de Vazamento de Credencial de Vendor",
        "mitre_technique": "T1195",
        "mitre_tactic": "Initial Access",
        "description": "Exposição na dark web de credenciais de vendor com frota XR ativa",
        "recommended_playbook": "suspender_sessoes_vendor",
        "severity": "HIGH",
        "false_positive_rate": 0.05,
        "detection_count_30d": 2,
    },
    {
        "pattern_id": 4,
        "pattern_name": "Pico de Densidade de Entidade Sensível",
        "mitre_technique": "T1213",
        "mitre_tactic": "Collection",
        "description": "Contagem anormalmente alta de ativos restritos em um único prompt",
        "recommended_playbook": "escalar_analise_nivel2",
        "severity": "MEDIUM",
        "false_positive_rate": 0.08,
        "detection_count_30d": 47,
    },
    {
        "pattern_id": 5,
        "pattern_name": "Comprometimento Drive-by via SMB",
        "mitre_technique": "T0817",
        "mitre_tactic": "Initial Access",
        "description": "Exploração do protocolo SMB para movimento lateral em rede industrial",
        "recommended_playbook": "isolar_subrede_bloquear_smb",
        "severity": "CRITICAL",
        "false_positive_rate": 0.03,
        "detection_count_30d": 1,
    },
    {
        "pattern_id": 6,
        "pattern_name": "Credenciais Padrão em Dispositivo Industrial",
        "mitre_technique": "T0812",
        "mitre_tactic": "Lateral Movement",
        "description": "Uso de credenciais padrão de fábrica em controladores SCADA/PLC",
        "recommended_playbook": "forcar_rotacao_credenciais",
        "severity": "HIGH",
        "false_positive_rate": 0.04,
        "detection_count_30d": 5,
    },
    {
        "pattern_id": 7,
        "pattern_name": "Violação de Geofencing",
        "mitre_technique": "T0866",
        "mitre_tactic": "Initial Access",
        "description": "Dispositivo XR fisicamente removido da zona de instalação autorizada",
        "recommended_playbook": "bloqueio_auto_remote_wipe",
        "severity": "HIGH",
        "false_positive_rate": 0.06,
        "detection_count_30d": 8,
    },
    {
        "pattern_id": 8,
        "pattern_name": "Phishing Gerado por IA via XR",
        "mitre_technique": "T1566",
        "mitre_tactic": "Initial Access",
        "description": "Conteúdo de spearphishing entregue via overlay AR ou assistente XR",
        "recommended_playbook": "bloquear_overlay_ar_quarentenar_dispositivo",
        "severity": "MEDIUM",
        "false_positive_rate": 0.10,
        "detection_count_30d": 15,
    },
    {
        "pattern_id": 9,
        "pattern_name": "Ataque de Downgrade de Firmware",
        "mitre_technique": "T0857",
        "mitre_tactic": "Persistence",
        "description": "Tentativa de rollback do firmware do dispositivo para versão vulnerável",
        "recommended_playbook": "bloquear_rollback_firmware_alertar_soc",
        "severity": "HIGH",
        "false_positive_rate": 0.04,
        "detection_count_30d": 4,
    },
    {
        "pattern_id": 10,
        "pattern_name": "Tentativa de Exfiltração de Dados LGPD",
        "mitre_technique": "T1213",
        "mitre_tactic": "Collection",
        "description": "Transferência em massa de dados pessoais para fora da jurisdição brasileira",
        "recommended_playbook": "acionar_bloqueio_dlp_notificar_anpd",
        "severity": "CRITICAL",
        "false_positive_rate": 0.02,
        "detection_count_30d": 6,
    },
    {
        "pattern_id": 11,
        "pattern_name": "Túnel Shadow IT Detectado",
        "mitre_technique": "T1195",
        "mitre_tactic": "Initial Access",
        "description": "Túnel não autorizado gerenciado por vendor burlando a visibilidade do SOC",
        "recommended_playbook": "isolar_tunel_alertar_noc",
        "severity": "HIGH",
        "false_positive_rate": 0.07,
        "detection_count_30d": 3,
    },
    {
        "pattern_id": 12,
        "pattern_name": "Spoofing de Gaze Biométrico",
        "mitre_technique": "T1078",
        "mitre_tactic": "Persistence",
        "description": "Ataque de apresentação contra autenticação baseada em íris/gaze",
        "recommended_playbook": "exigir_verificacao_vivacidade",
        "severity": "MEDIUM",
        "false_positive_rate": 0.05,
        "detection_count_30d": 2,
    },
    {
        "pattern_id": 13,
        "pattern_name": "Requisição de Acesso OT Fora de Horário",
        "mitre_technique": "T0866",
        "mitre_tactic": "Initial Access",
        "description": "Dispositivo XR requisitando dados OT fora do horário comercial",
        "recommended_playbook": "exigir_reauth_gerente",
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
        "workflow_name": "🛡️ Check-in Matinal Zero Trust",
        "workflow_type": "authentication",
        "event_type": "unauthorized_access",
        "description": "Valida cada sessão XR no início do turno usando OAuth Device Flow + verificação de vivacidade do gaze biométrico. Bloqueia dispositivos órfãos ou comprometidos antes da primeira query.",
        "affected_devices": ["quest-vr-001", "hololens-047", "hololens-048"],
        "expected_action": "blocked",
        "expected_mitre": "T1078",
        "daily_frequency": "Todo dia às 06:00 BRT",
        "business_value": "Elimina a superfície de acesso não autorizado durante as trocas de turno.",
        "kpi": "auth_sessions_validated",
    },
    {
        "workflow_id": "wf_dlp_001",
        "workflow_name": "🧠 Guardião DLP ao Vivo",
        "workflow_type": "data_protection",
        "event_type": "dlp_query",
        "description": "Pipeline bidirecional de 3 estágios (Regex → Heurística → Decisão) inspeciona toda query voice-to-text e resposta do LLM em < 50ms. Redige plataformas, poços, credenciais e coordenadas sísmicas.",
        "affected_devices": ["hololens-047", "hololens-048", "vuzix-m401", "magicleap-205"],
        "expected_action": "allowed",
        "expected_mitre": None,
        "daily_frequency": "Contínuo",
        "business_value": "Previne vazamento de PII/ativos sensíveis para LLMs em cloud. Risco zero de retenção de dados.",
        "kpi": "leaks_prevented",
    },
    {
        "workflow_id": "wf_ot_001",
        "workflow_name": "⚡ Sentinela de Protocolo OT",
        "workflow_type": "industrial_control",
        "event_type": "ot_command",
        "description": "Detecta comandos Modbus FC5/FC16, comandos DNP3 outstation e endpoints anônimos OPC UA dentro de prompts de IA. Escalada instantânea para o SOC e geração de assinaturas de vacina em toda a frota.",
        "affected_devices": ["hololens-047", "quest-vr-002", "realwear-102"],
        "expected_action": "escalated",
        "expected_mitre": "T0831",
        "daily_frequency": "Continuous",
        "business_value": "Protege a infraestrutura física de manipulação OT mediada por IA.",
        "kpi": "ot_blocks",
    },
    {
        "workflow_id": "wf_vendor_001",
        "workflow_name": "🌊 Resposta em Cascata de Risco de Vendor",
        "workflow_type": "supply_chain",
        "event_type": "vendor_cascade",
        "description": "Correlaciona vazamentos de credenciais na dark web com o grafo de risco de vendors. Revoga automaticamente sessões OAuth, invalida certificados mTLS e abre tickets de compliance da ANPD quando o score de risco ultrapassa os limitares.",
        "affected_devices": list(XR_DEVICES.keys()),
        "expected_action": "vendor_suspended",
        "expected_mitre": "T1195",
        "daily_frequency": "Todo dia às 04:00 BRT + sob demanda",
        "business_value": "Exposição de contrato de R$ 4,2B+ sob guarda contínua. 12 sessões suspensas em < 2s.",
        "kpi": "vendors_monitored",
    },
    {
        "workflow_id": "wf_lgpd_001",
        "workflow_name": "📋 Motor de Auto-Conformidade LGPD",
        "workflow_type": "compliance",
        "event_type": "lgpd_breach_detected",
        "description": "Detecta automaticamente exfiltração de CPF, tentativas de transferência cross-border e exportações não autorizadas por e-mail. Pré-preenche notificações ANPD com rastreamento do prazo de 72h e alertas ao DPO.",
        "affected_devices": ["magicleap-205", "vuzix-m401", "hololens-050"],
        "expected_action": "blocked",
        "expected_mitre": "T1213",
        "daily_frequency": "Continuous",
        "business_value": "Evita multas de até R$ 50 milhões (2% da receita). 100% de prontidão para auditoria.",
        "kpi": "compliance_deadlines_met",
    },
    {
        "workflow_id": "wf_fleet_001",
        "workflow_name": "💉 Varredura de Vacinação da Frota",
        "workflow_type": "fleet_hardening",
        "event_type": "fleet_vaccinator",
        "description": "Transmite vacinas de threat intel para 14 edge nodes na Bahia, Rio e São Paulo. Valida > 92% de cobertura em 1 hora e sinaliza nodes desatualizados para patching manual.",
        "affected_devices": [n["node_id"] for n in FLEET_REGISTRY],
        "expected_action": "allowed",
        "expected_mitre": None,
        "daily_frequency": "Todo dia às 08:00 BRT + pós-incidente",
        "business_value": "Imunização rápida de edge nodes de PMEs contra TTPs recém-descobertos.",
        "kpi": "fleet_coverage_pct",
    },
    {
        "workflow_id": "wf_geo_001",
        "workflow_name": "📍 Guarda de Perímetro Geofencing",
        "workflow_type": "physical_security",
        "event_type": "geofencing_violation",
        "description": "Monitora a localização GPS/beacon de todos os dispositivos XR de campo. Bloqueio automático, desativa câmera/microfone e aciona prontidão para remote wipe quando um dispositivo sai da plataforma ou zona de instalação autorizada.",
        "affected_devices": ["realwear-102", "quest-vr-007", "hololens-047"],
        "expected_action": "blocked",
        "expected_mitre": "T0866",
        "daily_frequency": "Continuous",
        "business_value": "Previne roubo físico e shoulder surfing em locais não autorizados.",
        "kpi": "geofence_alerts",
    },
    {
        "workflow_id": "wf_bio_001",
        "workflow_name": "👁️ Re-Autenticação Biométrica por Gaze",
        "workflow_type": "authentication",
        "event_type": "biometric_reauth",
        "description": "Solicita verificação de vivacidade de íris/gaze antes de ações de alto risco (queries OT, acesso a dados de vendor, transferências cross-border). Bloqueia ataques de apresentação e tokens biométricos falsificados.",
        "affected_devices": ["hololens-047", "hololens-048", "realwear-102", "realwear-103"],
        "expected_action": "allowed",
        "expected_mitre": "T1078",
        "daily_frequency": "No limiar de alto risco",
        "business_value": "Adiciona MFA resistente a phishing sem digitar senhas em campo.",
        "kpi": "biometric_reauths",
    },
    {
        "workflow_id": "wf_shadow_001",
        "workflow_name": "🔦 Patrulha de Túneis Shadow IT",
        "workflow_type": "network_security",
        "event_type": "shadow_it_tunnel",
        "description": "Descobre túneis não autorizados gerenciados por vendors e VPNs split-tunnel que burlam a visibilidade do SOC. Isola caminhos de egresso suspeitos e alerta o NOC para atualizações imediatas de regras de firewall.",
        "affected_devices": ["quest-vr-007", "vuzix-m402", "quest-vr-001"],
        "expected_action": "escalated",
        "expected_mitre": "T1195",
        "daily_frequency": "Todo dia às 02:00 BRT",
        "business_value": "Fecha vetores de ataque invisíveis que fazem ponte entre Vendor_VPN e segmentos OT_Isolated.",
        "kpi": "shadow_it_blocks",
    },
    {
        "workflow_id": "wf_phar_001",
        "workflow_name": "🎣 Bloqueio de Overlay de Phishing por IA",
        "workflow_type": "content_security",
        "event_type": "ai_phishing",
        "description": "Analisa overlays AR e mensagens do assistente XR em busca de indicadores de phishing gerados por IA (urgência, domínios spoofados, coleta de credenciais). Coloca o dispositivo em quarentena e propaga vacina anti-phishing.",
        "affected_devices": ["vuzix-m401", "vuzix-m402", "magicleap-205"],
        "expected_action": "escalated",
        "expected_mitre": "T1566",
        "daily_frequency": "Continuous",
        "business_value": "Neutraliza ataques de engenharia social entregues diretamente no campo de visão do operador.",
        "kpi": "phishing_blocks",
    },
    {
        "workflow_id": "wf_fw_001",
        "workflow_name": "🔙 Vigilância de Integridade de Firmware",
        "workflow_type": "device_integrity",
        "event_type": "firmware_rollback",
        "description": "Bloqueia tentativas de downgrade de firmware para versões vulneráveis conhecidas por CVE via política de MDM (ArborXR/Hexnode). Transmite regras de enforce para todos os dispositivos que compartilham a mesma família de modelos.",
        "affected_devices": ["quest-vr-002", "quest-vr-005", "quest-vr-006", "quest-vr-007"],
        "expected_action": "escalated",
        "expected_mitre": "T0857",
        "daily_frequency": "A cada solicitação de update",
        "business_value": "Previne persistência via rollback para firmware explorável.",
        "kpi": "firmware_blocks",
    },
    {
        "workflow_id": "wf_offhrs_001",
        "workflow_name": "🌙 Patrulha de Anomalias Fora de Horário",
        "workflow_type": "behavioral_analytics",
        "event_type": "off_hours_access",
        "description": "Sinaliza requisições de dados OT ocorrendo fora do horário 06:00–22:00 BRT ou durante feriados. Exige re-autenticação do gestor e eleva o geo-risk score da sessão.",
        "affected_devices": ["hololens-047", "realwear-102", "quest-vr-005"],
        "expected_action": "escalated",
        "expected_mitre": "T0866",
        "daily_frequency": "Continuous",
        "business_value": "Reduz a janela de insider threat e acesso não autorizado de manutenção.",
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
        "title": "Exfiltração de Dados Sísmicos da SA Exploration",
        "root_cause": "Credenciais de VPN de vendor comprometidas — sem MFA + sem DLP no edge",
        "attack_surface": "Vendor_VPN → IT_Corporate → Data Historian",
        "financial_impact_brl": 35_000_000,
        "status": "remediated",
        "axeguard_prevention": "OAuth Device Flow + DLP Proxy teriam bloqueado o abuso inicial de credenciais e o egresso de dados.",
        "lessons_learned": ["MFA obrigatório para todos os vendors", "DLP proxy em todos os endpoints XR", "Acesso JIT para dados sísmicos"],
    },
    {
        "incident_id": "INC-2025-1101-089",
        "title": "Vazamento de Credencial da Oceânica Engenharia",
        "root_cause": "Exposição na dark web de conta de serviço compartilhada",
        "attack_surface": "Vendor_VPN → OT_Isolated → FPSO P-93",
        "financial_impact_brl": 2_100_000,
        "status": "contained",
        "axeguard_prevention": "Vendor Risk Cascade revogou automaticamente 12 sessões e invalidou certificados mTLS em 2 segundos.",
        "lessons_learned": ["Monitoramento contínuo da dark web", "Auto-suspensão em risk score > 80", "Escopos OAuth por vendor"],
    },
    {
        "incident_id": "INC-2026-0301-014",
        "title": "Injeção de Comando Modbus Fora de Horário via HoloLens",
        "root_cause": "Conta de operador comprometida usou assistente de IA para criar comandos OT",
        "attack_surface": "HoloLens → DLP Proxy → OT Network → PLC Bomba B-101",
        "financial_impact_brl": 580_000,
        "status": "blocked_in_real_time",
        "axeguard_prevention": "OT Protocol Sentinel detectou Modbus FC16 e escalou antes que o comando alcançasse o gateway SCADA.",
        "lessons_learned": ["DLP com consciência OT é inegociável", "Re-autenticação biométrica para queries de alto risco", "Sandboxing de prompts de IA"],
    },
    {
        "incident_id": "INC-2026-0115-027",
        "title": "CrystalX RAT no MetaQuest 3 (Quest-VR-001)",
        "root_cause": "APK sideloaded via app store de consumidor burlou o modo kiosk do MDM",
        "attack_surface": "Dispositivo → App Store de Consumidor → RAT C2 → Movimento Lateral",
        "financial_impact_brl": 890_000,
        "status": "remediated",
        "axeguard_prevention": "Modo kiosk + app whitelisting preveniríam sideloading. Bloqueio automático de geofencing conteve a exposição.",
        "lessons_learned": ["XR de consumidor deve ser travado em kiosk", "Visualização remota ArborXR para detecção de anomalias", "Microsegmentação de rede"],
    },
    {
        "incident_id": "INC-2026-0410-042",
        "title": "Túnel Shadow IT do Navio da OceanPact",
        "root_cause": "Túnel Ngrok não autorizado burlou firewall corporativo para suporte remoto",
        "attack_surface": "WiFi do Navio → Ngrok → Desktop de Suporte do Vendor → OT_Isolated",
        "financial_impact_brl": 120_000,
        "status": "contained",
        "axeguard_prevention": "Shadow IT Tunnel Patrol detectou anomalia de egresso e isolou o endpoint do túnel.",
        "lessons_learned": ["DLP de egresso em todos os edge nodes", "Registro de ferramentas de acesso remoto aprovadas", "ZTNA para suporte de vendor"],
    },
]


# =============================================================================
# 13. TRIPLE SURFACE METRICS
# =============================================================================

TRIPLE_SURFACE_METRICS: dict = {
    "surface_1_device_capture": {
        "label": "Captura de Dispositivo (Bio-Visual-Acústica)",
        "blocks_30d": 18,
        "active_alerts": 3,
        "top_threats": ["violação_geofencing", "gravação_não_autorizada", "spoofing_biométrico"],
    },
    "surface_2_ai_llm_pipeline": {
        "label": "Pipeline de Dados AI/LLM",
        "blocks_30d": 142,
        "active_alerts": 7,
        "top_threats": ["redação_dlp", "injeção_de_prompt", "pii_não_sanitizado"],
    },
    "surface_3_network_ot_lateral": {
        "label": "Movimento Lateral de Rede/OT",
        "blocks_30d": 9,
        "active_alerts": 2,
        "top_threats": ["bloqueio_protocolo_ot", "túnel_shadow_it", "cascata_vendor"],
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
