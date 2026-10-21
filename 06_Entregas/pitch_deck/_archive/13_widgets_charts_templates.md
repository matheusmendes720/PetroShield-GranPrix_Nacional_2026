# PARTE 10 — Widgets, Charts, Diagramas & Slide Templates

> **Deliverable:** Blueprint visual completo dos 13 slides do pitch — pronto para implementação em Figma/Framer/CSS.
> **Função:** Cada template detalha layout, componentes, animações e notas de implementação.
> **Versão:** v0.1 — Outubro 2026
> **Tokens base:** ver `12_design_tokens.md` (PARTE 9)

---

## 📐 SEÇÃO 1 — Reusable Widgets

### **W1 — Card Glass (genérico)**

```
┌──────────────────────────────────────┐
│  [icon]                              │
│                                      │
│  Título do Card                      │
│  ─────────────                       │
│  Body description text goes here.    │
│  Smaller details in tertiary.        │
│                                      │
│                    [valor] [badge]   │
└──────────────────────────────────────┘
```

**Component config:**
- `.card-glass` com `--space-5` padding
- Border-top 2px (varia conforme accent: matrix / trust / danger / warning)
- Glow effect conforme accent
- Animation: slide-up + fade-in ao entrar no viewport

---

### **W2 — KPI Hero (número grande + label)**

```
   ┌────────────────────────┐
   │                        │
   │      197 dias          │  ← .kpi-hero (mono, 96px, matrix, glow)
   │                        │
   │  ─────────────────     │
   │                        │
   │  MTTD INDÚSTRIA       │  ← .kpi-label (body-sm, tertiary, uppercase)
   │                        │
   └────────────────────────┘
```

**Variações por accent:**
- `.kpi-hero--matrix` — verde matrix (success, "depois")
- `.kpi-hero--danger` — vermelho (risco, "antes")
- `.kpi-hero--trust` — azul trust (defesa, neutral)

**Animation:** Count from 0 to target em 1200ms (usar `--duration-counter`)

---

### **W3 — Icon Circle (pequeno destaque)**

```
       ┌───────┐
       │  🛡️   │  ← Icon 32px, em círculo de 64px
       └───────┘
              Border 2px = accent color
              Glow sutil
```

**Tamanhos:**
- `sm` — 48px circle, icon 24px
- `md` — 64px circle, icon 32px (padrão)
- `lg` — 96px circle, icon 48px (slide hero)

---

### **W4 — Badge / Pill**

```
   [● Ativo]  [● Histórico]  [● Crítico]
```

- Background semi-transparente (var(--danger-bg), etc.)
- Border-radius 999px (pill)
- Padding 4px 12px
- Dot color = semantic

---

### **W5 — Tag (categoria)**

```
   [SUPPLY CHAIN]  [ENDPOINT]  [CREDENCIAL]  [EXFILTRAÇÃO]  [SOBRECARGA]
```

- Uppercase, letter-spacing 0.08em
- Font 12-14px, medium weight
- Border 1px, color = padrão da categoria

---

## 📊 SEÇÃO 2 — Reusable Charts

### **C1 — Bar Chart Comparativo (Antes vs Depois)**

```
   MTTD                    MTTD
   ┌─────┐                 ┌─────┐
   │     │                 │     │
   │ 322 │ BR (atual)      │  12 │ BR (com AxeGuard)
   │ dias│                 │ segs│
   │     │                 │     │
   └─────┘                 └─────┘
   ────────────────────────────────
   100%                    0.04%
```

**Spec:**
- Bar height proporcional (escala log se necessário)
- Color: Antes = danger gradient; Depois = success gradient
- Label abaixo de cada barra
- Animation: bars crescem de baixo (height 0 → target) em 800ms

---

### **C2 — Number Counter Animation**

**Uso:** KPIs animados em sequência durante o pitch.

**Implementation:**
```js
// Pseudo-code
const counter = new Counter(element, {
  from: 0,
  to: 197,
  duration: 1200,
  formatter: (v) => `${Math.round(v)} dias`,
  onComplete: () => counter2.start() // encadeia
});
```

