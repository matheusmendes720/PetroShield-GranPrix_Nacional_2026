# INDEX — Pitch Deck AxeGuard / PetroShield

> Navegação mestre de todos os arquivos do scaffold (`pitch_deck/`).
> Deliverable: Pitch de Elevador 3 min — YouTube — SENAI GP 2026 (Entrega 3).
> Audiência primária: IA pré-triagem SENAI + banca humana + Petrobras anchor.

---

## Quick Links

- [Master Scaffold](./00_master_scaffold.md) — narrativa canônica + arco de slides
- [Proposta Única (QR + SOC + DLP + ZT)](./11_unique_proposal_pillars.md) — PARTE 8 (slide 8)
- [Style Guide Canônico (Option D Holographic)](./13_style_guide_option_D_holographic.md) — **USAR ESTE** para tokens visuais
- [Slide Templates Visuais (v2)](./14_widgets_charts_templates.md) — **USAR ESTE** para widgets/charts (base Option D)
- [Deck renderizado (11 slides)](./index.html) — **ARTEFATO VISUAL** do pitch (contador "SLIDE 0X / 11")
- [Roteiro de fala slide-a-slide](./14_spoken_narration.md) — narração do vídeo 3 min
- [Caso Bacia de Campos (âncora)](./06_caso_bacia_de_campos.md) — coração emocional
- [Modelo de viabilidade econômica](../19_Viabilidade_Economica_Modelo.md) — **TCO, ROI, NPV, payback, cenários** (slide 10)
- [Viability Enterprise](./09_viability_enterprise.md) — ROI de exposição 47× (slide 11)
- [Convite / CTA](./10_invitation_cta.md) — slide 11
- [Diagramas D2](./diagrams/) — `l7_proxy_zt.svg` (slide 9) · `opportunity_cost.svg` (slide 10) · `dlp_pipeline` · `tco_waterfall` · `vetores_defesas` · `attack_timeline`

---

## Estrutura por Slide do Pitch (11 slides — OPÇÃO A2)

| Slide | Arquivo(s) | Conteúdo | Duração alvo |
|---|---|---|---|
| 1 | `00_master_scaffold.md` §Mapa | ABERTURA / HOOK — 197 dias de MTTD | 10s |
| 2 | `06_caso_bacia_de_campos.md` | HOOK CASO — Bacia de Campos (teaser) | 12s |
| 3 | `02_attack_diagnosis_global.md` | PROBLEMA — paradoxo XR | 12s |
| 4 | `02_attack_diagnosis_global.md` | PROBLEMA — 5 superfícies de ataque | 12s |
| 5 | `06_caso_bacia_de_campos.md` | ★ CASO BACIA DE CAMPOS (técnico) ★ | 45s |
| 6 | `05_petrobras_national_vulnerabilities.md` | VULNERABILIDADES — indústria BR + Petrobras | 18s |
| 7 | `04_mitigation_per_pattern.md` | MITIGAÇÃO — cada vetor tem resposta | 16s |
| 8 | `11_unique_proposal_pillars.md` + `08_strategy_antifragil.md` | ⭐ PROPOSTA ÚNICA — QR + SOC + DLP + Zero Trust (antifrágil/ZT folded in) | 25s |
| 9 | `07_solution_4_layers.md` + `10_Arquitetura_SOC_Agêntico.md` | CORE — proxy de Camada 7: DLP + segmentação OT/IT + Zero Trust + SOC Agêntico (`diagrams/l7_proxy_zt.svg`) | 16s |
| 10 | `../19_Viabilidade_Economica_Modelo.md` | VIABILIDADE — custo de oportunidade + TCO 3 anos + ROI 6,4× + NPV + payback 2,3 meses (`diagrams/opportunity_cost.svg`) | 16s |
| 11 | `09_viability_enterprise.md` + `10_invitation_cta.md` + `session_traction_ask.md` | CONVITE — CTA "Piloto 90 dias" + ROI de exposição 47× inline (merge dos antigos 12+13) | 20s |

> **Revisão 3 (Out/2026):** o slide 9 antigo ("4 camadas + COTS") virou o slide 9 **CORE** (diagrama D2 do proxy L7) e a viabilidade virou o slide 10 **próprio** (TCO/ROI/NPV/payback + custo de oportunidade). O CTA é o slide 11. Total mantido em **202s = 3:22** — orçamento rebalanceado, nenhum bloco acima de 45s.
>
> **Reconciliação do ROI:** **6,4×** (slide 10) = benefício esperado realizado ÷ TCO de 3 anos. **47×** (slide 11) = ROI de exposição, R$ 354M ÷ R$ 7,5M. São métricas diferentes, cada uma rotulada no slide. O modelo completo e a sensibilidade estão em `../19_Viabilidade_Economica_Modelo.md`.
>
> **Numeração reconciliada (21/10/2026):** a numeração canônica é a do **OPÇÃO A2 (11 slides)** — a mesma do `00_master_scaffold.md` §Mapa de slides e a implementada em `index.html` (`data-slide="1..11"`). O mapeamento de 13 slides que existia nesta tabela correspondia à Opção B/C (5 min), que viola o limite de 3 min do SENAI e foi descartada.
> **Camadas transversais (não são slides):** `session_evidence_wow.md` (tese de cobertura + Time-Travel XR → slides 3, 4 e 7) e `session_traction_ask.md` (TAM + ROI → slide 11).
> **Numeração interna dos docs-fonte:** os documentos narrativos (`03_…`, `06_…`, `08_…`, `09_…`, `10_…`, `11_…`) continuam citando as posições da antiga OPÇÃO B (ex.: “slide 11 (Viability)”, “slide 12 (CTA)”). A tabela acima é a única fonte de verdade para o mapeamento até o deck de 11 slides. **Exceção pendente:** `14_spoken_narration.md` ainda tem cronograma de 13 slides (`[SLIDE 11]`–`[SLIDE 13]`) e precisará ser reconciliado com os 11 slides antes da exportação do vídeo 3 min.

