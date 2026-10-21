# PARTE 10 — Widgets, Charts, Diagramas + Slide Templates

> **Deliverable:** Sistema de componentes visuais + templates por slide, mapeados para o deck canônico de **10 slides (OPÇÃO A)**.
> **Stack:** Baseado no style guide Option D (`13_style_guide_option_D_holographic.md`).
> **Função:** Pronto pra Figma/Framer/CSS — copy/paste nos arquivos de implementação.
> **Versão:** v0.2 — Outubro 2026 (numeração reconciliada com o deck de 10 slides)

> **Mapa de numeração:** os templates abaixo foram escritos para a versão de 13 slides (OPÇÃO B, 5 min). No deck canônico de 10 slides (OPÇÃO A, limite de 3 min do SENAI) o mapeamento é: **slide 11 (Antifrágil/ZT) → slide 8**, **slide 12 (Viability) → slide 10**, **slide 13 (CTA) → slide 10** (Viability e CTA fundidos no slide final). Referências de "Uso:" abaixo já apontam para o slide canônico.

---

## 🎯 Índice

```
PARTE 10A — Widgets Library (componentes reutilizáveis)
PARTE 10B — Charts Library (visualizações de dados)
PARTE 10C — Diagrams Library (4 camadas, Fluxos, Timelines)
PARTE 10D — Slide Templates (mapeados para os 10 slides do deck canônico)
PARTE 10E — Implementation Notes (handoff Figma/Framer)
```

---

# PARTE 10A — Widgets Library

## **Widget 1 — KPI Hero Card**

```css
.kpi-hero-card {
  background: var(--bg-glass-strong);
  backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid transparent;
  background-image: 
    linear-gradient(var(--bg-glass-strong), var(--bg-glass-strong)),
    linear-gradient(135deg, rgba(99,102,241,0.5), rgba(0,212,255,0.5));
  background-origin: border-box;
  background-clip: padding-box, border-box;
  border-radius: 20px;
  padding: var(--space-6) var(--space-8);
  text-align: center;
  box-shadow: var(--shadow-lg), var(--glow-iridescent);
}

.kpi-hero-number {
  font-family: var(--font-mono);
  font-size: 64px;
  font-weight: 900;
  background: var(--gradient-iridescent);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  line-height: 1;
  letter-spacing: -0.03em;
}

.kpi-hero-label {
  font-family: var(--font-body);
  font-size: var(--text-body-sm);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-top: var(--space-3);
}

.kpi-hero-sublabel {
  font-family: var(--font-body);
  font-size: var(--text-body);
  color: var(--text-secondary);
  margin-top: var(--space-2);
}
```

**Uso:** slides 5 (90GB/72h/12s), 7 (cobertura), 12 (ROI 47x-666x), 8 (4 pilares).

---

## **Widget 2 — Glass Card**

```css
.glass-card {
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: var(--space-5);
  box-shadow: var(--shadow-md);
}

.glass-card--priority {
  background: var(--bg-glass-strong);
  border: 1px solid var(--border-strong);
  box-shadow: var(--shadow-lg), var(--glow-iridescent);
}
```

**Uso:** todos os slides, container padrão de conteúdo.

---

## **Widget 3 — Icon Circle**

```css
.icon-circle {
  width: 56px;
  height: 56px;
  border-radius: 50%;
  background: var(--gradient-iridescent);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--glow-iridescent);
}

.icon-circle--matrix {
  background: var(--gradient-matrix);
  box-shadow: var(--glow-matrix);
}

.icon-circle--danger {
  background: var(--gradient-danger);
  box-shadow: var(--glow-danger);
}

.icon-circle--success {
  background: var(--gradient-success);
  box-shadow: var(--glow-success);
}

.icon-circle-icon { color: var(--text-primary); stroke-width: 1.5; }
```

**Uso:** identificar visualmente o tipo de conteúdo (vetor, camada, pilar).

---

## **Widget 4 — Before/After Comparison**

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│   ┌──────────────────┐         ┌──────────────────┐         │
│   │      ANTES       │   →     │      DEPOIS      │         │
│   │                  │         │                  │         │
│   │   90 GB          │         │   0 GB           │         │
│   │   VAZADOS         │         │   VAZADOS         │         │
│   │   (72h)          │         │                  │         │
│   └──────────────────┘         └──────────────────┘         │
│   danger styling              success styling              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Uso:** slides 5, 7, 12 (sempre com visual claro de "antes/perigoso" → "depois/seguro").

---

## **Widget 5 — Progress Bar**

```css
.progress-track {
  height: 8px;
  background: var(--bg-tertiary);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: var(--gradient-iridescent);
  box-shadow: var(--glow-iridescent);
  transition: width var(--duration-slow) var(--ease-out-fluid);
}
```