---

### **C3 — Coverage Donut (100% cobertura)**

```
        ╱─────╲
       ╱   100%  ╲
      │  COBERTURA │
      │   19→8→4   │
       ╲          ╱
        ╲──────╱

```
**Spec:**
- Donut SVG 240px diameter
- Center: número "100%" em display-xl mono + label
- Stroke color: gradient (matrix → trust)
- Animation: stroke-dashoffset de 100 → 0 em 1500ms

---

### **C4 — Severity Badge Distribution (padrão de status)**

```
   🔴 Crítico     × 4
   🟠 Alto        × 5
   🟡 Médio       × 1
```

**Spec:**
- Horizontal bar com 3 segmentos coloridos
- Legend com counts ao lado
- Animation: bars crescem sequencialmente em 600ms cada

---

## 🗺️ SEÇÃO 3 — Reusable Diagrams

### **D1 — Architecture Stack (4 camadas)**

```
                    ╔═══════════════════╗
                    ║   SOC AGÊNTICO    ║ ← Camada 5 (backend)
                    ║   MTTD < 12s      ║
                    ╚═══════╤═══════════╝
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
    ┌────▼────┐      ┌──────▼──────┐    ┌──────▼──────┐
    │ CAMADA 4 │      │  CAMADA 3   │    │  CAMADA 2   │ ...
    │  VNet    │      │  DLP Proxy  │    │  OAuth+TPM  │
    │ Enclave  │      │  Middleware │    │  Device Flow│
    │ No-Train │      │  Regex+NLP  │    │  PKCE       │
    └──────────┘      └─────────────┘    └─────────────┘
   
```

**Spec:**
- 5 caixas stacked verticalmente (SOC no topo, camadas 4→1 abaixo)
- Cada caixa 0.75rem height (proporcional ao "peso" da camada)
- Background da caixa = accent gradient
- Border glow conforme camada
- Texto dentro: nome + tecnologia + sample em keyframe

---

### **D2 — Attack Timeline (horizontal)**

```
   T-30d    T-7d    T-3d    T-0    T+72h    T+90d
   ──●───────●───────●───────●──────────●──────●──→
      │       │       │       │          │      │
   [phish] [disc] [auth] [exfil] [exfil] [disc]
                                          [Petrobras
                                          notificada]
```

**Spec:**
- Horizontal line com 6 dots/marcadores
- Cada marcador = momento do ataque
- Cor dos dots: amarelo (early) → vermelho (exfil) → vermelho forte (discovery)
- Animation: dots aparecem sequencialmente, line grows from left

---

### **D3 — Coverage Matrix (5 padrões × layer)**
```
                 L1    L2    L3    L4    SOC
   Supply        ●     ○     ○     ●     ●
   Endpoint      ●     ○     ○     ○     ●
   Credencial    ○     ●     ○     ○     ●
   Exfiltração    ○     ○     ●     ●     ●
   Sobrecarga    ○     ○     ○     ○     ●
```

**Spec:**
- 5×5 grid com dots coloridos
- ● = cobertura direta (matrix-green)
- ◐ = cobertura parcial (warning)
- ○ = sem cobertura
- Click/tap reveals detail (em apresentação interativa)

---

### **D4 — Stakeholder Mapping (4 personas)**

```
       👤 Operador        👔 CISO
            │                 │
            ▼                 ▼
        ┌─────┐           ┌─────┐
        │ QR  │           │ SOC │
        └─────┘           └─────┘
                              ▲
                              │
       🔬 Engenheiro    👔 CTO
            │                 │
            ▼                 ▼
        ┌─────┐           ┌─────┐
        │ DLP │           │ ZT  │
        └─────┘           └─────┘
```

**Spec:**
- 4 personas em 4 quadrantes
- Cada persona aponta para 1 dos 4 pilares
- Cores diferentes por pilar
- Conexões com setas animadas (stroke-dashoffset)

---

### **D5 — 3 Pilar Radial (Antifrágil + ZT)**

