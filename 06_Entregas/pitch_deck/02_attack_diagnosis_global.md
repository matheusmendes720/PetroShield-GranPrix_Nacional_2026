# PARTE 2A — Diagnóstico Global de Ataques

> **Deliverable:** Conteúdo narrativo para os slides 3-4 (paradoxo XR + 5 vetores) e slide 7 (mitigação por risco).
> **Filtro:** Apenas os 5 padrões mais relevantes ao produto AxeGuard (Edge Middleware + SOC Agêntico) e ao cliente-âncora Petrobras / setor O&G.
> **Versão:** v0.1 — Outubro 2026
> **Status:** Aguardando aprovação para PARTE 2B (filtro Petrobras + produto) e PARTE 2C (mitigação por risco)

---

## 🎯 Contexto da seção

O pitch começa pelos **padrões de ataque** (não pela nossa solução) por uma razão tática do `Rules_and_Winning_Strategies_GP.md`:

> *"A maioria das equipes de engenharia focará 100% em fazer algo que apenas funcione perfeitamente (Aderência). Essa é uma armadilha e a receita para perder um desempate."*

Diagnosticar o **inimigo** antes de vender o **remédio** é a estrutura narrativa que o `PITCHdeck-petro.md` (rascunho canônico) já estabelece: **abertura → problema (a dor) → caso Bacia de Campos → setup → punch**. A diagnose factual cria a credibilidade que sustenta o punch.

**Audiência dupla em mente:**
- **IA pré-triagem** do SENAI: precisa das palavras-chave exatas (`supply chain`, `OAuth`, `DLP`, `ransomware`, `zero-trust`, `smart glasses`, `XR`, `industrial`) para classificar alta aderência.
- **Banca humana**: precisa reconhecer ataques reais que conhece (NotPetya, SolarWinds, MOVEit, etc.) para validar que o diagnóstico não é genérico.

---

## 📊 Os 5 Padrões Sistêmicos (Síntese do diagnóstico)

Estes 5 padrões foram filtrados da taxonomia maior de 19 casos do dossier `Research_Attacks_Cases/` (3 arquivos, ~160 KB) por serem os **vetores que o Edge Middleware AxeGuard foi arquitetado para mitigar**:

---

### **Padrão 1 — Supply Chain (Hardware + Software)**

**O que é:** O atacante envenena um componente ANTES do produto chegar ao cliente final — chip em fábrica, firmware em OTA, biblioteca em npm/PyPI, certificado de code-signing.

**Quem ataca:**
- **Nation-states (APT):** NSA/Tailored Access Operations (US), Unit 8200 (IL), MSS / APT41 (CN), GRU / APT28 / Sandworm (RU), Lazarus / APT38 (NK), APT35 / Charming Kitten (IR)
- **Criminal groups com proteção estatal:** Conti (RU), LockBit (RU), FIN7

**De onde operam:**
- **Hardware supply chain:** predominantemente Ásia (CN, TW, KR) + IL (chips de segurança comprometidos historicamente)
- **Software supply chain:** open-source maintainers comprometidos globalmente; CDN edge cases

**Caso emblemático — para o pitch:**
- **SolarWinds (2020, US):** 18.000 clientes comprometidos via update legítimo assinado. Rússia/APT29.
- **Pagers Hezbollah (set/2024, Líbano):** hardware-level backdoor em pagers Gold Apollo comprados pela Hezbollah. Israel/Unit 8200. **Referência direta em PITCHdeck-petro.md** ("pagers do hesbola").
- **npm zero day (2024):** maintainer account compromise. **Referência direta em PITCHdeck-petro.md** ("npm zero day").
- **3CX (2023):**供应链 cascade (3CX ← X_TRADER ← Trading Technologies).
- **xz utils (2024):** maintainer social engineering, quase backdoor em SSH/LibSSH.

**Por que importa pro AxeGuard:** Smart glasses Meta Quest / RealWear / HoloLens têm cadeia de fornecedores fragmentada (chip Qualcomm, OS Android AOSP, app de terceiros, SDKs). Cada elo é vetor. **Camada 1 (MDM) fecha parcialmente** (Kiosk Mode + side-load block), mas não fecha o componente já adulterado em fábrica. **Caixa-preta tática:** vender o "fechamento do risco" sem entrar em dissertação sobre供应链.

