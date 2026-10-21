# PARTE 5 — Estratégia Antifrágil: Zero Trust (Postura) + 3 Táticas

> **Deliverable:** Conteúdo narrativo para slide 10 (estratégia antifrágil).
> **Função:** Onde o pitch mostra a **postura de segurança** que o produto oferece. Frame de "3 linhas de defesa em profundidade" alinhado com o draft `PITCHdeck-petro.md` (do autor).
> **Versão:** v0.1 — Outubro 2026

---

## 🎯 Contexto

Slide 10 é o **"PUNCH"** do pitch (do draft `PITCHdeck-petro.md`):

> `% punch - nossa estratégia antifrágil!`
> `- preventiva`
> `  - vigilancia zero day dos fabricantes`
> `  - autenticacao , por criptografia assimetrica temporaria`
> `  - dados e modelos privados, zero-trust sem dependencia de server ext`
> `- defenssiva`
> `  - casos comuns (prevencao de cada um dos ataques anteriores)`
> `  - procedimentos de rotina (inspecao ativa dos)`
> `- ostenssiva`
> `  - monitoramento automata + feedback humano (alertas de criticidade)`
> `  - preparados pra qualquer ataque inesperado (contra medidas pre treinadas)`

**Atenção:** o autor chamou de "antifrágil" — referência ao conceito de Nassim Taleb: sistemas que **ganham com o estresse**, não apenas sobrevivem. AxeGuard aprende com cada ataque. SOC agêntico tem isso como princípio.

---

## 📐 Slide 11 — Postura Zero Trust + 3 Táticas

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│  ESTRATÉGIA ANTIFRÁGIL AXEGUARD                                          │
│  ═══════════════════════════                                            │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │  🛡️ PREVENTIVA — "O ataque nunca entra"                       │     │
│  │  ═══════════════════════════════════════                       │     │
│  │                                                                 │     │
│  │  ▸ Vigilância Zero-Day dos fabricantes                        │     │
│  │    (SBOM + CTI feed + IOC tracking)                           │     │
│  │                                                                 │     │
│  │  ▸ Autenticação por criptografia assimétrica temporária       │     │
│  │    (OAuth Device Flow + PKCE + TPM binding)                   │     │
│  │                                                                 │     │
│  │  ▸ Dados e modelos privados, Zero-Trust sem dependência       │     │
│  │    externa (VNet Enclave + No-Train B2B)                       │     │
│  │                                                                 │     │
│  │  COBRE: Supply Chain, Endpoint, Credential                     │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                              ▼                                            │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │  ⚔️ DEFENSIVA — "Quando entra, é bloqueado"                   │     │
│  │  ═══════════════════════════════════════                       │     │
│  │                                                                 │     │
│  │  ▸ Prevenção de cada ataque documentado                       │     │
│  │    (mapeamento ataque → camada — vide PARTE 2C)              │     │
│  │                                                                 │     │
│  │  ▸ Procedimentos de rotina                                    │     │
│  │    (inspeção ativa de logs + forensics)                       │     │
│  │                                                                 │     │
│  │  ▸ DLP Middleware como cinturão                               │     │
│  │    (regex + NLP + UEBA)                                       │     │
│  │                                                                 │     │
│  │  COBRE: Exfiltração, Ransomware, Vendor VPN                   │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                              ▼                                            │
│  ┌────────────────────────────────────────────────────────────────┐     │
│  │  🎯 OSTENSIVA — "Quando é inesperado, contra-atacamos"          │     │
│  │  ═══════════════════════════════════════                       │     │
│  │                                                                 │     │
│  │  ▸ Monitoramento automático + feedback humano                  │     │
│  │    (SOC Agêntico + escalation inteligente)                     │     │
│  │                                                                 │     │
│  │  ▸ Contra-medidas pré-treinadas                               │     │
│  │    (LangGraph agents com playbook CISA + MITRE ATT&CK)       │     │
│  │                                                                 │     │
│  │  ▸ Aprendizado contínuo (modelos aprendem com cada incidente) │     │
│  │                                                                 │     │
│  │  COBRE: Cognitive overload, ataque zero-day, novo vetor        │     │
│  └────────────────────────────────────────────────────────────────┘     │
│                                                                          │
│  AXEGUARD = SISTEMA QUE GANHA COM O ESTRESSE                            │
│  (cada incidente torna o SOC mais esperto — antifragilidade)            │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Detalhamento por linha

### 🛡️ **POSTURA: Zero Trust (a estratégia)**

**O que é:**
- Princípio arquitetural: **"never trust, always verify, assume breach"**
- Cada request verificada explicitamente
- Nenhum acesso implícito (device, user, network)
- Least privilege: mínimo acesso necessário
- Microsegmentação: blast radius limitado

**Por que é ESTRATÉGIA (não tática):**
- É o guarda-chuva filosófico que dá forma às 3 táticas abaixo
- A Preventiva implementa ZT na entrada (verifica device)
- A Defensiva implementa ZT no dado (verifica conteúdo)
- A Ostensiva implementa ZT no tempo (verifica comportamento)

