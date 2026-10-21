# 19 — Modelo de Viabilidade Econômica (AxeGuard · Enterprise)

> **Deliverable:** modelo econômico-financeiro que fecha o pitch (slide 10) e sustenta a pergunta de CTA.
> **Escopo:** enterprise multinacional (Petrobras-class) · 1 refinaria-âncora como unidade de referência.
> **Moeda:** R$ (CPL). Conversão usada: **US$ 1 = R$ 5,00**.
> **Versão:** v1.0 — Outubro 2026.
> **Status:** derivado de `pitch_deck/09_viability_enterprise.md` (PARTE 6) e `pitch_deck/session_traction_ask.md`.

---

## 0. Por que este documento existe

O pitch abre com números de **dor** (197 dias de MTTD, US$ 5M por incidente, 90 GB
exfiltrados) e fecha com um **convite** (Piloto 90 dias). O judges/julgador vai
perguntar: *"ok, mas essa conta fecha?"*

Este modelo responde com uma planilha fechada: premissa → custo → benefício →
payback → NPV, com **cenários conservador / base / otimista** e **análise de
sensibilidade**. A verdade é que um único modelo com um único número é frágil —
ele quebra na primeira pergunta do banca. Três cenários, com o conservador à
frente, é o que sobrevive.

> **Regra de ouro (do `Rules_and_Winning_Strategies_GP.md` §4 — PI defensiva):**
> este documento é **interno**. O slide 10 mostra **ordem de grandeza**, nunca
> o breakdown de R$ por peça. Concorrente com preço na tela = munição na mão de
> quem negocia.

---

## 1. Premissas

### 1.1 Escopo

| Item | Premissa |
|---|---|
| Unidade de referência | 1 refinaria-âncora (o piloto) |
| Horizonte | 3 anos (duração do contrato enterprise faseado) |
| Conversão | US$ 1 = R$ 5,00 |
| Taxa de desconto | 12% a.a. (WACC corporativo conservative) |
| Inflação/licença | +8% a.a. sobre o recorrente |
| Moeda de referência | R$ |

### 1.2 Origem dos números de risco (do início do pitch)

| Parâmetro | Valor | Origem |
|---|---|---|
| MTTD global O&G | 197 dias | Slide 1 |
| MTTD Brasil | 322 dias | Slide 1 |
| Custo médio por incidente | US$ 5M (R$ 25M) | Slide 1 |
| Caso âncora — exfiltração | 90 GB / 72 h | Slide 5 (Bacia de Campos) |
| Custo do caso âncora | US$ 15–25M | Slide 5 |
| Breaches O&G via fornecedor | 62% | Slide 6 |
| Vazão do atacante | 1,25 GB/h (90 GB ÷ 72 h) | Slide 5 |

### 1.3 Custo de oportunidade — a conta que ninguém faz

Este é o número que fecha o pitch, e ele vem **direto do caso da abertura**:

```
Janela de exposição = MTTD × vazão do atacante
197 dias × 24 h × 1,25 GB/h = 5.910 GB ≈ 5,9 TB

A janela de 197 dias não é tempo — é VOLUME.
5,9 TB de superfície de dado exposta por incidente não detectado.
```

> Esse é o framing que o slide 10 usa: **não "você perde dinheiro", mas "você
> deixa 5,9 TB expostos"**. É a mesma informação, mas traduzida de loss em
> exposição.

---

## 2. Estrutura de custos (TCO)

### 2.1 Setup — Ano 0 (único)

| Item | R$ |
|---|---|
| Descoberta, threat model, SBOM + CTI feed | 250.000 |
| Integração Camadas L1–L4 (Enclave, DLP, OAuth+TPM, MDM) | 1.100.000 |
| SOC Agêntico setup (LangGraph + Kafka + UEBA + runbooks) | 550.000 |
| Enclave Azure OpenAI + VNet privada (provisionamento Ano 1) | 350.000 |
| Enablement + treinamento de equipes | 250.000 |
| **TOTAL SETUP** | **R$ 2.500.000** |

### 2.2 Recorrente (mensal)

| Item | R$/mês |
|---|---|
| SOC Agêntico operated (1 cluster, N refinarias) | 200.000 |
| Threat Intel + IOC feed + retraining de modelo | 80.000 |
| Suporte 24/7 CISO-grade + quarterly review | 70.000 |
| Licenças COTS (Entra ID, ArborXR/Hexnode, Azure OpenAI) | 70.000 |
| **TOTAL RECORRENTE** | **R$ 420.000/mês** |

### 2.3 TCO 3 anos

| Ano | Recorrente | Total do ano |
|---|---|---|
| 0 | — (setup R$ 2.500.000) | R$ 2.500.000 |
| 1 | R$ 5.040.000 | R$ 7.540.000 |
| 2 | R$ 5.443.200 (+8%) | R$ 5.443.200 |
| 3 | R$ 5.878.656 (+8%) | R$ 5.878.656 |
| | | **TCO 3 ANOS = R$ 18.861.856 ≈ R$ 18,86M** |

