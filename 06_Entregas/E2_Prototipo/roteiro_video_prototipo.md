# 🎬 [E2] Roteiro: Vídeo do Protótipo Conceitual (2 minutos)

> **Projeto:** AxeGuard / PetroShield  
> **Entrega:** Protótipo Conceitual + Vídeo Explicativo (até 2 min)  
> **Tom:** Técnico-cinematográfico, cyberpunk industrial, com dados concretos.

---

## Estrutura do Vídeo (120 segundos)

| Tempo | Seção | Conteúdo Visual | Narração |
|-------|-------|-----------------|----------|
| 00:00-00:08 | **Hook** | Splash screen do dashboard com glitch effect e música eletrônica sutil. | "Ransomware não dorme. E a sua defesa não pode depender de um antivirus de 2019." |
| 00:08-00:18 | **O que é** | Transição para o dashboard principal. Mostrar métricas e topologia do grafo. | "Este é o AxeGuard: um middleware de cibersegurança adaptativo, construído para proteger a indústria brasileira na borda." |
| 00:18-00:45 | **Cena 2: DLP em Ação** | Terminal log rolando em tempo real. Highlight nos nós `supervisor → dlp_edge → clevel_reporter`. Métricas de leaks prevenidos pulando. | "Um operador no HoloLens pergunta à IA sobre a Plataforma P-93 e cita uma senha. Em 23 milissegundos, o DLP Edge identifica três entidades sensíveis, mascara os dados e libera a query sanitizada. Zero vazamento." |
| 00:45-01:15 | **Cena 3: Ataque Industrial OT** | Terminal log mostrando detecção de Modbus FC16. Nós `dlp_edge → intel_cloud → fleet_vaccinator` acendendo em laranja. Broadcast da vacina para edge nodes. | "Agora, imagine um comando SCADA disfarçado de prompt de IA. Modbus FC16 detectado. Threat score: 0.98. O sistema não apenas bloqueia: ele gera uma vacina de segurança e propaga para toda a frota — 13 de 14 nodes em segundos. Downtime evitado: 580 mil reais." |
| 01:15-01:40 | **Cena 4: Vendor Risk Cascade** | Highlight nos nós `supervisor → vendor_cascade → fleet_vaccinator`. Mostrar sessões suspensas e compliance ledger. | "E se um vendor de 4 bilhões de reais tem credenciais vazadas na dark web? O AxeGuard suspende 12 sessões XR automaticamente, revoga tokens OAuth e abre ticket de compliance ANPD. Antes do seu café esfriar." |
| 01:40-01:55 | **Sumário Executivo** | Scroll até o final do terminal com o relatório C-Level. Cards de métricas finais. | "O resultado: incidentes neutralizados, faturamento protegido e conformidade LGPD garantida. Tudo por uma fração do custo de um SOC tradicional." |
| 01:55-02:00 | **Call to Action** | Voltar para splash screen. Mostrar hashtag/selo PetroShield. | "AxeGuard. O porto seguro digital da indústria baiana." |

---

## 🎙️ Narração Completa (Português — para TTS/IA)

```text
Ransomware não dorme. E a sua defesa não pode depender de um antivirus de 2019.

Este é o AxeGuard: um middleware de cibersegurança adaptativo, construído para proteger a indústria brasileira na borda.

[PAUSA 1s]

Cena um: DLP em Ação. Um operador no HoloLens pergunta à IA sobre a Plataforma P-93 e cita uma senha corporativa. Em vinte e três milissegundos, o DLP Edge identifica três entidades sensíveis, mascara os dados e libera a query sanitizada. Zero vazamento. Três leaks prevenidos.

[PAUSA 1s]

Cena dois: Ataque Industrial. Um comando SCADA disfarçado de prompt de IA. Modbus FC16 detectado. Threat score: zero vírgula noventa e oito. O sistema não apenas bloqueia: ele gera uma vacina de segurança e propaga para toda a frota — treze de quatorze nodes em segundos. Downtime evitado: quinhentos e oitenta mil reais.

[PAUSA 1s]

Cena três: Vendor Risk Cascade. Um vendor de quatro bilhões de reais tem credenciais vazadas na dark web. O AxeGuard suspende doze sessões XR automaticamente, revoga tokens OAuth e abre ticket de compliance ANPD. Antes do seu café esfriar.

[PAUSA 1s]

O resultado: oito incidentes neutralizados, frota vacinada a mais de noventa e dois por cento, e conformidade LGPD garantida. Tudo por uma fração do custo de um SOC tradicional.

AxeGuard. O porto seguro digital da indústria baiana.
```

---

## 🎵 Sugestões de Trilha/Áudio

- **Música:** Cyberpunk ambient / industrial tech (sem voz). Sugestões: buscar "cyberpunk ambient no copyright" no YouTube Audio Library ou usar geradores como Udio/Suno.
- **SFX:** 
  - Glitch digital no início (0:00)
  - Beep de terminal a cada log de ação
  - Whoosh de transição entre cenas
- **Narração:** Gerar com ElevenLabs (voz "Rachel" ou "Adam" em português), ou usar TTS do CapCut/Clipchamp.

---

## 🛠️ Checklist de Gravação

- [ ] Abrir `scripts/dlp_proxy/static/dashboard.html` em tela cheia (F11) no Chrome/Edge.
- [ ] Garantir que o zoom esteja em 100% para legibilidade.
- [ ] Desativar notificações do sistema.
- [ ] Usar OBS Studio ou ScreenRec para capturar tela em 1920x1080, 30fps.
- [ ] Gravar narração separadamente (melhor qualidade) e sincronizar no editor.
- [ ] Exportar em MP4, H.264, tamanho final menor que 100MB.

---

## 📁 Arquivo do Protótipo

- **Dashboard:** `scripts/dlp_proxy/static/dashboard.html`
- **Instruções de execução:** Basta abrir o arquivo HTML diretamente no navegador. Não requer backend. O Auto-Play inicia sozinho após 6 segundos na splash screen.
