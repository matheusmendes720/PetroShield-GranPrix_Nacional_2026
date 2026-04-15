# [E1] Entrega: Ideação + Lean Canvas

## Grand Prix SENAI de Inovação 2026 — Desafio Petrobras

**Projeto:** PetroShield — AxeGuard Middleware
**Escuderia:** Camaçari Shield | SENAI CIMATEC
**Tema:** Cibersegurança & Ética Digital
**Data:** Abril/2026

---

## 🛡️ Descrição Executiva da Solução

O **AxeGuard** é um Middleware de Cibersegurança Adaptativo projetado especificamente para o ecossistema operacional da **Petrobras** — a maior produtora de petróleo em águas profundas do mundo e responsável por **~70% do superávit comercial brasileiro** em 2026.

A solução opera sob o paradigma **Zero-Trust** e atua como uma camada de **Prevenção de Perda de Dados (DLP) em tempo real** sobre o tráfego de pacotes gerado por **dispositivos móveis e wearables XR de terceiros** que acessam dados sensíveis da operação. Isso inclui óculos inteligentes (HoloLens 2, RealWear), tablets e smartphones de prestadores em plataformas FPSO, bases de exploração sísmicas e centros logísticos integrados à cadeia operacional da Petrobras.

O contexto é inequívoco: em **novembro de 2025**, o grupo Everest Ransomware penetrou os sistemas da **SA Exploration** — fornecedora de levantamento sísmico da Petrobras — e exfiltrou **90GB de dados estratégicos** da Bacia de Campos (coordenadas DGPS, posições OBN, parâmetros 3D/4D) via credenciais de VPN comprometidas, **sem nenhum MFA, DLP ou monitoramento ativo**. O AxeGuard é a resposta direta a essa falha sistêmica.

---

## 📊 Blocos do LEAN CANVAS — Foco Petrobras

---

### 01 🔴 Problema e Alternativas Existentes

#### O Problema Central: A Superfície de Ataque da Cadeia Petrobras

A Petrobras opera com um ecossistema de **mais de 10.000 fornecedores ativos**, sendo:

- **~500 vendors críticos** (Tier 1) com acesso direto a redes OT/IT
- **~2.000 vendors de alto acesso** com dados sísmicos, de poços ou de plataformas
- **~3.000 vendors internacionais** (30%) sujeitos a transferências transfronteiriças LGPD

Em suas operações de E&P (US$ 69,2B de capex 2026-2030), a Petrobras emprega diariamente **centenas de técnicos terceirizados** em:

- Plataformas FPSO e semi-submersíveis (pre-sal: Búzios, Mero, Sepetiba, Almirante Tamandaré)
- Navios de suporte offhore (Oceânica Engenharia: R$4,2B; OceanPact/CBO: R$3,2B)
- Bases sísmicas e centros de análise geológica (contratadas como SA Exploration)
- Refinarias e centros logísticos (RTM: US$15,8B de capex)
- Centros de inteligência de dados (Libra Rocks: R$151M em IA/ML para o pre-sal)

Esses técnicos e parceiros utilizam **dispositivos móveis de terceiros** — tablets, smartphones, óculos AR/VR — para acessar sistemas críticos, consultar assistentes de IA via voz e transmitir dados operacionais. Nenhum desses fluxos é monitorado por DLP adequado.

#### O Vetor de Ataque Triplo ("Triple Surface")

```
SUPERFÍCIE 1 — CAPTURA NO DISPOSITIVO (Bio-Visual-Acústica)
├── Câmera: gravação de telas SCADA, coordenadas de poços, layouts de plataforma
├── Microfone: captura de senhas verbalizadas, comandos operacionais, nomes de ativos
├── Eye-tracking: padrões de atenção do operador ≈ PII não anonimizável
└── Mapeamento espacial: exposição de zonas restritas de FPSOs e plataformas

SUPERFÍCIE 2 — PIPELINE DE IA/LLM (Exfiltração via Prompt)
├── Queries de voz contendo nomes de ativos: "Plataforma P-93", "Poço Tupi-10"
├── Prompts não sanitizados enviados a APIs LLM externas (OpenAI, Anthropic)
├── Retenção de dados de treinamento por vendors (risco de residência de dados)
└── Prompt injection atacando o comportamento do assistente de campo

SUPERFÍCIE 3 — LATERAL MOVEMENT OT/ICS (Dispositivo → Núcleo)
├── Dispositivo XR comprometido como pivô na rede corporativa/VPN da plataforma
├── Apps sideloaded com capacidade de scan de rede (Modbus TCP 502, DNP3 20000)
├── Redes OT planas (flat networks) permitindo acesso a PLCs de wellheads
└── Túneis Shadow IT de apps de vendors bypassando visibilidade do SOC
```

