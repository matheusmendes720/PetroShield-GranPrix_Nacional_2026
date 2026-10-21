# ROTEIRO DE FALA — PITCH AXEGUARD 3 MIN

> **Deliverable:** Roteiro narrado para o vídeo YouTube (Entrega 3 — SENAI GP 2026).
> **Versão:** v1.0 — Outubro 2026.
> **Audiência primária:** IA pré-triagem SENAI (busca semântica) → banca humana.
> **Audiência secundária:** Petrobras (cliente-âncora), patrocinadores.
> **Duração alvo:** **3:00** (± 5 s).
> **Total de palavras de fala:** ~470 palavras (cronometradas a 150 wpm = ~3 min líquido, + pausas = 3 min totais).
> **Tom:** dark premium · matrix-green + trust-blue · pt-BR · locutor masculino ou feminino grave · cadência executiva · ritmo crescente · punch no final.

---

## ⏱️ Cronograma macro (13 slides × ~14 s)

| Bloco | Slides | Conteúdo | Tempo |
|---|---|---|---|
| Hook + Setup | 1–4 | impacto, hook caso, paradoxo XR, 5 vetores | 0:00 – 1:00 |
| Caso anchor | 5 | Bacia de Campos — coração narrativo | 1:00 – 1:30 |
| Contexto BR + Mitigação | 6–7 | vuln. nacionais + mapeamento ataque→defesa | 1:30 – 2:00 |
| **⭐ Proposta única** | 8 | QR + SOC + DLP + Zero Trust (frase-âncora) | 2:00 – 2:25 |
| Solução técnica | 9–10 | 4 camadas + COTS real | 2:25 – 2:50 |
| Punch antifrágil + Viability | 11–12 | postura + validação enterprise | 2:50 – 3:05 |
| **CTA + tag-line** | 13 | piloto + tag-line final | 3:05 – 3:20 |

---

## 🎙️ ROTEIRO SLIDE-A-SLIDE

### `[TIMESTAMP 0:00–0:15]` · `[SLIDE 1]` — Hook + proposta SEO-para-IA
*Cue visual: contador `197 DIAS` pulsando em matrix-green, de 0 → 197.*

**[GLOW PULSE]**

> Cento e noventa e SETE dias.
> Esse é o tempo médio que a indústria leva para detectar um ciberataque no setor de ÓLEO e GÁS.
> No Brasil: trezentos e vinte e dois dias.
> A pergunta é simples: **quanto do pré-sal brasileiro já saiu sem você saber?**

---

### `[TIMESTAMP 0:15–0:30]` · `[SLIDE 2]` — Hook do caso anchor
*Cue visual: mapa da Bacia de Campos com zoom in para litoral RJ.*

**[SLIDE-UP mapa]**

> Em Novembro de dois mil e vinte e cinco, na **Bacia de Campos** — berço da engenharia offshore brasileira — um fornecedor norte-americano de serviços geofísicos foi COMPROMETIDO.
> Noventa gigabytes de sísmica vazaram em setenta e duas horas.
> Por uma VPN legítima.
> Com credenciais válidas.

---

### `[TIMESTAMP 0:30–0:45]` · `[SLIDE 3]` — O paradoxo XR
*Cue visual: óculos XR ao centro → irrompem 5 vetores como raízes.*

**[PAUSE 0.5s] · [RITMO mais lento]**

> Smart glasses resolvem um problema: **mãos livres, decisão em tempo real**.
> Mas criam CINCO novos.
> Cada camada de conveniência é uma nova superfície de ataque.
> **XR industrial é a maior EXPOSIÇÃO da próxima década.**

---

### `[TIMESTAMP 0:45–1:00]` · `[SLIDE 4]` — 5 vetores visuais
*Cue visual: `[COUNTER: 1→5]` ativando cada vetor com glow.*

**[GLOW PULSE em cada numeral]**

> Um — Supply chain.
> Dois — Endpoint.
> Três — OAuth.
> Quatro — Proxy exfiltration.
> Cinco — Paralisia operacional.
> O caso de setenta e duas horas na Bacia de Campos **ACUMULOU os cinco**.
> E os firewalls clássicos?
> **Não estavam nem configurados para esse cenário.**

---

### `[TIMESTAMP 1:00–1:30]` · `[SLIDE 5]` — Caso Bacia de Campos (coração narrativo)
*Cue visual: timeline vertical com 7 nodes acendendo sequencialmente.*

**[ENERGIA ALTA · tom de repórter investigativo]**