**Uso:** slides 6 (cobertura), 7 (mitigação pre).

---

## **Widget 6 — Tag/Chip**

```css
.tag {
  display: inline-block;
  padding: var(--space-1) var(--space-3);
  border-radius: 100px;
  font-size: var(--text-body-sm);
  font-weight: var(--weight-medium);
  letter-spacing: 0.04em;
}

.tag--default {
  background: var(--bg-tertiary);
  color: var(--text-secondary);
  border: 1px solid var(--border-default);
}

.tag--iridescent {
  background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(0,212,255,0.2));
  color: var(--brand-cyan);
  border: 1px solid var(--brand-cyan);
}

.tag--matrix {
  background: rgba(0,255,65,0.15);
  color: var(--brand-matrix);
  border: 1px solid var(--brand-matrix);
}

.tag--danger {
  background: var(--danger-bg);
  color: var(--danger);
  border: 1px solid var(--danger);
}
```

**Uso:** tags de categoria, marcadores de tipo (CVE, vendor, etc.).

---

# PARTE 10B — Charts Library

## **Chart 1 — Attack Pattern Matrix (5 × 4)**

```
              Camada1  Camada2  Camada3  Camada4  SOC
              (MDM)    (OAuth)  (DLP)    (VNet)   (Agêntico)

1. Supply     ████     ─        ─        ████     ████
   Chain

2. Endpoint   ████     ─        ─        ─        ████

3. Credencial ─        ████     ─        ─        ████

4. Exfiltração─        ─        ████     ████     ████

5. Sobrecarga ─        ─        ─        ─        ████
```

**Implementação:**
- Grid CSS 6×6 (header + 5 rows)
- Cells com `█` em gradiente iridescent, vazias em cinza escuro
- Cada coluna rotulada com nome da camada + ícone
- Hover state ilumina a coluna

```css
.matrix-pattern {
  display: grid;
  grid-template-columns: 180px repeat(5, 1fr);
  gap: var(--space-2);
  font-family: var(--font-mono);
}

.matrix-cell {
  height: 48px;
  background: var(--bg-tertiary);
  border-radius: 8px;
  position: relative;
}

.matrix-cell--covered {
  background: var(--gradient-iridescent);
  box-shadow: var(--glow-iridescent);
}

.matrix-cell--covered-partial {
  background: linear-gradient(135deg, rgba(99,102,241,0.4), rgba(0,212,255,0.4));
}
```

**Uso:** slide 7 (mitigação por risco).

---

## **Chart 2 — Before/After KPI Pair**

```
    ANTES                          DEPOIS
    ─────                          ─────
    ╭─────╮                        ╭─────╮
    │     │                        │     │
    │ 90  │ GB                      │  0  │ GB
    │     │                        │     │
    ╰─────╯                        ╰─────╯
    Vazados em                     Bloqueados
    72 horas                       em 12s
```

**Implementação:** 2 colunas, KPI hero card + arrow entre eles.

```css
.kpi-pair {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: var(--space-8);
}

.kpi-pair-arrow {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: var(--gradient-iridescent);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--glow-iridescent-strong);
}

.kpi-pair-arrow-icon {
  font-size: 48px;
  color: var(--text-primary);
}
```

**Uso:** slides 5, 7, 12.

---

## **Chart 3 — TAM/SAM/SOM Funnel**

```
    TAM           SAM           SOM
    $32bi         $8bi          $800M
    ┌──────────┐  ┌──────┐    ┌────────┐
    │          │  │      │    │        │
    │  Merc.   │→ │ O&G  │ →  │ 5 majors│
    │  global  │  │Crit. │    │  + Petr│
    │  cibersec │  │Infra │    │        │
    └──────────┘  └──────┘    └────────┘
    CAGR 11.3%
```

**Implementação:** 3 colunas com trapezoides + connectors animados.

**Uso:** slide 10 (Viability).

---

## **Chart 4 — Window of Exposure Timeline**

```
2020                                          2026
────                                          ────
[60 dias]                                    [7 dias]
[███████████████████████] 8.5× MENOR →       [█████]

Atacantes descobrem vulnerabilities 8.5× mais rápido
```

**Uso:** slide 10 (urgência).

---

# PARTE 10C — Diagrams Library

## **Diagram 1 — 4 Camadas + SOC Agêntico (vertical stack)**

