# 🛡️ PetroShield Technical Manifesto

## 1. Visão Arquitetônica
O PetroShield não é apenas um site; é uma interface de comando (Command Center). A arquitetura deve suportar alta densidade visual sem sacrificar a performance da "Main Thread".

### Camadas de Renderização (Stacking Order)
1.  **Background (Canvas 2D/WebGL):** `CircuitBackground` operando em loop contínuo.
2.  **Middle-Ground (UI Content):** Onde residem os escudos e o banner.
3.  **Foreground (Overlays):** Glitches, scanlines e vinhetas globais.

---

## 2. Requisitos de Ativos (Asset Pipeline)
Para que os escudos fiquem "surrealmente bonitos", as imagens base devem seguir estes critérios:
*   **Formato:** WebP com canal Alpha (transparência).
*   **Resolução:** Mínimo de 1024px de altura para garantir nitidez no Parallax 3D.
*   **Layering:** Cada escudo deve ser pensado em pelo menos 3 sub-camadas:
    *   **Base:** O metal/PCB (estático).
    *   **Emissive:** As partes que brilham (máscaras de luz).
    *   **VFX Layer:** Onde o fogo e os raios são injetados via código.

---

## 3. Matriz de Interatividade (The "Feel")
A interação deve ser **mecânica e pesada**, não "elástica".
*   **Damping:** Elevado (para simular inércia de metal).
*   **Stiffness:** Moderado (para evitar vibrações excessivas).
*   **Efeito Glare:** Um gradiente linear branco com opacidade 5% que atravessa o escudo no eixo X conforme o mouse se move.

---

## 4. Próximos Documentos de Detalhamento
*   `docs/VFX_FIRE.md`: Engenharia de fluidos e chamas verdes.
*   `docs/VFX_ELECTRIC.md`: Arcos voltaicos e runas de dados.
*   `docs/VFX_PCB_GLOW.md`: Iluminação de circuitos e o cadeado de fusão.
