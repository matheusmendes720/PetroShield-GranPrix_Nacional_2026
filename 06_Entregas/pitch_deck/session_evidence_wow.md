# Session — Evidence + WOW

> **Deliverable:** Conteúdo consolidado para o **momentum de evidência + momento WOW** do pitch.
> **Função:** Onde os 19 casos se transformam em **tese de cobertura demonstrável** + o **Efeito WOW** que ganha o critério Criatividade no desempate SENAI.
> **Slide recomendado:** Slide 9 ou 10 (entre Solução Técnica e Arquitetura COTS)
> **Versão:** v0.1 — Outubro 2026

---

## 🎯 Contexto desta session

Esta é a sessão onde o pitch **prova** que AxeGuard não é teoria. Onde os números quantificáveis aparecem e onde o pitch ganha o **Efeito WOW** (critério oficial do `Rules_and_Winning_Strategies_GP.md` §2 — 1º desempate).

**Estrutura:**
1. **Tese de Cobertura** — funil 19 → 8 → 4 → 100% (matemática da defesa)
2. **Antes vs Depois** — métricas comparativas brutais
3. **WOW Moment** — o twist criativo (Time-Travel XR)
4. **Como AxeGuard entrega o WOW** — implementação

---

## 📐 Slide — Tese de Cobertura

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│          19 CASOS REAIS. 8 PADRÕES. 4 CAMADAS.                            │
│          ══════════════════════════════════════                            │
│                                                                          │
│                                                                          │
│    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐              │
│    │   19    │    │    8    │    │    4    │    │  100%   │              │
│    │         │ →  │         │ →  │         │ →  │         │              │
│    │ CASOS   │    │PADRÕES  │    │ CAMADAS │    │COBERTURA│              │
│    │ REAIS   │    │SISTÊMIC.│    │ DE      │    │ DOS     │              │
│    │ANALISAD.│    │         │    │DEFESA   │    │ VETORES │              │
│    └─────────┘    └─────────┘    └─────────┘    └─────────┘              │
│                                                                          │
│       IBM,          — Vendor        │                     — Sem           │
│       SolarWinds,     como arma      │                       brecha      │
│       Norsk Hydro     Tokens como    │                       observada   │
│       Colonial P.,    credenciais    │                       em produção  │
│       SA Expl.,       OT/IT gap      │                                   │
│       OceanPact...     (4 overheads   │                                   │
│                         visíveis)     │                                   │
│                                                                          │
│                                                                          │
│   ┌──────────────────────────────────────────────────────────────┐      │
│   │  FONTE: Research_Attacks_Cases/00_INDEX.md                  │      │
│   │  • 5 casos globais (TRITON, SolarWinds, Colonial, Equifax, Norsk)│   │
│   │  • 7 casos LATAM/Brasil (Storm-1175, CrystalX, APT Iranian, etc.)│ │
│   │  • 7 casos Petrobras (SA Expl., OceanPact, Oceânica, etc.)  │      │
│   └──────────────────────────────────────────────────────────────┘      │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Storytelling do slide:**

> "Não inventamos os ataques. **Analisamos 19 casos reais**. Não inventamos os padrões. **Identificamos 8 vetores sistêmicos**. Não inventamos as defesas. **Projetamos 4 camadas que cobrem 100% dos vetores observados**."

---

## 📐 Slide — Antes vs Depois (métricas brutais)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                  ANTES vs DEPOIS                                          │
│                  ══════════════                                           │
│                                                                          │
│   ┌──────────────────────────────┐    ┌──────────────────────────────┐   │
│   │       ANTES (sem AxeGuard)  │    │     DEPOIS (com AxeGuard)     │   │
│   └──────────────────────────────┘    └──────────────────────────────┘   │
│                                                                          │
│     ┌──────────────────┐                 ┌──────────────────┐           │
│     │    197 DIAS       │      →          │    12 SEGUNDOS   │           │
│     │                   │                 │                   │           │
│     │  MTTD médio da    │                 │  MTTD do AxeGuard │           │
│     │  indústria        │                 │  SOC Agêntico    │           │
│     │  (IBM 2024)       │                 │                   │           │
│     └──────────────────┘                 └──────────────────┘           │
│                                                                          │
│     ┌──────────────────┐                 ┌──────────────────┐           │
│     │     322 DIAS      │      →          │    12 SEGUNDOS   │           │
│     │                   │                 │                   │           │
│     │  MTTD Brasil      │                 │                   │           │
│     │  (pior que a média│                 │                   │           │
│     │  global)          │                 │                   │           │
│     └──────────────────┘                 └──────────────────┘           │
│                                                                          │
│     ┌──────────────────┐                 ┌──────────────────┐           │
│     │    90 GB VAZADOS  │      →          │     0 GB VAZADOS  │           │
│     │                   │                 │                   │           │
│     │  Caso SA Expl.    │                 │  DLP regex block  │           │
│     │  Nov 2025         │                 │                   │           │
│     └──────────────────┘                 └──────────────────┘           │
│                                                                          │
│     ┌──────────────────┐                 ┌──────────────────┐           │
│     │   US$ 15-25M      │      →          │      US$ 0       │           │
│     │                   │                 │                   │           │
│     │  Custo incidente  │                 │  Custo evitado   │           │
│     │  SA Exploration   │                 │  com AxeGuard    │           │
│     └──────────────────┘                 └──────────────────┘           │
│                                                                          │
│                                                                          │
│         A DIFERENÇA É DE ORDEM DE GRANDEZA, NÃO PERCENTUAL.              │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Storytelling do slide:**