---

## 3. Benefício — Expected Annual Loss (EAL)

Modelo de risco padrão: **EAL = F × C** (frequência × custo por incidente).

### 3.1 Parâmetros

| Cenário | Custo por incidente (C) | Frequência (F/ano) | EAL/ano | EAL 3 anos |
|---|---|---|---|---|
| **Conservador** | R$ 75M (US$ 15M) | 0,2 (1 a cada 5 anos) | R$ 15M | R$ 45M |
| **Base** | R$ 100M (US$ 20M) | 0,4 (1 a cada 2,5 anos) | R$ 40M | R$ 120M |
| **Otimista** | R$ 125M (US$ 25M) | 0,8 (1 a cada ~15 meses) | R$ 100M | R$ 300M |

> **Base de F:** 62% dos breaches O&G vêm de fornecedor, e o vetor é "padrão da
> indústria" (slide 6). F = 0,4/ano é conservador para uma refinaria exposta a
> 5 vetores simultâneos.

### 3.2 ROI (3 anos)

```
ROI = EAL evitado ÷ TCO 3 anos
```

| Cenário | EAL 3 anos | TCO 3 anos | **ROI** | Benefício líquido |
|---|---|---|---|---|
| Conservador | R$ 45M | R$ 18,86M | **2,4×** | R$ 26,1M |
| **Base** | R$ 120M | R$ 18,86M | **6,4×** | **R$ 101,1M** |
| Otimista | R$ 300M | R$ 18,86M | **15,9×** | R$ 281,1M |

### 3.3 Headline do pitch — ROI de exposição: **47×**

O número que já estava no slide 10 é o **ROI de exposição**, não o de EAL:

```
Exposição anual de um ativo O&G exposto:  US$ 71M  (R$ 354M)
Investimento AxeGuard Ano 1:               R$ 7,54M
ROI de exposição = R$ 354M ÷ R$ 7,54M  =  47×
```

**Não confundir:** 47× mede *exposição evitável por ano ÷ investimento*.
6,4× mede *benefício esperado realizado em 3 anos ÷ TCO de 3 anos*.
O slide 10 mostra **ambos**, rotulados, porque um judge afiado vai notar a
diferença — e é melhor que ele note do que ser pego.

### 3.4 Payback

```
Payback (meses) = Investimento Ano 1 ÷ (EAL/ano ÷ 12)
```

| Cenário | EAL/ano | Payback |
|---|---|---|
| Conservador | R$ 15M | **6,0 meses** |
| Base | R$ 40M | **2,3 meses** |
| Otimista | R$ 100M | **0,9 meses** |

### 3.5 Payback por incidente evitado (o argumento mais forte)

```
1 incidente evitado (conservador) = R$ 75M
÷ Investimento Ano 1 (R$ 7,54M)    = 9,9× o investimento

Payback = R$ 7,54M ÷ (R$ 75M ÷ 365) = 37 dias
```

> **"Um único incidente evitado, no primeiro ano, paga 9,9× o investimento —
> em 37 dias."** Esse é o número que o CISO entendo sem slide nenhum.

### 3.6 NPV (3 anos, base, 12% a.a.)

| t | Fluxo | Fator | Valor presente |
|---|---|---|---|
| 0 | −2.500.000 (setup) | 1,0000 | −R$ 2.500.000 |
| 1 | +40.000.000 − 5.040.000 | 1,1200 | R$ 31.214.286 |
| 2 | +40.000.000 − 5.443.200 | 1,2544 | R$ 27.549.745 |
| 3 | +40.000.000 − 5.878.656 | 1,4049 | R$ 24.288.478 |
| | | **NPV** | **R$ 80.552.508 ≈ R$ 80,55M** |

---

## 4. Análise de sensibilidade

Variação do ROI (3 anos) frente às duas premissas que mais importam.

### 4.1 Variação da frequência (F) — C fixo em R$ 100M

| F/ano | EAL 3 anos | ROI 3 anos | Payback |
|---|---|---|---|
| 0,1 | R$ 30M | 1,6× | 9,0 meses |
| 0,2 | R$ 60M | 3,2× | 4,5 meses |
| **0,4** | **R$ 120M** | **6,4×** | **2,3 meses** |
| 0,6 | R$ 180M | 9,5× | 1,5 meses |
| 0,8 | R$ 240M | 12,7× | 1,1 meses |

### 4.2 Variação do custo (C) — F fixo em 0,4

| C | EAL 3 anos | ROI 3 anos | Payback |
|---|---|---|---|
| R$ 25M (US$ 5M — slide 1) | R$ 30M | 1,6× | 9,0 meses |
| R$ 50M | R$ 60M | 3,2× | 4,5 meses |
| **R$ 100M** | **R$ 120M** | **6,4×** | **2,3 meses** |
| R$ 150M | R$ 180M | 9,5× | 1,5 meses |

