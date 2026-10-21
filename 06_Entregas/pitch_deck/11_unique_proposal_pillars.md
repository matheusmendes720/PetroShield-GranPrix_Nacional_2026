# PARTE 8 — A Proposta Única AxeGuard: 3 Soluções de Ponta + 1 Estratégia

> **Deliverable:** Conteúdo narrativo para NOVO slide 8 (entre PARTE 2C — Mitigação e PARTE 4 — Solução Técnica).
> **Função:** Onde o pitch **protagoniza** os 4 elementos diferenciais: **QR Code + SOC + DLP + Zero Trust** — a "Proposta Única" da AxeGuard.
> **Insight do autor:** Esses 4 elementos são o que torna AxeGuard diferente de "mais um produto de cibersegurança". Cada um fala com uma persona; juntos, compõem a arquitetura completa.
> **Versão:** v0.1 — Outubro 2026

---

## 🎯 Contexto

A banca vai ouvir dezenas de pitches de cibersegurança no SENAI GP. A pergunta que todo juiz faz é:

> **"O que torna o SEU projeto diferente?"**

A resposta da AxeGuard cabe em uma única frase-âncora:

> **"QR Code que autentica. SOC que detecta em 12 segundos. DLP que protege o dado. Zero Trust que assume breach. Tudo isso COMPOSTO sobre COTS real, não vaporware."**

Cada um dos 4 elementos é uma **solução de ponta** (3 técnicas + 1 estratégica) que compete, supera ou redefine o estado da arte:

| Elemento | Categoria | Estado da arte convencional | AxeGuard |
|---|---|---|---|
| **QR Code** | Solução de ponta (autenticação) | Senha + MFA digitado | QR + biometria celular + TPM binding |
| **SOC Agêntico** | Solução de ponta (detecção) | Equipe humana + dashboards | LangGraph agents + auto-response + antifrágil |
| **DLP Proxy** | Solução de ponta (proteção) | Regex estática + block | Regex + NLP atômica + substituição + forward |
| **Zero Trust** | Estratégia (postura) | Perímetro + firewall | Assume breach + verify always + least privilege |

---

## 📐 Slide 8 — A Proposta Única AxeGuard

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                                                                          │
│               A PROPOSTA ÚNICA AXEGUARD                                   │
│               ═══════════════════════                                      │
│                                                                          │
│                                                                          │
│            3 SOLUÇÕES DE PONTA. 1 ESTRATÉGIA.                              │
│                                                                          │
│                                                                          │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐       │
│  │                 │   │                 │   │                 │       │
│  │   📱 QR CODE     │   │   🎯 SOC          │   │   🔒 DLP          │       │
│  │   ──────────    │   │   ──────────    │   │   ──────────    │       │
│  │   AUTENTICA     │   │   DETECTA       │   │   PROTEGE       │       │
│  │                 │   │                 │   │                 │       │
│  │  • OAuth Device │   │  • 100%         │   │  • Regex + NLP  │       │
│  │    Flow         │   │    autônomo     │   │    ATÔMICA      │       │
│  │  • PKCE         │   │  • MTTD < 12s   │   │  • Substitui    │       │
│  │  • TPM 2.0      │   │  • LangGraph    │   │    PII / O&G    │       │
│  │    binding      │   │    agents       │   │  • Channel      │       │
│  │  • Biometria    │   │  • ANTIFRAGIL   │   │    inspector    │       │
│  │    celular      │   │    (aprende)    │   │  • UEBA        │       │
│  │                 │   │                 │   │                 │       │
│  │  👤 Operador     │   │  👔 CISO          │   │  🔬 Engenheiro   │       │
│  │  vê: facilidade │   │  vê: eficiência │   │  de dados vê:   │       │
│  │  + segurança    │   │  + velocidade   │   │  IP protegido  │       │
│  │                 │   │                 │   │                 │       │
│  └─────────────────┘   └─────────────────┘   └─────────────────┘       │
│                                                                          │
│                                                                          │
│                ╔═══════════════════════════════════════╗                 │
│                ║                                       ║                 │
│                ║   🛡️  ZERO TRUST — A ESTRATÉGIA        ║                 │
│                ║                                       ║                 │
│                ║   "Nunca confiar. Sempre verificar.    ║                 │
│                ║    Assumir breach. Mínimo privilégio." ║                 │
│                ║                                       ║                 │
│                ║   Postura que sustenta as 3 soluções   ║                 │
│                ║   de ponta + as 4 camadas + toda       ║                 │
│                ║   a arquitetura.                      ║                 │
│                ║                                       ║                 │
│                ║   👔 CTO / Board vê: postura            ║                 │
│                ║   estratégica de longo prazo            ║                 │
│                ║                                       ║                 │
│                ╚═══════════════════════════════════════╝                 │
│                                                                          │
│                                                                          │
│         COMPOSTO SOBRE COTS REAL. AUDITÁVEL. 90 DIAS SETUP.             │
│                                                                          │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Detalhamento de cada pilar