```
              ┌─────────────┐
              │  ZERO TRUST │
              │   POSTURA   │
              └──────┬──────┘
                     │ (3 arrows)
       ┌─────────────┼─────────────┐
       │             │             │
   ┌───▼──┐     ┌───▼──┐     ┌───▼──┐
   │PREV  │     │DEFEN │     │OSTEN │
   └──────┘     └──────┘     └──────┘
```

**Spec:**
- ZT no topo (fundo, brilho trust-blue)
- 3 táticas abaixo em row
- Linhas conectoras com animação
- Cada tática com icon + 1 linha

---

## 🎨 SEÇÃO 4 — 13 Slide Templates

---

### **SLIDE 1 — HOOK (Impacto)**

**Função:** Prender atenção em 5 segundos com 1 número devastador.

**Layout (1920x1080):**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                                                                          │
│                                                                          │
│                      (background atmosphere + grid scan)                  │
│                                                                          │
│                                                                          │
│                       197 DIAS                                          │
│                       ────────                                          │
│            É quanto a indústria leva, em média,                          │
│            para detectar um ataque.                                      │
│                                                                          │
│                                                                          │
│                                                                          │
│   AXEGUARD • CIBERSEGURANÇA INDUSTRIAL PARA XR                           │
│                                                                          │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- `.bg-atmosphere` + grid scan
- `.kpi-hero--danger` (197 DIAS) — 144px, danger color
- `.text-body-lg` para a frase de impacto
- Bottom: brand bar com `.text-mono-md` (uppercase, letter-spacing 0.1em)

**Animations:**
- 0s: bg + grid fade-in (300ms)
- 1s: número 0 → 197 (counter, 1200ms)
- 2.5s: frase slide-up + fade-in (500ms)
- 3.5s: brand bar slide-in (400ms)

**Duração total:** 4s entrada + 11s estática = 15s

---

### **SLIDE 2 — HOOK Caso (Bacia de Campos teaser)**

**Função:** Tease do caso anchor + transição emocional.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                                                                          │
│     BACIA DE CAMPOS, NOVEMBRO 2025.                                      │
│     ─────────────────────────────                                       │
│                                                                          │
│     Um fornecedor legítimo.                                              │
│     Credenciais válidas.                                                │
│     Acesso autorizado.                                                   │
│                                                                          │
│     90 GB de dados sísmicos.                                            │
│     Saindo por 72 horas.                                                │
│     Sem que ninguém visse.                                              │
│                                                                          │
│                                                                          │
│                                    [detalhes na próxima] →               │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title `.text-display-lg` com accent `--danger`
- 3 linhas de body `.text-body-lg` em sequência
- Mapa estilizado sutil no canto (opcional, SVG estilizado)
- Seta CTA no canto inferior direito

**Animations:**
- Title slide-up + fade-in (400ms)
- Cada linha de body aparece em sequência (200ms stagger)
- Seta pulse glow

**Duração:** 18s

---

### **SLIDE 3 — Paradoxo**

**Função:** Tensão central do pitch — XR ajuda mas vulnerabiliza.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      O PARADOXO DA XR INDUSTRIAL                                         │
│      ═══════════════════════════                                         │
│                                                                          │
│                                                                          │
│      ┌────────────────────┐    ┌────────────────────┐                   │
│      │ 🟢 GANHOS          │    │ 🔴 PERDAS           │                  │
│      │ ─────              │    │ ─────              │                   │
│      │ • Treinamento     │    │ • Câmera exposta   │                  │
│      │   imersivo         │    │ • Mic capturando   │                  │
│      │ • Assistência      │    │ • Token roubável   │                  │
│      │   remota           │    │ • Geolocalização   │                  │
│      │ • Digital twins    │    │   exposta           │                  │
│      │ • Manutenção       │    │ • Dados senssíveis  │                  │
│      │   preditiva        │    │   vazáveis          │                  │
│      └────────────────────┘    └────────────────────┘                   │
│                                                                          │
│           Mais dependência = Mais superfície de ataque.                  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title `.text-display-md`
- 2 cards `.card-glass` lado a lado
- Esquerda: border-left `--success` (matrix)
- Direita: border-left `--danger`
- Footer com `.text-h3`

