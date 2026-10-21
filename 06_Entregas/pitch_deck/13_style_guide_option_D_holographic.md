# Style Guide — OPTION D (Holographic/Futurist)

> **Deliverable:** Sistema visual canônico para o pitch deck AxeGuard — baseado na escolha do usuário.
> **Função:** Tokens prontos para Figma / Framer / CSS / Tailwind. Substitui a base genérica de `12_design_tokens.md`.
> **Vibe:** Apple Vision Pro + Meta spatial UI + cyberpunk-lite + iridescent futurism
> **Versão:** v0.1 — Outubro 2026
> **Status:** CANÔNICO — use este como referência para todos os 10 slides (OPÇÃO A)

---

## 🎯 Princípios visuais (signature)

| Princípio | Aplicação |
|---|---|
| **Spatial premium** | Cada elemento parece flutuar em uma camada — não em uma página plana |
| **Iridescent accents** | Gradientes sutis violeta→ciano como assinatura cromática |
| **Glassmorphism** | Cards translúcidos com blur backdrop, bordas finas iridescentes |
| **Typography-first** | Display bold em sans-serif moderna; mono para números técnicos |
| **Whitespace generoso** | Respiro entre blocos; density controlado (não Bloomberg-style) |
| **Motion fluido** | Spring easing, glow-pulse, translação sutil (não bouncing) |
| **Noise sutil** | Grain texture sobre bg para evitar "flat digital" |

---

## 🎨 Color Palette

### **Background & Surfaces**

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--bg-primary` | `#0A0E27` | 10, 14, 39 | Background principal (deep blue-purple dark) |
| `--bg-secondary` | `#131836` | 19, 24, 54 | Cards, surfaces elevadas |
| `--bg-tertiary` | `#1F2447` | 31, 36, 71 | Hover states, surfaces top |
| `--bg-overlay` | `rgba(10,14,39,0.85)` | — | Overlays + blur backdrop |
| `--bg-glass` | `rgba(31,36,71,0.6)` | — | Cards glassmorphism |
| `--bg-glass-strong` | `rgba(19,24,54,0.85)` | — | Cards prioritários |

### **Brand Colors (signature iridescent)**

| Token | HEX | RGB | Uso |
|---|---|---|---|
| `--brand-iridescent` | `#6366F1` | 99, 102, 241 | **DOMINANTE** — solução, defesa, zero-trust, indigo |
| `--brand-cyan` | `#00D4FF` | 0, 212, 255 | **APOIO** — AI, real-time, vector cyan |
| `--brand-matrix` | `#00FF41` | 0, 255, 65 | **HIGHLIGHTS** — SOC, detecção, success (raros) |
| `--brand-iridescent-glow` | `rgba(99,102,241,0.5)` | — | Glow effects (base) |
| `--brand-cyan-glow` | `rgba(0,212,255,0.5)` | — | Glow effects (realce) |
| `--brand-matrix-glow` | `rgba(0,255,65,0.45)` | — | Glow highlights (raros) |

### **Text Colors**

| Token | HEX | Uso |
|---|---|---|
| `--text-primary` | `#F8F9FB` | Headings, números grandes (off-white premium, não pure white) |
| `--text-secondary` | `#C7CAD9` | Body, parágrafos |
| `--text-tertiary` | `#7B7F95` | Caption, labels, metadata — no deck foi elevado para `#8A8EA6` (ver § Aplicação no deck) |
| `--text-disabled` | `#3F4262` | Disabled states |
| `--text-inverse` | `#0A0E27` | Texto em botões brand |
| `--text-iridescent` | `linear-gradient(135deg, #6366F1, #00D4FF)` | **Special**: títulos com gradient iridescente |

### **Semantic Colors (feedback)**

| Token | HEX | Uso |
|---|---|---|
| `--danger` | `#FF4757` | Ataques, "antes", alertas críticos |
| `--warning` | `#FFD33D` | Riscos residuais, atenção |
| `--success` | `#00FF41` (= matrix) | Defesa, success, "depois" |
| `--info` | `#00D4FF` (= cyan) | Neutro técnico, callouts |
| `--danger-bg` | `rgba(255,71,87,0.12)` | Background de alertas |
| `--success-bg` | `rgba(0,255,65,0.12)` | Background de success |

