# PARTE 9 — Design Tokens (Refined v0.2)

> **Deliverable:** Sistema visual consolidado do pitch AxeGuard — pronto para Figma / Framer / CSS / Tailwind.
> **Versão:** v0.2 — Outubro 2026
> **Mudanças vs v0.1:** aplicado `pitch-deck-visuals` skill — reduzido para **3 cores** (bg + brand + text), `Inter` único para display, kill `--brand-trust` como acento, body 28-32px, slides left-align com 1 visual + número.

---

## 🎯 Princípios (regras duras)

### Regra 1-6-6 (conteúdo)
- 1 ideia por slide
- ≤6 palavras por bullet
- ≤6 bullets por slide

### Regra 3 cores (paleta dura)
| Categoria | Token | HEX | Função |
|---|---|---|---|
| Background | `--bg-primary` | `#0D1117` | Único background (deep navy-charcoal) |
| Brand | `--brand-matrix` | `#00FF41` | Único acento (matrix-green) |
| Text | `--text-primary` | `#FFFFFF` | Texto principal |
| **Special** | `--danger` | `#F85149` | **APENAS** ataques/ameaças (não categoria de marca) |

**Removidos:** `--brand-trust` (#0052FF), `--warning`, `--info`, `--success` como categoria, gradientes em texto.

### Regra tipografia
- Display (titles): `Inter` 700-900
- Body: `Inter` 400-600
- Mono (KPIs): `JetBrains Mono` 700-900
- **NÃO usar Space Grotesk** — Inter cobre 100% do uso

### Regra layout
- Margins: **96px laterais / 64px topo-base**
- **Left-align** (não center) — exceto slides HOOK
- 1 visual dominante por slide
- **Slide number** sempre presente (canto inferior direito)
- 1920x1080 base, escala fluida por viewport

---

## 🎨 Color Palette (refined — 3 cores + 1 danger)

### Background (único)
```css
--bg-primary:    #0D1117;   /* deep navy-charcoal, base de tudo */
--bg-secondary:  #161B22;   /* surfaces elevadas (cards) */
--bg-tertiary:   #21262D;   /* hover, top layers */
--bg-glass:      rgba(22,27,34,0.6);  /* glassmorphism */
--bg-overlay:    rgba(13,17,23,0.85); /* modais */
```

### Brand (único accent — matrix-green)
```css
--brand-matrix:        #00FF41;            /* accent principal */
--brand-matrix-glow:   rgba(0,255,65,0.4); /* glow sutil */
--brand-matrix-soft:   rgba(0,255,65,0.15);/* backgrounds, fills */
```

### Text (único)
```css
--text-primary:   #FFFFFF;  /* títulos, números grandes */
--text-secondary: #C9D1D9;  /* body, parágrafos */
--text-tertiary:  #8B949E;  /* caption, labels */
--text-disabled:  #484F58;  /* disabled */
--text-inverse:   #0D1117;  /* texto em botões brand */
```

### Danger (special — APENAS para ataques/ameaças)
```css
--danger:        #F85149;             /* ataques, "antes" */
--danger-bg:     rgba(248,81,73,0.15);/* bg de alertas */
--danger-glow:   rgba(248,81,73,0.4); /* glow em ataques */
```

### Borders
```css
--border-default:  #30363D;            /* bordas sutis */
--border-strong:   #484F58;            /* ênfase */
--border-matrix:   rgba(0,255,65,0.6); /* accent border */
```

---

## 📐 Typography (Inter + JetBrains Mono)

### Font Families
```css
--font-display: 'Inter', system-ui, sans-serif;   /* TUDO em Inter (display, titles, body) */
--font-body:    'Inter', system-ui, sans-serif;   /* alias retro-compat */
--font-mono:    'JetBrains Mono', monospace;      /* SOMENTE para KPIs numéricos */
```

### Type Scale (alinhado à skill)

| Token | Size | Line | Letter | Uso |
|---|---|---|---|---|
| `--text-display-xl` | **144px** | 1.0 | -0.03em | KPI hero ("197 DIAS") |
| `--text-display-lg` | **72px** | 1.05 | -0.02em | Slide title principal |
| `--text-display-md` | **56px** | 1.10 | -0.015em | Subtitle, título secundário |
| `--text-h1` | 48px | 1.15 | -0.01em | Section title |
| `--text-h2` | 36px | 1.20 | -0.005em | Sub-section |
| `--text-h3` | **32px** | 1.30 | 0 | **Body destacado** (skill: 28-32) |
| `--text-body-lg` | **28px** | 1.40 | 0 | **Body principal** (skill: 28-32) |
| `--text-body` | 20px | 1.50 | 0 | Body secundário |
| `--text-caption` | 16px | 1.50 | 0.02em | Caption, metadata (skill: 16-20) |
| `--text-mono-xl` | 96px | 1.0 | -0.02em | KPI hero (regular) |
| `--text-mono-lg` | 48px | 1.10 | -0.01em | KPI regular |
| `--text-mono-md` | 24px | 1.20 | 0 | Números em cards |

### Font Weights
```css
--weight-regular:  400;
--weight-medium:   500;
--weight-semibold: 600;
--weight-bold:     700;
--weight-black:    900;
```

**Regra de uso:**
- Display titles: 700-900
- Body: 400-600
- Mono KPIs: 700-900

---

## 🌌 Shadows & Effects (moderados)

### Shadows
```css
--shadow-sm: 0 2px 4px  rgba(0,0,0,0.3);
--shadow-md: 0 8px 16px rgba(0,0,0,0.4);
--shadow-lg: 0 16px 32px rgba(0,0,0,0.5);
```

### Glow (matrix-green com moderação)
```css
--glow-matrix:        0 0 16px rgba(0,255,65,0.4);  /* SUTIL — default */
--glow-matrix-strong: 0 0 32px rgba(0,255,65,0.6);  /* APENAS em KPI hero */
--glow-danger:        0 0 16px rgba(248,81,73,0.4); /* APENAS em ataques */
```

**Regra:** glow em no máximo 1-2 elementos por slide (não pintar tudo de neon).

---

## 🌈 Gradients (apenas em backgrounds, NUNCA em texto)

```css
/* Background gradients */
--bg-atmosphere: radial-gradient(ellipse at top, #161B22 0%, #0D1117 70%);
--bg-spotlight:  radial-gradient(circle at 50% 30%, #1C2128 0%, #0D1117 60%);
--bg-grid:       linear-gradient(rgba(0,255,65,0.04) 1px, transparent 1px),
                 linear-gradient(90deg, rgba(0,255,65,0.04) 1px, transparent 1px);

/* Divider / accent line (1px) */
--divider-matrix: linear-gradient(90deg, #00FF41 0%, transparent 100%);
```

**PROIBIDO:** gradiente em texto (`background-clip: text` + `text-fill-color: transparent`) — cor sólida sempre.

---

## 📏 Spacing & Grid

### Base unit: 8px
```css
--space-1:  4px;
--space-2:  8px;
--space-3:  12px;
--space-4:  16px;
--space-5:  24px;
--space-6:  32px;
--space-8:  48px;
--space-10: 64px;
--space-12: 96px;  /* margins laterais */
--space-16: 128px;
```

### Layout Grid (1920x1080)
| Prop | Value |
|---|---|
| Slide | 1920×1080 |
| Margin lateral | **96px** |
| Margin top/bottom | **64px** |
| Colunas | 12 |
| Gutter | 24px |

---

## 🎬 Motion

### Easings
```css
--ease-out:    cubic-bezier(0.16, 1, 0.3, 1);
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);
```

### Durations
```css
--duration-fast:   150ms;
--duration-base:   300ms;
--duration-slow:   500ms;
--duration-counter: 1200ms;  /* número animado */
```

### Keyframes
```css
@keyframes fade-in    { from {opacity:0} to {opacity:1} }
@keyframes slide-up   { from {opacity:0; transform:translateY(24px)} to {opacity:1; transform:translateY(0)} }
@keyframes glow-pulse { 0%,100% {box-shadow:0 0 16px rgba(0,255,65,0.3)} 50% {box-shadow:0 0 32px rgba(0,255,65,0.6)} }
```

---

## 🧩 Component Library (refined)

### Card Glass
```css
.card-glass {
  background: var(--bg-glass);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border-default);
  border-radius: 16px;
  padding: var(--space-5);
}
.card-glass--accent { border-color: var(--brand-matrix); }
/* APENAS 2 variantes: default + accent (NÃO trust/matrix/iridescent) */
```

### KPI Hero (número grande)
```css
.kpi-hero {
  font-family: var(--font-mono);
  font-size: var(--text-mono-xl);   /* 96px */
  font-weight: 900;
  color: var(--brand-matrix);
  text-shadow: var(--glow-matrix);
  letter-spacing: -0.02em;
  line-height: 1;
}
.kpi-hero--xl { font-size: var(--text-display-xl); }  /* 144px */
.kpi-hero--danger { color: var(--danger); }            /* APENAS em ataques */

.kpi-label {
  font-family: var(--font-body);
  font-size: var(--text-caption);
  color: var(--text-tertiary);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: var(--space-2);
}
```

### Button (1 primary + 1 ghost)
```css
.btn-primary {
  background: var(--brand-matrix);
  color: var(--bg-primary);
  font-weight: 700;
  padding: 16px 32px;
  border: none;
  border-radius: 8px;
  font-family: var(--font-body);
  cursor: pointer;
}
.btn-primary:hover { box-shadow: var(--glow-matrix); }

.btn-ghost {
  background: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-strong);
  padding: 16px 32px;
  border-radius: 8px;
  font-family: var(--font-body);
  font-weight: 600;
}
```

### Tag (uppercase, letter-spacing 0.08em)
```css
.tag {
  display: inline-block;
  padding: 4px 12px;
  border: 1px solid var(--border-default);
  border-radius: 4px;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
  font-family: var(--font-body);
}
.tag--accent { border-color: var(--brand-matrix); color: var(--brand-matrix); }
```

### Chart (max 2 cores, label direto)
```css
.chart-line {
  fill: none;
  stroke: var(--brand-matrix);
  stroke-width: 3;
}
.chart-line--secondary { stroke: var(--text-tertiary); opacity: 0.5; }
.chart-label {
  font-family: var(--font-mono);
  font-size: 16px;
  fill: var(--text-secondary);
}
/* SEM legend separada — label inline na linha/barra */
```

### Slide Number (sempre presente)
```css
.slide-number {
  position: absolute;
  bottom: 32px;
  right: 96px;
  font-family: var(--font-mono);
  font-size: 16px;
  color: var(--text-tertiary);
  letter-spacing: 0.08em;
}
/* Formato: "03 / 13" */
```

---

## 🖼️ Background Atmosphere (todos os slides)

```css
.slide-canvas {
  background: var(--bg-atmosphere);
  position: relative;
  overflow: hidden;
  padding: 64px 96px;
  text-align: left;  /* LEFT-ALIGN (não center) */
}
.slide-canvas::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: var(--bg-grid);
  background-size: 50px 50px;
  pointer-events: none;
  opacity: 0.5;
}
```

---

## 📋 Implementation Notes

### Mudanças obrigatórias no `index.html` (deck atual)

1. **Remover `--brand-trust` e seus derivados** (`--brand-trust-glow`, `--gradient-defense`, etc.)
2. **Remover semantic colors** (`--warning`, `--info`, `--success`, `--warning-bg`, `--trust-bg`)
3. **Mudar `--font-display`** de `'Space Grotesk', Inter` para `'Inter', system-ui`
4. **Remover import do Google Fonts** para `Space+Grotesk` (deixar só `Inter` + `JetBrains+Mono`)
5. **Body text:** 20px → **28-32px** (ajustar `.body`, `.lede`, `.quote` etc.)
6. **KPI hero size:** 32px → **96-144px** (era `--text-mono-xl: 32px`, agora 96px)
7. **Adicionar slide number** em todos os 13 slides (canto inferior direito)
8. **Remover gradients em texto** (procurar `-webkit-background-clip: text` — apagar)
9. **Glow apenas em KPI hero** (não pintar cards de glow — usar `border-matrix` se precisar destaque)
10. **Margins:** padronizar 96px lateral (atualmente algumas áreas usam 64px)

### Tailwind config (se usar)
```json
{
  "theme": {
    "colors": {
      "bg":      { "primary": "#0D1117", "secondary": "#161B22", "tertiary": "#21262D" },
      "brand":   { "matrix": "#00FF41" },
      "text":    { "primary": "#FFFFFF", "secondary": "#C9D1D9", "tertiary": "#8B949E" },
      "danger":  "#F85149"
    },
    "fontFamily": {
      "display": ["Inter", "system-ui", "sans-serif"],
      "body":    ["Inter", "system-ui", "sans-serif"],
      "mono":    ["'JetBrains Mono'", "monospace"]
    }
  }
}
```

---

## ✅ Checklist de conformidade (vs v0.1)

| Regra | v0.1 | v0.2 |
|---|---|---|
| Max 3 cores | ❌ 5+ (matrix, trust, danger, warning, info) | ✅ 3 + danger |
| Display font | ❌ Space Grotesk | ✅ Inter 700-900 |
| Body size | ⚠️ 20px | ✅ 28-32px |
| KPI hero size | ❌ 32px | ✅ 96-144px |
| Margins | ✅ 96px | ✅ 96px (mantido) |
| Left-align | ⚠️ misto | ✅ left-align obrigatório |
| Slide number | ❌ ausente | ✅ obrigatório |
| 1 visual/slide | ⚠️ misto | ✅ obrigatório |
| Chart max 2 cores | ❌ sem regra | ✅ regra explícita |
| Gradients em texto | ❌ usado em KPI | ✅ proibido |
| Glow em texto/cards | ⚠️ excessivo | ✅ apenas KPI hero |
| Tags letter-spacing | n/a | ✅ 0.08em |

---

## ⏭️ Próxima parte

`SUBAGENT 2 — Rebuild do HTML deck` aplicando esses tokens refinados (10 mudanças obrigatórias listadas acima).

---

## ❓ Decisões pendentes

1. **Manter `--bg-secondary` (#161B22) como token?** Ou fundir tudo em 1 background? (Recomendo manter — surfaces elevadas precisam de contraste)
2. **Danger em glow** — manter `0 0 16px rgba(248,81,73,0.4)` ou reduzir para 0.25?
3. **Slide number** — formato `03/13` (padded) ou `3/13` (raw)?
4. **Body line-height** — 1.40 (skill padrão) ou 1.50 (mais respiratório)?
5. **Espaço entre seções de uma mesma slide** — `--space-8` (48px) ou `--space-10` (64px)?