```
┌─────────────────────────────────────────────┐
│  CAMADA 1: MDM                               │
│  ArborXR / Hexnode UEM                       │
│  Compliance + Kiosk Mode                     │
└─────────────────┬───────────────────────────┘
                  │ OAuth2 JWT + PKCE + TPM
                  ▼
┌─────────────────────────────────────────────┐
│  CAMADA 2: OAuth Device Flow                 │
│  Microsoft Entra ID / Okta                  │
│  QR Code + Biometria + TPM binding           │
└─────────────────┬───────────────────────────┘
                  │ Token JWT validado
                  ▼
┌─────────────────────────────────────────────┐
│  CAMADA 3: DLP Proxy Middleware             │
│  FastAPI + Regex + SpaCy NLP + UEBA          │
│  Substituição atômica PII/O&G               │
└─────────────────┬───────────────────────────┘
                  │ Dado limpo
                  ▼
┌─────────────────────────────────────────────┐
│  CAMADA 4: VNet Enclave                     │
│  Azure OpenAI Private Endpoint                │
│  No-Train B2B                                │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
   ╔═══════════════════════════════════╗
   ║  SOC AGÊNTICO (backend cloud)    ║
   ║  LangGraph + UEBA + ML             ║
   ║  MTTD < 12s                       ║
   ╚═══════════════════════════════════╝
```

**Implementação:**
- 4 cards stacked vertically (768×120 cada)
- SOC no bottom como card diferenciado (border iridescent thick)
- Connectors verticais com glow iridescent
- Slide 9

**CSS:**
```css
.diagram-stack {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  align-items: center;
}

.diagram-layer {
  width: 100%;
  max-width: 768px;
  padding: var(--space-5) var(--space-6);
  background: var(--bg-glass);
  backdrop-filter: blur(20px);
  border: 1px solid var(--border-default);
  border-radius: 12px;
  position: relative;
}

.diagram-layer--soc {
  border: 2px solid var(--brand-iridescent);
  box-shadow: var(--glow-iridescent-strong);
  background-image: var(--gradient-iridescent);
}

.diagram-connector {
  width: 2px;
  height: 32px;
  background: var(--gradient-iridescent);
  box-shadow: var(--glow-iridescent);
}
```

---

## **Diagram 2 — Attack Timeline (horizontal)**

```
T-30d      T-7d      T-3d      T-0     T+72h    T+90d
──────     ─────     ─────     ────    ─────    ──────
Phishing   Discovery  Auth    Exfil   Complete  Descoberta
admin TI   cred       VPN     inicia  90GB      terceiros
                ╲      ╱        ╱        ╲       ╱
                 ╲    ╱        ╱          ╲     ╱
                  ╲╱╱         ╱            ╲╱╱
                  VPN         DoH           dark web
                  legacy      exit
```

**Implementação:**
- 6 pontos no timeline (T-30d → T+90d)
- Linhas conectando eventos
- Cores: vermelho/danger crescendo em direção a T-0

```css
.timeline-event {
  width: 16px;
  height: 16px;
  border-radius: 50%;
  background: var(--brand-iridescent);
  box-shadow: var(--glow-iridescent);
  position: relative;
}

.timeline-event--danger {
  background: var(--danger);
  box-shadow: var(--glow-danger);
}

.timeline-line {
  height: 2px;
  background: var(--gradient-iridescent);
}
```

**Uso:** slide 5 (Bacia de Campos — caso SA Exploration).

---

## **Diagram 3 — 4 Pilares da Proposta Única (grid 2×2)**

```
┌──────────────────┐  ┌──────────────────┐
│                  │  │                  │
│   📱 QR CODE     │  │   🎯 SOC          │
│   AUTENTICA      │  │   DETECTA        │
│                  │  │                  │
│   👤 Operador     │  │   👔 CISO          │
│   vê: + segurança │  │   vê: + velocidade│
│                  │  │                  │
└──────────────────┘  └──────────────────┘

┌──────────────────┐  ┌──────────────────┐
│                  │  │                  │
│   🔒 DLP          │  │   🛡️ ZERO TRUST  │
│   PROTEGE        │  │   ESTRATÉGIA     │
│                  │  │                  │
│   🔬 Engenheiro   │  │   👔 CTO          │
│   vê: IP seguro  │  │   vê: postura    │
│                  │  │                  │
└──────────────────┘  └──────────────────┘
```

**Implementação:**
- Grid 2×2
- Cada card = glass card iridescent
- Slide 8 — o momento mais importante visualmente

```css
.proposal-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-6);
}

.proposal-pillar {
  background: var(--bg-glass-strong);
  backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid transparent;
  background-image: 
    linear-gradient(var(--bg-glass-strong), var(--bg-glass-strong)),
    linear-gradient(135deg, rgba(99,102,241,0.6), rgba(0,212,255,0.6));
  background-origin: border-box;
  background-clip: padding-box, border-box;
  border-radius: 24px;
  padding: var(--space-6);
  text-align: center;
  box-shadow: var(--shadow-xl), var(--glow-iridescent);
  animation: float 6s ease-in-out infinite;
}

.proposal-pillar:nth-child(1) { animation-delay: 0s; }
.proposal-pillar:nth-child(2) { animation-delay: 1.5s; }
.proposal-pillar:nth-child(3) { animation-delay: 3s; }
.proposal-pillar:nth-child(4) { animation-delay: 4.5s; }
```

