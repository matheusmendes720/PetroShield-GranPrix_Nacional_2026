# PARTE 2B — Filtro Petrobras + Relevância AxeGuard

> **Deliverable:** Conteúdo narrativo que conecta os 5 padrões globais ao produto AxeGuard e ao cliente-âncora Petrobras.
> **Função no pitch:** Preenche os slides 4 (vetores visuais) e 7 (mitigação) com a lógica "este ataque importa PARA NÓS".
> **Versão:** v0.1 — Outubro 2026
> **Status:** Aguardando aprovação para PARTE 2C (mitigação detalhada por padrão)

---

## 🎯 Por que filtrar

De todos os 19 ataques analisados no dossier `Research_Attacks_Cases/` (~160 KB), selecionamos os 5 padrões da PARTE 2A. Agora aplicamos um **filtro duplo**:

1. **Relevância para Petrobras** (cliente-âncora enterprise multinacional do setor O&G)
2. **Cobertura por camada AxeGuard** (qual camada do Edge Middleware + SOC Agêntico fecha o vetor)

O resultado é um **mapa de batalha**: para cada padrão, mostramos (a) por que Petrobras deveria se importar e (b) qual camada AxeGuard já é projetada para fechar. É a **tese de cobertura** que sustenta a credibilidade técnica do pitch.

---

## 🔍 Matriz de Relevância (5 padrões × Petrobras × AxeGuard)

```
┌────┬────────────────┬────────────────────────┬────────────────────────────────┬─────────────────────────────────────┐
│  # │ Padrão         │ Relevância Petrobras  │ Camada AxeGuard que fecha      │ Evidência de fechamento             │
├────┼────────────────┼────────────────────────┼────────────────────────────────┼─────────────────────────────────────┤
│ 1  │ Supply Chain   │ 🔴 CRÍTICA            │ Camada 1 (MDM) +               │ MDM fecha side-load contaminado;    │
│    │                │ Cadeia global complexa │ Camada 4 (VNet Enclave)        │ VNet isola backdoor residual       │
├────┼────────────────┼────────────────────────┼────────────────────────────────┼─────────────────────────────────────┤
│ 2  │ Endpoint       │ 🔴 CRÍTICA            │ Camada 1 (MDM Kiosk Mode)      │ ArborXR/Hexnode fecha side-load     │
│    │                │ XR = vetor primário    │                                │ + keylogger; root bypass bloqueado  │
├────┼────────────────┼────────────────────────┼────────────────────────────────┼─────────────────────────────────────┤
│ 3  │ Credencial     │ 🔴 CRÍTICA            │ Camada 2 (OAuth Device Flow    │ Smart glass + QR + biometria       │
│    │                │ Shoulder-surfing físico│ + PKCE + TPM Binding)          │ celular = vetor fechado; TPM =     │
│    │                │ é vetor XR-específico   │                                │ replay attack bloqueado            │
├────┼────────────────┼────────────────────────┼────────────────────────────────┼─────────────────────────────────────┤
│ 4  │ Exfiltração    │ 🔴 CRÍTICA            │ Camada 3 (DLP Proxy Middleware)│ Regex + NLP + UEBA + channel       │
│    │                │ Soberania energética + │ + Camada 4 (VNet Enclave)      │ inspector substitui PII/token em   │
│    │                │ LGPD + ANP compliance  │                                │ tempo real; egress para LLM = VNet │
├────┼────────────────┼────────────────────────┼────────────────────────────────┼─────────────────────────────────────┤
│ 5  │ Sobrecarga /   │ 🟠 ALTA               │ SOC Agêntico (backend cloud,   │ UEBA + ML + correlação cross-     │
│    │ Paralisia      │ 197 dias MTTD da       │ 5ª camada "escondida")         │ source + auto-response = 12s MTTD  │
│    │                │ indústria encapsula    │                                │ (vs 197 dias / 322 dias BR)        │
│    │                │ exatamente isso        │                                │                                     │
└────┴────────────────┴────────────────────────┴────────────────────────────────┴─────────────────────────────────────┘
```

---

## 📌 Anotações por padrão (1 linha por célula)

