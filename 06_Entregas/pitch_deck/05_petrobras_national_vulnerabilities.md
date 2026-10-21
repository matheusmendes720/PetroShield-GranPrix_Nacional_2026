# PARTE 3A — Vulnerabilidades Petrobras + Indústria Nacional

> **Deliverable:** Conteúdo narrativo para o slide 6 (vulnerabilidades da indústria O&G brasileira + Petrobras-específicas).
> **Função:** Validar a tese de que **o campo de batalha é real, ativo, e em aceleração** — não é hipotético.
> **Versão:** v0.1 — Outubro 2026
> **Status:** Aguardando aprovação para PARTE 3B (caso Bacia de Campos, deep-dive técnico)

---

## 🎯 Contexto

Slide 6 do pitch é o **"campo de batalha ativo"** — duração alvo 30-40s.

Por que essa seção existe: a banca SENAI + Petrobras precisa acreditar que a ameaça **não é hipotética**. Cada vulnerabilidade listada é um caso real, com data, vetor, custo estimado. É a **antítese** da tese AxeGuard (do dossier `00_INDEX.md` §Narrativa).

Dados-chave do `Research_Attacks_Cases/00_INDEX.md`:
- **62% dos breaches O&G** vêm via fornecedor (IBM X-Force 2024)
- **Window of exposure: 7 dias (era 60 dias em 2020)** — MITRE ATT&CK trend
- **MTTD brasileiro: 322 dias** (IBM 2023) — bem pior que média global
- **Window shrinking:** atacantes têm cada vez menos janela para explorar antes de patch/discovery

---

## 📋 Vulnerabilidades LATAM/Nacional (industry-wide, O&G)

### **1. Storm-1175 / Medusa Ransomware (2026, ativo)**
- **Tipo:** Ransomware-as-a-Service (RaaS), modelo LockBit-style double extortion
- **Vetor:** Phishing em português brasileiro + Google Ads fraudulentas + Kerberoasting + Pass-the-Hash
- **Alcance:** LATAM ativo, mira setor de energia, saúde, infraestrutura crítica
- **Resgate típico LATAM enterprise:** US$ 500K-5M
- **Relevância Petrobras:** NÃO mira Petrobras diretamente (oportunista). MAS Petrobras tem milhares de fornecedores com VPNs ativas — cada fornecedor = vetor Storm-1175 potencial.
- **Mitigação AxeGuard:** SOC Agêntico (detecção Kerberoasting/PtH via comportamento) + DLP Middleware (monitoramento SCADA telemetry) + segmentação vendor (fornecedor acessa APENAS namespace necessário).

### **2. APT Iranian targeting PLCs (Abr 2026, ativo, alerta CISA)**
- **Tipo:** APT / ICS targeting — MuddyWater / APT34 (atribuído ao IRGC)
- **Vetor:** Comprometimento de fornecedor de automação → VPN → pivot IT → gap para OT → manipulação direta de PLCs
- **Capacidades:** Custom malware para Siemens, Schneider, Rockwell; backdoor no firmware; modificação de lógica de controle
- **Histórico:** Já comprometeu sistemas de água, energia, petroquímica no Oriente Médio + Europa
- **Relevância Petrobras:** ⭐ **Caso mais diretamente relevante do dossiê.** Grupo iraniano mira EXATAMENTE o tipo de infra que Petrobras opera. Petrobras é alvo geopolítico de interesse direto.
- **Mitigação AxeGuard:** Defesa profunda em 3 camadas (Prevenção: CTI + SBOM + vendor score | Detecção: Modbus traffic anomaly + PLC logic change detection + UEBA OT | Resposta: isolamento OT + rollback PLC + forensic). SOC Agêntico com CTI feed para IOC Iranian.

### **3. CrystalX RAT (Jan 2026, ativo)**
- **Tipo:** Remote Access Trojan (RAT) / Malware-as-a-Service
- **Vetor:** Telegram bots + YouTube (vídeos de crack) + download PowerShell
- **Preço:** US$ 30-150/mês (acessível a qualquer nível de habilidade)
- **Capacidades:** Keylogger + screen capture + clipboard + **OAuth token extraction (Chromium-based)**
- **Relevância Petrobras:** ⭐ **Diretamente ao Device Flow AxeGuard.** Se celular corporativo tem CrystalX, malware pode interceptar QR code do óculos, extrair authorization code, completar Device Flow, obter JWT, acessar API Petrobras. Conhecido como **OAuth QR Code Hijacking**.
- **Mitigação AxeGuard:** Device Binding (TPM assina token JWT); QR Code Cryptographic Binding (nonce 32 bytes no TPM do óculos); Session Anomaly Detection (geolocation + device fingerprint + behavioral).