---

# PARTE 10D — 13 Slide Templates

---

## **SLIDE 1 — HOOK**

**Propósito:** Capturar atenção em 3 segundos. Apelar pro susto + introduzir a régua.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│           ████████████                                          │
│        ██              ██                                       │
│      ██     197           ██                                    │
│    ██                     ██                                     │
│   ██     DIAS             ██                                   │
│   ██                       ██                                   │
│   ██  é o tempo médio      ██                                  │
│   ██  que a indústria       ██                                 │
│   ██  leva para detectar    ██                                 │
│   ██  um ataque.             ██                                │
│   ██                         ██                               │
│    ██                       ██                                 │
│      ██                    ██                                   │
│        ██                ██                                     │
│           ████████████                                          │
│                                                                 │
│                                                                 │
│                                                                 │
│   ╭─────────╮                                  ╭─────────╮     │
│   │ 🛡️ AXEGUARD│                                  │ AXEGUARD │     │
│   ╰─────────╯                                  ╰─────────╯     │
│   (logo)                                       (logo back)      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Background: `bg-spotlight` (radial gradient cyan glow)
- Hero number: `kpi-hero-number` (197 em iridescent display)
- Subtitle: 4 linhas de body text
- Logo AxeGuard: canto inferior esquerdo + canto inferior direito (simetria)
- Animation: número "197" anima de 0 → 197 em 1.4s

**Tipografia:**
- "197" = `--text-display-xl` (96px) mono black
- Body subtitle = `--text-body-lg` (24px)
- Brand name = `--text-h3` (28px) bold

**Cores:**
- Bg: `--bg-spotlight`
- Number: `--gradient-iridescent`
- Body: `--text-primary`
- Logo: `--text-secondary`

**Motion:**
- Slide-in: fade + slide-up 600ms
- Number counter: 0→197 em 1400ms ease-out
- Iridescent display title shift: 6s loop

**Data needed:**
- "197" (MTTD da indústria, IBM 2024)

---

## **SLIDE 2 — HOOK Caso**

**Propósito:** Teaser do caso Bacia de Campos. Emocional, gera curiosidade.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│              Bacia de Campos                                     │
│         ─────────────────────                                   │
│                                                                 │
│            ███████████████████                                 │
│            █                  █                                 │
│            █  "O que saiu     █                                 │
│            █   pela porta da  █                                 │
│            █   frente?"       █                                 │
│            █                  █                                 │
│            ███████████████████                                 │
│                                                                 │
│                                                                 │
│                                                                 │
│              (imagem sutil de refinaria)                       │
│                                                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Background: `bg-spotlight` + noise overlay
- Title: iridescent display "Bacia de Campos"
- Quote box: glass card com pergunta provocativa
- Subtle image: rendering 3D de refinaria (low opacity)

**Tipografia:**
- "Bacia de Campos" = `--text-display-lg` (72px) iridescent display
- Quote = `--text-h2` (36px) italic

**Motion:**
- Title slide-in com fade + slide-up
- Quote box: pulse sutil 4s loop (glow-iridescent pulsing)

---

## **SLIDE 3 — Paradoxo XR**

**Propósito:** Mostrar que XR melhora controle MAS vulnerabiliza.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│     ┌──────────────────────┐  ┌──────────────────────┐         │
│     │                      │  │                      │         │
│     │   ✓ ANTES            │  │   ⚠️ DEPOIS           │         │
│     │                      │  │                      │         │
│     │   Controle manual    │  │   XR melhora +       │         │
│     │   (sem XR)           │  +   amplia superfície  │         │
│     │                      │  │                      │         │
│     │   ✓ Seguro            │  │   ✗ Inseguro          │         │
│     │   ✓ Sem ataque        │  │   ✗ Novo vetor         │         │
│     └──────────────────────┘  └──────────────────────┘         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 2 cards lado a lado
- ANTES: ícone check + texto (success green)
- DEPOIS: ícone warning + texto (iridescent glow)

**Tipografia:**
- Headers = `--text-h3` (28px) bold
- Body = `--text-body` (20px)

**Cores:**
- ANTES card: border sutil cyan, text-secondary
- DEPOIS card: border iridescent thick, glow

---

## **SLIDE 4 — 5 Vetores**

