# PARTE 6 — Viability (Técnica + Econômica) ENTERPRISE

> **Deliverable:** Conteúdo narrativo para slide 11 (viability) — vem ANTES do CTA conforme alinhamento do pitch.
> **⚠️ Scope: enterprise multinacional (Petrobras-class).** PME foi removido conforme correção do autor.
> **Função:** Onde o pitch valida que AxeGuard é **implementável** (viabilidade técnica) + **viable economicamente** (viabilidade econômica). É o que a banca SENAI julga para validar que o projeto é "real".
> **Versão:** v0.1 — Outubro 2026

---

## 🎯 Contexto

Slide 11 é o **"OK, mas dá pra fazer?"**. Antes do CTA, o juiz (ou Petrobras) precisa acreditar que:

1. **É tecnicamente viável** (pode ser construído / integrado)
2. **É economicamente viável** (cabe no orçamento + ROI justifica)

Se essa seção falha, o CTA ("Piloto 90 dias") cai no vazio.

**Posição estrutural confirmada:** slide 11 = viability. Slide 12 = convite. (Correção do autor: viability vem antes do CTA, não junto com tração/ROI como inicialmente proposto.)

---

## 📐 Slide 11 — As 2 Viabilidades

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│            AXEGUARD — VIABILIDADE TÉCNICA + ECONÔMICA                   │
│            ════════════════════════════════════════                     │
│                                                                          │
│   ┌─────────────────────────┐    ┌─────────────────────────┐             │
│   │  🔧 VIABILIDADE TECH.    │    │  💰 VIABILIDADE ECON.   │             │
│   │  ─────────────────       │    │  ─────────────────       │             │
│   │                         │    │                         │             │
│   │  ✅ COTS real (não       │    │  ✅ Custo único: R$ 0   │             │
│   │     vaporware)          │    │     em código proprietário│             │
│   │  ✅ Integração:         │    │                         │             │
│   │     90 dias setup       │    │  ✅ Setup: R$ 500K-2M  │             │
│   │  ✅ Sem reinventar       │    │     (descoberta +       │             │
│   │     roda (MDM, IdP,     │    │      integração 4       │             │
│   │     rede privada)        │    │      camadas)               │             │
│   │  ✅ Petrobras pode       │    │                         │             │
│   │     auditar peça        │    │  ✅ Recurring:           │             │
│   │     por peça              │    │     R$ 100K-500K/mês    │             │
│   │  ✅ Time-to-value        │    │     (SOC Agêntico +     │             │
│   │     vs 18 meses build    │    │      monitoring +        │             │
│   │     custom               │    │      updates)             │             │
│   │  ✅ SBOM completo        │    │                         │             │
│   │     auditável           │    │  ✅ ROI: 100x-500x      │             │
│   │                         │    │     (vs custo incidente)│             │
│   │  Risco residual         │    │                         │             │
│   │  declarado: Supply       │    │  Payback: < 1 dia      │             │
│   │  Chain HW em fábrica   │    │  (1 incidente evitado  │             │
│   │  (mitigado por          │    │   já cobre 12 meses)   │             │
│   │  procurement security)  │    │                         │             │
│   │                         │    │                         │             │
│   └─────────────────────────┘    └─────────────────────────┘             │
│                                                                          │
│              ⚠️ SCOPE: ENTERPRISE MULTINACIONAL                          │
│              Petrobras-class, não PME.                             │
│              Sales cycle: 6-12 meses (não transacional)        │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 🔧 Viabilidade Técnica

### **Argumento 1: COTS real, não vaporware**

Cada camada AxeGuard usa tecnologia de mercado **disponível hoje**:

| Camada | COTS | Vendor | Status |
|---|---|---|---|
| 1 (MDM) | ArborXR | ArborXR Inc | Produção |
| 1 alt (MDM) | Hexnode UEM | Hexnode | Produção |
| 2 (OAuth) | Microsoft Entra ID | Microsoft | Produção (Petrobras já tem?) |
| 2 alt (OAuth) | Okta | Okta Inc | Produção |
| 3 (DLP) | FastAPI + SpaCy | Open source | Produção |
| 3 alt (DLP) | Microsoft Purview | Microsoft | Produção |
| 4 (Enclave) | Azure OpenAI VNet | Microsoft Azure | Produção |
| 4 alt (Enclave) | AWS Bedrock + Llama 3 | AWS + Meta | Produção |
| 5 (SOC) | LangGraph + Kafka | Open source + Cloud | Produção |

**Para a banca:** nenhuma peça precisa ser inventada. Toda peça tem vendor, suporte, documentação, comunidade.

### **Argumento 2: Time-to-value de 90 dias**

```
MÊS 1 ─ Descoberta + procurement
       └── SBOM + CTI feed setup + vendor scorecard
MÊS 2 ─ Integração Camadas 1-2
       └── ArborXR + Entra ID + OAuth Device Flow + TPM binding
MÊS 3 ─ Integração Camadas 3-4
       └── DLP Proxy + VNet Enclave
MÊS 3 ─ SOC Agêntico operacional
       └── LangGraph + Kafka + UEBA + auto-response
MÊS 3 ─ Piloto pronto
       └── 1 refinaria, ambiente de teste
```

**Comparação:** projeto custom seria 12-18 meses para entregar a mesma cobertura.

### **Argumento 3: Audibilidade**

Cada peça é open-source ou vendor com certificação:
- ArborXR: SOC 2 Type II, ISO 27001
- Microsoft Entra ID: SOC 2, ISO 27001, FedRAMP
- Azure OpenAI: SOC 2, ISO 27001, HIPAA, GDPR
- FastAPI + SpaCy: MIT License, código aberto

Petrobras pode auditar cada peça independentemente.

### **Argumento 4: SBOM completo**

Cada dispositivo XR tem SBOM (Software Bill of Materials) declarado. Cada library opens source tem hash verificado. Cada dependência tem proveniência rastreável.

Petrobras pode validar a qualquer momento.

### **⚠️ Risco residual declarado**

**Supply Chain HW em fábrica não fecha 100%.**

Mesmo com SBOM + MDM + VNet, um componente adulterado durante fabricação (vide Hezbollah/Boston Scientific 2024) pode chegar ao ambiente operacional.

**Mitigação complementar:**
- Procurement security da Petrobras (vendor scorecard, inspeção de fábrica)
- Firmware integrity check no primeiro boot
- Hardware certificate pinning

**Transparência:** honestidade técnica agrega credibilidade com banca SENAI.

---

## 💰 Viabilidade Econômica

### **Modelo de Pricing — ENTERPRISE Multinacional**

| Componente | Custo (R$) | Frequência | Justificativa |
|---|---|---|---|
| **Setup / Descoberta** | 500K - 2M | único | SBOM + CTI + integração 4 camadas + 1 SOC Agêntico |
| **Recurring — SOC Agêntico** | 100K - 500K/mês | mensal | 1 cluster cloud serve N refinarias (escala horizontal) |
| **Updates + Threat Intel** | 50K - 150K/mês | mensal | IOC feed + ML model retraining + runbook curation |
| **Suporte Petrobras (24/7)** | 50K - 200K/mês | mensal | CISO-grade escalation + quarterly review |
| **TOTAL primeiro ano** | ~R$ 5M - 10M | anual | vs US$ 71M+ e esperado loss |

### **ROI — Cálculo Conservador**

```
INVESTIMENTO ANUAL: R$ 5M - 10M (setup + recurring + updates + suporte)
EXPECTED LOSS SEM AXEGUARD: US$ 71M+ / ano (Petrobras risk exposure)
ROI = (EXPECTED LOSS - INVESTIMENTO) / INVESTIMENTO
ROI = (R$ 354M - R$ 7.5M) / R$ 7.5M
ROI ≈ 47x no cenário conservador

CENÁRIO OTIMISTA:
EXPECTED LOSS: US$ 1B+ (Colonial Pipeline + NotPetya worst case)
ROI = (R$ 5B - R$ 7.5M) / R$ 7.5M
ROI ≈ 666x
```