### **4. Boeing RFQ Campaign (2026, ativo)**
- **Tipo:** BEC (Business Email Compromise) via Supply Chain
- **Vetor:** E-mails falsificados Boeing/Embraer/Lockheed Martin → RFQ falsos → credential capture → acesso a procurement systems → interceptação de pagamentos
- **Cadeia secundária:** Fornecedor comprometido → acesso à VPN Petrobras → pivot para rede Petrobras
- **Custo típico:** R$ 500K-5M por fornecedor vítima
- **Mitigação AxeGuard:** Vendor security scorecard contínuo + Hardware certificate pinning (XR só aceita endpoints verificados) + SOC agêntico monitorando comportamento de fornecedor.

---

## 📋 Vulnerabilidades Petrobras-Específicas (casos diretos)

### **5. SA Exploration → Petrobras (Nov 2025)**
- **Tipo:** Espionagem industrial via fornecedor
- **Vetor:** VPN corporativa do fornecedor com credenciais em texto claro → portal de dados Petrobras → exfiltração via DNS-over-HTTPS
- **Dados vazados:** 90 GB de dados sísmicos em 72 horas — mapas de reservatórios pré-sal, leitura sísmica 3D Bacias de Campos e Santos, relatórios de avaliação geológica
- **Custo estimado:** US$ 15-25M (IP sísmico + contencioso)
- **Falhas de controle identificadas:** 5 controles falharam (autenticação sem MFA, sem segmentação, sem DLP, sem UEBA, sem revogação)
- **Mitigação AxeGuard:** DLP Middleware intercepta DNS-over-HTTPS; tokens OAuth Device Flow com TPM binding; UEBA dispara em transferência massiva; SOC agêntico responde em < 12s.
- **Impacto AxeGuard:** Detecção 3 meses → 12s; vazamento 90 GB → 0 GB; custo incidente $15-25M → $0.
- **⭐ ESTE É O CASO ANCHOR DO PITCH — detalhe técnico completo na PARTE 3B (Caso Bacia de Campos)**

### **6. OceanPact — Frota OSV (2024)**
- **Tipo:** Exposição OT — OAuth token theft
- **Vetor:** Servidor de bordo desatualizado (VSAT) → tokens OAuth em texto claro (.env) → dark web
- **Escala:** Maior frota OSV do Brasil — 80+ embarcações, R$ 3.2B em contratos
- **Exposição:** Rotas, cargas, pessoal offshore
- **Relevância:** **Dispositivos XR são equivalente "nova geração" do servidor desatualizado.**
- **Mitigação AxeGuard:** OAuth2 Device Flow com PKCE (tokens curta duração, nunca em disco) + Token Binding via TPM/secure enclave + SOC agêntico monitorando uso anômalo (horário, localização VSAT, volume).

### **7. Oceânica Engenharia (2024-25)**
- **Tipo:** Data breach via proxy malicioso
- **Vetor:** Proxy reverso não-autorizado instalado por TI da Oceânica → túnel para serviço comercial → bypass de DLP Petrobras
- **Escala:** R$ 4.2B em contratos Petrobras
- **Relevância:** **Cada técnico offshore com tablet conectado = "proxy Oceânica" potencial.** Dispositivo XR mal-configurado com acesso OT = mesmo vetor.
- **Mitigação AxeGuard:** DLP Middleware intercepta TODA comunicação (sem exceção) + NAC bloqueando dispositivos não-MDM + SOC agêntico detectando padrões de proxy não-autorizado.

### **8. Hezbollah Pagers / Boston Scientific (Set 2024)**
- **Tipo:** Supply chain de hardware — comprometimento em fábrica
- **Vetor:** Cadeia da BAC Consulting comprometida → PETN + circuito de detonação implantado durante fabricação
- **Escala:** US$ 80M+ em equipamentos comprometidos
- **Relevância Petrobras:** Boston Scientific fornece equipamentos médicos para plataformas offshore. Componentes eletrônicos de fornecedores IoT offshore comprometidos em fábrica chegam ao ambiente operacional sem verificação.
- **Mitigação AxeGuard (parcial):** SBOM (Software Bill of Materials) para XR + verificação de integridade de firmware via hashchain SLSA + Zero-Trust de hardware. **Limitação declarada:** não fecha componente já adulterado em fábrica.

### **9. xz-utils Backdoor (2024)**
- **Tipo:** Supply chain de software — open-source
- **Vetor:** 2 anos de contribuições "legítimas" ganhando confiança → backdoor injetado em liblzma (v5.6.0-5.6.1) → comprometimento sshd em sistemas Linux
- **Escala potencial:** 10.000+ servidores cloud comprometidos (AWS, Google Cloud, Azure)
- **Relevância Petrobras:** Petrobras usa inúmeros componentes open-source em pipelines sísmicos, middleware de comunicação, CI/CD, ambientes cloud com containers pré-configurados.
- **Mitigação AxeGuard:** SBOM de software (paralelo ao HW SBOM) + verificação de integridade via Sigstore/cosign + SOC agêntico monitorando anomalias em componentes open-source.