#### Impacto Financeiro Direto para Petrobras

| Tipo de Falha                | Custo Estimado                   | Referência Real                               |
| :--------------------------- | :------------------------------- | :--------------------------------------------- |
| Breach de dados via vendor   | US$ 10–25M por incidente        | SA Exploration, Nov/2025                       |
| Multa ANPD (Lei 15.352/2026) | Até 2% da receita / R$50M       | Autarquia Especial ativo                       |
| Multa ANP (Res. 882/2022)    | Variável — danos operacionais  | Obrigação regulatória                       |
| Dano reputacional (mercado)  | Incalculável — PETR4 sensível | SA Exploration coincidiu com descoberta Campos |
| VaR 95% supply chain anual   | ~US$ 500M                        | Modelo econométrico interno                   |

#### Alternativas Existentes (e por que falham para Petrobras)

| Alternativa Atual                 | Falha Crítica no Contexto Petrobras                                                            |
| :-------------------------------- | :---------------------------------------------------------------------------------------------- |
| MDM genérico (Intune, Jamf)      | Não tem DLP de conteúdo semântico para entidades do setor de energia                         |
| SOC tradicional enterprise        | R$50k+/mês; latência de resposta incompatível com operação offshore em tempo real          |
| DLP corporativo padrão (Purview) | Não cobre fluxos de prompt para LLMs; não detecta vazamento acústico-visual                  |
| Avaliação anual de vendors      | Detecção média de breach:**287 dias** (IBM 2025). SA Exploration levou dias sem alerta |
| Segmentação de rede legacy      | Redes OT planas em plataformas de 15-20 anos permitem movimento lateral direto                  |

---

### 02 🟢 Solução — AxeGuard: DLP Proxy Adaptativo para o Ecossistema Petrobras

O AxeGuard intercepta, inspeciona e sanitiza **todas as transmissões de dados** originadas em dispositivos móveis/XR de terceiros antes que atinjam qualquer sistema sensível — seja um LLM de campo, um repositório de dados sísmicos ou uma rede OT industrial.

#### Camadas de Proteção

**Camada 1 — Autenticação Zero-Trust por Device Flow (OAuth 2.0 RFC 8628)**

- Nenhuma credencial digitada no dispositivo (elimina shoulder-surfing)
- Aprovação via smartphone corporativo do operador (canal separado)
- Sessões com TTL limitado + revogação instantânea via Redis
- Kiosk Mode obrigatório (ArborXR/Hexnode) — sem acesso a outros apps

**Camada 2 — DLP Proxy em Tempo Real (FastAPI + spaCy)**

- Intercepta todo tráfego de voz→texto e texto→LLM gerado pelo dispositivo
- Pipeline híbrido: Regex rápido + NER (Named Entity Recognition) semântico
- Dicionário de entidades sensíveis específico da Petrobras:

```python
PETROBRAS_SENSITIVE_ENTITIES = {
    "plataformas":  r"(?i)\bp-\d{2,3}\b",          # P-93, P-10, FPSO Carioca
    "pocos":        r"(?i)\bpo[çc]o\s+[a-z0-9-]+",  # Poço Tupi-10, Poço alfa-bravo
    "bacias":       ["Campos", "Santos", "pré-sal", "Tupi", "Búzios", "Mero"],
    "coordenadas":  r"-?\d{1,3}\.\d+,\s*-?\d{1,3}\.\d+",  # DGPS coords
    "ot_commands":  ["Function Code 16", "DNP3", "Modbus", "FCxx", "register"],
    "vendors_criticos": ["Oceânica", "SA Exploration", "OceanPact", "Subsea 7"],
    "credenciais":  r"\d{3}\.\d{3}\.\d{3}-\d{2}",  # CPF
}
# Saída: [ATIVO_RESTRITO], [COORD_BLOQUEADA], [CREDENCIAL_MASCARADA]
```