**Animations:**
- Cards slide-up sequencial (esquerda 0ms, direita 300ms)
- Itens dentro de cada card fade-in stagger (100ms cada)
- Footer pulse glow

**Duração:** 15s

---

### **SLIDE 4 — 5 Vetores**

**Função:** Visualizar os 5 padrões globais diagnosticados.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      OS 5 VETORES QUE DEFINEM O CAMPO DE BATALHA                          │
│                                                                          │
│                                                                          │
│   ┌────┐    ┌────┐    ┌────┐    ┌────┐    ┌────┐                      │
│   │ 1  │    │ 2  │    │ 3  │    │ 4  │    │ 5  │                       │
│   │ 🔗 │    │ 📱 │    │ 🔑 │    │ 📡 │    │ 🌪️ │                       │
│   │SUPL│    │END │    │CRED│    │EXFI│    │SOBR│                       │
│   │CHAIN    │POIN│    │ENCI│    │LTRA│    │CAR │                       │
│   └────┘    └────┘    └────┘    └────┘    └────┘                      │
│  Supply    Endpoint     ├IDMO    Exfilt.  Cogni.                       │
│  Chain     Compromise   OAuth  DLP      Overload                      │
│                                                                          │
│   Atacantes: CN/RU/IL/IR/NK (state) + criminal orgs                    │
│   ──────────────────────────────────────────────────                    │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 5 `.card-glass` mini cards em row
- Cada card: número grande + icon + tag
- Footer com 1 linha: atacantes + geografias

**Animations:**
- Cards slide-up sequencial (150ms stagger)
- Numbers count 0 → 5 em 800ms
- Footer fade-in depois dos cards

**Duração:** 18s

---

### **SLIDE 5 — ★ Bacia de Campos (deep-dive)**

**Função:** Coração emocional do pitch. Caso real com timeline.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      ★ CASO: BACIA DE CAMPOS — NOVEMBRO 2025 ★                           │
│                                                                          │
│                                                                          │
│   T-30d         T-7d          T-0           T+72h        T+90d          │
│   ─────         ─────         ─────         ──────       ──────         │
│   ●             ●             ●             ●            ●             │
│   │             │             │             │            │             │
│  Phish        Discovery     Auth          Exfil        Discovery     │
│  admin        credenciais   VPN           90GB sísmic  dark web       │
│  SA Exp.      texto claro   Petrobras    via DoH      "Brazilian    │
│               Petrop.              ↘                  offshore        │
│                                       Moldávia        seismic"        │
│                                                                          │
│                                                                          │
│      90 GB. 72 horas. Ninguém viu.                                       │
│                                                                          │
│      "O que sai pela SUA amanhã?"                                       │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title com `★` decorative
- `.timeline` (D2) horizontal
- 5 dots, line conectando
- Cada dot com label + sub-label
- Bottom: tagline em `.text-h3` com `.text-mono-xl` para "90 GB" e "72 horas"
- Pausa dramática no final

**Animations:**
- Line draw da esquerda para direita (1500ms)
- Cada dot aparece sequencialmente (200ms cada)
- Bottom tagline pulse glow + scale up

**Duração:** 60s (slide mais longo, coração do pitch)

---

### **SLIDE 6 — Vulnerabilidades (10 casos)**

