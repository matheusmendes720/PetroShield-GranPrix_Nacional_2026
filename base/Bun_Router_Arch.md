# Bun Router Architecture Blueprint (BFF & SSG Layer)

> [!IMPORTANT]  
> Este documento orquestra a estratégia de roteamento e injeção massiva de dados. O objetivo é escalar para Netlify (Static Functions + Edge) sem explodir os tempos de Load do browser e sem frameworks inchados no client-side.

## 1. Visão Geral da Arquitetura: SSG + TUI Nativo

Em vez de enviar um JS monstruoso gerado por Webpack/Vite que reconstrói a TUI inteira no cliente, seguiremos o protocolo **Bun Fast Compiler**.

**A Estratégia de Duas Camadas:**
1.  **Bun SSG (Static Site Generator):** Gera os "Shells" HTML em build-time. Rotas como `/dashboard.html` e `/intelligence.html` já carregam o layout do Terminal (Panels, ASCII arts, borders) puramente via CSS.
2.  **Bun BFF (Backend For Frontend) API:** A função principal desse middleware. Servirá o `synthetic_gen_v4.ts` diretamente via endpoins ultrarrápidos ou Server-Sent Events (SSE) para o HTML limpo.

## 2. Multi-Page Route Map (TCL Sub-Tabs)

A navegação será nativa (âncoras `<a>`) transacionando entre páginas distintas pré-compiladas, imitando comandos de abas num terminal (e.g., `Alt+1`, `Alt+2`).

### 📍 Route `/dashboard` (The C-Level Panopticon)
*   **Foco Funcional:** "Money & Risk".
*   **Widgets Dependentes do BFF:**
    *   `GET /api/v1/metrics/roi`: Recupera o somatório macro-econômico das ameaças bloqueadas.
    *   `GET /api/v1/fleet/status`: Retorna um JSON leve contendo os clusters afetados por anomalias (Base Búzios, Revap, etc.).

### 📍 Route `/edge-devices` (The Wearable Interceptor)
*   **Foco Funcional:** Inspeção profunda de endpoints móveis e vestíveis industriais.
*   **Widgets Dependentes do BFF:**
    *   `SSE /api/v1/streams/dpi`: Um canal aberto de Server-Sent Events transmitindo o dump em hexadecimal dos pacotes interceptados em tempo real de RealWears e HoloLens. Mostrando a "dissecação" da comunicação C2.

### 📍 Route `/swarm-orchestrator` (The Agentic Console)
*   **Foco Funcional:** O log assíncrono dos modelos NLP avaliando dados táticos.
*   **Widgets Dependentes do BFF:**
    *   `WS /api/v1/agentic-talks`: Conexão WebSocket para receber `yields` do gerador de diálogos (Agent Supervisor e Immunizer). Trata o cruzamento transversal do `AGENTIC_WORKFLOWS` e `AGENT_EVALUATIONS`.

## 3. Gestão de Densidade de Mock Data (Dense Dynamic Mock Layer)

A arquitetura para o serverless Netlify exige que os mocks de memória não quebrem a stack. 
Para gerar dados massivos:
*   As Functions em Bun importarão o `synthetic_gen_v4.ts` e invocarão arrays de matrizes táticas (ex: `1000 logs/segundo`).
*   O BFF aplicará um "Throttle & Sample" adaptativo (ex: envia só 5 logs por segundo por stream via WebSocket para evitar o *browser freeze*, mantendo a estética visual de "Live Console").
*   Todos os dados de custo em `$ milhões` originários do `mock_data.py` mapeado, serão agregados no momento da compilação pelo router do Bun para gerar índices estáticos pesados em formato `.json` consumível localmente.
