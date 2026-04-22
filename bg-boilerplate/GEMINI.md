# Project Overview: bg-boilerplate

A specialized React + Vite boilerplate featuring an animated, high-performance canvas background (**CircuitBackground**) decoupled from the application logic. This project is designed with a "cyberpunk/terminal" aesthetic, utilizing design tokens from the PetroShield identity.

## 🛠️ Tech Stack
- **Framework:** React 19
- **Build Tool:** Vite 6
- **Language:** TypeScript
- **Routing:** React Router 7
- **Styling:** Vanilla CSS with custom design tokens

## 🚀 Building and Running
- **Development:** `npm run dev` (starts server at `http://localhost:5173`)
- **Build:** `npm run build` (compiles TypeScript and builds for production)
- **Preview:** `npm run preview` (locally previews the production build)

## 📁 Architecture & Conventions
- **Routing (`src/App.tsx`):** All routes are wrapped in an `AppLayout` that provides the fixed `CircuitBackground`. New pages should be added to `src/pages/` and registered in `App.tsx`.
- **Background (`src/components/CircuitBackground.tsx`):** A standalone Canvas-based component that handles its own animation loop (Matrix rain, circuit nodes, particles) and mouse-driven parallax effects.
- **Styling (`src/index.css`):** Core design tokens are defined as CSS variables. Use these for consistency:
  - `--neon-green`: Primary status/highlights.
  - `--fire-orange`: Alerts/secondary highlights.
  - `--void-black`: Global background.
  - `--font-terminal`: For VT323 monospaced text.
- **Layout:** The application uses a fixed layout where the `.page-container` handles its own scrolling, keeping the background stationary.

## 📝 Development Notes
- **Performance:** The background uses `requestAnimationFrame` and a single canvas. Avoid adding heavy DOM-based animations that might conflict with the canvas render cycle.
- **Responsiveness:** The background automatically adjusts to window resizing via a `resize` listener.
- **Type Safety:** Adhere to the strict TypeScript configuration defined in `tsconfig.json`.

## 🛰️ Deep Dive: CircuitBackground Animations

O background é processado em um único `canvas` utilizando quatro camadas lógicas de renderização:

### 1. Matrix Rain (Fundo Distante)
- **Visual:** Chuva de caracteres Katakana e alfanuméricos (`ァアカサタナ...01AXEGUARD`).
- **Dinâmica:** As colunas caem verticalmente a uma velocidade constante de 12px por frame. Quando uma coluna atinge o fim da tela, ela tem 2.5% de chance de resetar para o topo, criando um fluxo irregular.
- **Parallax:** Reage de forma inversa ao mouse (offset de -8px a -5px), criando sensação de profundidade infinita.

### 2. Circuit Nodes & Connections (Camada Intermediária)
- **Nós:** 60 círculos verdes neon com pulsação de opacidade (`sin(node.pulse)`).
- **Conexões em "L":** Se dois nós estão a menos de 120px de distância, o sistema desenha uma linha conectora. Diferente de conexões diretas, estas são angulares (estilo PCB), decidindo se dobram primeiro no eixo X ou Y com base na maior distância.
- **Profundidade:** Cada nó possui um valor `depth` único (0.3 a 1.0), que multiplica o efeito de parallax do mouse, criando um efeito 3D real de camadas.

### 3. Nano Particles (Sparkles Superiores)
- **Quantidade:** 80 partículas flutuantes.
- **Cores:** 70% Verde Neon (`#00FF41`) e 30% Laranja Fogo (`#FF6200`).
- **Comportamento:** Flutuam de baixo para cima com velocidades e "tempo de vida" variados. Elas possuem um ciclo de `fadeIn` e `fadeOut` suave e um efeito de brilho (glow) extra quando a opacidade está alta.

### 4. Scanline Effect (Interferência)
- **Gatilho:** Ocorre ciclicamente a cada 300 frames.
- **Efeito:** Uma barra horizontal sutil de baixa opacidade percorre a tela de cima para baixo em 40 frames, simulando a varredura de um monitor CRT antigo.

### 🎮 Interatividade
O movimento do mouse (`mousemove`) não altera as posições reais dos objetos, mas sim os **offsets de visualização**. Isso garante que a física e as conexões permaneçam estáveis enquanto o usuário navega.