### **1. 📱 QR Code — Autenticação (Camada 2)**

**O que é:**
- OAuth 2.0 Device Authorization Grant (RFC 8628)
- Óculos exibe QR Code temporal (~30s TTL)
- Operador escaneia com celular Petrobras (já autenticado por biometria no MDM local)
- Token JWT injetado dinâmico no óculos
- TPM 2.0 assina o token → binding (token só roda naquele device)
- PKCE fecha authorization code attack

**Por que é "solução de ponta":**
- ❌ **Estado da arte:** Senha digitada em teclado físico (vulnerável a keylogger) ou teclado virtual em VR (vulnerável a shoulder-surfing físico + captura silenciosa de tela)
- ✅ **AxeGuard:** QR + biometria celular + TPM. **ZERO digitação no ar.** Fecha TODOS os vetores de credencial.

**Por que é único:**
- Nenhum concorrente de cibersec industrial combina OAuth Device Flow + PKCE + TPM binding para XR
- Microsoft Entra ID tem a tecnologia base (RFC 8628) — **a integração específica com XR é nossa**

**Quem se beneficia:** 👤 Operador offshore (facilidade de uso + segurança)

**Insight chave para pitch:**
> "O operador não digita nada. O óculos exibe um QR. O celular Petrobras autentica com FaceID. O token chega por NFC simulado via cloud. Nenhum atacante consegue capturar — nem via QR se pegar, o TPM rejeita; nem via token se copiar, o TPM rejeita."

---

### **2. 🎯 SOC Agêntico — Detecção (Camada 5, backend)**

**O que é:**
- 100% automatizado no cloud, sem fator humano no loop para 80% dos casos
- LangGraph agents com playbook CISA + MITRE ATT&CK
- UEBA + ML + correlação cross-source
- MTTD < 12 segundos (teórico) / < 60 segundos (realista)
- Auto-response: isolamento, quarantine, revoke
- Escalation inteligente para os 20% que precisam humano
- **Antifrágil** — aprende com cada incidente (modelos refinam)

**Por que é "solução de ponta":**
- ❌ **Estado da arte:** Equipe humana 24/7 (3-5 analistas) + dashboards + alertas manuais. Custo: R$ X bi/ano globalmente. MTTD: **197 dias indústria / 322 dias Brasil** (atacante tem MUITO tempo).
- ✅ **AxeGuard:** 1 cluster cloud serve N refinarias. Elimina o **MAIOR custo da cibersegurança** (analista humano). MTTD: **12 segundos**. **648.000× mais rápido** que indústria.

**Por que é único:**
- Combina LangGraph (stateful agents) + UEBA (comportamento) + auto-response (LangChain tools) + LangSmith como observability em SOC único
- SOC tradicional NÃO tem antifragilidade — piora com volume
- SENAI banca reconhece LangGraph / LangChain como vanguarda técnica (`V3 Core Implementation` skill no catálogo)

**Quem se beneficia:** 👔 CISO / Analista SOC (eficiência + velocidade + redução de custo operacional)

**Insight chave para pitch:**
> "O atacante não precisa ser silencioso. Precisa ser mais rápido que a análise humana. SOC humano: 197 dias. SOC Agêntico: 12 segundos. O atacante tem 0% de chance em 12 segundos."

---