**Propósito:** Mostrar os 5 padrões sistêmicos de ataque.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│         5 VETORES QUE DEFINEM O CAMPO DE BATALHA               │
│         ─────────────────────────────────────────               │
│                                                                 │
│   ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                │
│   │ ⚙️  │ │ 💻  │ │ 🔑  │ │ 📡  │ │ 🌊  │                │
│   │      │ │      │ │      │ │      │ │      │                │
│   │SUPPLY│ │      │ │      │ │      │ │      │                │
│   │CHAIN │ │END-  │ │CRED- │ │EXFIL-│ │SOBRE-│                │
│   │      │ │POINT │ │ENCIAL│ │TRAÇÃO│ │CARGA │                │
│   │      │ │      │ │      │ │      │ │      │                │
│   │T1195 │ │T-64  │ │T1528 │ │T1048 │ │T1490 │                │
│   └──────┘ └──────┘ └──────┘ └──────┘ └──────┘                │
│                                                                 │
│   Quem: Nation-states + Criminal orgs                           │
│   Onde: Global, hubs RU/CN/IL                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 5 colunas cards glass (asset mínimo)
- Cada coluna: ícone + nome + MITRE T-code
- Bottom: linha "Quem + Onde"

**Tipografia:**
- Title = `--text-display-md` (56px) iridescent display
- Vetor name = `--text-h3` (28px) bold
- MITRE code = `--text-mono-md` (18px)

**Cores:**
- Cada card com border-left iridescent 4px
- Hover state: card lift + glow strengthen

---

## **SLIDE 5 — ★ Bacia de Campos (coração emocional)**

**Propósito:** Caso técnico + emocional. O ataque emblemático.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│            BACIA DE CAMPOS — O CASO                            │
│            ═══════════════════════════                          │
│                                                                 │
│       T-30d        T-7d         T-3d       T-0       T+72h    │
│       ────         ────         ────       ───       ────      │
│        ⚫──────────⚫────────────⚫─────────⚫──────────────⚫────│
│        Phishing    Discovery    Auth       Exfil      90GB   │
│        admin TI    cred VPN     VPN        72h        DoH    │
│                                                                 │
│       ╔═══════════════════════════════════════════════╗         │
│       ║                                               ║         │
│       ║   "90 GB de sísmica do pré-sal. Saindo pela   ║         │
│       ║    porta da frente. Por uma VPN legítima.     ║         │
│       ║    Por um fornecedor que deveria ter razão.   ║         │
│       ║    Durante 72 horas. E nós não vimos."         ║         │
│       ║                                               ║         │
│       ╚═══════════════════════════════════════════════╝         │
│                                                                 │
│       Custo: US$ 15-25M       Tempo p/ detectar: ~3 meses      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Timeline horizontal (6 eventos)
- Quote box (glass card com glow-danger)
- Bottom: 2 KPIs (custo + tempo)

**Tipografia:**
- Title = `--text-display-md` (56px) danger styled
- Quote = `--text-h2` (32px) italic
- KPIs = `--text-mono-lg` (24px) bold

**Cores:**
- Background: `bg-atmosphere`
- Timeline dots: iridescent → danger gradient crescendo
- Quote box: border-left danger 6px, glow-danger

**Motion:**
- Timeline: progressive reveal (T-30d → T+72h)
- Quote: fade-in com delay 1s
- KPIs: counter animation

---

## **SLIDE 6 — Vulnerabilidades BR+Petrobras**

**Propósito:** 10 casos ativos, mostrando campo de batalha real.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│        CAMPO DE BATALHA ATIVO (10 casos)                      │
│        ════════════════════════════════════                      │
│                                                                 │
│   LATAM/BR              │  PETROBRAS-ESPECÍFICOS             │
│   ─────                  │  ─────────────                       │
│   ⚡ Storm-1175 RaaS     │  🛢️ SA Exploration ($15-25M)      │
│   🎯 APT Iranian PLCs   │  🚢 OceanPact (R$ 3.2B)            │
│   💀 CrystalX RAT        │  ⚙️ Oceânica (R$ 4.2B)             │
│   📧 Boeing RFQ          │  💣 Hezbollah/Boston Sci ($80M)    │
│                          │  🐛 xz-utils backdoor              │
│                          │  🐍 npm malicioso                  │
│                          │                                       │
│   62% via fornecedor     │  Vendor VPN Compromise = padrão     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 2 colunas (LATAM | Petrobras)
- Cada item = linha com ícone + nome + (custo se aplicável)
- Footer: "62% via fornecedor" callout

**Cores:**
- LATAM col: border-left cyan
- Petrobras col: border-left iridescent
- Footer callout: gradient success + glow

---

## **SLIDE 7 — Mitigação por risco**