### Padrão 1 — Supply Chain
- **Por que importa pra Petrobras:** Cadeia tecnológica de smart glasses (chip Qualcomm + OS Android AOSP + apps + SDKs) tem múltiplos elos de fornecedores globais. Cada elo é vetor. Petrobras usa fornecedores globais para VR (Meta, RealWear) e componentes (Qualcomm, etc.).
- **Como AxeGuard fecha:** MDM em Kiosk Mode (Camada 1) blinda o dispositivo contra componentes contaminados que tentem se ativar. VNet Enclave (Camada 4) isola qualquer backdoor residual que chegue até a LLM. Limitação conhecida: **não fecha o componente já adulterado em fábrica** — Petrobras deve continuar com procurement security.

### Padrão 2 — Endpoint
- **Por que importa pra Petrobras:** Smart glasses rodam Android modificado; matação nativa tem jailbreaks públicos (SideQuest, ALVR). Câmera + mic + dado confidencial = goldmine para spyware tipo Pegasus. **Pior vetor para XR.**
- **Como AxeGuard fecha:** MDM corporativo (ArborXR / Hexnode UVM) em **Kiosk Mode restrito** + App corporativo único + bloqueio de sideload. Atacante não consegue instalar keylogger sem privilégio admin.

### Padrão 3 — Credencial
- **Por que importa pra Petrobras:** Smart glass **vetorialmente perigosa** para credencial. Shoulder-surfing físico é trivial; tela é gravável por outro óculos próximo; digitação no ar é lenta e observável.
- **Como AxeGuard fecha:** OAuth 2.0 Device Authorization Grant (RFC 8628) + PKCE + TPM binding:
  - Óculos exibe QR Code temporal
  - Operador escaneia com celular Petrobras (autenticado por biometria no MDM local)
  - Token JWT injetado dinâmico
  - TPM binding: mesmo token em outro device = inválido
  - Shoulder-surfing do QR? PKCE fecha replay. Captura do token? TPM binding fecha.

### Padrão 4 — Exfiltração
- **Por que importa pra Petrobras:** **Soberania energética + LGPD + compliance ANP.** Dados como "Plataforma P-10", "Bacia de Campos", "Tupi-10", balanços de fluxo, sísmica do pré-sal = ativo estratégico nacional. Vazar para servidor estrangeiro = perda de soberania + sanção ANP + multa LGPD.
- **Como AxeGuard fecha:**
  - **Regex Engine** detecta PII + termos O&G em tempo real
  - **NLP Engine** (SpaCy / similar) detecta entidades geológicas / industriais
  - **UEBA** detecta anomalias (volume + horário + destino)
  - **Channel inspector** inspeciona DNS, streaming, HTTPS egress
  - **Substituição atômica:** "Plataforma P-10" → "[ATIVO_RESTRITO_01]" antes de chegar na LLM
  - **Camada 4 (VNet Enclave):** LLM sob contrato No-Train B2B (Azure OpenAI Private) — dado não chega em vendor público.

### Padrão 5 — Sobrecarga / Paralisia
- **Por que importa pra Petrobras:** A média brasileira de MTTD é **322 dias** (IBM 2023). O atacante **não precisa ser silencioso** — só precisa ser mais rápido que a análise humana. Smart glass gera telemetria massiva (cada frame de câmera, cada input de áudio); SOC tradicional **afoga**.
- **Como AxeGuard fecha:** SOC Agêntico (camada "5" — backend cloud):
  - **Ingest:** Event Hubs / Kafka — escala massiva
  - **Analytics:** UEBA + ML + correlação cross-source
  - **Decision:** auto-response + escalation inteligente
  - **Feedback:** melhoria contínua (modelos aprendem com cada incidente)
  - **Resultado:** MTTD < 12s (vs 197 dias / 322 dias)
  - **Lever de escala:** 1 cluster na nuvem serve N refinarias (Polo de Camaçari inteiro, replicável para qualquer enterprise).

---

## ⚠️ Scope Clarification (correção aplicada)

**Nota importante do autor:** o scope do pitch é **enterprise multinacional** (Petrobras-class), NÃO PME.

### Implicações no pitch:

| Aspecto | ❌ Frame PME (removido) | ✅ Frame enterprise (atual) |
|---|---|---|
| Pricing | R$ 1.000/mês | Sob proposta enterprise (centenas de milhares a milhões/ano) |
| Sales cycle | Transacional, self-serve | 6-12 meses, RFP, comitê de segurança |
| Buyer persona | Dono de fábrica | CISO + CTO + board de segurança |
| ROI calc | Riscoção de risco baixo (R$ X mil) | $71M+/ano (Petrobras tem exposição muito maior) |
| TAM/SAM/SOM | Distrito industrial (Camaçari BA) | Enterprise O&G global (Petrobras + Shell + BP + Total + Equinor + Saudi Aramco...) |
| Compliance | LGPD básico | LGPD + ANP + IBAMA + NIS2 + ISA/IEC 62443 + SOX |
| Sales motion | Auto-serve + suporte | Account executive + CISO sponsorship |

### Implicações na narrativa:

- **Foco em soberania energética + LGPD + ANP**, não em custo acessível
- **Cases emblemático** são Colonial Pipeline (2020), NotPetya (2017), Storm-0558 (2023) — **ataques de impacto enterprise**, não golpes PIX de pessoa física
- **Personas do pitch:** banca do SENAI (juízes), com Petrobras aparecendo como **validação de anchor enterprise**
- **ROI:** números em $M-$B, não em R$ X mil

---

## 💡 Melhorias adicionais que proponho (convite aberto do autor)

### Melhoria 1 — **Dual-audience com prioridade SENAI**
A audiência primária do pitch SENAI GP 2026 é a **banca de juízes** (incluindo IA pré-triagem), NÃO Petrobras-comprador. Petrobras aparece como **anchor validation** (prova social + alinhamento setorial). Reframe:
- Slide 11 (Viability): falar para **juízes técnicos + бизнес** — "implementável, vendável, escalável, defensável"
- Petrobras no slide como prova de alinhamento, não como buyer persona

### Melhoria 2 — **TAM/SAM/SOM para enterprise O&G global**
Reframe para TAM global enterprise O&G:
- **TAM:** ~US$ 32bi (mercado global de cibersegurança industrial, CAGR 12%)
- **SAM:** ~US$ 8bi (subset O&G + Critical Infrastructure)
- **SOM:** ~US$ 800M (5 majors: Petrobras, Shell, Total, BP, Equinor + Saudi Aramco) — first-2 anos

### Melhoria 3 — **Pricing defensável para enterprise**
Sugiro mover o número "R$ 1.000/mês" para fora do pitch (era o modelo PME) e usar **proposta enterprise-tier**:
- **Setup:** R$ 500K-2M (descoberta + integração Camadas 1-4 + SOC)
- **Recurring:** R$ 100K-500K/mês (SOC Agêntico + monitoramento + updates)
- **Racional:** Petrobras tem R$ 600bi+ receita, risco de US$ 1bi+ em produção — pricing enterprise é defensável e escala o negócio.

### Melhoria 4 — **Adicionar slide de risco residual declarado** (transparência)
SENAI juízes valorizam honestidade técnica. Adicionar 1 linha ao slide 11 (Viability): "Risco residual declarado: supply chain em chip não fecha 100%; Petrobras deve combinar AxeGuard com procurement security de fornecedores."

### Melhoria 5 — **Cross-link com dossier**
Cada padrão que estiver mencionando, linkar para o arquivo fonte do dossier:
- Padrão 1-5 → `Research_Attacks_Cases/01_Global_Attacks_Cases.md` e `02_Brazil_National_Attacks_Cases.md` e `03_Petrobras_Specific_Attacks_Cases.md`
- Mitigação: para `10_Arquitetura_SOC_Agêntico.md`
- Estratégia antifrágil: para `07_Sintese_TCC.md` (tese/antítese/síntese formal)

---

## ⏭️ Próxima parte

**PARTE 2C — Mitigação Breve por Padrão** (1 frase por padrão mapeando → camada AxeGuard + tecnologia COTS)

---

## ❓ Perguntas para você

1. As 5 melhorias propostas fazem sentido ou tem alguma que você não concorda?
2. Os números de TAM/SAM/SOM e pricing enterprise são placeholders — qual é o número real que você quer defender?
3. Quer manter o link para o dossier ou remover (cleaner pitch, mas perde rastreabilidade)?