### **Stroke / Borders**

| Token | Value | Uso |
|---|---|---|
| `--border-subtle` | `rgba(99,102,241,0.18)` | Borders cards glassmorphism |
| `--border-default` | `rgba(99,102,241,0.3)` | Borders sutis em cards |
| `--border-strong` | `rgba(99,102,241,0.55)` | Borders de ênfase |
| `--border-iridescent` | `linear-gradient(135deg, #6366F1, #00D4FF)` | Borders signature (1-2px) |

---

## 📐 Typography

### **Font Families**

| Token | Family | Free alternative | Uso |
|---|---|---|---|
| `--font-display` | `'Söhne', 'Inter Display', system-ui` | Inter (Google Fonts) | H1, H2 (impacto) |
| `--font-body` | `'Inter', system-ui, sans-serif` | Inter (Google Fonts) | Body, parágrafos |
| `--font-mono` | `'JetBrains Mono', 'IBM Plex Mono', monospace` | JetBrains Mono (Google Fonts) | KPIs, código, números |

**Nota:** Söhne é premium (Klim Type Foundry); se usar só fontes gratuitas, **Inter** + **JetBrains Mono** (Google Fonts) cobrem 95% da necessidade.

### **Type Scale (slide-screen)**

| Token | Size (px) | Line Height | Letter Spacing | Uso |
|---|---|---|---|---|
| `--text-display-xl` | 96 | 1.05 | -0.03em | Hero / HOOK slide |
| `--text-display-lg` | 72 | 1.10 | -0.02em | Títulos de seção |
| `--text-display-md` | 56 | 1.15 | -0.015em | Subtítulos grandes |
| `--text-h1` | 48 | 1.20 | -0.01em | Slide titles |
| `--text-h2` | 36 | 1.25 | -0.005em | Sub-seções |
| `--text-h3` | 28 | 1.30 | 0 | Títulos de cards |
| `--text-body-lg` | 24 | 1.45 | 0 | Body destacado |
| `--text-body` | 20 | 1.50 | 0 | Body padrão |
| `--text-body-sm` | 16 | 1.55 | 0 | Caption, metadata |
| `--text-mono-xl` | 32 | 1.15 | 0 | KPI hero number |
| `--text-mono-lg` | 24 | 1.20 | 0 | KPI regular |
| `--text-mono-md` | 18 | 1.30 | 0 | Números pequenos, código |

### **Font Weights**

| Token | Weight | Uso |
|---|---|---|
| `--weight-regular` | 400 | Body, parágrafos |
| `--weight-medium` | 500 | Subtítulos, labels |
| `--weight-semibold` | 600 | H3, ênfase em body |
| `--weight-bold` | 700 | H1, H2, números |
| `--weight-black` | 900 | Hero, display |

### **Special: Iridescent Display (signature)**

```css
.display-iridescent {
  background: linear-gradient(135deg, #6366F1 0%, #00D4FF 50%, #6366F1 100%);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
  animation: iridescent-shift 6s ease-in-out infinite;
}

@keyframes iridescent-shift {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

**Uso:** slide 8 (Proposta Única), slide 5 (Bacia de Campos — emocional), slide 10 (CTA).

---

## 🌌 Shadows & Effects

### **Shadows (dark-mode optimized)**

| Token | Value | Uso |
|---|---|---|
| `--shadow-sm` | `0 4px 12px rgba(0,0,0,0.45)` | Cards pequenos |
| `--shadow-md` | `0 8px 24px rgba(0,0,0,0.5)` | Cards médios |
| `--shadow-lg` | `0 16px 40px rgba(0,0,0,0.6)` | Cards elevados |
| `--shadow-xl` | `0 24px 56px rgba(0,0,0,0.7)` | Modais, overlays |

### **Glow Effects (signature iridescent)**

| Token | Value | Uso |
|---|---|---|
| `--glow-iridescent` | `0 0 24px rgba(99,102,241,0.4)` | Solução, defesa, zero-trust |
| `--glow-iridescent-strong` | `0 0 48px rgba(99,102,241,0.65)` | KPI hero, momentos chave |
| `--glow-cyan` | `0 0 24px rgba(0,212,255,0.5)` | AI, real-time |
| `--glow-cyan-strong` | `0 0 48px rgba(0,212,255,0.75)` | WOW slide, Time-Travel XR |
| `--glow-matrix` | `0 0 20px rgba(0,255,65,0.45)` | SOC, detecção (raros) |
| `--glow-danger` | `0 0 16px rgba(255,71,87,0.5)` | Alertas, "antes" |

### **Glassmorphism (foundational)**

```css
.glass {
  background: var(--bg-glass);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid var(--border-default);
  box-shadow: var(--shadow-md);
}