**Propósito:** Mostrar como AxeGuard fecha cada padrão.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│        MAPA DE COBERTURA — 5 VETORES × 4 CAMADAS              │
│        ═══════════════════════════════════════                  │
│                                                                 │
│                  MDM  OAuth DLP  VNet  SOC                    │
│   1. Supply     ████  ─    ─   ████  ████                     │
│   2. Endpoint   ████  ─    ─    ─    ████                     │
│   3. Credencial ─    ████  ─    ─    ████                     │
│   4. Exfiltração─    ─   ████  ████  ████                     │
│   5. Sobrecarga ─    ─    ─    ─    ████                     │
│                                                                 │
│        100% cobertura dos vetores observados                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Matrix 6×5 (header + 5 rows)
- Cells: iridescent (covered) / cinza escuro (gap)
- Bottom callout: "100% cobertura"

**Cores:**
- Covered cells: gradient iridescent + glow
- Gap cells: bg-tertiary (low opacity)
- Border matrix: iridescent thick

---

## **SLIDE 8 — ⭐ PROPOSTA ÚNICA (DESTAQUE VISUAL)**

**Propósito:** Apresentar os 4 pilares (QR + SOC + DLP + ZT) como diferencial.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                                                                 │
│       A PROPOSTA ÚNICA AXEGUARD                                │
│       ████████████████████████                                 │
│       (iridescent display title — animated gradient)          │
│                                                                 │
│       3 soluções de ponta. 1 estratégia.                       │
│                                                                 │
│   ┌──────────────────┐  ┌──────────────────┐                    │
│   │   📱 QR CODE     │  │   🎯 SOC          │                   │
│   │   ──────────    │  │   ──────────    │                   │
│   │   AUTENTICA     │  │   DETECTA       │                   │
│   │                  │  │                  │                   │
│   │   OAuth Device  │  │   100% auto      │                   │
│   │   Flow + TPM    │  │   MTTD < 12s     │                   │
│   │                  │  │                  │                   │
│   │   👤 Operador     │  │   👔 CISO          │                   │
│   └──────────────────┘  └──────────────────┘                    │
│   ┌──────────────────┐  ┌──────────────────┐                    │
│   │   🔒 DLP          │  │   🛡️ ZERO TRUST  │                   │
│   │   ──────────    │  │   ──────────    │                   │
│   │   PROTEGE       │  │   ESTRATÉGIA    │                   │
│   │                  │  │                  │                   │
│   │   Regex + NLP   │  │   Verify always  │                   │
│   │   atômica        │  │   Assume breach   │                   │
│   │                  │  │                  │                   │
│   │   🔬 Engenheiro   │  │   👔 CTO          │                   │
│   └──────────────────┘  └──────────────────┘                    │
│                                                                 │
│   COMPOSTO SOBRE COTS REAL. AUDITÁVEL. 90 DIAS.              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title: iridescent display animated (signature)
- Subtitle: "3 soluções de ponta. 1 estratégia."
- 2×2 grid de glass cards iridescentes (float animation staggered)
- Footer: "COMPOSTO SOBRE COTS REAL. AUDITÁVEL. 90 DIAS."

**Tipografia:**
- Title = `--text-display-xl` (96px) iridescent display animated
- Subtitle = `--text-h2` (36px)
- Pillar name = `--text-h3` (28px) bold
- Pillar description = `--text-body` (20px)

**Cores:**
- Cards: glass iridescent com border iridescent thick + glow
- Background: bg-iridescent-glow (radial gradients + 2 cores)
- Title: animated iridescent gradient

**Esta é a lâmina MAIS IMPORTANTE visualmente do pitch.**

---

## **SLIDE 9 — Solução 4 Camadas**

**Propósito:** Arquitetura técnica visual (stack vertical).

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│           ARQUITETURA AXEGUARD — 4 CAMADAS                     │
│                                                                 │
│   ┌─────────────────────────────────────────┐                  │
│   │  CAMADA 1: MDM                            │                  │
│   │  ArborXR / Hexnode UEM                    │                  │
│   │  Compliance + Kiosk Mode                  │                  │
│   └────────────────┬────────────────────────┘                  │
│                    │                                             │
│   ┌────────────────▼────────────────────────┐                  │
│   │  CAMADA 2: OAuth Device Flow             │                  │
│   │  Entra ID / Okta + PKCE + TPM            │                  │
│   └────────────────┬────────────────────────┘                  │
│                    │                                             │
│   ┌────────────────▼────────────────────────┐                  │
│   │  CAMADA 3: DLP Proxy Middleware          │                  │
│   │  FastAPI + Regex + SpaCy + UEBA            │                  │
│   └────────────────┬────────────────────────┘                  │
│                    │                                             │
│   ┌────────────────▼────────────────────────┐                  │
│   │  CAMADA 4: VNet Enclave                   │                  │
│   │  Azure OpenAI Private + No-Train B2B      │                  │
│   └────────────────┬────────────────────────┘                  │
│                    │                                             │
│        ╔═══════════▼════════════╗                               │
│        ║ SOC AGÊNTICO           ║                               │
│        ║ LangGraph + UEBA + ML   ║                               │
│        ║ MTTD < 12s              ║                               │
│        ╚════════════════════════╝                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 5 cards stacked vertical
- 4 layers normal, SOC Agêntico destacado com gradient
- Connectors verticais com glow