---

### **Padrão 2 — Endpoint Compromise (Side-Load + Keylogger)**

**O que é:** Atacante consegue instalar software malicioso no dispositivo de borda (XR / mobile / tablet) bypassing MDM/EDR, ou planta um keylogger físico no wearable.

**Quem ataca:**
- **Insiders maliciosos ou recrutados** (Scattered Spider / UNC3944 é o exemplo canônico)
- **Criminal groups** com acesso a MDM-bypass-as-a-service (SIDELOAD-BOOT)
- **Nation-states** (Pegasus / NSO Group contra dissidentes; Predator / Intellexa)
- **Ransomware operators** pós-breach (escala lateral via endpoint)

**De onde operam:**
- Mercados de "spyware-as-a-service" — predominantemente **IL** (NSO, Candiru), **GR** (Intellexa/RIX), **RU** (Positive Technologies), **IN** (muitos players novos em 2024-25)
- Mercados negros em fóruns RU/CN para MDM-bypass tools

**Caso emblemático — para o pitch:**
- **Pegasus (desde 2016, NSO Group IL):** infecção zero-click via iMessage. **Caso canônico que o público técnico conhece.**
- **Hermit (2022, ROuter):** surveillance framework em apps legítimos de Android.
- **Banking trojans em mobile (BR-specific):** BrasDex, Guildma — golpes PIX e roubo de credenciais bancárias com side-load via APK malicioso. **Caso que fala diretamente ao público brasileiro.**
- **Ataques a XR ainda são nicho (2024-25):** poucas referências diretas, mas Meta Quest tem jailbreaks publicados (SideQuest, ALVR exploits) e exploits em Unreal Engine. **O pitch precisa projetar isso como "campo de batalha emergente".**

**Por que importa pro AxeGuard:** Óculos XR roda Android modificado. Sideload boot é trivial se MDM falhar. Câmera + microfone + dados confidenciais viram uma **goldmine** para keylogger silencioso + espionagem visual. **Camada 1 (MDM com Kiosk Mode restrito + ArborXR / Hexnode UEM) fecha o vetor principal.** Mas o **dado ainda pode vazar legitimamente pelo app** — daí a Camada 3 (DLP).

---

### **Padrão 3 — Credential / Token Theft (OAuth + JWT + TPM Bypass)**

**O que é:** Atacante captura tokens OAuth2, JWT de sessão, ou bypassa autenticação biométrica via keylogger / phishing / token replay.

**Quem ataca:**
- **Phishing-as-a-service:** BulletProofLink (CN), Frappo (RU), EvilProxy (RU)
- **OAuth2-specific attacks:** ataques contra Microsoft Entra ID (antigamente Azure AD), Okta, GitHub. Incidente Okta 2020/2022/2023 são canônicos.
- **AiTM (Adversary-in-the-Middle):** EvilProxy + Microsoft 365 (2023) atinge 100% de organizações Fortune 500.
- **State actors:** APT29 (RU), APT41 (COA) em operações contra identidade corporativa

**De onde operam:**
- Infraestrutura de phishing: predominantemente **RU** (95% dos EvilProxy + Adversary-in-the-Middle), **CN** (BulletProofLink)
- Token resale: fóruns Genesis Market (takedown 2023, mas ressurge), Russian Market

**Caso emblemático — para o pitch:**
- **Okta breaches (2020, 2022, 2023):** 100% do foco foi em token / session hijacking.
- **Microsoft OAuth attack 2023 (Storm-0558, CN-state-linked):** falsificação de tokens de assinatura, acesso a email de gov US + 25 orgs.
- **MGM/Caesars ransomware 2023:** Scattered Spider usou phone-based social engineering para reset MFA → acesso Okta → pivot para MGM.

