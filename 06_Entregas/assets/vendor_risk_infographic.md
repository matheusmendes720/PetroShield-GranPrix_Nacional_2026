# 📊 Asset Visual: Estatísticas de Vendor Risk — Petrobras

> **Uso:** Pode ser incorporado no pitch (E3) como tela estática ou animada, ou usado como material de apoio na apresentação.  
> **Fonte:** `01_Intel_OSINT/Petrobras_Supply_Chain_Vendor_Intelligence.md`

---

## Infográfico: O Ecossistema de Risco

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│     ⚠️  PETROBRAS VENDOR ECOSYSTEM — ATTACK SURFACE ANALYSIS           │
│                                                                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                 │
│  │  10.000+    │    │    ~500     │    │   ~2.000    │                 │
│  │   VENDORS   │───→│   CRÍTICOS  │───→│ ALTO ACESSO │                 │
│  │   ATIVOS    │    │             │    │             │                 │
│  └─────────────┘    └─────────────┘    └─────────────┘                 │
│                                                                         │
│         ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────┐       │
│  │  🚨 BREACH CONFIRMADO: SA EXPLORATION — NOVEMBRO 2025       │       │
│  │                                                             │       │
│  │  • 190 GB de dados vazados                                  │       │
│  │  • Dados sísmicos do Campo de Campos expostos               │       │
│  │  • Causa: credenciais de VPN sem MFA                        │       │
│  │  • Custo estimado de recuperação: R$ 35M — R$ 110M+         │       │
│  └─────────────────────────────────────────────────────────────┘       │
│                                                                         │
│  ┌────────────────────────┐  ┌────────────────────────┐                │
│  │  OCEÂNICA ENGENHARIA   │  │      OCEANPACT         │                │
│  │    R$ 4.2 BILHÕES      │  │    R$ 3.2 BILHÕES      │                │
│  │   Contrato até 2031    │  │   Frota OSV #1 BR      │                │
│  │    RISCO: CRÍTICO      │  │    RISCO: CRÍTICO      │                │
│  └────────────────────────┘  └────────────────────────┘                │
│                                                                         │
│  ═══════════════════════════════════════════════════════════════════    │
│                                                                         │
│  CADA VENDOR É UMA PORTA. SEM MONITORAMENTO, É UMA PORTA ABERTA.       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Sugestões de Apresentação no Vídeo

### Opção A: Tela Estática com Efeito Ken Burns (Zoom Lento)
- **Timing:** Inserir no bloco "Problema" (00:10-00:40), logo após o hook.
- **Efeito:** Zoom lento no centro do infográfico, destacando os números 10.000+, 190GB e R$ 4.2B.
- **Áudio:** Narração do problema sincronizada com o aparecimento dos dados.

### Opção B: Animação Simples (Texto Aparecendo)
- **Timing:** Mesma janela.
- **Animação:**
  1. "10.000+ VENDORS ATIVOS" aparece com glitch.
  2. Seta animada aponta para "~500 CRÍTICOS".
  3. Box vermelho do breach SA Exploration surge com pulsação.
  4. Cards dos contratos bilionários deslizam de baixo para cima.
- **Ferramentas:** Canva (animações prontas) ou After Effects.

### Opção C: Overlay no Dashboard
- **Timing:** Durante a cena 4 do dashboard (Vendor Cascade).
- **Efeito:** Screen capture do dashboard com o infográfico como picture-in-picture no canto superior direito.
- **Vantagem:** Conecta o protótipo funcional aos dados reais de mercado.

---

## Dados-Chave para Destacar na Narração

Ao apresentar este visual, a narração pode enfatizar:

1. **Escala:** "Mais de dez mil vendors. Quinhentos críticos."
2. **Impacto real:** "Cento e noventa gigabytes vazados em novembro de 2025."
3. **Causa raiz:** "Credenciais de VPN sem MFA."
4. **Exposição financeira:** "Só a Oceânica Engenharia movimenta quatro vírgula dois bilhões de reais. Um breach ali não é um incidente. É uma crise nacional."

---

## Cores e Tipografia (Alinhado ao Design System PetroShield)

| Elemento | Cor | Uso |
|----------|-----|-----|
| Fundo | `#0A0A0A` | Base escura |
| Títulos | `#00FF41` | Neon Matrix Green |
| Destaques de risco | `#FF6200` | Fire Petroleum Orange |
| Dados numéricos | `#00FFFF` | Cyan |
| Alertas críticos | `#FF0040` | Vermelho |
| Fonte títulos | `VT323` | Tipografia terminal |
| Fonte corpo | `Inter` | Legibilidade |

---

## Arquivos de Referência

- **Inteligência completa:** `01_Intel_OSINT/Petrobras_Supply_Chain_Vendor_Intelligence.md`
- **Mock data dos vendors:** `scripts/agentic_soc/mock_data.py` (VENDOR_RISK_DB)
- **Dashboard com Cena 4:** `scripts/dlp_proxy/static/dashboard.html`

---

*Asset gerado para reforçar a credibilidade do pitch com inteligência de mercado real.*