**Função:** Catalogar campo de batalha ativo.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      CAMPO DE BATALHA: 10 CASOS ATIVOS E HISTÓRICOS                       │
│                                                                          │
│   ┌────────────────────┐  ┌────────────────────┐                       │
│   │ 🇧🇷 LATAM/BR        │  │ 🛢️ PETROBRAS         │                      │
│   │ ─────              │  │  ─────              │                      │
│   │ • Storm-1175       │  │ • SA Exploration     │                     │
│   │   RaaS 2026        │  │   Nov 2025           │                     │
│   │   [● Ativo]        │  │   [● Crítico]        │                     │
│   │                    │  │                      │                     │
│   │ • APT Iranian PLCs │  │ • OceanPact          │                     │
│   │   Abr 2026         │  │   2024               │                     │
│   │   [● Alerta CISA]  │  │   [● Token vazado]   │                     │
│   │                    │  │                      │                     │
│   │ • CrystalX RAT     │  │ • Oceânica           │                     │
│   │   Jan 2026         │  │   2024-25            │                     │
│   │   [● Mobile OAuth] │  │   [● Proxy bypass]   │                     │
│   │                    │  │                      │                     │
│   │ • Boeing RFQ       │  │ • Hezbollah/Boston   │                     │
│   │   2026             │  │   Set 2024           │                     │
│   │   [● BEC]          │  │   [● Supply HW]      │                     │
│   └────────────────────┘  └────────────────────┘                       │
│                                                                          │
│   + PADRÃO SISTÊMICO: 62% dos breaches O&G via fornecedor                │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- 2 colunas (LATAM/BR + Petrobras)
- Cada coluna: 4-5 case cards `.card-glass--mini`
- Cada case: nome + data + badge
- Footer: padrão sistêmico

**Animations:**
- Coluna esquerda slide-up + fade-in (0ms)
- Coluna direita slide-up + fade-in (300ms)
- Items stagger fade-in dentro de cada coluna
- Footer pulse glow

**Duração:** 30s

---

### **SLIDE 7 — Mitigação (5 padrões → camada)**

**Função:** Mostrar como AxeGuard responde a cada padrão.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      COMO AXEGUARD FECHA CADA PADRÃO                                     │
│                                                                          │
│                                                                          │
│   Padrão            Camada AxeGuard     Impacto                       │
│   ─────             ──────────────       ────────                     │
│   1. Supply Chain   L1 (MDM) + L4       SBOM 100% + root block       │
│   2. Endpoint       L1 (Kiosk Mode)     Side-load 0% sucesso         │
│   3. Credencial     L2 (OAuth+TPM)      QR ≠ token sem TPM            │
│   4. Exfiltração    L3 (DLP) + L4       90GB via DNS = 0GB egress    │
│   5. Sobrecarga     SOC Agêntico        197d → 12s MTTD              │
│                                                                          │
│                                                                          │
│   4 camadas. 1 SOC. 100% cobertura. 0 brechas observadas.               │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title `.text-display-md`
- Table-style layout (não Heading de 4 colunas)
- Cada row: padrão + camada + impacto
- Footer com tagline

**Animations:**
- Rows fade-in sequencial (150ms stagger)
- "100%" hover — counter 0 → 100
- Footer slide-up + glow pulse

**Duração:** 25s

---

### **SLIDE 8 — ⭐ PROPOSTA ÚNICA**

**Função:** Slide central de diferenciação. 3 soluções + 1 estratégia.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│              A PROPOSTA ÚNICA AXEGUARD                                   │
│              ═══════════════════════                                      │
│                                                                          │
│           3 SOLUÇÕES DE PONTA. 1 ESTRATÉGIA.                              │
│                                                                          │
│                                                                          │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐      │
│  │                 │   │                 │   │                 │      │
│  │   📱 QR CODE     │   │   🎯 SOC          │   │   🔒 DLP          │   │
│  │   ──────────    │   │   ──────────    │   │   ──────────    │   │
│  │   AUTENTICA     │   │   DETECTA       │   │   PROTEGE       │   │
│  │                 │   │                 │   │                 │   │
│  │  • OAuth Device │   │  • 100% auto    │   │  • Regex + NLP  │   │
│  │  • PKCE         │   │  • MTTD < 12s   │   │  • Atômica     │   │
│  │  • TPM 2.0      │   │  • LangGraph    │   │  • Channel     │   │
│  │                 │   │                 │   │  • UEBA         │   │
│  │  👤 Operador     │   │  👔 CISO          │   │  🔬 Engenheiro   │   │
│  └─────────────────┘   └─────────────────┘   └─────────────────┘      │
│                                                                          │
│                ╔═══════════════════════════════════════╗                │
│                ║   🛡️  ZERO TRUST — A ESTRATÉGIA        ║                │
│                ║   "Nunca confiar. Sempre verificar.    ║                │
│                ║    Assumir breach. Mínimo privilégio." ║                │
│                ║   👔 CTO/Board                        ║                │
│                ╚═══════════════════════════════════════╝                │
│                                                                          │
│           COMPOSTO SOBRE COTS REAL. AUDITÁVEL. 90 DIAS.                  │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title central
- 3 callouts `.card-glass--matrix/trust` (cores diferentes)
- 1 banner `.gradient-defense` no meio
- Footer: tagline final

