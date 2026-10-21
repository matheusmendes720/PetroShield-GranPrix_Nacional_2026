# Pitch Deck AxeGuard / PetroShield — MASTER SCAFFOLD

> **Deliverable:** Pitch de Elevador — 3 min, YouTube, SENAI GP 2026 (Entrega 3)
> **Audiência primária:** IA pré-triagem do SENAI (busca semântica) → banca humana
> **Audiência secundária:** Petrobras (cliente-âncora), patrocinadores, judges GP
> **Versão:** v0.1 — Outubro 2026
> **Status:** Narrativa consolidada — OPÇÃO A (10 slides) · deck renderizado em `index.html` · stack visual canônico = Option D Holographic (`13_style_guide_option_D_holographic.md` + `14_widgets_charts_templates.md`)

---

## 📍 Diretrizes estratégicas (do `Rules_and_Winning_Strategies_GP.md`)

- **Critérios oficiais:** Aderência / Criatividade / Qualidade do Pitch / Atratividade
- **Desempate:** Criatividade > Atratividade → favor do Efeito WOW
- **Tática dominante:** Vender O Quê + Impactos, abstrair o Como (Caixa Preta). Sacrificar complexidade técnica purista.
- **Tom visual pré-definido:** Dark mode premium + `#00FF41` matrix-green + `#0052FF` trust-blue
- **Roteiro:** Hiper-produzido com mograph / IA generativa / 1 humano obrigatório
- **SCOPE:** **Enterprise multinacional (Petrobras-class)**. NÃO PME. ⚠️ Correção aplicada após nota do autor — qualquer menção a PME no pitch foi removida e reflete no pricing/sales cycle/ROI nas partes 6+
- **Audiência primária dupla:** SENAI judges (Aderência + Criatividade + Atratividade) + Petrobras anchor validation (soberania + compliance)

---

## 🎬 Arco narrativo canônico (de `PITCHdeck-petro.md`)

```
1. ABERTURA   →  2. PROBLEMA  →  3. CASO BACIA DE CAMPOS
   impacto + hook      paradoxo XR         ataque emblemático
                            ↓
6. CONVITE  ←  5. COMPARAÇÃO  ←  4. PUNCH (antifrágil)
   CTA teste             vs mercado     preventiva+defensiva+ostensiva
```

---

## 🗂️ Mapa de slides — **OPÇÃO A2: 11 slides / 3 min** (default SENAI Entrega 3)

⚠️ **Decisão orçamentária (Out/2026):** O budget inicial de 13 slides deu ~5 min. SENAI Entrega 3 tem **limite rígido de 3 min** (`Rules_and_Winning_Strategies_GP.md` §3). Aplicada compressão: merge dos slides 10+11+12 em variantes dentro dos slides 8+9+10.

⚠️ **Revisão 3 (Out/2026) — núcleo técnico e viabilidade.** O slide 9 antigo ("4 camadas + COTS") foi **substituído** pelo diagrama de núcleo técnico (proxy L7 + DLP + Zero Trust + SOC, `diagrams/l7_proxy_zt.svg`) e o slide de viabilidade deixou de ser um badge inline no CTA, virou **slide 10 próprio** (`diagrams/opportunity_cost.svg` + TCO/ROI/NPV/payback). O CTA passou a 11. O orçamento foi **rebalanceado para manter 202s** — nenhum bloco ultrapassa 45s.

| # | Sessão | Função estratégica | Conteúdo | Duração |
|---|---|---|---|---|
| 1 | Abertura | Hook impacto + tagline | 197 dias de MTTD + hook industrial (implementado em `index.html` s1) | **10s** |
| 2 | Abertura | Hook caso | Bacia de Campos teaser | **12s** |
| 3 | Problema | O paradoxo XR | XR ajuda vs vulnerabiliza | **12s** |
| 4 | Problema | 5 vetores visuais | Supply chain / Endpoint / OAuth / Proxy / Paralisia | **12s** |
| 5 | Caso | ★ Bacia de Campos (técnico) ★ | Timeline + tensão + 90GB/72h | **45s** |
| 6 | Vulnerabilidades | Indústria BR + Petrobras | 10 casos ativos + 62% padrão vendor VPN | **18s** |
| 7 | Mitigação | Mapeamento ataque→defesa | Padrão → Camada → COTS → Impacto | **16s** |
| **8** | **⭐ PROPOSTA ÚNICA** | **3 soluções + 1 estratégia** | **QR + SOC + DLP + Zero Trust (inclui antifrágil)** | **25s** |
| **9** | **CORE** | **Núcleo técnico** | **Proxy de Camada 7: DLP + segmentação OT/IT + Zero Trust + SOC Agêntico** (`diagrams/l7_proxy_zt.svg`) | **16s** |
| **10** | **VIABILIDADE** | **Custo de oportunidade + TCO** | **Setup/Recorrente/Custo evitado · TCO 3 anos · ROI 6,4× · NPV · payback 2,3 meses** (`diagrams/opportunity_cost.svg`) | **16s** |
| **11** | Convite | CTA + ROI de exposição inline | Piloto 90 dias + ROI exposição 47× (merge dos slides 12+13 antigos) | **20s** |
| **TOTAL** | | | | **~202s = 3:22** ✅ |

