"""
dlp_engine.py — Motor DLP Expandido com Pipeline 3-Estágio
==========================================================
Extraído e expandido a partir de scripts/dlp_proxy/main.py.
Reutiliza os mesmos padrões regex mas adiciona:
  - Classificação formal por entidade
  - Score de ameaça multi-feature
  - Detecção de protocolos OT/ICS
  - Sanitização bidirecional (request + response)
  - Integração com audit hash chain

Complexidade: O(n × p) onde n = tamanho do texto, p = número de padrões
"""

import re
import hashlib
import time
from typing import List, Tuple

from .state import RedactedEntity, AuditEntry


# =============================================================================
# PADRÕES DE DETECÇÃO (SENSÍVEIS PETROBRAS)
# =============================================================================

DLP_PATTERNS = [
    {
        "name": "cpf",
        "regex": re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}'),
        "token": "[CPF_BLOQUEADO]",
        "classification": "Crítica",
        "is_substitution": False,
        "is_ot": False,
    },
    {
        "name": "platform",
        "regex": re.compile(r'(?i)\bP-\d{2,3}\b'),
        "token": "[ATIVO_RESTRITO]",
        "classification": "Alta",
        "is_substitution": False,
        "is_ot": False,
    },
    {
        "name": "well",
        "regex": re.compile(r'(?i)\bpo[çc]o\s+[a-z0-9-]+\b'),
        "token": "[ATIVO_RESTRITO]",
        "classification": "Estratégica",
        "is_substitution": False,
        "is_ot": False,
    },
    {
        "name": "password",
        "regex": re.compile(r'(?i)(senha|password)\s+([a-zA-Z0-9@#$!%^&*]+)'),
        "token": r'\1 [CREDENCIAL_BLOQUEADA]',
        "classification": "Crítica",
        "is_substitution": True,
        "is_ot": False,
    },
    {
        "name": "scada_command",
        "regex": re.compile(r'(?i)(modbus\s+fc\s*(5|6|15|16)|dnp3\s+outstation|opc\s*ua\s*anonymous)'),
        "token": "[COMANDO_OT_BLOQUEADO]",
        "classification": "Crítica",
        "is_substitution": False,
        "is_ot": True,
    },
    {
        "name": "seismic_data",
        "regex": re.compile(r'(?i)(3D\s*seismic|4D\s*seismic|OBN\s*position|DGPS\s*coordinate)'),
        "token": "[DADO_SISMICO_RESTRITO]",
        "classification": "Estratégica",
        "is_substitution": False,
        "is_ot": False,
    },
    {
        "name": "vendor_restricted",
        "regex": re.compile(r'(?i)(oceânica\s*engenharia|sa\s*exploration|oceanpact)'),
        "token": "[VENDOR_RESTRITO]",
        "classification": "Alta",
        "is_substitution": False,
        "is_ot": False,
    },
    {
        "name": "cnpj",
        "regex": re.compile(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}'),
        "token": "[CNPJ_BLOQUEADO]",
        "classification": "Crítica",
        "is_substitution": False,
        "is_ot": False,
    },
]