**Animations:**
- Title slide-up + fade-in
- 3 cards slide-up sequencial (200ms stagger)
- Banner ZT pulse glow (forte — slide central)
- Footer scale-up + slide-up

**Duração:** 25s

---

### **SLIDE 9 — Solução 4 Camadas**

**Função:** Visão técnica da arquitetura.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      A ARQUITETURA: 4 CAMADAS + 1 SOC                                    │
│                                                                          │
│                                                                          │
│                    ╔═══════════════════╗                                 │
│                    ║   SOC AGÊNTICO    ║                                 │
│                    ║   MTTD < 12s      ║                                 │
│                    ╚═══════╤═══════════╝                                 │
│                            │                                            │
│      ┌─────────────────────┼─────────────────────┐                      │
│      │                     │                     │                      │
│  ┌───▼─────────┐    ┌───────▼────────┐    ┌──────▼────────┐           │
│  │  CAMADA 4    │    │   CAMADA 3     │    │   CAMADA 2    │           │
│  │  VNet        │    │   DLP Proxy    │    │   OAuth+TPM   │           │
│  │  Enclave     │    │   Middleware   │    │   Device Flow  │           │
│  │  No-Train    │    │   Regex + NLP  │    │   PKCE         │           │
│  │  [Azure      │    │   [FastAPI +   │    │   [Entra ID    │           │
│  │   OpenAI]    │    │    SpaCy]      │    │    Okta]        │           │
│  └─────────────┘    └────────────────┘    └────────────────┘           │
│                                                                          │
│              ┌───────────────────────────────────┐                      │
│              │         CAMADA 1                  │                      │
│              │   MDM Kiosk Mode                  │                      │
│              │   [ArborXR / Hexnode]            │                      │
│              └───────────────────────────────────┘                      │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title `.text-display-md`
- `.architecture-stack` (D1) com 5 caixas
- Cores por camada (gradient conforme accent)
- COTS products em cada caixa

**Animations:**
- Stack aparece bottom-up (camada 1 primeiro, SOC último)
- Cada camada slide-up + fade-in sequencial (300ms stagger)
- Glow pulse ao final

**Duração:** 18s

---

### **SLIDE 10 — Arquitetura COTS**

**Função:** Mostrar produtos reais (audibilidade).

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      COMPOSTO SOBRE COTS REAL                                            │
│      ═══════════════════════                                            │
│                                                                          │
│      ✅ Não inventamos a roda.                                           │
│      ✅ Cada peça é tecnologia de mercado.                                │
│      ✅ Petrobras pode auditar separadamente.                            │
│                                                                          │
│                                                                          │
│   ┌──────────────────────────────────────────────────────────────┐     │
│   │  L1 MDM          │  ArborXR / Hexnode UEM  │  ●●●●●        │     │
│   │  L2 OAuth        │  Microsoft Entra ID      │  ●●●●●        │     │
│   │  L3 DLP Proxy    │  FastAPI + SpaCy         │  ●●●●○        │     │
│   │  L4 Enclave      │  Azure OpenAI VNet       │  ●●●●●        │     │
│   │  SOC             │  LangGraph + Kafka       │  ●●●●○        │     │
│   └──────────────────────────────────────────────────────────────┘     │
│                                                                          │
│   ●●●●● = produção • ●●●○ = prototype deployado                         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title com accent `--brand-trust`
- 3 linhas de benefícios com checkmark verde
- Tabela 5 linhas (L1..SOC × COTS × status)
- Footer com legenda dos dots