.glass-iridescent {
  background: var(--bg-glass);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid transparent;
  background-image: 
    linear-gradient(var(--bg-glass-strong), var(--bg-glass-strong)),
    linear-gradient(135deg, rgba(99,102,241,0.5), rgba(0,212,255,0.5));
  background-origin: border-box;
  background-clip: padding-box, border-box;
  box-shadow: var(--glow-iridescent);
}
```

---

## 🌈 Gradients (signature)

### **Brand Gradients**

| Token | Value | Uso |
|---|---|---|
| `--gradient-iridescent` | `linear-gradient(135deg, #6366F1 0%, #00D4FF 100%)` | **Signature** — solução, defesa, zero-trust |
| `--gradient-iridescent-diagonal` | `linear-gradient(45deg, #6366F1 0%, #00D4FF 50%, #6366F1 100%)` | Títulos, dividers |
| `--gradient-cyan-glow` | `linear-gradient(135deg, #00D4FF 0%, #6366F1 100%)` | AI, real-time |
| `--gradient-matrix` | `linear-gradient(135deg, #00FF41 0%, #00D4FF 100%)` | SOC, detecção (raros) |
| `--gradient-danger` | `linear-gradient(135deg, #FF4757 0%, #FFD33D 100%)` | "Antes", ataque, risco |
| `--gradient-success` | `linear-gradient(135deg, #00FF41 0%, #6366F1 100%)` | "Depois", defesa, ROI |

### **Background Gradients (atmosphere)**

| Token | Value | Uso |
|---|---|---|
| `--bg-atmosphere` | `radial-gradient(ellipse at top, #131836 0%, #0A0E27 70%)` | Background atmosphere principal |
| `--bg-spotlight` | `radial-gradient(circle at 50% 30%, #1F2447 0%, #0A0E27 60%)` | Slide de HOOK, hero |
| `--bg-iridescent-glow` | `radial-gradient(circle at 30% 70%, rgba(99,102,241,0.18) 0%, transparent 50%), radial-gradient(circle at 70% 30%, rgba(0,212,255,0.18) 0%, transparent 50%)` | Slides de solução, WOW |
| `--bg-noise` | `url("data:image/svg+xml;base64,<noise-pattern>")` | Overlay grain SVG (textura sutil) |

---

## 📏 Spacing & Grid

### **Base Unit**
`8px` — todos os tokens de spacing são múltiplos de 8

### **Spacing Scale**

| Token | Value | Uso |
|---|---|---|
| `--space-1` | 4px | Pequenos ajustes |
| `--space-2` | 8px | Entre linhas |
| `--space-3` | 12px | Entre parágrafos |
| `--space-4` | 16px | Entre blocos pequenos |
| `--space-5` | 24px | Padding padrão de cards |
| `--space-6` | 32px | Entre seções |
| `--space-8` | 48px | Entre blocos grandes |
| `--space-10` | 64px | Margens externas |
| `--space-12` | 96px | Hero padding |
| `--space-16` | 128px | Slide canvas padding |

### **Layout Grid (1920x1080)**

| Token | Value |
|---|---|
| Slide width | 1920px |
| Slide height | 1080px |
| Safe area horizontal | 96px (1728px útil) |
| Safe area vertical | 64px (952px útil) |
| Columns | 12 colunas |
| Gutter | 24px |

---

## 🎬 Animation & Motion

### **Easings (fluid, futurist)**

| Token | Value | Uso |
|---|---|---|
| `--ease-out-fluid` | `cubic-bezier(0.16, 1, 0.3, 1)` | Elementos entrando (slide-up, fade) |
| `--ease-in-out-fluid` | `cubic-bezier(0.65, 0, 0.35, 1)` | Transições balanceadas |
| `--ease-spring` | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Bounce sutil para ênfase |
| `--ease-glide` | `cubic-bezier(0.22, 1, 0.36, 1)` | Slides, transições longas |

### **Durations (controlados, não rápidos)**

| Token | Value | Uso |
|---|---|---|
| `--duration-fast` | 180ms | Hover, micro-interações |
| `--duration-base` | 360ms | Transições padrão |
| `--duration-slow` | 600ms | Entradas de elementos |
| `--duration-slower` | 900ms | Loading states, fades maiores |
| `--duration-counter` | 1400ms | Animated number counters |
| `--duration-iridescent` | 6s | Iridescent shift loop |

### **Common Animations**

```css
@keyframes fade-in {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slide-up {
  from { opacity: 0; transform: translateY(32px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes iridescent-pulse {
  0%, 100% { box-shadow: 0 0 24px rgba(99,102,241,0.3); }
  50% { box-shadow: 0 0 40px rgba(99,102,241,0.6); }
}

@keyframes cyan-pulse {
  0%, 100% { box-shadow: 0 0 24px rgba(0,212,255,0.3); }
  50% { box-shadow: 0 0 40px rgba(0,212,255,0.65); }
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-6px); }
}
```

---

## 🧩 Component Styles (Building Blocks)

### **Card — Glass Iridescent (signature)**

```css
.card-iridescent {
  background: var(--bg-glass-strong);
  backdrop-filter: blur(24px) saturate(180%);
  -webkit-backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid transparent;
  background-image: 
    linear-gradient(var(--bg-glass-strong), var(--bg-glass-strong)),
    linear-gradient(135deg, rgba(99,102,241,0.5), rgba(0,212,255,0.5));
  background-origin: border-box;
  background-clip: padding-box, border-box;
  border-radius: 20px;
  padding: var(--space-6);
  box-shadow: var(--shadow-lg), var(--glow-iridescent);
}

.card-iridescent:hover {
  box-shadow: var(--shadow-xl), var(--glow-iridescent-strong);
  transform: translateY(-2px);
  transition: transform var(--duration-fast) var(--ease-out-fluid);
}
```

### **Card — Subtle (apoio)**

```css
.card-subtle {
  background: var(--bg-secondary);
  border: 1px solid var(--border-subtle);
  border-radius: 16px;
  padding: var(--space-5);
  box-shadow: var(--shadow-md);
}
```

### **Button — Primary Iridescent**

```css
.btn-iridescent {
  background: var(--gradient-iridescent);
  color: var(--text-primary);
  font-weight: var(--weight-bold);
  padding: var(--space-3) var(--space-8);
  border-radius: 12px;
  border: none;
  box-shadow: var(--glow-iridescent);
  transition: all var(--duration-fast) var(--ease-out-fluid);
}

.btn-iridescent:hover {
  transform: translateY(-2px);
  box-shadow: var(--glow-iridescent-strong);
}
```

### **KPI Hero (número grande com glow)**

```css
.kpi-hero {
  font-family: var(--font-mono);
  font-size: var(--text-mono-xl);
  font-weight: var(--weight-black);
  background: var(--gradient-iridescent);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  color: transparent;
  letter-spacing: -0.02em;
  line-height: 1;
}

.kpi-hero--cyan {
  background: linear-gradient(135deg, #00D4FF 0%, #6366F1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.kpi-hero--matrix {
  color: var(--brand-matrix);
  text-shadow: var(--glow-matrix);
}

.kpi-label {
  font-family: var(--font-body);
  font-size: var(--text-body-sm);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  margin-top: var(--space-2);
}
```

---

## 🎨 Slide-Specific Tokens (accent por slide)

| Slide | Tema | Accent Color | Special Effect |
|---|---|---|---|
| 1 — HOOK | Impacto | `--gradient-iridescent` | `--bg-spotlight` |
| 2 — HOOK caso | Emoção | `--gradient-iridescent` | `--bg-spotlight` |
| 3 — Paradoxo | Tensão | `--text-secondary` | minimal |
| 4 — 5 Vetores | Análise | `--brand-cyan` | `--bg-iridescent-glow` |
| 5 — ★ Bacia de Campos | Caso emocional | `--gradient-danger` | glow-danger |
| 6 — Vulnerabilidades | Catalogação | `--warning` | minimal |
| 7 — Mitigação | Resposta | `--gradient-success` | glow-success |
| **8 — ⭐ PROPOSTA ÚNICA** | **Diferenciação** | **`--gradient-iridescent`** | **`--bg-iridescent-glow` + iridescent display title** |
| 9 — Solução 4 camadas | Arquitetura | `--gradient-iridescent` | `--bg-iridescent-glow` |
| 10 — Arquitetura COTS | Técnico | `--gradient-iridescent` | `--bg-iridescent-glow` |
| 11 — Antifrágil + ZT | Postura | `--gradient-iridescent-diagonal` | iridescent display | → fundido no slide 8 |
| **12 — Viability** | **Viabilidade** | **`--gradient-success`** | **glow-success iridescente** | → fundido no slide 10 |
| 13 — CTA | Convite | `--gradient-iridescent` | iridescent display final | → fundido no slide 10 |

> **Reconciliação 21/10/2026:** o deck canônico tem **10 slides (OPÇÃO A)**. As linhas 11–13 acima são a numeração da OPÇÃO B (13 slides, 5 min — descartada por violar o limite de 3 min do SENAI). Mapeamento: **11→8, 12→10, 13→10**.

---

## 🖼️ Background Atmosphere (signature look)

Aplicar em TODOS os slides:

```css
.slide-canvas {
  background: var(--bg-atmosphere);
  position: relative;
  overflow: hidden;
}

/* Noise overlay sutil */
.slide-canvas::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: var(--bg-noise);
  opacity: 0.04;
  pointer-events: none;
  mix-blend-mode: overlay;
}

/* Iridescent glow blob (canto superior direito) */
.slide-canvas::after {
  content: '';
  position: absolute;
  top: -20%;
  right: -10%;
  width: 60%;
  height: 60%;
  background: radial-gradient(circle, rgba(99,102,241,0.12) 0%, transparent 60%);
  pointer-events: none;
  animation: float 8s ease-in-out infinite;
}
```

Para slides de **solução + WOW + CTA** (4, 5, 7, 8, 9, 11, 12, 13):

```css
.slide-canvas--iridescent {
  background: var(--bg-primary);
}

.slide-canvas--iridescent::after {
  background: 
    radial-gradient(circle at 30% 70%, rgba(99,102,241,0.18) 0%, transparent 50%),
    radial-gradient(circle at 70% 30%, rgba(0,212,255,0.18) 0%, transparent 50%);
  top: 0;
  right: 0;
  width: 100%;
  height: 100%;
}
```

---

## 📋 Iconografia

Use **Lucide Icons** (open source, perfect stroke weight):

| Categoria | Ícones | Stroke |
|---|---|---|
| **Brand** | 🛡️ Shield, Hexagon | 1.5px |
| **Ataque** | ⚠️ AlertTriangle, Skull, Bomb | 1.5px |
| **Defesa** | 🛡️ ShieldCheck, Lock, KeyRound | 1.5px |
| **Camadas** | Layers, Box, Server | 1.5px |
| **Fluxo** | ArrowRight, RefreshCw, GitBranch | 1.5px |
| **AI/ML** | Bot, Brain, Sparkles | 1.5px |
| **XR/AR/VR** | Glasses, Eye, ScanEye | 1.5px |
| **Cloud** | Cloud, Globe, Wifi | 1.5px |
| **Time/ROI** | Clock, TrendingUp, DollarSign | 1.5px |

**Cor padrão:** `--text-secondary` com `--glow-iridescent` em hover

**Special:** para ícones críticos (slide 8, slide 5, slide 10), usar `--gradient-iridescent` como fill via SVG mask.

---

## 📐 Implementation Notes

### **Para Figma**

1. **Frame base:** 13 frames 1920x1080
2. **Background:** rectangle fill `--bg-primary` + noise overlay (4% opacity)
3. **Components:** criar `Card Iridescent`, `Card Subtle`, `Button Iridescent`, `KPI Hero`, `Slide Title` (iridescent), `Icon Circle`
4. **Variables:** importar todos os tokens acima como Variables no Figma
5. **Text Styles:** importar Type Scale + Style Weight como Text Styles
6. **Effect Styles:** Glow + Shadow como Effect Styles

### **Para Framer**

1. **Variants por slide** com override de accent
2. **Code Components** com motion (Framer Motion)
3. **Override per slide:** accent color + bg-gradient

### **Para CSS / Tailwind (rápido)**

```json
// tailwind.config.json
{
  "theme": {
    "colors": {
      "bg": { 
        "primary": "#0A0E27",
        "secondary": "#131836",
        "tertiary": "#1F2447"
      },
      "brand": { 
        "iridescent": "#6366F1",
        "cyan": "#00D4FF",
        "matrix": "#00FF41"
      },
      "text": { 
        "primary": "#F8F9FB",
        "secondary": "#C7CAD9",
        "tertiary": "#7B7F95"
      },
      "danger": "#FF4757",
      "warning": "#FFD33D"
    },
    "fontFamily": {
      "display": ["Inter", "system-ui"],
      "body": ["Inter", "system-ui"],
      "mono": ["'JetBrains Mono'", "monospace"]
    },
    "extend": {
      "backgroundImage": {
        "iridescent": "linear-gradient(135deg, #6366F1 0%, #00D4FF 100%)",
        "atmosphere": "radial-gradient(ellipse at top, #131836 0%, #0A0E27 70%)"
      },
      "boxShadow": {
        "glow-iridescent": "0 0 24px rgba(99,102,241,0.4)",
        "glow-iridescent-strong": "0 0 48px rgba(99,102,241,0.65)"
      }
    }
  }
}
```

---

## 🧩 Aplicação no deck (`index.html`) — 21/10/2026

O deck renderizado (`pitch_deck/index.html`, 10 slides) já foi re-tematizado com este guide. Tokens efetivamente gravados no `:root`:

| Papel | Token | Valor no deck |
|---|---|---|
| Fundo principal | `--bg-primary` | `#0A0E27` |
| Superfícies | `--bg-secondary` / `--bg-tertiary` | `#131836` / `#1F2447` |
| Vidro | `--bg-glass` | `rgba(31,36,71,0.6)` |
| Brand dominante | `--brand` | `#6366F1` |
| Apoio | `--brand-cyan` | `#00D4FF` |
| Highlight raro | `--brand-matrix` | `#00FF41` — restrito à camada SOC/deteção (slide 9) |
| Borda | `--border` | `rgba(99,102,241,0.18)` |

**Desvios deliberados (acessibilidade — WCAG AA)**

| Token | Guide | Deck | Motivo |
|---|---|---|---|
| `--text-tertiary` | `#7B7F95` | `#8A8EA6` | `#7B7F95` = 3.79:1 sobre `#1F2447` (abaixo de AA para texto pequeno); `#8A8EA6` = 4.64:1 |
| `--brand-text` (novo, só no deck) | — | `#8B8CF9` | `#6366F1` = 4.25:1 — insuficiente para rótulos ≤22px. Usado só em texto pequeno; títulos, KPIs e bordas mantêm o indigo dominante |

Contraste medido no render: texto principal 18.04:1 · secundário 11.65:1 · terciário 4.81:1 · `--brand-text` 6.53:1 · `--brand-cyan` 10.73:1 · `--brand-matrix` 13.92:1.

---

## 🎨 Reference Inspirations

| Style | Inspiração |
|---|---|
| Apple Vision Pro marketing | Spatial depth, glassmorphism |
| Meta spatial UI | Indigo + cyan glow, floating elements |
| Stripe homepage 2024 | Clean typography, generous whitespace |
| Linear app dark mode | Premium minimal, mono numbers |
| Apple Keynote spring 2026 | Iridescent gradients, noise overlay |
| Vercel marketing | Bold display, mono KPIs |

---

## ⏭️ Próxima parte

**PARTE 10 — Widgets, Charts, Diagramas & Slide Templates** (13 templates específicos por slide usando este style guide)

---

## ❓ Perguntas para você

1. **Palette iridescent** (`#6366F1` + `#00D4FF`) com **matrix-green** (`#00FF41`) como highlights raros — confirma?
2. **Fontes Inter + JetBrains Mono** (Google Fonts gratuitas) ou prefere Söhne (premium)?
3. **Noise overlay sutil** (4% opacity) ou prefere sem?
4. **Glassmorphism pesado** em todos os cards prioritários ou só nos slides chave (5, 8, 12)?
5. **Iridescent display title** (gradient animado nos textos principais) — em quais slides?