**Camada 3 — Monitoramento Comportamental de Vendors (Vendor Risk Graph)**

- Score de risco contínuo (0–100) para cada vendor da cadeia Petrobras
- Integração com dark web monitoring: alerta imediato sobre credenciais vazadas
- Modelo de risco ponderado: acesso OT (25%) + histórico de incidentes (20%) + maturidade (20%)
- Cascata automática: se vendor comprometido → suspensão de sessões XR associadas

**Camada 4 — Conformidade Regulatória Automatizada (LGPD + ANP + ANPD)**

- Geração automática de notificações ANPD (prazo: 3 dias úteis — Res. 15/2024)
- Registros LGPD Art. 37 para todos os fluxos de processamento de dados de campo
- Relatório estruturado ANP Res. 882/2022 com evidências forenses
- SCC ANPD para transferências internacionais (Res. 19/2024)

---

### 03 📈 Métricas-Chave — Linguagem C-Level Petrobras

| Métrica Técnica                                | Tradução para o Negócio Petrobras         | Meta                                               |
| :----------------------------------------------- | :------------------------------------------- | :------------------------------------------------- |
| **MTTD (Mean Time to Detect)**             | De 287 dias (atual) para < 60 segundos       | Elimina janela Everest/SA Exploration              |
| **Taxa de redução de incidentes vendor** | De 1,5 incidentes/ano para 0,3 (-80%)        | VaR supply chain: US$500M → US$100M               |
| **Cobertura DLP de prompts**               | 100% dos fluxos LLM monitorados              | Zero prompts com dados estratégicos não redacted |
| **Uptime SLA de autenticação**           | 99,95% — crítico para ops offshore 24/7    | Sem impacto na produção de 2,4M bpd              |
| **Conformidade ANPD**                      | Notificação automática em < 3 dias úteis | Evita multas de até R$50M por incidente           |
| **ROI**                                    | 320% — break-even em < 12 meses             | US$ 5M investimento vs. US$ 21M/ano economizados |

---

### 04 💎 Proposta de Valor Única e Conceito de Alto Nível

> **UVP:** O único middleware que entende o vocabulário operacional da Petrobras — de coordenadas DGPS de poços do pre-sal a comandos Modbus de wellheads em FPSOs — e bloqueia o vazamento desses dados em tempo real, mesmo quando o vetor de exfiltração é a voz de um técnico terceirizado consultando um assistente de IA de campo.

**Conceito de Alto Nível:** Uma "membrana inteligente e invisível" que se posiciona entre cada dispositivo móvel de terceiro e qualquer sistema crítico da Petrobras — filtrando dados estratégicos de exploração, protegendo segredos industriais do pre-sal e garantindo que os US$109B do Business Plan 2026-2030 sejam protegidos por uma camada de segurança proporcional à sua magnitude.

**A diferença decisiva:** Enquanto soluções genéricas protegem "dados corporativos", o AxeGuard protege **ativos de soberania nacional** — a tecnologia de águas profundas que posiciona o Brasil entre os 5 maiores produtores de petróleo do mundo.

---

### 05 🔐 Vantagem Injusta — Por Que Ninguém Mais Faz Isso

**1. Especialização Semântica no Domínio Oil & Gas**
O dicionário de entidades sensíveis do AxeGuard é construído a partir da inteligência real da cadeia operacional da Petrobras: nomes de FPSOs, bacias sedimentares, protocolos OT (Modbus/DNP3/OPC UA), vendors do Petronect, e padrões de dados sísmicos 3D/4D. Nenhuma solução genérica de DLP chega nesse nível de especificidade.

