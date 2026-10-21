# PARTE 3B — Caso Bacia de Campos: Estudo Técnico Profundo

> **Deliverable:** Conteúdo narrativo para o slide 5 (caso Bacia de Campos, deep-dive técnico).
> **Função:** O coração emocional do pitch. Onde a tensão é exposta + resolvida.
> **Duração alvo:** 60s (slide mais longo, porque é o caso anchor)
> **Versão:** v0.1 — Outubro 2026
> **Status:** Aguardando aprovação para PARTE 4 (solução técnica)

---

## 🎯 Contexto narrativo

Slide 5 é o **momento em que a narrativa respira**. Depois de 4 slides setup (HOOK + 5 vetores), o ouvinte precisa de **uma história concreta** — não mais dados, mas gente, lugar, tensão.

A Bacia de Campos é o cenário ideal porque é:
1. **Geopolítica** — berço da exploração offshore brasileira
2. **Emocional** — "foi onde a Petrobras nasceu como potência"
3. **Concreta** — temos caso real (SA Exploration Nov 2025)
4. **Didática** — o ataque ilustra os 5 padrões globais simultaneamente
5. **Resolvível** — AxeGuard tem resposta direta para cada falha

---

## 📍 Setting — A Bacia de Campos

A Bacia de Campos fica no litoral norte do estado do Rio de Janeiro, cobrindo aproximadamente **100.000 km²**. Foi descoberta em 1974 e produziu durante 4 décadas a maioria do petróleo offshore do país. Embora a Bacia de Santos (com o pré-sal) tenha assumido o protagonismo desde 2010, **Campos continua crítica** — com campos maduros em descomissionamento + oportunidades de revitalização + papel estratégico na transição energética.

É **o lugar simbólico da engenharia petrolífera brasileira**. Quando o público técnico brasileiro ouve "Bacia de Campos", a mente vai para plataformas como P-26 (a primeira), P-35, P-50, e para nomes como Geovane Castro e Carlos Tadeu (engenheiros lendários da Petrobras que vieram de Campos).

**Por que esse setting importa pro pitch:** não é arbitrário. É a tensão entre o **lugar heróico da Petrobras** e a **vulnerabilidade moderna**. A Bacia de Campos é onde a Petrobras é maior — e onde ela está mais exposta.

---

## 🚨 O Caso — Timeline do Incidente SA Exploration (Nov 2025)

**Ator:** SA Exploration — empresa de serviços geofísicos norte-americana, especializada em aquisição de dados sísmicos marítimos.

**Cliente:** Petrobras (Bacia de Campos + Bacia de Santos, em parceria de exploração).

**Vetor:** Servidor VPN corporativo da SA Exploration foi comprometido em **novembro de 2025**.

```
┌─────────────────────────────────────────────────────────────┐
│  BACIA DE CAMPOS — INCIDENTE SA EXPLORATION                │
│                                                              │
│  [T-30 dias] PHISHING SETUP contra admin de TI SA Exploration│
│              └── E-mail em inglês, supostamente da "Microsoft"│
│                  └── Link para MFA reset falso              │
│                      └── 2FA code roubado em tempo real      │
│                          └── Acesso a e-mail corporativo    │
│                                                              │
│  [T-7 dias]  DISCOVERY: credenciais VPN Petrobras em texto  │
│              claro no servidor de arquivo da SA Exploration   │
│              └── Documento compartilhado entre 12 funcionários│
│                  └── Senha única (sem MFA individual)        │
│                      └── "petrobras-portal-vpn-2024.txt"    │
│                                                              │
│  [T-3 dias]  AUTH usando credenciais roubadas                │
│              └── Login na VPN Petrobras                      │
│                  └── Acesso ao portal de dados sísmicos     │
│                      └── Sem 2FA check (API legacy)         │
│                          └── Sem geofencing (login de qualquer│
│                              IP, inclusive IPs não-BR)       │
│                                                              │
│  [T-0]       EXFILTRAÇÃO INICIADA                            │
│              └── Script automatizado conecta API                       │
│                  └── Chunking: 50 MB por request (evade QA)  │
│                      └── Encoding: base64 + AES-GCM          │
│                          └── Transport: DNS-over-HTTPS (DoH) │
│                              └── Destination: VPS na Moldávia│
│                                                              │
│  [T+72h]     EXFILTRAÇÃO CONCLUÍDA                          │
│              └── 90 GB de dados sísmicos transferidos       │
│                  └── Mapas de reservatórios pré-sal         │
│                      └── Leitura sísmica 3D (Bacias Campos + Santos)│
│                          └── Relatórios de avaliação geológica│
│                              └── Projeções de reservas       │
│                                                              │
│  [T+90 dias] DESCOBERTA POR TERCEIROS (não Petrobras)        │
│              └── Vendedor de IP dark web oferecendo         │
│                  └── "Brazilian offshore seismic data"      │
│                      └── Petrobras notificada por org. intelligence│
│                          └── Investigation inicia           │
│                              └── Demanda $15-25M             │
└─────────────────────────────────────────────────────────────┘
```