**Padrão NIST:** NIST SP 800-207 (Zero Trust Architecture)

**Quem se beneficia:** 👔 CTO / Board (postura de longo prazo)

---

### 🛡️ **Preventiva** — A linha de frente (anti-entrada)

**Postura:** o ataque nunca deveria ter chegado aqui.

**3 mecanismos:**

1. **Vigilância Zero-Day dos Fabricantes**
   - SBOM (Software Bill of Materials) obrigatório para XR, Core, IA
   - CTI feed com IOC Iranian / Lazarus / APT41 — atualizados diariamente
   - Vendor scorecard contínuo (security posture dos fornecedores)
   - Hashchain SLSA framework para firmware integrity

2. **Autenticação por Criptografia Assimétrica Temporária**
   - OAuth 2.0 Device Flow (RFC 8628) — sem digitação no ar
   - PKCE (Proof Key for Code Exchange) — fecha authorization code attack
   - TPM 2.0 binding — token amarrado ao hardware
   - Short-lived JWT (15 min) — janela de uso mínima

3. **Dados e Modelos Privados, Zero-Trust sem Dependência Externa**
   - VNet Enclave (Azure OpenAI Private Endpoint)
   - Contrato No-Train B2B (vendor não retém dado)
   - Customer-managed keys (criptografia sob controle Petrobras)
   - Sem internet pública na rota do dado

---

### ⚔️ **Defensiva** — O cinturão (anti-exfiltração)

**Postura:** se passou da preventiva, é parado antes do impacto.

**3 mecanismos:**

1. **Prevenção de Cada Caso Conhecido**
   - Mapeamento direto ataque → camada (vide PARTE 2C)
   - 5 padrões globais × 10 vulnerabilidades BR+Petrobras = cobertura documentada
   - Cada ataque do Research_Attacks_Cases/ tem resposta específica

2. **Procedimentos de Rotina**
   - Inspeção ativa de logs (SOC Agêntico + UEBA)
   - Forensics automatizada (PCAP, logs PLC, eventos MDM)
   - Threat hunting contínuo (não reativo — proativo)

3. **DLP Middleware como Cinturão**
   - Regex + SpaCy NLP + UEBA
   - Channel inspector (DNS, streaming, HTTPS egress)
   - Substituição atômica antes da LLM
   - Bloqueio automático de transferência massiva

---

### 🎯 **Ostensiva** — O contra-ataque (anti-incerteza)

**Postura:** quando é inesperado (zero-day, novo vetor), o sistema contra-ataca e aprende.

**3 mecanismos:**

1. **Monitoramento Automático + Feedback Humano**
   - SOC Agêntico opera 100% automatizado no cloud
   - Auto-response para 80% dos casos (isolamento, quarantine, revoke)
   - Escalation inteligente para os 20% que precisam humano
   - Alertas de criticidade via canal Petrobras (Teams / Slack corporativo)

2. **Contra-Medidas Pré-Treinadas**
   - LangGraph agents com playbook CISA + MITRE ATT&CK
   - IOC database com curadoria Petrobras
   - Runbooks para os 19 casos do dossiê + 100+ variações
   - Decisão tomada em < 60 segundos (não dias)

3. **Aprendizado Contínuo (a parte antifrágil)**
   - Cada incidente alimenta o modelo
   - Cada falso positivo vira regra
   - Cada novo vetor vira IOC
   - O sistema fica **mais esperto** com o tempo (≠ resiliente, **antifrágil**)

---

## 🎯 Por que "antifrágil" e não "robusto"?

**Diferença técnica:**

| Conceito | Definição | Como reage a estresse |
|---|---|---|
| **Frágil** | Quebra com estresse | Piora |
| **Robusto/resiliente** | Resiste a estresse | Mantém-se |
| **Antifrágil** | Ganha com estresse | **Melhora** |

AxeGuard é **antifrágil** porque:
- Cada incidente alimenta os modelos ML do SOC Agêntico
- Cada novo IOC vira regra automática no DLP Proxy
- Cada falso positivo refina o Regex engine
- Cada novo padrão de ataque vira playbook LangGraph

**Resultado:** o custo de defesa **diminui** com o tempo (não aumenta).

---

## 💡 Storytelling do slide

```
"Nem todo sistema aguenta o ataque.
A maioria sobrevive.
Mas AxeGuard APRENDE com cada ataque.

O sistema que fica mais forte com o uso.
Esse é antifrágil."
```

**Por que esse enquadramento é poderoso para banca SENAI:**
- Critério **Criatividade** de desempate (`Rules_and_Winning_Strategies_GP.md` §2)
- Conceito de Nassim Taleb é amplamente reconhecido (FCA, MIT, Yale)
- Diferencia de produtos "robustos" genéricos
- Demonstra pensamento de primeira ordem

---

## ⏭️ Próxima parte

**PARTE 6 — Viability (técnica + econômica)** (slide 12, ANTES do CTA, scope enterprise multinational)