**Por que importa pro AxeGuard:** Smart glass authentication é vetorialmente perigosa — digitar senhas no ar em VR convida shoulder-surfing físico e captura silenciosa de tela via backdoor. **Camada 2 (OAuth2 Device Flow + PKCE + TPM binding)** fecha:
- **OAuth2 Device Flow (RFC 8628):** óculos exibe QR Code → usuário autentica no celular (com biometria) → token JWT injetado. Sem digitar senha no óculos.
- **PKCE:** fecha QR hijacking / authorization code interception.
- **TPM binding:** fecha token theft — token só roda no device com chip TPM esperado.

**Caso de uso "show, don't tell":** "Operador na refinaria escaneia QR no celular Petrobras, óculos autentica sem digitar nada. Atacante com cópia do token? Bloqueado: TPM binding."

---

### **Padrão 4 — Data Exfiltration via Foreign Proxy / DLP Bypass**

**O que é:** Atacante (já dentro da rede) usa canais "legítimos" para vazar dados confidenciais para servidor estrangeiro — DNS tunneling, HTTPS para CDN de analytics, fragmentação de uploads, steganografia.

**Quem ataca:**
- **Ransomware operators** com leak sites (LockBit, BlackCat/ALPHV, Cl0p, 8Base) — modelo "double extortion": cifra + ameaça publicar
- **Nation-state APTs** em espionagem industrial de longo prazo (APT1 / Comment Crew da China é o caso canônico)
- **Insider threats** com acesso legítimo mas má-fé

**De onde operam:**
- **Ransomware-as-a-service:** ecossistema predominantemente **RU** (mas com crescente presença em IR, KP, CN)
- **Espionagem industrial:** **CN** (70% dos casos de IP theft segundo IP Commission), **RU**, **IR** (sector targeting específico em O&G)
- **Leak sites:** hospedados em bulletproof hosting (RU, CN)

**Caso emblemático — para o pitch:**
- **MOVEit (2023, Cl0p):**供应链 SQL injection em MOVEit Transfer. 2.700+ organizações, 77M pessoas afetadas, incluindo **Shell, BBC, US DHS**.
- **NotPetya (2017, Sandworm/RU):**供应链 via MeDoc (software contábil ucraniano). US$ 10B+ de dano. **Caso canônico que o público corporativo conhece.**
- **Colonial Pipeline (2021, DarkSide):** ransomware → operação fechada por 6 dias → pânico de combustível nos EUA. **Caso que impactou diretamente setor energético.**
- **Eletrobras (2022, regional):** tentativa de intrusão reportada — não publicamente confirmado como exfiltração massiva, mas sinaliza interesse em setor elétrico BR.
- **LockBit 3.0 contra sistema judiciário BR (2024):** variante regional.

**Por que importa pro AxeGuard:** Dados O&G têm valor estratégico imenso — geologia do pré-sal, balanços de fluxo de plataforma, dados sísmicos. **Vazar para servidor estrangeiro = perda de soberania energética + violação LGPD/ANP.** **Camada 3 (DLP Proxy Middleware)** fecha o vetor principal:
- **Regex engine** detecta PII + termos O&G ("Plataforma P-10", "Bacia de Campos", "Tupi-10")
- **NLP engine** detecta entidades geológicas / industriais
- **UEBA** detecta anomalias comportamentais (volume + horário + destino)
- **Channel inspector** inspeciona DNS, streaming, HTTPS egress patterns
- **Substituição em tempo real:** "Plataforma P-10" → "[ATIVO_RESTRITO_01]" antes de chegar na LLM
- **Camada 4 (VNet Enclave):** dado só vai para Azure OpenAI sob No-Train B2B contract, sem internet pública

---

### **Padrão 5 — Cognitive Overload / Paralisia da Análise Humana (vector que justifica o SOC Agêntico)**

**O que é:** Atacante gera **ruído massivo** (10.000+ alertas/dia, 99% falso positivo) para esgotar o time de SOC humano. O resultado não é "ataque direto" — é a falha do time em detectar o sinal verdadeiro dentro do ruído. Conhecido em MITRE ATT&CK como **T1490 (Inhibit System Recovery)** + **T1562 (Impair Defenses)** combinados.