**Margem de manobra:** 22s (~3:30 com pausas naturais). Conforme regra do SENAI: ≤ 3 min. **Ajustar final se passar.**

> **Implementação:** `index.html` materializa exatamente este mapa — 11 seções `data-slide="1..11"`, com o contador "SLIDE 0X / 11" no topo de cada slide. A numeração deste scaffold é a canônica; qualquer referência a 13 slides nos demais arquivos é resíduo da Opção B/C.

> **Reconciliação do ROI (Out/2026):** o deck usa **dois** números de ROI, deliberadamente rotulados — **6,4×** = benefício esperado realizado ÷ TCO de 3 anos (slide 10, `19_Viabilidade_Economica_Modelo.md`) e **47×** = ROI de exposição, R$ 354M ÷ R$ 7,5M (slide 11, `09_viability_enterprise.md`). O slide 10 declara explicitamente que o 47× vem no slide seguinte. **Nunca misturar os dois em um único slide.**

---

## 📐 Slides eliminadas (conteúdo incorporado em outros)

| Antigo | Destino | O que foi absorvido |
|---|---|---|
| Antigo 9 (Solução 4 camadas) | Slide 9 (merge com 10) | Stack visual preservado |
| Antigo 10 (Arquitetura COTS) | Slide 9 (merge) | COTS products em row abaixo da stack |
| Antigo 11 (Antifrágil + ZT) | Slide 8 (merge em Proposta Única) | ZT como postura + 3 táticas como sub-bloco dentro do banner ZT |
| Antigo 12 (Viability) | Slide 10 (merge com CTA) | 1 box pequeno com KPIs antes do CTA |

---

## 🆚 Comparação Opção A vs Opção B vs Opção C

| Opção | Slides | Duração | Trade-off |
|---|---|---|---|
| **A** ← *escolhida* | 10 | 3:22 | Cabe no orçamento; perde 1 slide de Viability dedicado e 1 de COTS |
| B | 13 | 5:00 | Melhor narrativa; **viola limite SENAI** |
| C | 13 + renegociação | 5:00 | Mesmo risco da B; depende de aprovação da banca |

---

## 📁 Estrutura de arquivos desta pasta

```
06_Entregas/pitch_deck/
├── 00_master_scaffold.md                       ← este arquivo
├── 02_attack_diagnosis_global.md               ← PARTE 2A
├── 03_attack_filter_petrobras_relevance.md     ← PARTE 2B
├── 04_mitigation_per_pattern.md                 ← PARTE 2C
├── 05_petrobras_national_vulnerabilities.md    ← PARTE 3A
├── 06_caso_bacia_de_campos.md                  ← PARTE 3B
├── 07_solution_4_layers.md                     ← PARTE 4 (slide 9)
├── 08_strategy_antifragil.md                   ← PARTE 5 (fold no slide 8 — antifrágil/ZT)
├── 09_viability_enterprise.md                  ← PARTE 6 (fold no slide 10 — ROI inline)
├── 10_invitation_cta.md                        ← PARTE 7 (slide 10)
├── 11_unique_proposal_pillars.md               ← PARTE 8 (slide 8 — NOVO!)
├── 13_style_guide_option_D_holographic.md      ← PARTE 9 CANÔNICA (tokens Option D)
├── 14_widgets_charts_templates.md              ← PARTE 10 CANÔNICA (widgets/charts, base Option D)
├── 14_spoken_narration.md                      ← roteiro de fala slide-a-slide (3 min)
├── session_evidence_wow.md                     ← camada de evidência (slides 3, 4 e 7)
├── session_traction_ask.md                     ← camada de tração (slide 10)
├── index.html                                  ← deck renderizado — 10 slides (OPÇÃO A)
└── _archive/                                   ← 12_design_tokens.md + 13_widgets_charts_templates.md (v1, stale)
```

---

## ⚠️ Gaps em aberto

- [ ] **WOW criativo (qual escolher entre os 5 candidatos do draft anterior)**
- [ ] **Quem é o porta-voz** (afeta tom e linguagem)
- [ ] **Estatística de impacto financeiro ($$ bi perdidos)** — saiu do slide 1 (que usa 197 dias de MTTD) e vive na PARTE 6 (viability). Definir fonte e número (IBM? ENISA? ANP?) antes de exportar
- [ ] **Confirmação do caso Bacia de Campos** — temos autorização para citar nominalmente? É o "sponsor" mencionado em PITCHdeck-petro
- [ ] **Pricing real enterprise** — confirmar modelo enterprise Petrobras (proposta em construção na PARTE 6)
- [ ] **⚠️ CORREÇÃO APLICADA:** Scope = enterprise multinacional. Pricing/TAM/sales motion NÃO pode mencionar PME (corrigido nos arquivos subsequentes)
- [ ] **⚠️ Nota do autor:** há typos nas notas de estudo (`PITCHdeck-petro.md`, `AxeGuard_SOC_PetroShield.md`). O autor vai sinalizar mais correções conforme lembrar

---

*Próxima parte: PARTE 2B (Filtro Petrobras + relevância AxeGuard). Conteúdo abaixo em arquivo separado.*