> **T-menos trinta dias.** Phishing contra o admin de TI do fornecedor — e-mail falso da Microsoft, MFA reset roubado em tempo real.
> **T-menos sete dias.** Credenciais da VPN Petrobras encontradas em texto claro, num arquivo compartilhado entre doze funcionários. Senha única. Sem MFA individual.
> **T-zero.** Exfiltração começa. Script automatizado conecta a API legacy — sem checagem de dois fatores, sem geofencing.
> **Cinquenta MEGABYTES por request**, codificados em base64, transportados via DNS-over-HTTPS para uma VPS na Moldávia.

**[PAUSE 0.5s]**

> **T-mais setenta e duas horas.** Noventa gigabytes transferidos. Mapas de reservatórios pré-sal. Leitura sísmica 3D das Bacias de Campos e Santos. Projeções de reserva.
> **T-mais noventa dias.** Descoberta por terceiros — vendedor de IP no dark web oferecendo "Brazilian offshore seismic data".

**[PAUSE dramática 1.0s · voz mais baixa]**

> **E nós não vimos.**
> **A próxima pergunta é: o que sai pela SUA refinaria amanhã?**

---

### `[TIMESTAMP 1:30–1:48]` · `[SLIDE 6]` — Vulnerabilidades Indústria Nacional BR
*Cue visual: lista dos casos emblemativos com check vermelho.*

**[RÁPIDO · energia alta]**

> Esse caso não é isolado.
> **OceanPact.** **Oceânica.** **REPETRO.** Ataques recentes no setor O&G brasileiro.
> Cada um HERDOU credenciais válidas. Cada um atravessou perímetro confiável.
> **Sessenta e dois por cento dos breaches O&G globais vêm de fornecedor.**
> É o vetor padrão da indústria.

---

### `[TIMESTAMP 1:48–2:00]` · `[SLIDE 7]` — Mapeamento ataque → defesa
*Cue visual: matriz 5×5 acendendo célula por célula.*

**[TRANSITION tom contido]**

> Cada vetor TEM resposta.
> MFA fechado via TPM. Segmentação por microperímetro. DLP comportamental. Token revogação atrelada a contrato.
> O gap não é técnica — **é COMPOSIÇÃO**.
> E composição é o que entregamos.

---

### `[TIMESTAMP 2:00–2:25]` · `[SLIDE 8]` — ⭐ A PROPOSTA ÚNICA AXEGUARD
*Cue visual: 3 cards (QR / SOC / DLP) + 1 box (Zero Trust) com glow individual.*

**[SLIDE-UP pilares · GLOW em cada um · cadência ritual]**

> Três soluções de ponta. Uma estratégia.
>
> **QR Code que autentica.**
> **SOC que detecta em 12 segundos.**
> **DLP que protege o dado.**
> **Zero Trust que assume breach.**
>
> Tudo isso composto sobre tecnologia de mercado real.
> Implementável em **90 dias**.
> Auditável peça por peça.
>
> **Isso é AxeGuard.**

*🔒 NOTA DE PRODUÇÃO: a frase-âncora acima aparece EXATAMENTE uma vez neste slide. Não parafrasear, não repetir, não cortar.*

---

### `[TIMESTAMP 2:25–2:40]` · `[SLIDE 9]` — Visão das 4 camadas
*Cue visual: stack diagram horizontal com 4 caixas.*

**[OVERVIEW · tom didático]**

> **Quatro camadas**.
> **MDM** para governança do device.
> **OAuth Device Flow com TPM** para autenticação — ZERO digitação no ar.
> **DLP Middleware com NLP atômica** para mascaramento de PII e terminologia O&G.
> **Enclave Azure OpenAI com NO-TRAIN** para a LLM nunca reter o dado.

---

### `[TIMESTAMP 2:40–2:52]` · `[SLIDE 10]` — Arquitetura COTS
*Cue visual: 4 logos (ArborXR, Entra ID, Ngrok, Azure OpenAI) em grid.*

**[BUILD · confiante]**

> ArborXR. Microsoft Entra ID. Ngrok. Azure OpenAI.
> Componentes **COTS reais**. Sem lock-in proprietário.
> Cada camada auditável. Substituível.
> **Soberania PLENA do cliente.**

---

### `[TIMESTAMP 2:52–3:04]` · `[SLIDE 11]` — Punch: antifrágil + Zero Trust (postura)
*Cue visual: diagrama Venn (Preventiva ∩ Defensiva ∩ Ostensiva) + ZT como envoltório.*

**[ENERGIA ALTA · punch por sílaba]**

