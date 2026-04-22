# ⚖️ Motion Engineering: Cinematic 3D Physics

Para alcançar o "feel" profissional de objetos 3D reais, vamos implementar três pilares de física: **Inércia Amortecida**, **Oclusão Ambiental Dinâmica** e **Efeito Specular Fresnel**.

## 1. O Algoritmo de Movimento (Smooth Lerp & Springs)
A animação "seca" (linear ou ease-in-out simples) é o que causa o aspecto artificial. Objetos reais têm peso.

### Especificação da Mola (Framer Motion):
*   **Mass (Massa):** `1.2` (Dá a sensação de que o escudo é feito de metal pesado, não plástico).
*   **Stiffness (Rigidez):** `120` (Uma mola mais "relaxada" que permite um balanço orgânico).
*   **Damping (Amortecimento):** `25` (Crucial para evitar que o objeto trema como uma mola de brinquedo. O damping alto faz o movimento "morrer" de forma suave e elegante).

### Perspectiva e Ponto Focal:
*   `perspective: 2000px`: Aumentar a distância da perspectiva torna a distorção 3D mais sutil e realista (telephoto lens feel), evitando o efeito "olho de peixe" de perspectivas curtas (500px-800px).

---

## 2. Dynamic Ambient Occlusion (A Sombra Viva)
Em objetos reais, a sombra não apenas cresce; ela se move e muda de densidade com base na inclinação.

*   **Shadow Translation:** Quando o escudo inclina para a esquerda (`rotateY: -15deg`), a sombra deve se deslocar levemente para a direita (`translateX: 10px`).
*   **Softness Mapping:** Quanto mais alto o escudo "pula" (Z-axis), maior deve ser o `blur-radius` da sombra e menor a sua `opacity`. Isso simula a dispersão da luz ambiente.

---

## 3. Fresnel Glare (O Reflexo Óptico)
Este é o "toque de mestre" que vende a ilusão de 3D. Objetos metálicos refletem a luz de forma diferente dependendo do ângulo de visão.

*   **Layer:** Uma camada de gradiente radial branco/transparente com `mix-blend-mode: overlay` e opacidade 5-10%.
*   **Logic:** O centro desse gradiente deve se mover na direção **oposta** à inclinação do escudo.
    *   *Se o escudo vira para a direita, o reflexo corre para a esquerda.*
    *   Isso simula o comportamento da luz batendo em uma superfície metálica curva.

---

## 4. Micro-Interações de Velocidade
*   **Velocity Overshoot:** Ao entrar no hover rapidamente, o escudo deve passar levemente do ponto final e "assentar" (settle) suavemente. Isso é controlado nativamente pelas propriedades de mola citadas acima.
*   **Tilt Tracking:** O movimento não deve ser um giro fixo de 360°, mas sim uma inclinação constante que segue a posição exata do cursor dentro do card (Gyroscope effect).

---

## 🛠️ Resumo Técnico para Implementação:
| Propriedade | Valor Sugerido | Objetivo |
| :--- | :--- | :--- |
| `rotateY` Range | -15° a +15° | Inclinação baseada na posição X do mouse. |
| `rotateX` Range | -10° a +10° | Inclinação baseada na posição Y do mouse. |
| `scale` | 1.08 | Aumento sutil para evitar clipping. |
| `transition.mass` | 1.2 | Peso metálico. |
| `transition.damping`| 25 | Parada suave (Professional Ease). |
