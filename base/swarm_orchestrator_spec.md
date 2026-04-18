# Specification: AxeGuard Swarm Agent Orchestration (v4.2)

Esta especificação define o protocolo de colaboração e a hierarquia de decisão para o enxame de agentes (**Swarm**) que opera no core do PetroShield SOC.

## 1. Arquitetura do Enxame (Swarm Topology)

O enxame opera sob um modelo de **Coordenação Descentralizada com Supervisor**, onde cada agente possui autonomia tática, mas reporta estados críticos a uma camada de orquestração superior.

### Roles & Responsabilidades

| Agente | Perfil | Responsabilidade Principal |
| :--- | :--- | :--- |
| **SUPERVISOR_V2** | Orchestrator | Gestão de estado global, roteamento de tarefas e consolidação de relatórios finais. |
| **DLP_GUARDIAN** | Triage / Policy | Inspeção de pacotes e strings para detecção de vazamentos de dados (Regex, NER). |
| **INTEL_HUNTER** | RAG / Context | Enriquecimento de alertas com base na base de conhecimento MITRE e dados OSINT. |
| **IMMUNIZER_X** | Action / Response | Geração de regras de contenção (firewall hashes, isolamento de nodes). |

---

## 2. Fluxo de Colaboração (Inter-Agent Protocol)

O fluxo de trabalho segue o "Storytelling Plot" definido pelo AxeGuard Engine:

1.  **DETECÇÃO:** `DLP_GUARDIAN` identifica um padrão anômalo (ex: *SMB Exploit*) nos Edge Nodes.
2.  **ESCALADA:** `SUPERVISOR_V2` recebe a telemetria e despacha a tarefa de análise para o `INTEL_HUNTER`.
3.  **ANÁLISE (RAG):** `INTEL_HUNTER` identifica a variante (ex: *LockBit v3.0*) e extrai TTPs (Táticas, Técnicas e Procedimentos).
4.  **DECISÃO:** `SUPERVISOR_V2` valida o risco financeiro e instrui o `IMMUNIZER_X` a agir.
5.  **AÇÃO:** `IMMUNIZER_X` gera o hash da regra de imunização e faz o broadcast para toda a frota multi-tenant.
6.  **FECHAMENTO:** `SUPERVISOR_V2` loga a conclusão e atualiza as métricas de "Downtime Saved".

---

## 3. Estruturas de Dados de Telemetria (Live Metrics Matriz)

Para alimentar as interfaces de alta densidade, o enxame gera matrizes de variância compostas por:

- **Fleet Health Matrix:** Composta por `[ID_Node, Latency, Auth_Status, Rule_Version]`.
- **Threat Vector Tensor:** Representa a intensidade do ataque em 3 eixos: `[Volume, Complexidade, Persistência]`.

## 4. Exemplos de Diálogo de Agentes (Agent Talk)

*Exemplos para o Dashboard Console:*

> **DLP_GUARDIAN:** "Anomalia detectada em Camaçari-01: Tentativa de travessia lateral SMB via porta 445."
> **SUPERVISOR_V2:** "Alerta recebido. INTEL_HUNTER, analise o payload para extração de TTP."
> **INTEL_HUNTER:** "Padrão identificado: LockBit v3.0. Recomendo isolamento imediato e geração de regra de imunização."
> **IMMUNIZER_X:** "Regra de imunização gerada. Propagando para os 50 nodes da frota..."

---
*Status: Especificação Técnica Aprovada para Implementação v4.2.*
