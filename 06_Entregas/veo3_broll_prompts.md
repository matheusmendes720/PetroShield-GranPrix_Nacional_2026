# 🎬 Diretrizes de B-Roll Cinematico para Google VEO 3

Este documento contém a engenharia de prompts (Prompt Tuning) elaborada especificamente para o motor **Google VEO 3**. O objetivo é gerar o B-Roll hiper-realista que acompanhará cada slide do `pitch_deck_e3.html` no Grand Prix SENAI Nacional.

> [!IMPORTANT]
> **Estética Base (PetroShield Core Style):** Estilo Cyberpunk industrial, paleta "Matrix Green" (#00FF41) e "Fire Petroleum Orange" (#FF6200) contrastando com preto profundo ("Deep Void Black"). Lentes anamórficas, aberração cromática sutil e névoa volumétrica industrial.

---

## Slide 1: Hook (O Vazamento de Dados)
**Contexto do Slide:** *Vazamento de 90 GB. O vetor é um wearable.*

**Prompt VEO 3:**
> `Cinematic establishing shot, extremely precise physics. Close-up macro tracking shot of a high-tech smart watch (wearable) on the wrist of an offshore oil rig worker in a dark, rain-slicked industrial hallway. The watch screen flickers with a red glitching interface reading 'SYNC ERROR'. Suddenly, holographic data streams (neon matrix green, #00FF41) violently erupt from the watch, bleeding into the air as they are stolen. Heavy volumetric industrial smoke, anamorphic lens flares, shallow depth of field (f/1.4), ARRI Alexa 65, cinematic lighting, dramatic shadows, 4k ultra-realistic texture on the worker's fire-retardant suit (petroleum orange, #FF6200). Subtle camera shake.`

---

## Slide 2: Problema O&G (A Superfície Expandida)
**Contexto do Slide:** *Milhares de vendors, IAs, Realidade Mista em FPSOs e Refinarias.*

**Prompt VEO 3:**
> `First-person Point of View (POV) looking through an ultra-futuristic Mixed Reality (XR) engineering headset (smart glasses) deep inside a complex offshore oil refinery. The camera slowly pans across highly intricate, hyper-realistic metal pipes, industrial valves, and towering oil extraction structures. Overlaying the physical pipes is a brilliant, glowing holographic HUD layer (cyberpunk Neon Matrix Green, #00FF41, and Warning Amber, #FF9500) tracking real-time pressure data, flow diagnostics, and fluid dynamics in 3D space. Intense volumetric lighting cutting through thick industrial steam, anamorphic lens flares from cinematic practical lighting, incredibly detailed textures on brushed steel and condensation. Rack focus from the holographic projection dropping back to the endless labyrinth of pipes in the distance. Shot on ARRI Alexa 65, 35mm lens, f/1.8, 8k resolution, masterful sci-fi cinematic composition.`

---

## Slide 3: Arquitetura AxeGuard (AI-SOC na Borda)
**Contexto do Slide:** *Zero-trust, DLP, tempo de interceptação ultrabaixo.*

**Prompt VEO 3:**
> `Inside a hyper-modern, darkened server room simulating an 'Edge' computing hub. In the center, a glowing glass cube representing the AxeGuard Middleware intercepts a fast-moving physical beam of red malware light. As the red light hits the cube, it freezes mid-air, shatters like glass in extreme slow-motion (Phantom Flex 4k style, 1000fps), and transforms into harmless, glowing green binary streams (matrix green, #00FF41). Volumetric lighting, rack focus, extremely detailed particle physics, reflections on the polished black floor, high contrast, cinematic commercial style.`

---

## Slide 4: Visual Hyperscaling (O Efeito Multi-Tenant)
**Contexto do Slide:** *Vacina sendo forjada em segundos, protegendo dezenas de plataformas simultaneamente.*

**Prompt VEO 3:**
> `Time-lapse style wide shot mapping the dark Brazilian coastline from lower orbit (satellite perspective). A violent digital explosion of red neon happens at one pinpoint (Bacia de Campos). Instantly, a wave of bright, protective digital forcefield (neon matrix green, #00FF41) ripples outward like a shockwave across the ocean, covering 100+ other glowing offshore platforms down to Santos. The forcefield crystallizes over each platform with satisfying geometric precision. Photorealistic fluid dynamics for the clouds and ocean, glowing technological overlay, cinematic lighting, epic soundtrack feel, 8k resolution macro-orbit view.`

---

## Slide 5: Business Impact (Métricas C-Level)
**Contexto do Slide:** *Proteção de bilhões em CAPEX/OPEX e Compliance de forma invisível.*

**Prompt VEO 3:**
> `Smooth Steadicam push-in inside a luxurious, dimly lit corporate C-level boardroom with a panoramic view of a cyberpunk metropolis at night. On the massive mahogany table, a sleek holographic projector displays the AxeGuard dashboard. A sharply dressed executive gestures, and the hologram expands showing upward-trending financial charts in bright green (#00FF41) and 'US$ 25M SAVED' in crisp typography. The atmosphere is calm, secure, and highly sophisticated. Depth of field isolates the hologram, high-end corporate sci-fi aesthetic, soft key lighting, 24fps motion blur.`

---

## Slide 6: Encerramento (PetroShield)
**Contexto do Slide:** *O poder da segurança agêntica.*

**Prompt VEO 3:**
> `Super macro slow-motion shot of a heavy, forged titanium shield emblem (PetroShield logo) dropping onto a dark, obsidian surface. Upon impact, a ripple of intense, matrix-green electrical energy bursts outward from the shield's edges, illuminating the pitch-black void. The metal shows micro-scratches and hyper-realistic industrial wear. Intense rim lighting, anamorphic lens flares from the sparks, purely cinematic dramatic climax, high contrast, visually striking, photorealistic 8k.`

---

### Dicas de Parâmetros Extras (Tuning VEO 3)
* Para garantir a fidelidade das cenas, enfatize: *"Do not render text, render pure visuals"*. Elementos como "100+", "US$ 25M" ou labels devem ser compostos posteriormente via Motion Graphics (After Effects/Premiere), focando o VEO estritamente na *física cinemática, fotografia e iluminação volumétrica*.
