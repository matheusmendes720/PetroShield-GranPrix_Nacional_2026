# EVOLUTION.md — CircuitBackground v2.0 Roadmap

> Especificação de evolução do background animado `CircuitBackground` para o boilerplate PetroShield.
> **Status:** `IMPLEMENTED` ✅

---

## 1. Visão Geral

A versão 1.0 do `CircuitBackground` era um canvas 2D com:
- Chuva Matrix sutil
- Nodos de circuito com conexões em L
- Partículas flutuantes
- Parallax direto (1:1) com posição do mouse

A **v2.0** transforma o canvas em um **ecossistema interativo reativo** com múltiplas camadas de profundidade, física suavizada, e feedback táctil/visual ao movimento do cursor.

---

## 2. Camadas do Sistema (Layers)

| Layer | Nome | Z-Depth | Descrição |
|-------|------|---------|-----------|
| 0 | `VOID` | 0.0 | Fundo puro com gradiente dinâmico baseado no quadrante do mouse |
| 1 | `MATRIX_RAIN` | 0.15 | Chuva de caracteres com parallax profundo e opacidade baixa |
| 2 | `GRID_FIELD` | 0.35 | Grade de circuito hexagonal/ortogonal sutil |
| 3 | `CIRCUIT_NODES` | 0.60 | Nodos principais com conexões em L e pacotes de dados |
| 4 | `PARTICLES` | 0.85 | Partículas nano com glow e comportamento de vida |
| 5 | `MOUSE_TRAIL` | 1.00 | Rastro de energia que segue o cursor com easing |
| 6 | `RIPPLES` | 1.00 | Ondas de perturbação originadas por cliques |
| 7 | `SCANLINES` | 1.00 | Efeitos de scanline, vignette e bloom de overlay |

---

## 3. Sistema de Parallax Responsivo

### 3.1 Smooth Tracking (Lerp)
- O mouse não é mais lido diretamente
- `mouse.smoothX` e `mouse.smoothY` interpolam com fator `0.08` por frame
- Cria movimento "pesado" e fluido, como líquido

### 3.2 Multi-Layer Coefficients
```
Layer 0 (Void):       0x  parallax  — gradiente muda por quadrante, não por offset
Layer 1 (Matrix):     4x  parallax  — movimento lento, fundo distante
Layer 2 (Grid):       12x parallax  — grade média
Layer 3 (Nodes):      25x parallax  — nodos principais
Layer 4 (Particles):  15x parallax  — partículas médias
Layer 5 (Trail):      0x  parallax  — fixo na tela, segue cursor absoluto
```

### 3.3 Perspective Tilt
- O canvas inteiro aplica uma micro-rotação 3D simulada via offset dos layers
- Quando mouse está no canto superior-esquerdo, layers inferiores "afundam" para baixo-direita
- Efeito sutil de "janela para outra dimensão"

---

## 4. Interatividade Avançada

### 4.1 Proximity Glow (Campo de Força do Cursor)
- Nodos dentro de `180px` do cursor ganham:
  - Raio aumentado em até `2.5x`
  - Alpha elevado para `0.9`
  - Cor temporária shift para ciano (`#00FFFF`)
- Linhas de conexão próximas ao cursor ficam mais grossas (`1.5px`) e mais opacas

### 4.2 Magnetic Nodes
- Nodos muito próximos ao cursor (`< 100px`) são levemente atraídos
- Força de atração é inversamente proporcional à distância
- Ao sair da zona de influência, nodos retornam à trajetória original com elasticidade

### 4.3 Data Packets (Pacotes de Dados)
- Aleatoriamente, uma conexão ativa entre dois nodos "transmite" um pacote
- Pacote é um pequeno ponto branco/ciano que percorre a linha em L
- Velocidade proporcional à "pressão" do sistema (mouse velocity)

### 4.4 Mouse Trail
- Cursor deixa rastro de `15` pontos de energia
- Cada ponto tem vida decay e tamanho decay
- Cor alterna entre verde neon e laranja com base na velocidade do mouse
- Alta velocidade = rastro mais quente (laranja)

