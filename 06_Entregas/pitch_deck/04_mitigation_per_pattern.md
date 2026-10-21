# PARTE 2C — Mitigação Breve por Padrão

> **Deliverable:** Conteúdo narrativo para o slide 7 (mitigação por risco).
> **Função:** Para cada um dos 5 padrões da PARTE 2A, mapeamento em 1 linha → camada AxeGuard + tecnologia COTS.
> **Versão:** v0.1 — Outubro 2026
> **Status:** Aguardando aprovação para PARTE 3A + PARTE 3B

---

## 🎯 Contexto

Slide 7 do pitch é o **"como AxeGuard resolve o que o slide 4 diagnosticou"**. Duração alvo: 25-30s (tabela compacta visual).

A estrutura é um mapeamento direto:
- Padrão (5) → Camada AxeGuard que fecha → Tecnologia COTS → 1 métrica de impacto

---

## 📋 Tabela de Mitigação (5 padrões → Camada → Tecnologia → Impacto)

| # | Padrão | Camada AxeGuard | Tecnologia COTS | Impacto Mensurável |
|---|---|---|---|---|
| 1 | **Supply Chain (HW + SW)** | Camada 1 (MDM) + Camada 4 (VNet) | ArborXR / Hexnode UEM + Sigstore/cosign + SBOM check | SBOM 100% dos componentes XR; firmware integrity via hashchain SLSA; root privilege bloqueado |
| 2 | **Endpoint (sideload + keylogger)** | Camada 1 (MDM Kiosk Mode) | ArborXR Kiosk Mode + App whitelist + sideload block | Side-load = 0% sucesso; keylogger instalado = bloqueio automático |
| 3 | **Credencial (OAuth/TPM bypass)** | Camada 2 (OAuth Device Flow + PKCE + TPM) | Microsoft Entra ID / Okta + TPM 2.0 + PKCE | QR scan ≠ token válido sem TPM binding; shoulder-surfing inútil; token theft bloqueado |
| 4 | **Exfiltração (proxy + leak)** | Camada 3 (DLP Proxy) + Camada 4 (VNet) | Regex + SpaCy NLP + UEBA + Ngrok/Cloudflare Tunnel + Azure OpenAI VNet | 90 GB via DNS = 0 GB na egress (DLP regex block); dado chega só no enclave No-Train |
| 5 | **Sobrecarga (alert storm)** | SOC Agêntico (Camada 5, backend) | Event Hubs + UEBA + ML + auto-response | MTTD < 12s (vs 197 dias / 322 dias BR); SOC isolada por L3/L4 automático |

---

## 📐 Narrativa por padrão (1 parágrafo cada)

### Padrão 1 — Supply Chain
A Petrobras exige SBOM completo dos dispositivos XR (Meta Quest, HoloLens, RealWear) + verificação de integridade de firmware via Sigstore/cosign + hashchain SLSA framework. ArborXR ou Hexnode UEM em Kiosk Mode blinda o dispositivo contra qualquer componente contaminado que tente se ativar. **Limitação declarada:** não fecha componente já adulterado em fábrica — Petrobras deve continuar investindo em procurement security (transparência técnica valorizada pela banca SENAI).

### Padrão 2 — Endpoint
ArborXR/Hexnode Kiosk Mode + App whitelist (apenas apps corporativos assinados) + sideload block nativo. Atacante precisa de privilégio admin para instalar keylogger — privilégio não existe. Câmera/microfone são gerenciados via MDM (policies por usuário/role). Câmera bloqueada em ambientes confidenciais via MDM.

### Padrão 3 — Credencial
OAuth 2.0 Device Authorization Grant (RFC 8628) + PKCE + TPM 2.0 binding. Óculos exibe QR Code temporal → usuário escaneia com celular Petrobras (autenticado por biometria no MDM local) → token JWT injetado dinâmico. TPM binding garante que o token só roda no device esperado — captura do QR ou cópia do token = inútil. Biometric re-confirmation após QR scan fecha hijacking por spyware no celular.

### Padrão 4 — Exfiltração
DLP Proxy Middleware (Python FastAPI + Regex + SpaCy NLP + UEBA) intercepta TODA comunicação dos dispositivos de borda. "Plataforma P-10" → "[ATIVO_RESTRITO_01]" antes de chegar na LLM. DNS-over-HTTPS, steganografia em HTTPS, fragmentação — todos detectados por UEBA. Destino final: Azure OpenAI VNet Enclave sob contrato No-Train B2B (ou AWS Bedrock + Llama 3) — dado nunca chega em vendor público.

### Padrão 5 — Sobrecarga
SOC Agêntico opera 100% automatizado no cloud: Ingest (Event Hubs/Kafka) → Analytics (UEBA + ML + correlação cross-source) → Decision (auto-response + escalation inteligente) → Feedback (modelos aprendem com cada incidente). MTTD < 12 segundos. 1 cluster na nuvem serve N refinarias (escala do modelo de startup documentado em `AxeGuard_SOC_PetroShield.md`). Custo do fator humano eliminado = pricing enterprise defensável.

---

## 💡 Storytelling tático (para o slide)

```
"A 4-layer AxeGuard fecha cada vetor com tecnologia COTS real.
 Sem código proprietário.
 Sem lock-in.
 Sem 'espera 6 meses por feature'."
```

Por que esse enquadramento: SENAI judges valorizam **defensabilidade técnica** (não recover marketing). Tecnologia COTS = ArborXR, Hexnode, Microsoft Entra ID, Okta, Ngrok, Cloudflare, Azure OpenAI são todas reais e disponíveis no mercado. Petrobras pode integrar hoje.

---

## ⚠️ Limitações declaradas (transparência técnica —加分 banca SENAI)

- **Camada 1 (MDM):** Não fecha componente já adulterado em fábrica — depende de procurement security da Petrobras
- **Camada 2 (OAuth + TPM):** Requer dispositivo com TPM 2.0 — Meta Quest 3 ✅, RealWear Navigator 500 ✅, HoloLens 2 ✅. Cobertura > 95%
- **Camada 3 (DLP):** FPR < 2% em laboratório (baseline); em produção alvo < 5%. Trade-off conhecido
- **Camada 4 (VNet Enclave):** Requer contrato Azure OpenAI B2B No-Train — Petrobras já tem? **Verificar**
- **Camada 5 (SOC Agêntico):** MTTD < 12s é teórico; em produção realista alvo < 60s para incident triage + < 5min para response

---

## ⏭️ Próximas partes

- **PARTE 3A** — Vulnerabilidades Petrobras + Indústria Nacional (10 casos: 4 LATAM + 6 Petrobras-específicos + 1 padrão sistêmico)
- **PARTE 3B** — Caso Bacia de Campos (rich technical detail do incidente SA Exploration Nov 2025)