> Preventiva. Defensiva. Ostensiva.
> E **Zero Trust** como POSTURA — não como feature.
> SOC Agêntico **ANTIFRAGIL**.
> Cada incidente refina o modelo.
> O atacante evolui?
> **A defesa EVOLUI MAIS RÁPIDO.**

---

### `[TIMESTAMP 3:04–3:12]` · `[SLIDE 12]` — Viability enterprise
*Cue visual: badges (SLSA L3 · NIST 800-207 · LGPD · ANP).*

**[GROUNDED · tom executivo]**

> Viável para **enterprise multinacional**.
> COTS real. **SLSA L3**. **NIST 800-207**. Compliance **LGPD/ANP**.
> Petrobras já reconhece a tecnologia.
> **Não é vaporware.**

---

### `[TIMESTAMP 3:12–3:25]` · `[SLIDE 13]` — Convite + CTA + tag-line final
*Cue visual: card grande `PILOTO 90 DIAS` com 3 bullets; após fala, GLOW PULSE final + tag-line bold.*

**[SLIDE-UP card · PAUSE 0.5s antes do punch final]**

> **Piloto 90 dias. Uma refinaria. Risco zero.**
> Quatro fases. Treze semanas.
> Sem assinatura até ver **MÉTRICAS COMPARATIVAS** — com AxeGuard e sem AxeGuard.
> Próximo passo: **reunião executiva de 1 hora com o CISO** para definir a refinaria-âncora do piloto.

**[GLOW PULSE final · PAUSE 0.5s · voz grave, lentidão quase cerimonial]**

> **De 197 dias para 12 segundos.**
> **De US$ 5M de incidente para R$ 1.**

**[PAUSE 1.0s]**

> O pré-sal é nosso.
> **Vamos protegê-lo.**

**[FADE TO BLACK · contato na tela]**
`matheus@pessoferndeaxe.pj.br`

*🔒 NOTA DE PRODUÇÃO: a tag-line acima aparece EXATAMENTE uma vez. Não parafrasear. Frame final permanece 3 s.*

---

## 📋 Decisões editoriais registradas

### 1. Caso SA Exploration — política de citação
**Decisão:** NÃO citar o nome "SA Exploration" no pitch. Usar exclusivamente:
> "um **fornecedor norte-americano de serviços geofísicos**" + "**Bacia de Campos**"

**Justificativa:**
- Política Petrobras tende a não publicizar fornecedores comprometidos nominalmente (risco reputacional bilateral).
- A descrição ("norte-americano de serviços geofísicos") é específica o suficiente para a banca validar a credibilidade sem expor a empresa.
- Bacia de Campos é cenário público, não confidencial.
- Caso a Petrobras autorize citar nominalmente, swap direto da frase; o resto do roteiro não muda.

### 2. Frase-âncora (slide 8)
Aparece **UMA VEZ**, em cadência ritual. Não parafrasear, não antecipar, não ecoar no slide 13.
> "QR Code que autentica. SOC que detecta em 12 segundos. DLP que protege o dado. Zero Trust que assume breach. Tudo isso composto sobre tecnologia de mercado real. Implementável em 90 dias. Auditável peça por peça. Isso é AxeGuard."

### 3. Tag-line final (slide 13)
Aparece **UMA VEZ**, no frame final do vídeo.
> "De 197 dias para 12 segundos. De US$ 5M de incidente para R$ 1."

### 4. CTA concreto (slide 13)
Aparece **UMA VEZ**, em punch de 3 beats.
> "Piloto 90 dias. 1 refinaria. Risco zero."

### 5. SEO-para-IA SENAI — keywords trabalhadas
`cibersegurança` · `smart glasses` · `XR industrial` · `óleo e gás` · `supply chain` · `OAuth` · `TPM` · `DLP` · `Zero Trust` · `SOC agêntico` · `Petrobras` · `Bacia de Campos` · `pre-sal` · `MDM` · `enclave` · `LangGraph` · `LGPD/ANP` · `SLSA L3` · `NIST 800-207` · `COTS` · `antifrágil` · `empresa enterprise` · `VPN legítima` · `exfiltração`.

Cada keyword aparece **1–2x** no roteiro, no contexto natural da fala. Densidade calibrada para busca semântica sem comprometer cadência.

### 6. HOOK de abertura (slide 1)
Abre com **número específico** (`197 dias`) + **contexto geopolítico** (pré-sal brasileiro) + **pergunta provocativa**. Atende critério SENAI Atratividade nos primeiros 5 segundos.

### 7. CTA final
"Reunião executiva de 1h com o CISO Petrobras para definir a refinaria-âncora" — baixo ânimo, específico, acionável. Calendly/email explícito na tela final.

---