### **3. 🔒 DLP Proxy Middleware — Proteção do dado (Camada 3)**

**O que é:**
- FastAPI (Python) + Regex + SpaCy NLP + UEBA
- Intercepta TODA comunicação dos óculos antes de chegar na LLM
- **Substituição atômica** de PII / O&G terminology:
  - "Plataforma P-10" → "[ATIVO_RESTRITO_01]"
  - "Tupi-10" → "[ATIVO_RESTRITO_02]"
  - "Bacia de Campos" → "[BACIA_RESTRITA]"
  - "Pré-Sal" → "[RESERVATORIO_RESTRITO]"
- **Channel inspector:** DNS-over-HTTPS, steganografia em HTTPS, fragmentação — todos detectados
- **UEBA comportamental:** detecta transferência massiva (90 GB em 72h) por comportamento, não regex
- Não bloqueia — **transforma e encaminha** (forward clean)

**Por que é "solução de ponta":**
- ❌ **Estado da arte:** DLP signature-based (regex estático) + **block** (não transforma). Falsos positivos altos (~15%). Não detecta exfiltração ofuscada (DoH, stego, fragmentação).
- ✅ **AxeGuard:** DLP **transforma** o dado (não bloqueia) + canal egress inspecionado + UEBA detecta anomalia comportamental. PII e O&G vão **LIMPOS** para a LLM. LLM recebe contexto sem expor IP.

**Por que é único:**
- Nenhum DLP comercial combina: Regex Petrobras-specific + atomic transform + channel inspector + UEBA em middleware único
- Microsoft Purview tem partes; **a composição é nossa**
- A "Teoria Restrita" (regex engine treinada com 19 casos Petrobras + NLP custom em terminologia sísmica) fica no produto, não na documentação pública (`Rules_and_Winning_Strategies_GP.md` §4 — PI defensiva)

**Quem se beneficia:** 🔬 Engenheiro de dados / Compliance (IP protegido) + Petrobras (soberania energética)

**Insight chave para pitch:**
> "Petrobras vê dado original. LLM recebe dado transformado. Atacante que interceptar via DoH vê só [ATIVO_RESTRITO_01]. Zero risco de IP vazado. Zero risco de LLM reter dado para treino. Compliance LGPD/ANP preservado."

---

### **4. 🛡️ Zero Trust — A Estratégia**

**O que é:**
- Princípio arquitetural: **"never trust, always verify, assume breach"**
- Cada request verificada explicitamente
- Nenhum acesso implícito (device, user, network)
- Least privilege: mínimo acesso necessário
- Microsegmentação: blast radius limitado
- Postura que sustenta as 3 soluções de ponta + as 4 camadas + toda a arquitetura

**Por que é "estratégia de ponta":**
- ❌ **Estado da arte:** Perimeter defense (firewall) + VPN. Assume rede interna = confiável. **Falso.** 62% dos breaches O&G vêm via fornecedor que já está "dentro" (IBM X-Force 2024).
- ✅ **AxeGuard:** Zero Trust = padrão NIST SP 800-207. Cada camada, cada request, cada device verificado. Assume que o atacante JÁ está dentro.

**Por que é único (em conjunto com as outras 3):**
- Não é feature — é **postura filosófica** que conecta todas as outras decisões
- Cada ataque do dossiê (SA Exploration, OceanPact, Oceânica) tinha **Token de Acesso Válido** — Zero Trust inverte essa injeção
- Petrobras compra AWS Stack, Palo Alto, CrowdStrike. Não compra "Zero Trust" — compra **postura que escala**. Os 4 elementos juntos mostram que AxeGuard não é "mais uma ferramenta" — é uma **arquitetura de postura**.

**Quem se beneficia:** 👔 CTO / Board de Segurança (postura estratégica de longo prazo)

**Insight chave para pitch:**
> "SA Exploration tinha credencial VÁLIDA. VPN federal. Acesso 'autorizado'. O atacante não 'entrou' — ele HERDOU credenciais. Zero Trust inverte isso: não existe 'autorizado por herança'. Cada request, cada device, cada usuário: verificado. Sempre."

---

## 🎯 Por que esses 4 elementos merecem slide dedicado