class DLPEngine:
    """
    Motor de Data Loss Prevention com pipeline de 3 estágios:
    
    Estágio 1 (REGEX):      Detecção rápida por padrões compilados
    Estágio 2 (SCORE):      Cálculo de threat score multi-feature  
    Estágio 3 (CLASSIFY):   Classificação e decisão de ação
    
    Complexidade temporal: O(n × p) por query
    Complexidade espacial: O(e) onde e = entidades detectadas
    """

    def __init__(self):
        self.patterns = DLP_PATTERNS
        self._total_redactions = 0
        self._total_queries = 0

    def redact(self, text: str) -> Tuple[str, List[RedactedEntity], List[str]]:
        """
        ESTÁGIO 1: Regex scan + redação.
        
        Retorna: (texto_sanitizado, entidades_redatadas, flags_anomalia)
        """
        sanitized = text
        entities: List[RedactedEntity] = []
        anomaly_flags: List[str] = []

        for pattern in self.patterns:
            for match in pattern["regex"].finditer(text):
                raw_value = match.group(0)

                if pattern["is_substitution"]:
                    sanitized = pattern["regex"].sub(pattern["token"], sanitized)
                    token_display = "[CREDENCIAL_BLOQUEADA]"
                else:
                    sanitized = sanitized.replace(raw_value, pattern["token"], 1)
                    token_display = pattern["token"]

                entities.append(RedactedEntity(
                    type=pattern["name"],
                    value=raw_value,
                    token=token_display,
                    classification=pattern["classification"],
                ))

                if pattern["is_ot"]:
                    anomaly_flags.append("ot_protocol_detected")
                    anomaly_flags.append("unauthorized_control_command")

        # Deduplicar entidades por valor
        seen = set()
        unique_entities = []
        for e in entities:
            key = e["value"].lower()
            if key not in seen:
                seen.add(key)
                unique_entities.append(e)

        self._total_redactions += len(unique_entities)
        self._total_queries += 1

        return sanitized, unique_entities, list(set(anomaly_flags))

    def compute_threat_score(
        self,
        entities: List[RedactedEntity],
        anomaly_flags: List[str],
        text: str,
        has_session: bool = True,
    ) -> float:
        """
        ESTÁGIO 2: Cálculo de threat score heurístico.
        
        Features:
          - Número de entidades sensíveis detectadas (peso: 0.10/entidade, max 0.40)
          - Protocolo OT detectado (peso: 0.50)
          - Comando de controle não-autorizado (peso: 0.30)
          - Comprimento anômalo da query (peso: 0.05)
          - Sessão ausente (peso: 0.45)
          - Classificação "Estratégica" presente (peso: 0.10)
        
        Score final: min(sum, 1.0)
        """
        score = 0.0

        # Feature 1: Quantidade de entidades
        score += min(len(entities) * 0.10, 0.40)

        # Feature 2: Protocolo OT
        if "ot_protocol_detected" in anomaly_flags:
            score += 0.50

        # Feature 3: Comando de controle
        if "unauthorized_control_command" in anomaly_flags:
            score += 0.30

        # Feature 4: Comprimento anômalo
        if len(text) > 200:
            score += 0.05

        # Feature 5: Sessão ausente
        if not has_session:
            score += 0.45

        # Feature 6: Dados estratégicos
        if any(e["classification"] == "Estratégica" for e in entities):
            score += 0.10

        return min(round(score, 2), 1.0)

    def decide_action(
        self,
        threat_score: float,
        anomaly_flags: List[str],
        has_session: bool,
    ) -> Tuple[str, str]:
        """
        ESTÁGIO 3: Matriz de decisão.
        
        Retorna: (operator_action, mitre_technique)
        """
        mitre_technique = None

        if not has_session:
            return "blocked", "T1078"

        if "ot_protocol_detected" in anomaly_flags:
            return "escalated", "T0831"

        if threat_score > 0.80:
            mitre_technique = "T1213"
            return "escalated", mitre_technique

        return "allowed", mitre_technique

    def full_pipeline(
        self,
        text: str,
        has_session: bool = True,
    ) -> dict:
        """
        Pipeline completo: REDACT → SCORE → DECIDE.
        Retorna dict com todos os resultados para injetar no AgenticState.
        """
        start = time.time()

        sanitized, entities, flags = self.redact(text)
        score = self.compute_threat_score(entities, flags, text, has_session)
        action, mitre = self.decide_action(score, flags, has_session)

        latency_ms = max(1, int((time.time() - start) * 1000))

        return {
            "dlp_sanitized_query": sanitized,
            "dlp_entities": entities,
            "dlp_anomaly_flags": flags,
            "dlp_threat_score": score,
            "dlp_action": action,
            "dlp_latency_ms": latency_ms,
            "mitre_technique": mitre,
            "data_leak_prevented": text != sanitized,
        }

    @property
    def stats(self) -> dict:
        """Estatísticas acumuladas do motor DLP."""
        return {
            "total_queries_processed": self._total_queries,
            "total_redactions": self._total_redactions,
            "avg_redactions_per_query": (
                round(self._total_redactions / max(self._total_queries, 1), 2)
            ),
        }


# =============================================================================
# AUDIT HASH CHAIN
# =============================================================================

def compute_audit_hash(previous_hash: str, row_data: dict) -> str:
    """
    Computa hash SHA-256 encadeado para integridade forense.
    Cada entrada referencia o hash da anterior → cadeia tamper-evident.
    
    Algoritmo:
      hash_n = SHA256(hash_{n-1} | session_id | device_id | query | timestamp)
    """
    payload = (
        f"{previous_hash}|"
        f"{row_data.get('session_id', 'N/A')}|"
        f"{row_data.get('device_id', 'N/A')}|"
        f"{row_data.get('original_query', 'N/A')}|"
        f"{row_data.get('created_at', 'N/A')}"
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def create_audit_entry(
    log_id: int,
    session_id: str,
    device_id: str,
    operator_id: str,
    original_query: str,
    dlp_result: dict,
    previous_hash: str,
) -> AuditEntry:
    """Cria uma entrada de auditoria com hash chain."""
    created_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    row_data = {
        "session_id": session_id,
        "device_id": device_id,
        "original_query": original_query,
        "created_at": created_at,
    }
    log_hash = compute_audit_hash(previous_hash, row_data)

    return AuditEntry(
        log_id=log_id,
        session_id=session_id,
        device_id=device_id,
        operator_id=operator_id,
        original_query=original_query,
        sanitized_query=dlp_result["dlp_sanitized_query"],
        data_leak_prevented=dlp_result["data_leak_prevented"],
        redaction_count=len(dlp_result["dlp_entities"]),
        redacted_entities=dlp_result["dlp_entities"],
        threat_score=dlp_result["dlp_threat_score"],
        anomaly_flags=dlp_result["dlp_anomaly_flags"],
        operator_action=dlp_result["dlp_action"],
        mitre_technique=dlp_result.get("mitre_technique"),
        latency_ms=dlp_result["dlp_latency_ms"],
        prev_log_hash=previous_hash,
        log_hash=log_hash,
        created_at=created_at,
    )
