# 🎬 Guia de Produção de Vídeo: E2 + E3

> **Ferramentas recomendadas:** OBS Studio (gravação), CapCut ou Clipchamp (edição), ElevenLabs/CapCut TTS (narração), Google VEO 3 ou Midjourney (renders/imagens em movimento).

---

## 1. Gravando o Protótipo (E2 — 2 min)

### Passo a passo

1. **Abra o dashboard:**
   ```
   scripts/dlp_proxy/static/dashboard.html
   ```
   Dê duplo clique no arquivo. Ele abrirá no navegador padrão.

2. **Entre em tela cheia:**
   Pressione `F11` no Chrome/Edge.

3. **Aguarde o Auto-Play:**
   - A splash screen aparece automaticamente.
   - Após ~6 segundos, o dashboard inicia e as 8 cenas começam a rodar sozinhas.

4. **Grave a tela com OBS Studio:**
   - Baixe em: https://obsproject.com
   - Configure: `1920x1080`, 30fps, saída MP4.
   - Fonte: "Display Capture" ou "Window Capture" do navegador.
   - Dica: desligue a webcam para gravar só a tela.

5. **Corte no editor:**
   - Remova o início se necessário (antes da splash screen).
   - Foque nas 3 cenas principais: **Cena 2 (DLP)**, **Cena 3 (OT)** e **Cena 4 (Vendor)**.
   - Acelere trechos sem ação (ex: pausas entre logs) para caber em 2 minutos.

6. **Adicione narração:**
   - Use o roteiro em `06_Entregas/E2_Prototipo/roteiro_video_prototipo.md`.
   - Grave com celular ou gere por IA (ElevenLabs).
   - Sincronize os picos de áudio com os momentos de ação no terminal.

---

## 2. Produzindo o Pitch (E3 — 3 min)

### Opção A: Montagem Rápida no Canva

**Ideal se você não tem experiência com edição avançada.**

1. Crie um projeto de vídeo em `1920x1080`.
2. Use o storyboard do roteiro em `06_Entregas/E3_Pitch/roteiro_pitch_youtube.md`.
3. Faça upload das imagens da pasta `design/`.
4. Use as transições "Zoom" e "Fade" entre cenas.
5. Adicione texto animado para os dados-chave (ex: "R$ 580K evitados").
6. Exporte em MP4.

### Opção B: Edição Profissional no CapCut (Recomendado)

**Melhor controle de timing, legendas automáticas e TTS integrado.**

1. Importe todos os assets:
   - Screen capture do dashboard
   - Imagens de `design/`
   - Trilha sonora
2. Crie uma timeline com 7 faixas principais (uma por bloco do pitch).
3. Use a ferramenta **"Auto captions"** para gerar legendas em português.
4. Ajuste o volume da música para não cobrir a narração.
5. Adicione efeitos de som (SFX) nos momentos de impacto.
6. Exporte em `1080p`, 30fps.

### Opção C: Usando Google VEO 3 para Cenas Cinematográficas

**Se você tiver acesso ao VEO 3, pode gerar clips de IA para o pitch.**

**Prompts sugeridos para VEO 3:**

```
Cinematic wide shot of a futuristic industrial control room in Brazil.
Neon green and orange holographic security interfaces float in the air.
Operators wear augmented reality glasses. Cyberpunk aesthetic.
```

```
Aerial drone shot of an oil refinery at night. Glowing green circuit patterns
overlay the pipelines, representing an AI-powered security mesh.
Dark, moody, cinematic lighting.
```

```
Close-up of a digital world map of Brazil. Green dots light up one by one
across industrial regions. Cyberpunk UI style. High tech, clean, futuristic.
```

**Como integrar no vídeo:**
- Gere clips de 4-8 segundos no VEO 3.
- Baixe em MP4.
- Insira entre as cenas de screen capture no editor.
- Use transição "Cross Dissolve" para suavizar.

---

## 3. Gerando Narração com IA

### Opção 1: ElevenLabs (Mais natural)

1. Acesse: https://elevenlabs.io
2. Cole o roteiro do pitch ou do protótipo.
3. Vozes recomendadas em PT-BR:
   - **Rachel** (clara, corporativa)
   - **Adam** (grave, autoridade técnica)
4. Ajuste `Stability: 0.45` e `Clarity + Similarity: 0.75`.
5. Gere o áudio em MP3 e importe no editor.

### Opção 2: CapCut TTS (Gratuito e rápido)

1. No CapCut, vá em `Text > Text to Speech`.
2. Selecione a voz em português mais adequada (geralmente "Narração 1" ou "Narração 2").
3. Cole o texto do roteiro.
4. Ajuste a velocidade para `1.0x` ou `1.1x` se necessário.

---

## 4. Checklist Final Antes do Upload

- [ ] Vídeo do protótipo tem **até 2 minutos**.
- [ ] Pitch no YouTube tem **até 3 minutos**.
- [ ] Ambos têm **legendas em português**.
- [ ] Áudio está claro e música não ofusca a narração.
- [ ] Não há informações pessoais reais ou dados sensíveis reais.
- [ ] O link do protótipo (se mostrado) funciona.

---

## 5. Upload no YouTube (E3)

1. Acesse: https://youtube.com/upload
2. Selecione o arquivo MP4 do pitch.
3. **Título:** `AxeGuard | Pitch GP SENAI 2026 — Protegendo a Indústria Brasileira`
4. **Descrição:**
   ```
   AxeGuard é o middleware de cibersegurança adaptativo da PetroShield,
   projetado para proteger PMEs industriais contra ransomware, vazamento de
   dados e comandos OT maliciosos — em tempo real, na borda.

   🛡️ Protótipo interativo: [link do protótipo ou repositório]
   🏆 Grand Prix SENAI Nacional 2026
   ```
5. **Visibilidade:** Selecione **"Não listado"**.
6. **Idioma e legendas:** Defina como Português (Brasil).
7. Clique em **Publicar** e copie a URL.

---

## 6. Entrega na Plataforma SENAI

- **E2:** Anexe o vídeo do protótipo (ou link, se a plataforma permitir) + indique o arquivo `dashboard.html`.
- **E3:** Cole a URL do YouTube Unlisted no campo correspondente.

---

## 📞 Dúvidas Frequentes

**P: Não consigo abrir o dashboard. Dá tela em branco.**  
R: Use Chrome ou Edge atualizado. O arquivo é HTML puro, não precisa de servidor. Verifique se o zoom está em 100%.

**P: O vídeo ficou com mais de 3 minutos. E agora?**  
R: Acelere as cenas de terminal log ou corte pausas entre as falas da narração. No CapCut, use `Speed > 1.25x` em trechos longos.

**P: Não tenho acesso ao VEO 3. Alternativas?**  
R: Use as imagens estáticas da pasta `design/renders/` com o efeito "Ken Burns" (zoom/pan) no Canva ou CapCut. Fica muito cinematográfico.

**P: Posso usar música com copyright?**  
R: Não. Prefira bibliotecas no-copyright (YouTube Audio Library, Artlist, Udio, Suno) ou gere a sua.
