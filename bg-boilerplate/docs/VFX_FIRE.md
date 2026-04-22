# 🔥 VFX Spec: The Beacon (Fire & Fluids)

Este documento especifica a implementação das chamas verde-neon e o brilho vulcânico do primeiro escudo.

## 1. Composição Visual
*   **Fogo Primário:** Chama verde-neon vibrante (#00FF41).
*   **Fogo Secundário (Núcleo):** Chama laranja incandescente (#FF6200).
*   **Efeito de Fuligem:** Pequenas faíscas (sparks) que sobem e desaparecem.

## 2. Abordagem de Implementação (Engineering)
Para evitar o uso de shaders complexos de WebGL em cada botão, utilizaremos **SVG Filter Displacement**:

### O Algoritmo de Turbulência:
```xml
<filter id="fire-distortion">
  <feTurbulence type="fractalNoise" baseFrequency="0.05" numOctaves="3" seed="1">
    <animate attributeName="seed" from="1" to="100" dur="10s" repeatCount="indefinite" />
  </feTurbulence>
  <feDisplacementMap in="SourceGraphic" scale="20" />
</filter>
```
Este filtro deve ser aplicado a uma div com gradientes radiais sobrepostos. A animação do `seed` cria o movimento orgânico de "fluido ardente".

## 3. Comportamento no Hover
1.  **Glow Expansion:** O `filter: drop-shadow` do fogo aumenta de 10px para 40px.
2.  **Particle Density:** O sistema de faíscas (Sparks) dobra a taxa de emissão por segundo.
3.  **Heat Distortion:** O `scale` do `feDisplacementMap` aumenta para simular ar quente distorcendo a imagem.