**Conclusão:** ROI conservador ~47x. Otimista ~666x. Payback em < 1 dia se UM incidente for evitado.

### **Por que enterprise pricing (não R$ 1.000/mês PME)**

| Aspecto | ❌ Frame PME (incorreto) | ✅ Frame enterprise (correto) |
|---|---|---|
| Sales cycle | Transacional, self-serve | 6-12 meses, RFP, comitê |
| Buyer | Dono de fábrica | CISO + CTO + board |
| ROI calc | R$ X mil evitados | R$ X bi evitados |
| TAM | Distrito industrial | US$ 32bi global O&G |
| Compliance | LGPD básico | LGPD + ANP + IBAMA + NIS2 + ISA/IEC 62443 |
| Defensabilidade | Concorrência com vendors baratos | Diferenciação técnica + soberania |

**Nota do `Rules_and_Winning_Strategies_GP.md` §4 (PI defensiva):** o modelo de pricing é parte da estratégia competitiva. Petrobras não quer "barato barato" — quer **defensável**.

### **Comparação com mercado (Atratividade / Vencedora)**

| Alternativa | Custo anual | Cobertura | Lacuna |
|---|---|---|---|
| **Palo Alto + CrowdStrike + Splunk** | ~R$ 30M | Endpoint + SIEM | Não cobre XR + DLP sem código |
| **Microsoft Defender P2 + Sentinel** | ~R$ 15M | Endpoint + SIEM + IdP | Não cobre DLP Petrobras-specific |
| **Projeto custom interno** | ~R$ 50M+ | Teórica | 18 meses + risco de execução |
| **AxeGuard enterprise** | R$ 5M - 10M | 4 camadas + SOC | Setup 90 dias, audível |

---

## 🎯 Sales Motion ENTERPRISE

**Como Petrobras compra:**

1. **Mês 1-2:** Descoberta + demo executiva (CISO + CTO)
2. **Mês 3-4:** RFP técnico + due diligence (procurement + segurança)
3. **Mês 5-6:** Piloto controlado (1 refinaria + 1 ambiente cloud)
4. **Mês 7-9:** Avaliação de resultados + negociação
5. **Mês 10-12:** Contrato enterprise + rollout faseado

**Total: 6-12 meses do primeiro contato ao contrato assinado.**

**Por que isso importa pro pitch:**
- Banca SENAI entende que não é "vende e pronto"
- Petrobras (se for o público) entende que o sales cycle respeita procurement corporativo
- Demonstra maturidade de go-to-market

---

## ⚠️ Risco do Pitch — Pricing como alvo competitivo

**Cuidado:** se o pitch mostra pricing detalhado, concorrentes aparecem com preços menores. Petrobras pode usar para negociação.

**Tática do manual §4 (PI defensiva):**

> *Foco em usar APIS consolidadas como pilares da solução visível, reduzindo a nossa exposição à perda criativa profunda em longo prazo se quisermos escalar o app após a competição.*

**O que mostrar:** ROI de ordem de grandeza (47x conservador).
**O que NÃO mostrar:** breakdown exato de R$ por peça.

---

## 💡 Storytelling do slide

```
"Cada hora sem detecção = mais 1.25 GB vazados.
 Cada dia sem nossa semana = mais 30 GB vazados.
 Em 72 horas = 90 GB de sísmica do pré-sal.

 Investimento: 1 ano de AxeGuard.
 Custo de 1 incidente SA Exploration: US$ 15-25M.

 A pergunta não é se Petrobras pode pagar AxeGuard.
 É se pode pagar NÃO ter AxeGuard."
```

---

## ⏭️ Próxima parte

**PARTE 7 — Convite + CTA** (slide 12, "Piloto 90 dias. 1 refinaria. Risco zero.")