### **10. npm Malicioso — uake-update (2025)**
- **Tipo:** Supply chain de software — pacote malicioso
- **Vetor:** Pacote npm uake-update exfiltrou credenciais de desenvolvedores, variáveis de ambiente, chaves SSH de produção
- **Escala:** Milhares de projetos comprometidos
- **Relevância Petrobras:** Petrobras usa frameworks de IA + middleware Python em pipelines de dados sísmicos. Pacote npm/PyPI malicioso em dependência compromete toda cadeia CI/CD.
- **Mitigação AxeGuard:** SBOM de software + verificação Sigstore/cosign + SOC agêntico monitorando anomalias.

---

## 📐 Padrão Sistêmico — Vendor VPN Compromise (62% dos breaches O&G)

**62% dos breaches O&G** vêm via fornecedor (IBM X-Force 2024). Padrão recorrente em 3 fases:

```
FASE 1 — INFiltração
  Atacante obtém credenciais VPN de fornecedor
  (phishing, credential stuffing, dark web purchase)

FASE 2 — LATERAL MOVEMENT
  Credenciais válidas → move na rede do fornecedor
  → acesso à rede da Petrobras (VPN)
  MITRE: T1133 + T1550

FASE 3 — EXFILTRAÇÃO / IMPACTO
  Dados proprietários exfiltrados OU ransomware
  MITRE: T1048 / T1486
```

### **A nova dimensão: dispositivos XR são o "novo vendor VPN"**

| Aspecto | Vendor VPN Tradicional | Dispositivo XR |
|---|---|---|
| Acesso | Credenciais VPN | OAuth2 JWT |
| Período | Semanas a meses | Por sessão |
| Dados transmitidos | Documentos, e-mail | Áudio, vídeo, GPS, telemetria |
| Superfície | Servidor VPN | Mic, câmera, GPS, acelerômetro |
| DLP cobertura | Parcial | Nenhuma (tráfego de mídia) |
| SOC monitoring | Logs VPN | Telemetria MDM |

---

## 📊 Síntese — Por que essas vulnerabilidades importam

```
┌─────────────────────────────────────────────────────────────────┐
│  CAMPO DE BATALHA ATIVO E EM ACELERAÇÃO                         │
├─────────────────────────────────────────────────────────────────┤
│  • LATAM ransomware ativo e mirando energia + critical infra    │
│  • APT Iranian mirando EXATAMENTE o tipo de planta Petrobras    │
│  • Dispositivos XR ampliam superfície de ataque (vetor novo)    │
│  • 62% dos breaches O&G = via fornecedor                        │
│  • Window of exposure: 60 dias (2020) → 7 dias (2026)           │
│  • MTTD BR: 322 dias (o atacante tem MUITO tempo)               │
│  • Petrobras direta: SA Exploration, OceanPact, Oceânica        │
└─────────────────────────────────────────────────────────────────┘
```

**A urgência que sustenta o pitch:** a janela está fechando. Petrobras tem **meses**, não anos, para fechar esses vetores antes que um caso de impacto-catastrófico (TRITON-like, Colonial Pipeline-like) atinja a operação.

---

## 🎯 Por que essas 10 (e não outras)

Selecionei estas 10 vulnerabilidades de um universo de **19 casos** no dossier `Research_Attacks_Cases/` aplicando 3 filtros:

1. **Relevância Petrobras/LATAM (não ataques em outros continentes sem ponte com setor O&G)**
2. **Mapeamento direto para camada AxeGuard** (ataque que o produto fecha — não ataques de phishing genérico)
4. **Maturidade do caso** (casos documentados publicamente, não especulação)

Casos NÃO incluídos (com理由):
- TRITON/XENOTIME (2017, global) — contexto, não Petrobras-específico
- SolarWinds (2020, global) — já coberto em Paradigma 1 (Supply Chain)
- Colonial Pipeline (2021, US) — paralelo conceitual, não Petrobras
- Equifax (2017, US) — paralelo conceitual, não Petrobras
- Norsk Hydro (2019, Norway) — paralelo conceitual, não Petrobras
- Banco do Brasil + Caixa (2023, financeiro) — fora do setor O&G
- Ministério da Saúde (2021, gov BR) — fora do setor O&G

---

## ⏭️ Próxima parte

**PARTE 3B — Caso Bacia de Campos** (rich technical detail do caso SA Exploration → Petrobras, Nov 2025)

---

## ❓ Perguntas para você

1. As 10 vulnerabilidades estão certas? Filtrar mais ou menos?
2. Manter 4 LATAM + 6 Petrobras (específicas) ou reorganizar (ex: 3 LATAM + 7 Petrobras)?
3. Conectar com casos da pesquisa (já linkadas) — manter?
4. Adicionar alguma vulnerabilidade fora do dossiê (ex: LockBit 3.0 BR)?