**Animations:**
- Benefícios fade-in stagger (200ms)
- Tabela rows slide-up sequencial
- Footer pulse glow

**Duração:** 18s

---

### **SLIDE 11 — Antifrágil + Zero Trust**

**Função:** Postura estratégica + 3 táticas.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      ESTRATÉGIA ANTIFRÁGIL AXEGUARD                                      │
│                                                                          │
│                                                                          │
│         ╔═══════════════════════════════════════════════╗               │
│         ║                                               ║               │
│         ║   🛡️  POSTURA: ZERO TRUST                      ║               │
│         ║                                               ║               │
│         ║   "Nunca confiar. Sempre verificar.           ║               │
│         ║    Assumir breach. Mínimo privilégio."        ║               │
│         ║                                               ║               │
│         ╚════════════════╤══════════════════════════════╝               │
│                          │                                               │
│                          │ (3 táticas)                                   │
│                          ▼                                               │
│       ┌──────────────────┼──────────────────┐                          │
│       │                  │                  │                          │
│       ▼                  ▼                  ▼                          │
│   ┌─────────┐        ┌─────────┐        ┌─────────┐                   │
│   │ 🛡️ PREV  │        │ ⚔️ DEF   │        │ 🎯 OST   │                   │
│   │         │        │         │        │         │                   │
│   │ Nunca   │        │ Quando  │        │ Inespe- │                   │
│   │ entra   │        │ entra,  │        │ rado,   │                   │
│   │         │        │ bloque- │        │ contra- │                   │
│   │         │        │ ado     │        │ ataca   │                   │
│   └─────────┘        └─────────┘        └─────────┘                   │
│                                                                          │
│      AXEGUARD = SISTEMA QUE GANHA COM O ESTRESSE                        │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title
- Banner ZT no topo (`.gradient-defense`)
- 3 cards táticas (`.card-glass`)
- Footer com tagline antifrágil

**Animations:**
- ZT banner slide-down + pulse glow (entrada forte)
- 3 cards táticas slide-up sequencial (200ms stagger)
- Conexões ZT→táticas com stroke-dashoffset animado
- Footer scale-up

**Duração:** 18s

---

### **SLIDE 12 — Viability (Técnica + Econômica)**

**Função:** Provar que é implementável + vale o investimento.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│      VIABILIDADE TÉCNICA + ECONÔMICA                                      │
│                                                                          │
│                                                                          │
│      ┌──────────────────────┐    ┌──────────────────────┐               │
│      │ 🔧 TÉCNICA            │    │ 💰 ECONÔMICA          │              │
│      │ ─────                │    │ ─────                │              │
│      │                      │    │                      │              │
│      │ ✅ COTS real          │    │ ✅ Custo: R$ 0        │             │
│      │ ✅ 90 dias setup     │    │    em código próprio  │              │
│      │ ✅ Sem reinventar     │    │                      │              │
│      │ ✅ Auditável          │    │ ✅ Setup: R$ 500K-2M │              │
│      │                      │    │                      │              │
│      │ ⚠️ Risco residual:    │    │ ✅ Recurring:         │              │
│      │ Supply Chain HW      │    │    R$ 100-500K/mês   │              │
│      │ em fábrica (mitigado │    │                      │              │
│      │ por procurement)     │    │ ✅ ROI: 100x-500x     │              │
│      │                      │    │                      │              │
│      │                      │    │ ✅ Payback: < 1 dia  │              │
│      └──────────────────────┘    └──────────────────────┘               │
│                                                                          │
│      SCOPE: ENTERPRISE MULTINACIONAL (não PME)                          │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Title `.text-display-md`
- 2 colunas (Técnica + Econômica)
- Cada coluna: cards/linhas com checkmarks
- Footer: scope reminder

**Animations:**
- 2 colunas slide-up simultâneo
- Items stagger fade-in
- Números KPI animated (ROI counter, payback counter)
- Footer pulse glow

**Duração:** 25s

---

### **SLIDE 13 — CTA (Convite)**

**Função:** Fechar o pitch com proposta concreta.