### **1. Diferenciação clara**
A banca ouve 50 pitches. A maioria fala "fazemos X, Y, Z". AxeGuard fala: "fazemos **QR + SOC + DLP + Zero Trust COMPOSTOS** em COTS real, não vaporware".

### **2. Stakeholder mapping (4 personas cobertas)**
Cada elemento fala com um stakeholder diferente:

| Stakeholder | Elemento que o convence |
|---|---|
| 👤 Operador | QR Code (uso) |
| 👔 CISO | SOC Agêntico (gestão) |
| 🔬 Engenheiro de dados | DLP Proxy (IP) |
| 👔 CTO / Board | Zero Trust (postura) |

**Todos os 4 stakeholders se sentem vistos** — incluindo o board da banca SENAI que avalia composto integralmente.

### **3. Critério de desempate (Criatividade)**
`Rules_and_Winning_Strategies_GP.md` §2:
> "A maioria das equipes de engenharia focará 100% em fazer algo que apenas funcione perfeitamente (Aderência). Essa é uma armadilha e a receita para perder um desempate."

A banca vê dezenas de projetos que implementam Zero Trust. Mas combinar **QR + SOC + DLP + Zero Trust** sobre COTS real, com MTTD < 12s, com antifragilidade, é o **Efeito WOW** que sustenta o desempate.

### **4. Atende banca SENAI + Petrobras simultaneamente**
- **SENAI judges** veem: vanguarda técnica (LangGraph, OAuth RFC 8628, TPM 2.0, SLSA, NIST 800-207) + composição inteligente
- **Petrobras** (se assistir) vê: solução aplicável hoje, auditável, com COTS real, sem lock-in

### **5. Memorabilidade**
Pitch é uma narrativa de 3 minutos. **4 pilares nomeáveis + 1 frase-âncora** = banca lembra.

---

## 💡 Frase-âncora do pitch (para colar no roteiro de fala)

```
"QR Code que autentica.
SOC que detecta em 12 segundos.
DLP que protege o dado.
Zero Trust que assume breach.

Tudo isso composto sobre tecnologia de mercado real.
Implementável em 90 dias.
Auditável peça por peça.

Isso é AxeGuard."
```

**Por que essa frase-âncora:**
- 4 beats rítmicos (QR / SOC / DLP / Zero Trust)
- Estrutura paralela (verbo + objeto)
- Última linha é a definição
- 19 segundos de fala (~6s/pillar)

---

## 📍 Inserção no narrative

**Posição recomendada:** Slide 8 (entre PARTE 2C — Mitigação e PARTE 4 — Solução Técnica)

**Renumeração dos slides subsequentes:**
- Antigo slide 8 (Solução visão) → slide 9
- Antigo slide 9 (Arquitetura COTS) → slide 10
- Antigo slide 10 (Antifrágil) → slide 11
- Antigo slide 11 (Viability) → slide 12
- Antigo slide 12 (CTA) → slide 13

**Total:** 13 slides × ~14s = ~3 min (mantém orçamento)

---

## 🔗 Cross-references

Esta parte é referenciada por:
- **PARTE 1** (Master scaffold) — slide 8 desta parte
- **PARTE 4** (Solução técnica) — slide 9 desta parte (visão 4 camadas passa por esses 4 pilares)
- **PARTE 5** (Estratégia antifrágil) — slide 11 desta parte (Zero Trust = postura, 3 níveis = táticas)
- **PARTE 6** (Viability) — slide 12 desta parte (pricing enterprise + ROI)
- **PARTE 7** (CTA) — slide 13 desta parte (CTA herda a força desses 4 pilares)

---

## ❓ Perguntas para você

1. **Slide 8 dedicada à Proposta Única** ou como callout/overlay em outro slide?
2. **A divisão 3 (soluções de ponta) + 1 (estratégia)** faz sentido?
3. **Stakeholder mapping** (operador/CISO/engenheiro/CTO) está alinhado com quem vai estar na banca SENAI?
4. **Frase-âncora** funciona como está ou precisa iterar?
5. **Renumeração dos slides 9-13** aprova?
6. **Zero Trust como "estratégia"** (não como feature) faz sentido estratégico?