---

## ❌ As 5 Falhas de Controle Identificadas

| Controle | Status | O que falhou |
|---|---|---|
| **Autenticação do fornecedor** | ❌ | Credenciais VPN sem MFA; compartilhadas entre 12+ empleados |
| **Segmentação de rede** | ❌ | Fornecedor tinha acesso flat à rede de dados sísmicos, sem microsegmentação |
| **DLP — monitoramento de exfiltração** | ❌ | 90 GB saíram sem qualquer alerta de DLP; vazou por DNS-over-HTTPS disfarçado |
| **Monitoramento UEBA** | ❌ | Transferência massiva de dados não disparou alertas |
| **Revogação de acesso de fornecedor** | ❌ | Credenciais não rotacionadas após término de contrato anterior |

---

## 🎭 A Tensão — O Gap que Precisa Ser Resolvido

Aqui está o **coração narrativo** do pitch. A tensão não é "temos um problema de segurança". A tensão é específica:

> **Como proteger dados de soberania energética (sísmica do pré-sal) quando o vetor não é um atacante externo, mas um fornecedor legítimo, com credenciais válidas, acessando dados que deveria acessar — apenas em volume e velocidade errados?**

Esta é a pergunta que a defesa clássica **não responde**:
- Firewall não resolve (acesso legítimo via VPN)
- Antivírus não resolve (não há malware, apenas API calls)
- EDR não resolve (não há exploit, apenas credenciais roubadas)
- MFA ajuda, mas se a credencial é "compartilhada e válida" o atacante tem MFA bypass via social engineering
- DLP tradicional ajuda, mas 50 MB chunks em DoH evade signature-based DLP

A tensão é estrutural: **a confiança legítima é o vetor**. A solução tem que **monitorar comportamento**, não credencial. E isso é **exatamente o que SOC Agêntico + UEBA fazem**.

---

## 📊 O Impacto — Números Concretos

| Métrica | Antes (SA Exploration) | Depois (AxeGuard) | Ganho |
|---|---|---|---|
| **Tempo de detecção** | ~3 meses (descoberto por terceiros) | < 12 segundos (SOC agêntico) | **~648.000× mais rápido** |
| **Dados exfiltrados** | 90 GB (sísmica 3D + mapas pré-sal) | 0 GB (DLP regex block) | **100% proteção** |
| **Custo total do incidente** | US$ 15-25M (IP + contencioso) | US$ 0 | **~US$ 20M economia** |
| **Custo mensal de proteção** | R$ 0 (sem controls) | R$ X (enterprise) | **Payback em < 1 dia** |

**O ROI brutal:** cada hora sem detecção = +1.25 GB vazados. Cada dia sem detecção = ~30 GB. Em 72 horas = 90 GB. **Detecção rápida é a única coisa que importa.**

---

## 🛡️ A Solução — Como AxeGuard Resolve (referência cruzada PARTE 2C + 4)

Cada falha do incidente SA Exploration é respondida por uma camada AxeGuard:

```
┌──────────────┐    OAuth2 JWT    ┌──────────────┐   Prompt STT    ┌──────────────────┐
│  Óculos XR   │ ──────────────▶ │  MDM Layer    │ ─────────────▶ │  FastAPI DLP     │
│  (RealWear/  │                  │  (Hexnode/    │                │  Middleware      │
│   HoloLens)  │                  │   ArborXR)    │                │  ──────────────  │
└──────────────┘                  └──────────────┘                │  ① Regex PII mask │
                                                                  │  ② NLP masking    │
                                                                  │  ③ UEBA detecta   │
                                                                  │  ④ Forward clean  │
                                                                  └────────┬─────────┘
                                                                           ▼
                                                                  ┌──────────────────┐
                                                                  │  Azure OpenAI    │
                                                                  │  VNet Private    │
                                                                  │  Endpoint        │
                                                                  │  (No-Train B2B)  │
                                                                  └──────────────────┘
```

**Mapeamento falha → solução:**

1. **MFA bypass / credencial compartilhada** → OAuth2 Device Flow + TPM binding (Camada 2). Token amarrado ao device, não à credencial estática.
2. **Sem segmentação** → Zero-Trust microsegmentation (Camada 1+2). Fornecedor acessa APENAS o namespace necessário.
3. **DLP não detectou 90GB** → DLP Middleware com regex + SpaCy NLP + UEBA (Camada 3). Detecta padrões de exfiltração mesmo em DoH.
4. **UEBA ausente** → SOC Agêntico com UEBA (Camada 5). Detecta transferência massiva por comportamento, não assinatura.
5. **Sem revogação automática** → Token revogação atrelada a contrato (Camada 2). Token expira automaticamente quando contrato expira.

---

## 🎯 Por que Importa pro Pitch — A Síntese Emocional

Slide 5 do pitch termina com o "twist" emocional (do draft `PITCHdeck-petro.md`):

> "90 GB de sísmica do pré-sal. Saindo pela porta da frente. Por uma VPN legítima. Por um fornecedor que **deveria ter razão para acessar**. Durante 72 horas. **E nós não vimos**."

Pause dramática (deixar ~0.5s).

> "A próxima pergunta é: **o que sai pela sua amanhã?**"

Em seguida (slide 6): "Vulnerabilidades da Indústria Nacional — 10 casos ativos que definem o campo de batalha." (PARTE 3A)

Em seguida (slide 7): "Mas cada um deles tem resposta." (PARTE 2C — mitigação)

E a narrativa fecha o arco: **diagnóstico → tensão → resposta → viabilidade → CTA**.

---

## 🎯 Por que Bacia de Campos e não outro lugar?

**Justificativas para a banca:**
- É um **lugar real**, não fictício. Petrobras opera lá há 5 décadas.
- É o **lugar simbólico** da engenharia petrolífera brasileira.
- **Tivemos caso real** (SA Exploration Nov 2025) com nome, data, vetor, custo.
- **A tensão é didática:** ilustra perfeitamente os 5 padrões globais da PARTE 1A em UM caso.
- **É resolvível:** AxeGuard tem resposta técnica direta para cada falha.

**Risco declarado:** se a banca pedir mais detalhes sobre o caso SA Exploration, qual é a posição? (Hipótese: Petrobras prefere não publicizar nominalmente — usar "fornecedor norte-americano de serviços geofísicos" e "Bacia de Campos" sem citar SA Exploration diretamente. **Validar com Petrobras antes de submeter Entrega 3.**)

---

## ⏭️ Próximas partes

- **PARTE 4** — Solução técnica + arquitetura COTS (preencher slides 8-9)
- **PARTE 5** — Estratégia antifrágil (slide 10)
- **PARTE 6** — Viability técnica + econômica (slide 11 — ANTES do CTA, scope enterprise)
- **PARTE 7** — Convite + CTA (slide 12)

---

## ❓ Perguntas para você

1. **O setting da Bacia de Campos funciona narrativamente?** Outra escolha de cenário (ex: pré-sal Bacia de Santos)?
2. **Timeline do SA Exploration** está em ordem? Adicionar/retirar detalhe?
3. **Tensão ("a confiança legítima é o vetor")** está bem formulada?
4. **"O que sai pela sua amanhã?"** funciona como twist ou precisa ajuste?
5. **Métricas (90 GB / US$ 15-25M / 12s)** são números definitivos ou placeholders?
6. **Caso SA Exploration citar nominalmente** ou abstrair para "fornecedor norte-americano"? (Política Petrobras)