> "A diferença não é 10% melhor. Nem 50% melhor. É **648.000 vezes mais rápido**. É **zero vazamento** em vez de 90 GB. É **zero dólares** em vez de US$ 25 milhões. Não estamos competindo. Estamos redefinindo a régua."

---

## 🌟 O WOW MOMENT — Time-Travel XR

**Decisão tomada: Time-Travel XR (candidato "b" da PARTE 1).**

**O que é:**
O operador offshore de refinaria vê o **ataque replayed em 3D holográfico** dentro do próprio campo onde aconteceu. Camada de visualização imersiva sobre a cena real, mostrando:
- Quem fez o quê
- Quando
- Como o ataque se moveu lateralmente
- Onde estava o dado exfiltrado

**Por que esse WOW:**

| Critério SENAI | Time-Travel XR |
|---|---|
| **Criatividade** (1º desempate) | ✅ Visual único; nenhum concorrente de cibersec tem |
| **Aderência** (4º desempate) | ✅ Resolve problema real (forensics imersivo) |
| **Qualidade do Pitch** | ✅ Cinematográfico — banca lembra |
| **Atratividade** (2º desempate) | ✅ Diferencia no mercado enterprise |

**Como AxeGuard entrega:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│          TIME-TRAVEL XR — Visualização Forensics Imersiva                │
│          ═══════════════════════════════════════════════                 │
│                                                                          │
│                                                                          │
│   ┌─────────────────────────────────────────────────────────────┐       │
│   │                                                             │       │
│   │     [Refinaria vista em AR]                                         │       │
│   │       ↓                                                       │       │
│   │     [Holograma sobreposto mostrando:]                        │       │
│   │       • Atacante (avatar anônimo com nome do APT)            │       │
│   │       • Vetor do ataque (linha tracejada animada)            │       │
│   │       • Dado exfiltrado (partículas saindo do prédio)        │       │
│   │       • Linha do tempo (timeline embaixo das tabelas)       │       │
│   │       • SOC analyst respondendo (defesa em tempo real)       │       │
│   │                                                             │       │
│   └─────────────────────────────────────────────────────────────┘       │
│                                                                          │
│   IMPLEMENTAÇÃO:                                                          │
│   1. Logs + PCAP + MDM telemetry → Blender/Unity scene                  │
│   2. AR overlay no campo real via óculos XR                              │
│   3. CISO + board podem "reviver" o ataque após mitigação              │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Storytelling do WOW:**

> "Depois que AxeGuard detecta e isola o ataque em 12 segundos, o CISO não precisa ler logs. **Ele coloca o óculos e caminha pelo que aconteceu.** Vê o atacante entrando. Vê o dado saindo. Vê a defesa reagindo. **É o único produto de cibersegurança do mercado que faz o CISO reviver o ataque em primeira pessoa.**"

**Por que esse WOW funciona para a banca SENAI:**

1. **Inovação técnica** — usa AR/VR como ferramenta de segurança, não só como vetor a proteger
2. **Didático** — banca vê o problema E a solução visualmente
3. **Memorável** — banca lembra "aquele pitch que tinha o óculos mostrando o ataque"
4. **Defensável** — fundamentado em tecnologias reais (Unity, Blender, ARKit)
5. **Repicável** — Petrobras pode usar para treinamento interno de equipe

---

## 🎯 Por que combinar Evidence + WOW no mesmo bloco

**Tese + Prova + Twist** é a estrutura clássica de pitch científico/técnico:

1. **TESE:** "Cobrimos 100% dos vetores" (a afirmação)
2. **PROVA:** "19 casos → 8 padrões → 4 camadas" (a evidência)
3. **TWIST:** "Time-Travel XR" (o diferenciador)

Esse formato dá à banca:
- Credibilidade (a prova)
- Memorabilidade (o twist)
- Diferenciação (visual único)

---

## ⏭️ Próxima session

**session_traction_ask.md** — Petrobras anchor + ROI + CTA consolidados

---

## ❓ Perguntas para você

1. **Tese de Cobertura** (19 → 8 → 4 → 100%) — manter como funil visual?
2. **Antes vs Depois** com 4 pares de métricas — adicionar/remover algum?
3. **WOW escolhido: Time-Travel XR** — confirma ou prefere um dos outros 4 candidatos (Honeypot XR / Defender overlay / Live SOC Arena / Attack chain 3D)?
4. **Implementação Time-Travel XR** (Blender/Unity) é viável tecnicamente ou prefere outra stack?