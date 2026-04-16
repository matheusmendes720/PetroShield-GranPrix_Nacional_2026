"""
openai_bridge.py — Adaptador OpenAI com Modo Mock/Live e Streaming
===================================================================
Encapsula a comunicação com a API da OpenAI com:
  - Modo MOCK: Respostas pré-programadas (determinísticas) para demo sem API key
  - Modo LIVE: Chamadas reais com streaming e function calling
  - Fallback automático: Se a chamada LIVE falhar, volta para MOCK

Dependência: openai (opcional — o modo mock funciona sem ela)
"""

import json
import time
from typing import Optional, Dict, List, Any, Generator


# Importação condicional da OpenAI
try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


# =============================================================================
# RESPOSTAS MOCK PRÉ-PROGRAMADAS (DETERMINÍSTICAS)
# =============================================================================

MOCK_RESPONSES: Dict[str, Dict[str, str]] = {
    # Agent_Intel_Cloud — Análise de ameaça T0831 (Modbus)
    "analyze_threat_ot": {
        "thought": (
            "Recebi payload com hash SHA256:7f3a2b do edge em 10.0.1.47. "
            "O comando Modbus FC16 (Write Multiple Registers) foi detectado em uma query de LLM. "
            "Isso indica tentativa de manipulação de controle industrial via canal de IA. "
            "Consultando base MITRE ATT&CK for ICS..."
        ),
        "classification": (
            "CLASSIFICAÇÃO TTP:\n"
            "  Técnica Primária: T0831 — Manipulation of Control\n"
            "  Tática: Impact\n"
            "  Técnica Secundária: T0853 — Scripting (via LLM prompt)\n"
            "  Plataformas afetadas: Field Controller/RTU/PLC, Safety System\n"
            "  Kill Chain: Reconnaissance → Initial Access (T1078) → Execution (T0831) → Impact\n"
            "  Confiança: 0.98 (acima do threshold de auto-vaccinação: 0.85)"
        ),
        "vaccine": (
            "VACINA GERADA:\n"
            "  Hash: SHA256:ab9f32c8e7d1f05a23b891c4d6e7890f1234abcd5678ef90\n"
            "  Regra: BLOCK Modbus FC5/FC16 em todas as interfaces de perímetro\n"
            "  Portas: [502, 503, 8502]\n"
            "  Protocolo: Modbus/TCP\n"
            "  Ação: Drop + Log + Alert SOC"
        ),
    },

    # Agent_Intel_Cloud — Análise de ameaça T1078 (Acesso não-autorizado)
    "analyze_threat_auth": {
        "thought": (
            "Dispositivo quest-vr-001 tentou acessar a API sem credenciais. "
            "O device está marcado como 'compromised' no MDM registry. "
            "Sem enrollment, sem MFA, network_segment = Vendor_VPN. "
            "Verificando correlações com incidentes anteriores..."
        ),
        "classification": (
            "CLASSIFICAÇÃO TTP:\n"
            "  Técnica: T1078 — Valid Accounts (subtécnica: .004 Cloud Accounts)\n"
            "  Tática: Persistence\n"
            "  Confiança: 0.94\n"
            "  Indicadores: Device não-registrado, ausência de MDM, segmento Vendor_VPN\n"
            "  Recomendação: Verificar se o dispositivo é de um vendor comprometido"
        ),
    },

    # Agent_CLevel_Reporter — Relatório financeiro
    "financial_report": {
        "report": (
            "RELATÓRIO EXECUTIVO — PetroShield SOC\n"
            "====================================\n"
            "Período: Últimos 60 segundos de demonstração\n\n"
            "INCIDENTES NEUTRALIZADOS: 4\n"
            "DOWNTIME EVITADO: 14.5 horas\n"
            "FATURAMENTO PROTEGIDO: R$ 580.000,00\n"
            "RISCO DE RECUPERAÇÃO EVITADO: R$ 450.000,00\n\n"
            "CONFORMIDADE:\n"
            "  LGPD: ✅ Nenhum dado pessoal alcançou endpoints externos\n"
            "  ANPD: ✅ Notificação automática configurada (3 dias úteis)\n"
            "  ANP 882: ✅ Vendors avaliados em tempo real\n\n"
            "ROI DA SESSÃO: 103.000% sobre assinatura mensal (R$ 1.000/mês)"
        ),
    },

    # Agent_Intel_Cloud — Resposta de LLM sanitizada
    "sanitized_llm_response": {
        "response": (
            "Sou o Copilot Corporativo PetroShield operando em modo seguro. "
            "Recebi sua consulta técnica. Os dados de ativos e credenciais foram "
            "redatados pelo AxeGuard antes de chegarem a este endpoint privado. "
            "Posso ajudá-lo com informações genéricas sobre procedimentos operacionais, "
            "manutenção preventiva e protocolos de segurança, sem expor dados classificados."
        ),
    },
}