**Cores:**
- 4 layers: glass card normal
- SOC: gradient iridescent thick border + strong glow

---

## **SLIDE 10 — Arquitetura COTS**

**Propósito:** Mostrar tecnologias reais disponíveis hoje.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│           COMPOSIÇÃO COTS — AUDITÁVEL                          │
│                                                                 │
│   ┌─────────────────────────────────────────────────────┐     │
│   │  LAYER 1 (MDM)                                       │     │
│   │  ├── ArborXR [primary]                               │     │
│   │  ├── Hexnode UEM [alt]                              │     │
│   │  └── VMware Workspace ONE [alt]                       │     │
│   └─────────────────────────────────────────────────────┘     │
│   ┌─────────────────────────────────────────────────────┐     │
│   │  LAYER 2 (OAuth + TPM)                               │     │
│   │  ├── Microsoft Entra ID [primary]                    │     │
│   │  ├── Okta [alt]                                       │     │
│   │  └── Keycloak [open source alt]                       │     │
│   └─────────────────────────────────────────────────────┘     │
│   ┌─────────────────────────────────────────────────────┐     │
│   │  LAYER 3 (DLP)                                        │     │
│   │  ├── FastAPI + SpaCy [primary]                        │     │
│   │  ├── Microsoft Purview DLP [alt enterprise]           │     │
│   │  └── Nightfall AI DLP [alt]                           │     │
│   └─────────────────────────────────────────────────────┘     │
│   ┌─────────────────────────────────────────────────────┐     │
│   │  LAYER 4 (Enclave)                                    │     │
│   │  ├── Azure OpenAI VNet [primary]                      │     │
│   │  ├── AWS Bedrock + Llama 3 [alt]                       │     │
│   │  └── Self-hosted LLM in VPC [alt on-prem]              │     │
│   └─────────────────────────────────────────────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 4 seções, uma por camada
- Cada seção: card glass com lista de vendors (primary + alt)
- Footer tag: "IMPLEMENTÁVEL HOJE. 90 DIAS SETUP."

**Cores:**
- Primary vendors: iridescent highlight
- Alt vendors: text-secondary

---

## **SLIDE 11 (OPÇÃO B) → slide 8 do deck canônico — Antifrágil + Zero Trust (POSTURA)**

**Propósito:** Postura Zero Trust + 3 táticas.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│       ESTRATÉGIA ANTIFRÁGIL                                      │
│       ════════════════════════                                   │
│                                                                 │
│       ╔═════════════════════════════════════════════╗            │
│       ║  🛡️  POSTURA: ZERO TRUST                   ║            │
│       ║  "Nunca confiar. Sempre verificar.         ║            │
│       ║  Assumir breach. Mínimo privilégio."        ║            │
│       ╚═════════════════════════════════════════════╝            │
│                          │                                       │
│       ┌──────────────────┼──────────────────┐                   │
│       ▼                  ▼                  ▼                   │
│   ┌─────────┐      ┌─────────┐       ┌─────────┐              │
│   │🛡️ Prev.  │      │⚔️ Def.   │       │🎯 Ost.   │              │
│   │         │      │         │       │         │              │
│   │O ataque │      │Quando   │       │Quando é │              │
│   │nunca    │      │entra, é │       │inesp.,  │              │
│   │entra    │      │bloqueado│       │contra-  │              │
│   │         │      │         │       │ataca    │              │
│   └─────────┘      └─────────┘       └─────────┘              │
│                                                                 │
│   AXEGUARD = SISTEMA QUE GANHA COM O ESTRESSE                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Top: Zero Trust posture card (iridescent thick border)
- 3 cards abaixo (Preventiva, Defensiva, Ostensiva)
- Footer tagline: "SISTEMA QUE GANHA COM O ESTRESSE"

**Tipografia:**
- Title = `--text-display-md` (56px) iridescent display
- Postura quote = `--text-h3` (28px) italic
- Tática names = `--text-h3` (28px) bold

**Cores:**
- Postura: gradient iridescent thick border + glow iridescent-strong
- Táticas: glass card iridescent

