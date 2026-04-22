# 📜 PetroShield: Master Technical Specification (v1.0)

Este documento estabelece os padrões técnicos, arquiteturais e visuais definitivos para a interface PetroShield.

---

## 1. Arquitetura de Sistemas (Global)

### 1.1. Camadas de Renderização (Stacking Order)
A interface é composta por uma pilha de 5 camadas lógicas para garantir profundidade e performance:
1.  **L0 (Deep Canvas):** `CircuitBackground` (150+ nós, 7 camadas de parallax).
2.  **L1 (Underlay):** Gradientes dinâmicos por quadrante e Vinheta Global.
3.  **L2 (UI Interface):** `TopBanner` e `ShieldGrid` (O conteúdo principal).
4.  **L3 (Overlay VFX):** Faíscas (Sparks), Arcos Elétricos e Chamas (transprent alpha).
5.  **L4 (Post-Process):** Glitches aleatórios, Scanlines de 360 frames e Chromatic Aberration no movimento.

### 1.2. Performance & Pipeline
*   **Rendering:** Prioridade total para a GPU. Uso de `will-change: transform, opacity`.
*   **Asset Logic:** Imagens em **WebP 2.0** (Lossless Alpha). Vídeos de partículas em **WebM (VP9/Alpha)**.
*   **Frame Rate Target:** 60 FPS constante. Loops de animação fora da Main Thread onde possível.

---

## 2. Módulo 0: CircuitBackground (The Digital Void)

O background deve simular um mainframe "vivo".
*   **Sistema de Nós:** 150 instâncias com `depth` variável (0.1 a 2.0).
*   **Conexões PCB:** Trilhas ortogonais (em "L") com efeito de bloom neon.
*   **Interatividade:** Proximidade do mouse ativa o modo "Magnetic Attraction" e altera o glow para Cyan (#00FFFF).
*   **Idle Mode:** Após 3s de inatividade, entra em "Breathing Mode" (pulsação lenta e redução de 50% na velocidade).

---

## 3. Módulo 1: TopBanner (The Mainframe Header)

Painel metálico de comando centralizado no topo.
*   **Visual:** Metal negro escovado com ranhuras de PCB em baixo relevo.
*   **Fire Borders:** Animação de chamas reais nas bordas (mix-blend-mode: screen).
*   **Logo Logic:** 
    *   *Exterior:* Webkit-Text-Stroke Verde Neon com Shadow Blur de 20px.
    *   *Interior:* Gradiente dinâmico de brasa laranja pulsante.

---

## 4. Módulo 2: Interactive Relics (The Shields)

As três interfaces de ação principais.

### 4.1. Física Cinemática (Motion Spec)
*   **Engine:** `Framer Motion` (Physics-based).
*   **Massa:** 1.2 | **Damping:** 25 | **Stiffness:** 120.
*   **Gyro-Tracking:** O escudo inclina `±15°` no eixo Y e `±10°` no eixo X acompanhando a posição real do mouse dentro do card.
*   **Fresnel Glare:** Camada de reflexo (Overlay 10%) que se move na direção oposta à inclinação para simular luz física em metal.

### 4.2. Especificações de Identidade Visual (VFX)

| Shield | Nome | Identidade Visual | VFX Ativo (Hover) |
| :--- | :--- | :--- | :--- |
| **01** | **The Beacon** | Metal Martelado | Fogo Verde-Neon + Fuligem Ascendente |
| **02** | **The Enforcer** | Rúnico/Gótico | Arcos Voltaicos Ciano + Runas Piscantes |
| **03** | **The Vault** | Fibra de Carbono/PCB | Fluxo de Dados nas Trilhas + Núcleo de Fusão |

---

## 5. Módulo 3: Post-Processing & Glitch Engine

Sistema de "falhas de sistema" para reforçar o mood cyberpunk.
*   **Chromatic Aberration:** Ativado apenas quando `mouseVelocity > 100px/frame`. Deslocamento máximo de 6px nos canais R e B.
*   **Glitch Displacement:** Faixas horizontais aleatórias (0.2% de chance por frame) que deslocam a imagem original lateralmente em ±30px por 1 único frame.
*   **Scanlines:** Overlay de baixa opacidade (1.2%) que percorre a tela verticalmente a cada 6 segundos.

---

## 6. Engineering Requirements (Checklist de Execução)
- [ ] Implementar `Custom Hook` para rastreamento de posição do mouse relativa ao centro do card.
- [ ] Configurar `SVG Filters` globais para distorção de fogo e eletricidade.
- [ ] Validar carregamento assíncrono de assets pesados com `Skeleton Screens` metálicos.
- [ ] Garantir `Touch-support` (fallback de inclinação para dispositivos móveis via acelerômetro ou toque).