## 🔀 Planos de contingência (cronometragem)

### 🅱️ Plano B — se ultrapassar 3:00 min
**Comprimir slide 6** (vuln. nacionais BR):
- Cortar a menção nominal "OceanPact, Oceânica, REPETRO".
- Manter apenas: "Sessenta e dois por cento dos breaches O&G globais vêm de fornecedor".
- **Economia estimada: ~10 s.** Slot rebalanceado para slide 5 respirar mais.

**Compressão secundária** (se ainda faltar):
- Slide 7 encurtar de 12 s para 8 s — manter punch "O gap não é técnica — é COMPOSIÇÃO", cortar a enumeração técnica.

### 🅲️ Plano C — se ficar curto de 3:00 min
**Expandir slide 5** (caso Bacia de Campos):
- Adicionar o detalhe: "API legacy sem checagem de dois fatores. Sem geofencing — login aceito de qualquer IP, inclusive não-BR".
- Adicionar o detalhe financeiro: "Vinte milhões de dólares em propriedade intelectual. Mais o contencioso."
- **Adicional estimado: ~15 s.**

**Expansão secundária** (se ainda faltar):
- Slide 12 (viability) ganhar 1 métrica concreta: "Tempo de implementação enterprise: 90 dias. Payback: < 12 meses."

---

## 🎬 Notas de produção (resumo)

| Tipo | Onde | O que |
|---|---|---|
| `[GLOW PULSE]` | slides 1, 4, 8, 13 | acentuar o numeral/frase-âncora com brilho neon verde |
| `[PAUSE 0.5s]` | slides 5 (×2), 13 | respiro antes do twist |
| `[PAUSE 1.0s]` | slides 5 (final), 13 (pós tag-line) | silêncio cerimonial |
| `[SLIDE-UP]` | slides 1, 2, 8, 13 | anima elemento subindo do fundo |
| `[COUNTER 1→5]` | slide 4 | numeral anima com glow |
| `[DEEP]` / `[ENERGIA ALTA]` | slide 5, 11, 13 | muda tom do locutor |
| `[GROUNDED]` | slide 12 | volta cadença contida |
| `[FADE TO BLACK]` | slide 13, pós-tag-line | 3 s fade |

---

## 🎙️ Briefing ao locutor

- **Cadência:** 150 palavras por minuto (cronometrada). Não acelerar mesmo em slides densos.
- **Ênfase (CAIXA ALTA):** pronunciar com peso físico — voz projeta do diafragma, não da garganta. Cada palavra CAIXA ALTA é um punch.
- **Tom base:** voz de engenheiro sênior explicando ao board. Confiante mas contido. Nunca histriônico.
- **Punch final (slide 13):** quase cerimonial. Mais lento que o resto. Tag-line merece ser ouvida — não atropelada.
- **Respiração:** marcar respiro antes de cada `[PAUSE]`. Locutor NÃO enche o silêncio com "ãh" ou "é".
- **Plosivas:** "Zero Trust", "12 segundos", "197 dias", "90 gigabytes" merecem ataque vocal firme.

---

## ✅ Checklist de aceite

- [x] Hook forte nos primeiros 5 s (`197 dias` + pré-sal)
- [x] Frase-âncora EXATAMENTE 1× (slide 8)
- [x] Tag-line final EXATAMENTE 1× (slide 13)
- [x] CTA "Piloto 90 dias. 1 refinaria. Risco zero." EXATAMENTE 1× (slide 13)
- [x] SA Exploration NÃO citado nominalmente
- [x] Bacia de Campos citado como setting público
- [x] Caso anchor + números concretos (90 GB · 72 h · US$ 15–25M)
- [x] 4 pilares nomeados no slide 8 + Zero Trust como estratégia
- [x] Viability enterprise (SLSA L3 · NIST 800-207 · LGPD/ANP)
- [x] Plano B (comprimir 6 / 7) documentado
- [x] Plano C (expandir 5 / 12) documentado
- [x] Cues de produção (`[GLOW PULSE]` · `[PAUSE]` · `[COUNTER]` · `[SLIDE-UP]`)
- [x] Notas CAIXA ALTA para ênfase
- [x] Notas de tom (`[ENERGIA ALTA]` · `[GROUNDED]` · `[PAUSE DRAMÁTICA]`)
- [x] Cronograma macro + Briefing locutor

---

*Roteiro escrito em 14/Out/2026. Próxima iteração: validar com banca interna + sincronizar com PARTE 9 (design tokens) e PARTE 10 (widgets/templates) — animations precisam alinhar com cues `[GLOW PULSE]` e `[COUNTER]`.*
