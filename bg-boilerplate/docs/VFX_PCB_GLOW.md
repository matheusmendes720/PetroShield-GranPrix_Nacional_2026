# 🔐 VFX Spec: The Vault (PCB Glow & Fusion Lock)

Este documento especifica a iluminação das trilhas eletrônicas e o núcleo do cadeado do terceiro escudo.

## 1. Composição Visual
*   **Data Flow:** Trilhas do circuito impresso que brilham sequencialmente.
*   **Fusion Core:** O buraco da fechadura atua como um reator termonuclear (Laranja Vibrante).
*   **Material:** Placa de fibra de carbono com reflexos especulares agressivos.

## 2. Abordagem de Implementação (Engineering)
Utilizaremos **Mask Clipping & Gradient Animation**:

### Lógica do Fluxo de Dados:
1.  **Layer 0:** Imagem do escudo com trilhas apagadas.
2.  **Layer 1 (Mask):** Um SVG mask que contém apenas o desenho das trilhas do PCB.
3.  **Layer 2 (Content):** Uma div com gradiente linear multicolorido (Cyan/Green) que se move continuamente por trás da máscara.
    *   *Resultado:* Dá a impressão de que pacotes de dados estão viajando pelas veias do escudo.

## 3. Comportamento no Hover
1.  **Core Ignition:** O brilho laranja do cadeado começa a pulsar em uma frequência mais alta (3Hz).
2.  **Circuit Activation:** A velocidade do gradiente por trás da máscara de trilhas triplica, simulando processamento intenso.
3.  **Perspective Glitch:** Ao inclinar o escudo, as trilhas devem ter um leve `offset` de paralaxe em relação ao corpo do metal, criando uma sensação de camadas internas.