**2. Arquitetura Multi-Tenant Escalável para 10.000+ Vendors**
O motor centralizado na nuvem (arquitetura multi-tenant) permite processar a telemetria de toda a cadeia de fornecedores da Petrobras massificadamente. Se um vendor é comprometido, **a defesa de todos os 10.000 é atualizada em segundos** — inteligência cooperativa com custo operacional pulverizado.

**3. Cobertura da "Triple Surface" — O Gap que Ninguém Monitora**
A convergência de IA assistiva (voice-to-text) + dispositivos XR + redes OT cria três superfícies de ataque simultâneas que nenhum produto COTS endereça de forma integrada. O AxeGuard é arquitetado especificamente para esta interseção.

**4. Integração Nativa com o Ecossistema Regulatório Brasileiro**
LGPD Art. 37, ANPD Res. 15/2024, ANP Res. 882/2022, Decreto 12.572/2025 (PNSI), Decreto 12.573/2025 (ENaC) — o AxeGuard gera automaticamente os artefatos de conformidade exigidos pelo marco regulatório brasileiro, eliminando o overhead jurídico que soluções estrangeiras não conseguem endereçar.

---

### 06 📡 Canais — Rota de Entrada na Petrobras

| Canal                                                  | Estratégia Específica                                                         | Gatilho                    |
| :----------------------------------------------------- | :------------------------------------------------------------------------------ | :------------------------- |
| **Grand Prix SENAI 2026**                        | Pitch direto para juízes Petrobras com demo live do AxeGuard                   | Evento abril/2026          |
| **Petronect (Marketplace Petrobras)**            | Cadastro como solução de cibersegurança para vendors Tier 1                  | 104+ transações/2025     |
| **Parceria SENAI-Petrobras (Autonomia e Renda)** | Programa de 10k+ jovens em TI/Telecom — canal de penetração talent           | Março/2026 ativo          |
| **Programa ENFUSE/Unicamp**                      | Incubação como hard tech startup para setor energético                       | Parceria Petrobras/Unicamp |
| **Projeto 3W (Open Innovation)**                 | Submissão como solução para desafio técnico de supply chain security        | Plataforma ativa           |
| **Novo Diretor de Logística**                   | Angelica Laureano (desde abr/2026): foco em supply chain = janela de prioridade | Mudança de liderança     |

---

### 07 🎯 Segmentos de Clientes e Primeiros Adotantes

#### Cliente Principal: Petrobras S.A.

| Atributo                                   | Dado                                              |
| :----------------------------------------- | :------------------------------------------------ |
| **Capitalização**                  | ~R$640B (~US$120B)                                |
| **Lucro Líquido 2025**              | US$19,6B (+160% YoY)                              |
| **Produção**                       | 2,4M bpd (recorde histórico)                     |
| **Plano de investimentos 2026-2030** | US$109B                                           |
| **Meta de otimização de custos**   | US$12B de economia operacional                    |
| **Ecossistema de vendors**           | 10.000+ ativos / ~US$45B gasto/ano                |
| **Exposição cyber (VaR 95%)**      | ~US$500M/ano em perdas potenciais de supply chain |

**Por que a Petrobras é o early adopter ideal:**

- Motivação urgente pós-breach SA Exploration (nov/2025): mandato executivo para inovação em segurança
- Nova liderança (Pogliese/Laureano, abr/2026): janela de priorização de novas iniciativas
- Capacidade financeira: US$27B em caixa, alavancagem de apenas 0,4x Dívida/EBITDA
- Pressão regulatória: ANPD como autarquia especial + ANP Res. 882 = urgência de compliance

#### Cadeia de Parceiros Logísticos e de Inteligência — Alvos Secundários

O problema de vazamento de dados via dispositivos móveis de terceiros não é exclusivo da Petrobras: ele percorre **toda a sua cadeia operacional**. Os seguintes parceiros são alvos naturais de expansão:

| Empresa                                          | Tipo de Parceria                      | Superfície de Exposição                          | Risco de Vazamento                           |
| :----------------------------------------------- | :------------------------------------ | :-------------------------------------------------- | :------------------------------------------- |
| **Oceânica Engenharia**                   | Navios subsea (R$4,2B até 2031)      | Conectividade real-time para plataformas offshore   | CRÍTICO — acesso OT direto                 |
| **OceanPact/CBO**                          | Maior frota OSV do Brasil (R$3,2B)    | Logística de suporte offshore                      | CRÍTICO — dados de posicionamento          |
| **Subsea 7 / TechnipFMC**                  | Engenharia subsea multi-bilionária   | Dados de equipamentos, specs de wellheads           | ALTO                                         |
| **Empresas de levantamento sísmico**      | Contratos de aquisição de dados     | Dados sísmicos 3D/4D — ativo estratégico máximo | CRÍTICO (SA Exploration: 90GB)              |
| **Parceiros de IA/ML**                     | Projeto Libra Rocks (R$151M)          | Dados geológicos pro-sal em pipelines MLOps        | ALTO — risco de treinamento não autorizado |
| **Provedores de cloud (AWS/Azure Brasil)** | Transformação digital Petrobras     | Dados sísmicos em multi-cloud                      | ALTO — soberania de dados                   |
| **Integradoras SAP/ERP**                   | Financeiro, procurement, supply chain | Dados de contratos, CAPEX, inventário              | MÉDIO-ALTO                                  |

---

### 08 💰 Estrutura de Custos

**Filosofia:** Arquitetura cloud-native com OPEX concentrado em processamento de telemetria — sem dependência de hardware proprietário em plataformas offshore (onde reposição é logisticamente proibitiva).

| Componente                                               | Natureza      | Racional                                                                                |
| :------------------------------------------------------- | :------------ | :-------------------------------------------------------------------------------------- |
| **DLP Proxy Engine (FastAPI + spaCy NER)**         | OPEX cloud    | Processamento massificado multi-tenant dos fluxos de 10.000+ vendors                    |
| **LLM Privado (Azure OpenAI — Private Endpoint)** | OPEX cloud    | Endpoint privado com B2B no-train clause — dados Petrobras nunca treinam modelo vendor |
| **Vendor Risk Graph (PostgreSQL + TimescaleDB)**   | OPEX cloud    | Time-series para scoring contínuo de 10.000+ vendors                                   |
| **Dark Web Monitoring (integração APIs)**        | OPEX SaaS     | Alertas de credenciais comprometidas em tempo real                                      |
| **Compliance Ledger (append-only + hash chain)**   | OPEX cloud    | Auditoria LGPD/ANP tamper-evident                                                       |
| **Certificação e onboarding de vendors**         | OPEX serviço | Integração Petronect + SAP + Active Directory                                         |

**Diferencial de custo:** A arquitetura multi-tenant dilui o custo operacional entre todos os vendors monitorados. O custo marginal de adicionar o 5.001º vendor ao monitoramento é próximo de zero.

---

### 09 💵 Fluxos de Receita

| Modelo                                               | Estrutura                                                                      | Escala Petrobras                                    |
| :--------------------------------------------------- | :----------------------------------------------------------------------------- | :-------------------------------------------------- |
| **Security as a Service (SaaS) — Enterprise** | Contrato anual por volume de vendors monitorados                               | R$2–5M/ano para cobertura de 500 vendors críticos |
| **Platform License — Full Ecosystem**         | Cobertura total dos 10.000+ vendors Petrobras                                  | R$10–20M/ano (benchmark: ROI 320% projetado)       |
| **Setup & Integration Fee (One-time)**         | Onboarding, integração Petronect/SAP, configuração de entidades sensíveis | R$3–5M                                             |
| **Compliance Reports (Pay-per-use)**           | Relatórios ANPD/ANP automatizados sob demanda                                 | R$50–200k/relatório                               |
| **Vendor Certification Program**               | Avaliação e onboarding seguro de novos vendors                               | R$10–50k/vendor certificado                        |

**Total Addressable Market (Petrobras):** US$45B em gastos anuais com vendors → 0,01% em segurança de DLP = US$4,5M/ano. Patamar conservador, muito abaixo do custo de um único breach.

---