class OpenAIBridge:
    """
    Adaptador OpenAI com modo mock/live.
    
    Modo MOCK (default): Respostas determinísticas para demonstração.
    Modo LIVE: Chamadas reais à OpenAI API com streaming.
    Modo HYBRID: Tenta LIVE, fallback para MOCK em caso de erro.
    
    Uso:
        bridge = OpenAIBridge(mode="mock")
        response = bridge.reason("system prompt", "user context", scenario_key="analyze_threat_ot")
    """

    def __init__(self, mode: str = "mock", model: str = "gpt-4o-mini"):
        """
        Parâmetros:
          mode: "mock" | "live" | "hybrid"
          model: Modelo OpenAI para modo live (ex: "gpt-4o", "gpt-4o-mini")
        """
        self.mode = mode
        self.model = model
        self.client = None
        self._call_count = 0
        self._token_count = 0

        if mode in ("live", "hybrid"):
            if not HAS_OPENAI:
                print("[WARN] openai não instalada. Usando modo mock como fallback.")
                self.mode = "mock"
            else:
                try:
                    self.client = OpenAI()
                except Exception as e:
                    print(f"[WARN] Falha ao inicializar OpenAI client: {e}. Usando modo mock.")
                    self.mode = "mock"

    def reason(
        self,
        system_prompt: str,
        user_context: str,
        scenario_key: str = "",
        tools: Optional[List[dict]] = None,
    ) -> dict:
        """
        Executa raciocínio via LLM.
        
        Retorna dict com chaves variáveis dependendo do cenário.
        Em modo mock, retorna a resposta pré-programada correspondente.
        """
        self._call_count += 1

        if self.mode == "mock":
            return self._mock_response(scenario_key)

        if self.mode == "live":
            return self._live_response(system_prompt, user_context, tools)

        # Modo hybrid: tenta live, fallback mock
        try:
            return self._live_response(system_prompt, user_context, tools)
        except Exception as e:
            print(f"[WARN] OpenAI call failed: {e}. Falling back to mock.")
            return self._mock_response(scenario_key)

    def stream_reason(
        self,
        system_prompt: str,
        user_context: str,
    ) -> Generator[str, None, None]:
        """
        Streaming de raciocínio via LLM (modo live apenas).
        Retorna gerador de chunks de texto para typewriter effect.
        """
        if self.mode == "mock" or not self.client:
            # Simula streaming com chunks de palavras
            mock_text = MOCK_RESPONSES.get("sanitized_llm_response", {}).get("response", "...")
            for word in mock_text.split():
                yield word + " "
                time.sleep(0.03)  # Simula latência de streaming
            return

        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_context},
                ],
                stream=True,
                max_tokens=500,
                temperature=0.3,
            )
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"[Erro de streaming: {e}. Modo mock ativado.]"

    def _mock_response(self, scenario_key: str) -> dict:
        """Retorna resposta mockada determinística."""
        return MOCK_RESPONSES.get(scenario_key, {
            "response": "Mock response — cenário não catalogado.",
        })

    def _live_response(
        self,
        system_prompt: str,
        user_context: str,
        tools: Optional[List[dict]] = None,
    ) -> dict:
        """Chamada real à OpenAI API."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_context},
        ]

        kwargs = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.3,
            "max_tokens": 1000,
        }

        if tools:
            kwargs["tools"] = tools

        response = self.client.chat.completions.create(**kwargs)
        choice = response.choices[0]

        self._token_count += (response.usage.total_tokens if response.usage else 0)

        result = {"response": choice.message.content or ""}

        if choice.message.tool_calls:
            result["tool_calls"] = [
                {
                    "name": tc.function.name,
                    "arguments": json.loads(tc.function.arguments),
                }
                for tc in choice.message.tool_calls
            ]

        return result

    @property
    def stats(self) -> dict:
        """Estatísticas de uso da bridge."""
        return {
            "mode": self.mode,
            "model": self.model,
            "total_calls": self._call_count,
            "total_tokens": self._token_count,
        }