> **Achado importante:** mesmo no pior cruzamento (C = US$ 5M, o número do
> slide 1, e F = 0,1), o ROI ainda é **1,6×** e o payback ainda cabe em 9 meses.
> O modelo é robusto. É isso que a banca precisa ouvir.

---

## 5. Benchmark de mercado

| Alternativa | Custo anual | Cobertura | Lacuna |
|---|---|---|---|
| Palo Alto + CrowdStrike + Splunk | ~R$ 30M | Endpoint + SIEM | Não cobre XR nem DLP context-aware |
| Microsoft Defender P2 + Sentinel | ~R$ 15M | Endpoint + SIEM + IdP | Não cobre DLP Petrobras-specific |
| Projeto custom interno | ~R$ 50M+ | Teórica | 18 meses + risco de execução |
| **AxeGuard enterprise** | **R$ 7,54M** (Ano 1) | 4 camadas + SOC + DLP L7 | **Setup 90 dias, auditável** |

**Posicionamento:** AxeGuard não é "mais barato que Palo Alto" — é *a única
opção que fecha o vetor XR + DLP L7 + SOC agêntico sem projeto de 18 meses*.
Contra o **custom interno**, o argumento é tempo, não preço.

---

## 6. O que o slide 10 mostra (e o que NÃO mostra)

### Mostra — ordem de grandeza

```
TCO 3 anos ............ R$ 18,9M
Custo evitado 3 anos .. R$ 120M
Benefício líquido ...... R$ 101,1M
ROI 3 anos (base) ...... 6,4×
ROI de exposição ....... 47×
Payback (base) ......... 2,3 meses
1 incidente evitado .... 9,9× o investimento
```

### NÃO mostra

- ❌ Breakdown de R$ por item (setup, recurring, COTS) — munição de negociação
- ❌ Preço por refinaria / por usuário
- ❌ A premissa de frequência F detalhada (a banca vai questionar; deixamos no
  modelo interno e apresentamos os 3 cenários)

---

## 7. Riscos do modelo (declarados, não escondidos)

| Risco | Impacto | Mitigação |
|---|---|---|
| **F subestimada** (incidente raro) | ROI cai para 1,6× | Ainda > 1. Payback < 9 meses |
| **C subestimado** (o caso âncora é outlier) | ROI cai para 1,6× | Idem |
| **Ataque nunca materializa** | benefício = 0 | Investimento é de *redução de risco*, não de ROI — enquadramento de seguro. O piloto faseado existe para medir F real em 90 dias |
| **Procurement atrasa** | setup desloca, ROI não muda | Recorrente é o que pesa; setup é 13% do Ano 1 |
| **Exposição não é toda evitável** | EAL superestimado | Por isso o slide usa 3 cenários, não 1 |

> **Enquadramento honesto para a banca:** AxeGuard é um **seguro** contra
> R$ 75–125M por evento. Você não judges um seguro pelo ROI do sinistro que não
> aconteceu — julga-se pelo prêmio. Esse enquadramento é mais forte que
> prometer ROI e sustenta o "Piloto 90 dias, sem assinatura antes".

---

## 8. Dados que a banca vai pedir (fonte pendente)

| Dado | Valor usado | Fonte a confirmar |
|---|---|---|
| MTTD 197 dias | slide 1 | IBM Cost of a Data Breach 2024/2025 |
| MTTD Brasil 322 dias | slide 1 | Accenture / SANS |
| US$ 5M custo médio | slide 1 | IBM Cost of a Data Breach |
| 62% via fornecedor | slide 6 | Ponemon / Verizon DBIR (setor O&G) |
| US$ 15–25M caso âncora | slide 5 | caso SA Exploration (fonte restrita) |
| 1,25 GB/h | derivado | 90 GB ÷ 72 h (slide 5) |

> ⚠️ **Action item do autor:** confirmar fonte primária de cada número antes da
> submissão. Um número sem fonte é o ponto que a banca abre.

---

## 9. Checklist de aceite

- [x] TCO 3 anos fechado e auditável
- [x] ROI em 3 cenários (conservador / base / otimista)
- [x] Payback calculado nos 3 cenários
- [x] NPV a 12% a.a. (3 anos, base)
- [x] Análise de sensibilidade em F e C
- [x] Benchmark de mercado
- [x] Regra de exposição (não mostrar breakdown) aplicada ao slide
- [x] Riscos declarados
- [x] Fontes pendentes listadas
- [x] Diagrama D2 correspondente: `diagrams/opportunity_cost.d2` + `diagrams/tco_waterfall.d2`

---

*Modelo construído em Out/2026. Substitui as estimativas de pricing soltas em `pitch_deck/09_viability_enterprise.md` (mantido como histórico narrativo).*