## 🗺️ Contexto Estratégico: Por Que Esse Problema É Urgente AGORA

```
CONVERGÊNCIA DE FATORES — Abril 2026
════════════════════════════════════════════════════════════

FATOR 1 — BREACH RECENTE (Urgência Executiva)
  • Nov/2025: Everest Ransomware → SA Exploration → 90GB dados Petrobras
  • Vetor: VPN sem MFA, sem DLP, sem monitoramento comportamental
  • Dado: Coordenadas sísmicas Bacia de Campos = ativo de soberania nacional

FATOR 2 — ESCALONAMENTO REGULATÓRIO (Custo de Inação Cresce)
  • Jan/2026: Lei 15.352 → ANPD vira Autarquia Especial (multas até 2% receita)
  • Ativo: Res. ANPD 15/2024 — notificação de breach em 3 dias úteis
  • Ativo: ANP Res. 882/2022 — relatório de incidente obrigatório setor O&G

FATOR 3 — EXPANSÃO DA SUPERFÍCIE DE ATAQUE (Business Plan)
  • US$109B em investimentos 2026-2030 → mais plataformas, mais vendors, mais dispositivos
  • Pico de produção: 2,7M bpd (2028) → mais operadores de campo com acesso a dados
  • Libra Rocks R$151M: IA/ML sobre dados sísmicos ultra-sensíveis

FATOR 4 — AMEAÇAS ATIVAS EM ESCALONAMENTO
  • Abr/2026: CISA alerta APTs iranianos atacando PLCs de infraestrutura crítica
  • Ativo: Storm-1175/Medusa ransomware com foco em América Latina
  • Ativo: Boeing RFQ Campaign — phishing de documentos para suppliers industriais
  • XENOTIME (Dragos): APT nível crítico com TTPs de targeting de SIS (Safety Systems)

FATOR 5 — JANELA DE LIDERANÇA (Oportunidade de Influência)
  • Abr/2026: Novo Chairman Marcelo Pogliese → novas prioridades estratégicas
  • Abr/2026: Nova Diretora de Logística Angelica Laureano → foco em supply chain
  • Histórico: Mudanças de liderança precedem novas iniciativas de cibersegurança
```

---

## 🔗 Mapeamento MITRE ATT&CK — Cadeia de Ataque Petrobras

| Fase MITRE     | Técnica                    | ID    | Superfície Petrobras                           | Controle AxeGuard                              |
| :------------- | :-------------------------- | :---- | :---------------------------------------------- | :--------------------------------------------- |
| Initial Access | External Remote Services    | T1133 | VPN de vendors sísmicos (ex: SA Exploration)   | OAuth Device Flow + JIT access                 |
| Initial Access | Supply Chain Compromise     | T1195 | Vendors Tier 1 com acesso OT                    | Vendor Risk Graph contínuo                    |
| Persistence    | Valid Accounts              | T1078 | Credenciais legítimas de vendors comprometidas | Behavioral analytics + revogação automática |
| Collection     | Data from Info Repositories | T1213 | Servidores de dados sísmicos Campos Basin      | DLP Proxy — bloqueio de download massivo      |
| Collection     | Audio Capture               | T1123 | Microfone de dispositivos XR em área restrita  | DLP de áudio — STT local + mascaramento      |
| Exfiltration   | Exfil Over C2 Channel       | T1041 | Tunelamento via apps de vendor                  | Egress filtering + ZTNA                        |
| ICS — Impair  | Manipulation of Control     | T0835 | PLCs de wellheads via Modbus plano              | Proxy bloqueia commands ICS em prompts LLM     |
| ICS — Impact  | Theft of Operational Info   | T0817 | Dados sísmicos, coordenadas DGPS, OBN          | DLP bidirecional (request + response)          |

---

## 📐 Arquitetura Conceitual