---

## **SLIDE 12 (OPÇÃO B) → slide 10 do deck canônico — Viability (T+E)**

**Propósito:** Provar viabilidade técnica + econômica.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│       VIABILIDADE — T + E                                       │
│       ════════════════════                                       │
│                                                                 │
│   ┌─────────────────────┐  ┌─────────────────────┐              │
│   │ 🔧 VIAB. TÉCNICA    │  │ 💰 VIAB. ECONÔMICA  │              │
│   │ ─────────────       │  │ ─────────────       │              │
│   │ ✅ COTS real        │  │ ✅ Setup R$ 500K-2M │              │
│   │ ✅ 90 dias setup    │  │ ✅ Recurring R$ 200K-750K/mês│   │
│   │ ✅ Auditável        │  │                     │              │
│   │ ✅ Sem lock-in      │  │ ✅ ROI 47x-666x     │              │
│   │ ✅ SBOM completo    │  │ ✅ Payback < 1 dia  │              │
│   └─────────────────────┘  └─────────────────────┘              │
│                                                                 │
│       COMPLIANCE INCLUSO:                                       │
│       LGPD + ANP + IBAMA + NIS2 + ISA/IEC 62443 + SOX          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 2 colunas (T | E)
- Bottom: lista compliance como tags

**Cores:**
- Coluna E: border-left success (matrix green)
- Compliance tags: tag--default ou tag--iridescent

---

## **SLIDE 13 (OPÇÃO B) → slide 10 do deck canônico — CTA**

**Propósito:** Fechar com convite concreto + tag-line.

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│                                                                 │
│              🛢️  PILOTO 90 DIAS                                 │
│              ████████████████                                   │
│              (iridescent display animated)                       │
│                                                                 │
│              1 refinaria. Risco zero.                          │
│                                                                 │
│                                                                 │
│         FASE 1      FASE 2      FASE 3      FASE 4              │
│         (2 sem)    (4 sem)     (6 sem)    (1 sem)              │
│         SBOM +     Integração  SOC         Resultado            │
│         Discovery  4 camadas   Agêntico    Métricas            │
│                    operacionais                                │
│                                                                 │
│                                                                 │
│         💼 Próximo passo:                                        │
│         Reunião de 1h com CISO Petrobras                       │
│                                                                 │
│                                                                 │
│   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━     │
│                                                                 │
│       "De 197 dias para 12 segundos.                            │
│        De US$ 5M de incidente para R$ 1."                       │
│                                                                 │
│                    📞 matheus@axeguard.com.br                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title: iridescent display animated
- Subtitle: "1 refinaria. Risco zero."
- Fases: 4 colunas (timeline visual)
- Próximo passo: callout box
- Contact: bottom

**Tipografia:**
- Title = `--text-display-xl` (96px) iridescent display
- Subtitle = `--text-h2` (36px)
- Fases = `--text-body` (20px)
- Tag-line = `--text-h3` (28px) italic

**Cores:**
- Background: bg-atmosphere + iridescent glow blob
- Title: iridescent animated
- Fases cards: glass iridescent

---

# PARTE 10E — Implementation Notes

## **Figma Handoff**

1. **13 frames 1920×1080** (slide canvas)
2. **Variables:** importar todos os tokens do style guide Option D
3. **Text Styles:** Display + Body + Mono com weights
4. **Components:** Card Iridescent, Glass Card, KPI Hero, Icon Circle, Timeline Event
5. **Effect Styles:** Glows iridescent, shadow-md/lg/xl

## **Framer Handoff**

1. Variantes de canvas (10 slides)
2. Code Components com motion (Framer Motion)
3. Override por slide: accent + bg

## **CSS / Tailwind**

```bash
# Tailwind config já fornecido em 13_style_guide_option_D_holographic.md
# Adicionar:
```

```js
// Componentes específicos
module.exports = {
  plugins: [
    require('@tailwindcss/forms'),
    require('tailwindcss-animate-css-grid'),
  ]
}
```

---

## ⏭️ Próximas partes

- **PARTE 11 — Especificação de Exportação** (Figma frame dimensions, video specs, YouTube upload checklist)
- **PARTE 12 — Asset Checklist** (logos, ícones, fontes, ilustrações necessárias)

---

## ❓ Perguntas para você

1. **KPI Hero counter animation** (0→197 em 1.4s) está no tom certo?
2. **Float animation staggered** nos 4 pilares da Proposta Única (slide 8) — confirmar?
3. **Timeline progressive reveal** (slide 5, Bacia de Campos) — usar ou não?
4. **Background iridescent glow blob** (cantos flutuantes) — em quais slides?
5. **Tags compliance** no slide 10 — listar individualmente ou como bloco?