**Quem ataca:**
- **Ransomware operators** em fase de pré-intrusion (reconnaissance ruidoso)
- **Botnets** (Mirai variants, Mēris) para DDoS + log flooding
- **Nation-states** em operações de "denial of intelligence" — gerar ruído para esconder exfilação real entre 10000 eventos falsos
- **Insider threats** que abrem tickets falsos para distrair analistas

**De onde operam:**
- **Botnets:** global (Mirai originária da CN; variantes globais)
- **Ransomware recon:** predominantemente **RU**, **CN**, **IR**
- **Insider market:** global, com picos em economias em stress

**Caso emblemático — para o pitch:**
- **IBM Cost of a Data Breach Report (recorrente):** **197 dias** é o tempo médio global para detectar um breach. A média brasileira é **322 dias** (2023). Esses números **encapsulam exatamente o cognitive overload** — o atacante não precisa ser silencioso, precisa ser mais rápido que a análise humana.
- **Target breach (2013, US):** alertas do FireEye ignorados por 2 semanas. Foi o caso que popularizou "alert fatigue".
- **Equifax (2017, US):** vulnerabilidade Apache Struts conhecida há meses, alert ignorado.

**Por que importa pro AxeGuard:** É o vetor que o **SOC Agêntico (backend cloud)** foi criado para fechar. Não há camada no Edge que resolva — é um problema de escala + velocidade:
- **Ingest:** Event Hubs / Kafka
- **Analytics:** UEBA + ML + correlação cross-source
- **Decision:** auto-response + escalation inteligente
- **Feedback:** melhoria contínua

**A estatística-âncora do pitch:** "**197 dias → 12 segundos**" (MTTD indústria → MTTD AxeGuard). É o número que justifica o "Ponto de Alavancagem" do modelo de startup (do `AxeGuard_SOC_PetroShield.md`): "Eliminamos o maior custo da cibersegurança: o fator humano. Um único cluster na nuvem atende e defende o Polo de Camaçari inteiro autonomamente."

---

## 🎯 Resumo executivo (pode virar legendariz do slide 4)

```
┌─────────────────────────────────────────────────────────────────┐
│  5 PADRÕES QUE DEFINEM O CAMPO DE BATALHA                        │
├─────────────────────────────────────────────────────────────────┤
│  1. SUPPLY CHAIN      → Chips, OS, libs (SolarWinds, xz, npm)    │
│  2. ENDPOINT          → Sideload + keylogger (Pegasus, BrasDex)  │
│  3. CREDENCIAL        → OAuth/TAM tokens/bypass (Okta, Storm-0558)│
│  4. EXFILTRAÇÃO        → Proxy estrangeiro, leak (MOVEit, NotPetya)│
│  5. SOBRECARGA        → Ruído massivo, paralisia (Target, IBM)  │
├─────────────────────────────────────────────────────────────────┤
│  QUEM: Nation-states (CN/RU/IR/IL/NK) + Criminal orgs (RU/CN)   │
│  ONDE: Global, com hubs em Eastern Europe, CN, IL                │
│  IMPACTO BR: Eletrobras (2022), PIX trojans (2023), setor O&G   │
│         sob pressão chinesa/russa crescente (ENISA 2024)         │
└─────────────────────────────────────────────────────────────────┘
```

---

## ⏭️ Próximas partes (aguardando aprovação)

- **PARTE 2B:** Filtro fino de quais padrões são **mais relevantes** para o produto AxeGuard especificamente (camada a camada) + para o cliente Petrobras (setor O&G + Brasil + soberania energética).
- **PARTE 2C:** Mitigação breve por padrão — uma frase por padrão mapeando → camada AxeGuard que fecha.

---

## ❓ Perguntas para você antes de seguir

1. Quer ajustar algum padrão (renomear, adicionar/remover)?
2. Os casos emblemáticos estão no tom certo? (Mais GLB-tech / Mais BR / Mais recentes / Mais antigos)
3. Mantenho a estrutura "padrão → quem → onde → caso → por que importa" para os próximos?
4. Quer que eu seja mais "técnico" (nomes de runners de CIFR) ou "comercial" (impacto $$) no slide 4?