---

## Estrutura por Parte do Scaffold

| Parte | Arquivo | Status | Slide |
|---|---|---|---|
| PARTE 1 | `00_master_scaffold.md` | ✅ Aprovado | Arco narrativo |
| PARTE 2A | `02_attack_diagnosis_global.md` | ✅ Aprovado | 3-4 |
| PARTE 2B | `03_attack_filter_petrobras_relevance.md` | ✅ Aprovado | 4 |
| PARTE 2C | `04_mitigation_per_pattern.md` | ✅ Aprovado | 7 |
| PARTE 3A | `05_petrobras_national_vulnerabilities.md` | ✅ Aprovado | 6 |
| PARTE 3B | `06_caso_bacia_de_campos.md` | ✅ Aprovado | 5 |
| PARTE 4 | `07_solution_4_layers.md` | ✅ Aprovado | 9 |
| PARTE 5 | `08_strategy_antifragil.md` | ✅ Aprovado | folded no 8 |
| PARTE 6 | `09_viability_enterprise.md` | ✅ Aprovado | folded no 10 |
| PARTE 7 | `10_invitation_cta.md` | ✅ Aprovado | 10 |
| PARTE 8 | `11_unique_proposal_pillars.md` | ✅ Aprovado | 8 (novo) |
| PARTE 9 (stale) | `_archive/12_design_tokens.md` | 🗄️ Arquivado — substituído por Option D | n/a (tokens) |
| PARTE 9 (canônico) | `13_style_guide_option_D_holographic.md` | ✅ Canônico | n/a (style) |
| PARTE 10 (v1) | `_archive/13_widgets_charts_templates.md` | 🗄️ Arquivado — usa tokens antigos | n/a (templates) |
| PARTE 10 (v2) | `14_widgets_charts_templates.md` | ✅ Canônico — baseado em Option D | n/a (templates) |
| Narração | `14_spoken_narration.md` | ✅ Aprovado | roteiro 3 min |
| Session | `session_evidence_wow.md` | ✅ Aprovado | camadas 3, 4, 7 |
| Session | `session_traction_ask.md` | ✅ Aprovado | camada 10 |

---

## Cross-References (mapa de dependências)

```
00_master_scaffold
   ├─→ 02_attack_diagnosis_global (slides 3-4)
   │      ├─→ 03_attack_filter_petrobras_relevance (slide 4)
   │      │      └─→ 04_mitigation_per_pattern (slide 7)
   │      └─→ 04_mitigation_per_pattern (slide 7)
   │             └─→ 11_unique_proposal_pillars (slide 8)
   ├─→ 05_petrobras_national_vulnerabilities (slide 6)
   │      └─→ 06_caso_bacia_de_campos (slides 2 e 5)
   ├─→ 07_solution_4_layers (slide 9)
   │      └─→ 11_unique_proposal_pillars (slide 8)  [inserido entre 2C e 4]
   ├─→ 08_strategy_antifragil (folded no slide 8)
   ├─→ 09_viability_enterprise (folded no slide 10)
   │      └─→ 10_invitation_cta (slide 10)
   └─→ session_traction_ask (camada do slide 10)
          └─→ 10_invitation_cta (slide 10)

Visual stack (independente da narrativa):
   13_style_guide_option_D_holographic  ← CANÔNICO (substitui _archive/12_design_tokens)
        └─→ 14_widgets_charts_templates  ← CANÔNICO (substitui _archive/13_widgets)
                  └─→ 11_unique_proposal_pillars
                  └─→ 07_solution_4_layers
                  └─→ 08_strategy_antifragil

Evidence layer:
   session_evidence_wow ←→ 02, 04, 11 (prova cobertura 19→8→4→100%)
   session_traction_ask ←→ 09, 10, 11 (viability + CTA)
```

---

## Estatísticas

- **Total de arquivos canônicos:** 17 (15 numerados + narração + 2 sessions) + `index.html` (deck renderizado)
- **Total de palavras:** ~32.446
- **Total de bytes:** ~301 KB
- **Slides cobertos:** 10 (OPÇÃO A — mapeamento completo e reconciliado)
- **Partes do scaffold:** 1-10 (todas com deliverable)
- **Idade dos arquivos:** 14/10/2026 (sessão única, ~2h de construção) · reconciliação de numeração e arquivamento em 21/10/2026 · re-tematização Option D do deck em 21/10/2026
- **Arquivos stale:** 2 — arquivados em `_archive/` (ver abaixo)

