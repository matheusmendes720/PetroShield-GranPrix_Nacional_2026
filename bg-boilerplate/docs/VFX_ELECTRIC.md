# ⚡ VFX Spec: The Enforcer (Electricity & Runes)

Este documento especifica a implementação dos arcos voltaicos e runas de dados do segundo escudo.

## 1. Composição Visual
*   **Arcos Elétricos:** Raios rápidos que viajam pelo gume dos machados.
*   **Runas Digitais:** Padrões rúnicos no cabo e base do escudo que emitem pulsos binários de luz.
*   **Cor Dominante:** Ciano Terminal (#00FFFF) e Verde Neon (#00FF41).

## 2. Abordagem de Implementação (Engineering)
Utilizaremos **SVG Line Drawing** para os raios:

### Lógica de "Lightning Bolt":
1.  Definir 4 caminhos (`<path>`) em ziguezague ao redor das lâminas.
2.  Aplicar `stroke-dasharray` para segmentar a linha.
3.  Animar o `stroke-dashoffset` com funções de tempo irregulares (usando JavaScript ou `keyframes` com `step`).
4.  **O Segredo:** Aplicar um filtro de `feGaussianBlur` e `feColorMatrix` para criar o efeito de "luz de plasma" concentrada.

## 3. Comportamento no Hover
1.  **Runas Ativas:** As runas gravadas no metal mudam de opacidade 0.2 para 1.0 em um efeito de "flicker" (piscada rápida).
2.  **Electric Overload:** Os arcos elétricos tornam-se maiores e saltam para fora do limite do escudo (overflow: visible).
3.  **Haptic Visuals:** O movimento do mouse altera a frequência do tremor (jitter) dos raios.
