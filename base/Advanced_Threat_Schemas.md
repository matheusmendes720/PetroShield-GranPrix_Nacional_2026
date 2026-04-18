# Advanced Threat & Deep Packet Inspection (DPI) Schemas

> [!WARNING]
> Esse documento descreve o modelo de dados semântico das ameaças complexas ("tricky expensive threats"). Estes schemas garantem que NENHUM DADO atravesse redes externas não documentadas sem análise prévia dos Agentes do Swarm.

## 1. A Filosofia "Drop-First" & Inspect

Dispositivos de Borda (*Edge Wearables* - como headsets industriais ou smartglasses operando em alto mar) não possuem *whitelist* contínua na internet pública pelo AxeGuard. 

O paradigma:
1. Requerimento de Saída (Ex: Query do Assitente NLP do HoloLens para traduzir manual russo de válvula).
2. Empacotamento das Metadados Locais.
3. DPI Proxy (DLP Guardian) disseca e bloqueia qualquer *fingerprint* ou IP sem verificação do *Supervisor_V2*.

## 2. Padrões de "Expensive Threats"

Ameaças caras se disfarçam de operações legítimas e escoam lentamente. Eis os schemas táticos usados para bombear o modelo de dados sintéticos (`synthetic_soc_dataset.json`):

### Schema: Operação `Stealth C2 Egress` (Wearables)
*   **Contexto:** Um Smartglass comprometido tenta enviar informações geo-sensíveis ("Seismic Data") durante requisições de DNS ou telemetria ping ordinárias.
*   **Target Device:** HoloLens 2, RealWear Nav.
*   **DPI Agent Action:**
    *   Lê a entropia da string.
    *   Faz a verificação do nível de acesso do Operador no Turno vs Nível Crítico dos dados tentados.
    *   **Resultado Operacional:** `BLOCK_AND_ISOLATE`.
*   **JSON Representation (Mock Payload):**
```json
{
  "event_id": "thr-9942a",
  "threat_type": "DNS_TUNNEL_EXFILTRATION",
  "source_device_profile": "RealWear_Nav500_Operator_XYZ",
  "payload_inspection": {
    "protocol": "DNS/UDP",
    "anomaly_type": "High Entropy Request",
    "decoded_sensitive_content": "[GEODATA_SEISMIC_BASIN_SANTOS_X_Y_Z]"
  },
  "blocked_by": "AGENT_DLP_GUARDIAN_v3",
  "estimated_financial_loss_prevented": 14500000.00
}
```

### Schema: Operação `OT-Over-IT Privilege Escalation`
*   **Contexto:** Um tablet IT comum acessando a planta Wi-Fi tenta invocar malformações de rede usando protocolos Modbus ou DNP3 encapsulados por baixo de pacotes HTTPS para os PLCs (Programmable Logic Controllers) de uma refinaria.
*   **Target Device:** Supervisor Tablet / Maintenance Laptop.
*   **DPI Agent Action:** Dissecação profunda de cabeçalhos HTTPS. Encontrando os opcodes típicos de SCADA (SCADA Read Holding Registers). 
*   **Resultado Operacional:** Triage cruzado (Supervisor envia alerta massivo em *Fire Petroleum Orange*), desconecta VLAN.
*   **JSON Representation (Mock Payload):**
```json
{
  "event_id": "thr-8012b",
  "threat_type": "OT_OVER_IT_BYPASS",
  "target_asset": "VALVE_ACTUATOR_V12_REMAN",
  "payload_inspection": {
    "protocol_encapsulation": "HTTPS(Port 443) -> DNP3(Port 20000)",
    "suspicious_opcodes": ["[SCADA_OVERRIDE_WRITE]"]
  },
  "agent_triage_actions": ["ISOLACAO_VLAN", "REVOGACAO_TOKEN_OAUTH"],
  "estimated_financial_loss_prevented": 300000000.00
}
```

## 3. O Ciclo de "Machine Learning" do Swarm
Ao isolar ameaças complexas, o `synthetic_gen_v4.ts` simula a troca de informações ("Agentic NLP Talk").
O `Immunizer_X` deve reportar:
> *"Pacote Anômalo dissecado de headset em Revap-02. Assinatura de túnel ICMP detectada contendo metadados JSON do atuador. Vacina aplicada na frota inteira. RSI incrementado em $4.2M."* 

As funções do backend que populam os logs consumirão rigorosamente esses Schemas estruturais para gerar visões de gráficos de barras coloridas precisas no Terminal.