---

## 🗄️ Arquivos Arquivados (histórico — não usar como referência canônica)

| Arquivo | Motivo | Substituído por |
|---|---|---|
| `_archive/12_design_tokens.md` | Tokens genéricos (dark mode + matrix-green + trust-blue) substituídos pela versão Option D (Holographic/Futurist) com gradientes violeta→ciano, glassmorphism, iridescent accents. O próprio arquivo declara: *"Substitui a base genérica de `12_design_tokens.md`"*. | `13_style_guide_option_D_holographic.md` |
| `_archive/13_widgets_charts_templates.md` | Versão 1 dos templates. Referencia `12_design_tokens.md` (stale) como base de tokens. Versão 2 foi reescrita para usar Option D. | `14_widgets_charts_templates.md` |

> **Movidos em 21/10/2026.** Nenhum arquivo do repositório (fora este INDEX) linkava para eles — grep repo-wide confirmou zero referências externas. Ambos ficaram lado a lado em `_archive/`, então o link relativo interno do v1 → `12_design_tokens.md` continua resolvendo dentro do arquivo.

---

## Próximas Ações

- [x] **Reconciliar numeração de slides** — OPÇÃO A (10 slides) é a numeração canônica; master scaffold e este INDEX agora apontam para os mesmos 10 slides, com o slide 8 (PARTE 8) absorvido. O deck renderizado (`index.html`) já usa `data-slide="1..10"`.
- [x] **Arquivar arquivos stale** (`12_design_tokens.md`, `13_widgets_charts_templates.md`) — movidos para `_archive/` em 21/10/2026; zero referências externas quebradas.
- [x] **Validar referências cruzadas** — `14_widgets_charts_templates.md` aponta para `13_style_guide_option_D_holographic.md` (canônico) nas duas ocorrências; nenhuma referência viva a `12_design_tokens.md`.
- [x] **Re-tematizar o deck com os tokens Option D** — aplicado em 21/10/2026 no `index.html` (bloco `:root` + regras de acento, 10 slides re-renderizados e conferidos). Ver seção “Re-tematização Option D” abaixo.
- [ ] **Exportar deck final** — a partir do deck re-tematizado, gerar o vídeo 3 min roteirizado conforme `14_spoken_narration.md` (mograph + IA generativa + 1 humano obrigatório).
- [ ] **QA de áudio/narração** — duração total alvo: 180s. Cada slide já tem duração sugerida; somar e validar.

---

## Re-tematização Option D (aplicada em 21/10/2026)

`index.html` (10 slides) foi re-tematizado com o guide canônico `13_style_guide_option_D_holographic.md`.

**Tokens aplicados (`:root`)**

| Papel | Token | Valor |
|---|---|---|
| Fundo principal | `--bg-primary` | `#0A0E27` |
| Superfície elevada | `--bg-secondary` / `--bg-tertiary` | `#131836` / `#1F2447` |
| Vidro | `--bg-glass` | `rgba(31,36,71,0.6)` |
| Brand dominante | `--brand` | `#6366F1` (indigo) |
| Brand de apoio | `--brand-cyan` | `#00D4FF` |
| Highlight raro | `--brand-matrix` | `#00FF41` — **só na camada SOC/deteção do slide 9** |
| Texto | `--text-primary` / `--text-secondary` / `--text-tertiary` | `#F8F9FB` / `#C7CAD9` / `#8A8EA6` |
| Borda | `--border` | `rgba(99,102,241,0.18)` (indigo sutil) |

**Desvios deliberados em relação ao guide** (acessibilidade)

| Token | Guide | Deck | Motivo |
|---|---|---|---|
| `--text-tertiary` | `#7B7F95` | `#8A8EA6` | `#7B7F95` dá apenas 3.79:1 sobre a superfície elevada `#1F2447`; `#8A8EA6` dá 4.64:1 (AA para texto pequeno) |
| — (novo) | — | `--brand-text: #8B8CF9` | Indigo `#6366F1` dá 4.25:1 — insuficiente para texto pequeno. Usado apenas em rótulos de 12–22px; títulos, números KPI e bordas seguem no indigo dominante |

**Contraste verificado (medido no render, não estimado):** texto principal 18.04:1 · texto secundário 11.65:1 · texto terciário 4.81:1 no fundo · `--brand-text` 6.53:1 · `--brand-cyan` 10.73:1 · `--brand-matrix` 13.92:1.

**QA visual:** slides 1, 3, 6, 9 e 10 renderizados em 1920×1080 (headless) e conferidos — sem texto cortado, sem sobreposição, verde neon restrito à camada SOC. O rodapé dos slides 3, 4, 6, 7 e 9 encostava na borda inferior do quadro; corrigido com `padding-bottom: var(--s-2)` (8px) nesses cinco slides, sem alterar conteúdo.

---

*INDEX gerado em 14/10/2026 — sessão única de construção do pitch deck.*