### 4.5 Click Ripples
- Ao clicar, emana uma onda circular de perturbação
- A onda:
  - Expande em raio por `~2s`
  - Afeta nodos em seu caminho (empurra-os levemente)
  - Deixa linhas temporariamente mais brilhantes
  - Desaparece com easing suave

---

## 5. Behaviors Procedurais

### 5.1 Idle Breathing
- Se o mouse permanece parado por `> 3s`:
  - Sistema entra em modo "respiração"
  - Nodos pulsam em sincronia global (onda senoidal)
  - Partículas reduzem velocidade
  - Matrix rain fica mais lenta
- Ao mover o mouse, sistema "acorda" instantaneamente

### 5.2 Velocity Response
- Velocidade do cursor modula parâmetros globais:
  - `> 500px/s`: Partículas aceleram, trail fica mais denso
  - `> 1000px/s`: Efeito "túnel" — linhas de conexão alongam-se na direção do movimento
  - `< 50px/s`: Modo calmo, baixa energia

### 5.3 Dynamic Color Palette
- O fundo aplica um gradiente sutil que muda conforme o quadrante do mouse:
  - Superior-esquerdo: Verde puro (default)
  - Superior-direito: Ciano/Água
  - Inferior-esquerdo: Âmbar/Laranja
  - Inferior-direito: Magenta/Rosa sutil
- A mudança é interpolada (lerp) por frame, nunca abrupta

---

## 6. Otimizações de Performance

| Técnica | Implementação |
|---------|---------------|
| **Responsive Density** | `devicePixelRatio` considerado; menos partículas em telas `< 768px` |
| **Frame Budget** | Cada layer pode ser desabilitado se `deltaTime > 20ms` |
| **Spatial Hash** | Nodos usam grid espacial 2D para O(1) lookup de vizinhos (em vez de O(n²)) |
| **Offscreen Cache** | Grade de fundo (layer 2) é pré-renderizada em offscreen canvas e apenas deslocada |
| **RequestAnimationFrame** | Loop com `timestamp` nativo para deltaTime consistente |

---

## 7. API Interna (Hooks de Canvas)

O componente foi reestruturado com funções utilitárias internas:

```typescript
// Sistema de easing
function lerp(start: number, end: number, factor: number): number
function smoothDamp(current: number, target: number, velocity: number, smoothTime: number): number

// Física 2D
function dist(a: Vector2, b: Vector2): number
function attract(node: Node, target: Vector2, strength: number): void

// Render helpers
function drawGlow(ctx: CanvasRenderingContext2D, x: number, y: number, radius: number, color: string): void
function drawCircuitLine(ctx: CanvasRenderingContext2D, a: Vector2, b: Vector2, style: LineStyle): void
```

---

## 8. Tokens CSS Adicionais

Novas variáveis adicionadas ao `index.css`:

```css
:root {
  --cursor-glow: rgba(0, 255, 255, 0.4);
  --ripple-color: rgba(0, 255, 65, 0.25);
  --packet-color: #ffffff;
  --depth-far: 0.2;
  --depth-mid: 0.6;
  --depth-near: 1.0;
}
```

---

## 9. Changelog

### v2.0 — 2026-04-21
- [x] Parallax multi-camada com coeficientes independentes
- [x] Smooth mouse tracking (lerp 0.08)
- [x] Proximity glow + magnetic nodes
- [x] Mouse trail com velocity color mapping
- [x] Click ripples com perturbação física
- [x] Data packets viajando nas conexões
- [x] Idle breathing mode (> 3s parado)
- [x] Dynamic gradient por quadrante do mouse
- [x] Offscreen cache da grade de fundo
- [x] Vignette, scanlines e film grain overlay
- [x] Elastic return + ripple disturbance em nodos

---

*Documento gerado por agente de IA. Alterações devem refletir tanto neste MD quanto no código fonte.*