**Layout:**

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│                                                                          │
│                    🛢️  PILOTO 90 DIAS                                   │
│                                                                          │
│                    1 refinaria                               │
│                    Risco zero                              │
│                                                                          │
│                                                                          │
│       SEM 1-2       SEM 3-6       SEM 7-12       SEM 13                │
│       ───────       ───────       ───────        ─────                │
│       ●             ●             ●             ●                    │
│       Descoberta    Integração    SOC            Resultado            │
│       SBOM+CTI    Camadas 1-4   Agêntico       Métricas            │
│                                                  + ROI demo            │
│                                                                          │
│                                                                          │
│       📞 Reunião executiva de 1h com CISO Petrobras                    │
│                                                                          │
│                                                                          │
│       "De 197 dias para 12 segundos.                                     │
│        De US$ 5M de incidente para R$ 1."                             │
│                                                                          │
│                                                                          │
│       📞 matheus@axeguard.com.br                                        │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

**Componentes:**
- Headline massiva `.text-display-xl`
- Sub-headline: 3 linhas
- Timeline horizontal 4 fases
- CTA button (gradient defense)
- Tag-line final
- Email contato

**Animations:**
- Headline scale-up + glow pulse (entrada com força)
- Sub-headline slide-up
- Timeline dots stagger fade-in
- Button pulse glow contínuo
- Tag-line scale-up com background

**Duração:** 15s

---

## 📋 Resumo de durações por slide

| Slide | Função | Duração |
|---|---|---|
| 1 | HOOK impacto | 15s |
| 2 | HOOK caso | 18s |
| 3 | Paradoxo | 15s |
| 4 | 5 vetores | 18s |
| 5 | ★ Bacia de Campos ★ | 60s |
| 6 | Vulnerabilidades | 30s |
| 7 | Mitigação | 25s |
| 8 | ⭐ Proposta Única | 25s |
| 9 | Solução 4 camadas | 18s |
| 10 | Arquitetura COTS | 18s |
| 11 | Antifrágil + ZT | 18s |
| 12 | Viability | 25s |
| 13 | CTA | 15s |
| **TOTAL** | | **300s = 5min** |

⚠️ **OVER-BUDGET**: 13 slides dá ~5 min, não 3 min. **Recomendações:**

**Opção A — Cortar para 10 slides (3 min):**
- Remover slide 10 (Arquitetura COTS — fundir com slide 9)
- Remover slide 11 (Antifrágil separado — fundir com slide 8 Proposta Única)
- Manter 12 + 13

**Opção B — Manter 13 slides, target 5 min:**
- Aceitar que é pitch mais longo (5 min é viável se regra permitir; verificar regulamento SENAI Entrega 3 — limite rígído 3 min)

**Opção C — Slides paralelos:**
- Alguns slides podem ter versão resumida (slide-up rápido, fica 10s)
- Cortar tempo de slides 1-4 (mais curtos)
- Manter slide 5 (coração) com 60s

---

## ⏭️ Fim do scaffold visual

**Todas as 10 partes estão prontas:**

✅ 1 — Master scaffold
✅ 2A — Diagnóstico global de ataques
✅ 2B — Filtro Petrobras + relevância AxeGuard
✅ 2C — Mitigação por risco
✅ 3A — Vulnerabilidades Petrobras + LATAM
✅ 3B — Caso Bacia de Campos
✅ 4 — Solução técnica + COTS
✅ 5 — Estratégia Antifrágil + Zero Trust
✅ 6 — Viability enterprise
✅ 7 — Convite + CTA
✅ 8 — Proposta Única (QR + SOC + DLP + ZT)
✅ 9 — Design tokens
✅ 10 — Widgets + 13 slide templates

---

## ❓ Decisão pendente — Orçamentos de tempo

1. **Manter 13 slides (5 min)** ou **cortar para 10 slides (3 min)**?
2. **Slides 1-4 muito curtos** (10s cada) — cortaria 20s do orçamento
3. **Slide 5 Bacia de Campos com 60s** é justo ou excessivo?

Aguardando seu OK pra fechar ou ajustar.