```
                    ┌──────────────────────────────────────────────┐
                    │         ECOSISTEMA OPERACIONAL PETROBRAS      │
                    │  (FPSOs, Plataformas Pre-sal, Bases Sísmicas) │
                    └────────────────────┬─────────────────────────┘
                                         │
                    ┌────────────────────▼─────────────────────────┐
                    │         DISPOSITIVOS DE TERCEIROS             │
                    │  HoloLens2 | RealWear | Tablets | Smartphones │
                    │    (Técnicos de Oceânica, SA Exp., Subsea 7)  │
                    └────────────────────┬─────────────────────────┘
                                         │  Todo o tráfego passa aqui
                                         ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                         AxeGuard MIDDLEWARE                             │
├──────────────┬──────────────┬────────────────┬──────────────────────────┤
│ Auth Gateway │  DLP Proxy   │  Threat Intel  │    Compliance Engine     │
│ OAuth 2.0    │ FastAPI +    │  Vendor Risk   │  LGPD Art.37 | ANP 882   │
│ Device Flow  │ spaCy NER    │  Graph + Dark  │  ANPD Notif. Automática  │
│ Kiosk Mode   │ Regex + NLP  │  Web Monitor   │  Hash-chain Audit Log    │
└──────────────┴──────────────┴────────────────┴──────────────────────────┘
                                         │
                    ┌────────────────────▼─────────────────────────┐
                    │          BACKEND PRIVADO PETROBRAS            │
                    │  Azure OpenAI (Private Endpoint, No-Train)    │
                    │  Repositórios Sísmicos | SCADA/OT Networks    │
                    │  SAP/ERP | Petronect | Active Directory       │
                    └──────────────────────────────────────────────┘
```

---

## 📎 Referências de Inteligência Utilizadas

> *Este Lean Canvas foi construído sobre inteligência verificada, não sobre suposições de mercado.*

| Dado                                       | Fonte                                                                         | Relevância                     |
| :----------------------------------------- | :---------------------------------------------------------------------------- | :------------------------------ |
| Breach SA Exploration 90GB, nov/2025       | `01_Intel_OSINT/Petrobras_Supply_Chain_Vendor_Intelligence.md`              | Funda o caso de uso central     |
| 10.000+ vendors, US$45B gasto/ano          | `05_Market_Intelligence/Econometric_Analysis_Global_to_Petrobras.md`        | Escala do TAM                   |
| "Triple Surface" attack vector XR          | `04_BI_Ofensivo/XR_EdgeSecurity_DeepResearch_AxeGuard_DataModel.md`         | Framework técnico da solução |
| Threat actors: XENOTIME, Everest, APT Irã | `04_BI_Ofensivo/Strategic_Proposal_Petrobras_CyberSec_Grand_Prix_2026.md`   | Contexto de ameaça ativa       |
| LGPD Res.15/2024, ANP 882, Lei 15.352/2026 | `03_Arquitetura_Projeto/Technical_Deep_Dive_SCADA_LGPD_MITRE.md`            | Marco regulatório              |
| Business Plan 2026-2030 US$109B            | `04_BI_Ofensivo/OSINT_Deep_Research_Report_Petrobras_Cybersec_Hackathon.md` | Contexto financeiro             |
| Pogliese/Laureano (liderança abr/2026)    | `01_Intel_OSINT/Latest_Intelligence_Brief_April_2026.md`                    | Janela estratégica             |
| VaR supply chain US$500M (95%)             | `05_Market_Intelligence/Econometric_Analysis_Global_to_Petrobras.md`        | Quantificação de risco        |
| Modbus/DNP3/OPC UA vulnerabilidades OT     | `03_Arquitetura_Projeto/Technical_Deep_Dive_SCADA_LGPD_MITRE.md`            | Fundo técnico OT               |
| Oceânica R$4,2B / OceanPact R$3,2B        | `01_Intel_OSINT/Petrobras_Supply_Chain_Vendor_Intelligence.md`              | Vendors críticos identificados |

---

*Documento gerado por: PetroShield Research Automation Pipeline*
*Versão: 2.0 — Refatoração para foco exclusivo Petrobras*
*Data: Abril 2026 | Classificação: Inteligência Estratégica — Grand Prix SENAI 2026*
*Gerado com suporte de IA: propósito de demonstração competitiva; dados de breaches e financeiros são de fontes abertas verificadas*
