# Relatório de Pesquisa: Deploy do TUI PetroShield em Web App

> **PetroShield AxeGuard — Grand Prix SENAI Nacional 2026**  
> Pesquisa de viabilidade técnica para portar/embbedar o TUI Python (Textual) em uma aplicação web React, com foco em deploy estático (Netlify) e alternativas Node.js/TypeScript.

---

## 1. Resumo Executivo

Este relatório avalia **três vetores estratégicos** para levar a experiência do terminal PetroShield ao browser:

1. **Terminal Embutido em React** — usar `xterm.js` (ou wrappers React) para renderizar um terminal funcional dentro de uma seção da página web.
2. **Portabilidade Nativa para Node.js/TypeScript** — reescrever/replicar o TUI em bibliotecas CLI como `Ink` ou `blessed`, mantendo a capacidade de rodar localmente.
3. **Deploy em Netlify (Static Hosting)** — arquitetura 100% client-side com Python rodando no browser via WebAssembly (`Pyodide`) + mock data estruturado.

**Conclusão rápida:** a rota mais viável para um *tech demo* interativo no navegador, sem backend dedicado, é **React + xterm.js + Pyodide (WASM)**. Para uma versão nativa local em Node.js, **Ink** é a escolha moderna e com maior ecossistema de componentes.

---

## 2. Bibliotecas React para Terminal Embutido (Web Apps)

### 2.1 xterm.js — O Padrão de Mercado

| Critério | Avaliação |
|----------|-----------|
| **Maturidade** | Usado no VS Code, GitHub Codespaces, Jupyter — altíssima confiabilidade. |
| **ANSI/Unicode** | Suporte completo a cores ANSI, emojis, Unicode e custom keybindings. |
| **Addons** | `@xterm/addon-fit` (responsive), `@xterm/addon-attach` (WebSocket), `@xterm/addon-web-links`, etc. |
| **Integração React** | Requer wrapper; há várias opções (ver abaixo). |
| **Bundle Size** | ~300 KB (core) + addons. Aceitável para dashboards. |

**Por que é a base ideal:**
- O TUI Python atual gera saída com Rich/Textual, que são essencialmente streams de texto com códigos ANSI. O `xterm.js` interpreta essa saída fielmente.
- Se conseguirmos pipear o stdout do Python (rodando no browser via Pyodide) para uma instância de `xterm.js`, teremos uma réplica visual muito próxima do terminal nativo.

### 2.2 Wrappers React Recomendados

#### A) `react-xtermjs` (Qovery)
- **GitHub:** `Qovery/react-xtermjs`
- **Destaques:** Hook `useXTerm` + componente `XTerm`. Suporta addons dinâmicos. Ativo em 2026.
- **Quando usar:** se você quer controle total sobre a instância do terminal via hooks React.

```tsx
import { useXTerm } from 'react-xtermjs'
import { FitAddon } from '@xterm/addon-fit'

function TerminalPanel() {
  const { instance, ref } = useXTerm()

  React.useEffect(() => {
    const fit = new FitAddon()
    instance?.loadAddon(fit)
    fit.fit()
    instance?.writeln('\x1b[32mPetroShield TUI Web v1.0\x1b[0m')
  }, [instance])

  return <div ref={ref} style={{ height: '100%', width: '100%' }} />
}
```

#### B) `@pablo-lion/xterm-react`
- **GitHub:** `PabloLION/xterm-react`
- **Destaques:** Componente declarativo, TypeScript-native.
- **Quando usar:** se você prefere abordagem puramente component-based e não precisa de hooks de baixo nível.

#### C) `xterm-for-react`
- **GitHub:** `robert-harbison/xterm-for-react`
- **Cuidado:** não atualizado há alguns anos; pode não suportar React 18+ corretamente. **Evitar** para projetos novos.

### 2.3 Alternativas Leves (não-xterm)

| Biblioteca | Uso recomendado | Limitação |
|------------|-----------------|-----------|
| `react-terminal-ui` | Simulação de terminal estilo "hacker" | Não é um emulador VT100 real; suporte ANSI limitado. |
| `react-console-emulator` | Comandos simples, quizzes | Não renderiza saída ANSI de Rich/Textual corretamente. |

**Veredicto:** para o PetroShield, que depende de Rich (ANSI colors, box drawing, painéis), **xterm.js é obrigatório**. Os wrappers `react-xtermjs` ou `@pablo-lion/xterm-react` são as melhores pontes para React.

---

## 3. Bibliotecas TypeScript / Node.js para TUI Nativo

Se a estratégia for criar uma versão 100% local em Node.js (paralela ao Python), as principais candidatas são:

### 3.1 Ink e o Ecossistema Ink UI — O "Padrão Mercado" para React CLI

| Critério | Avaliação |
|----------|-----------|
| **Paradigma** | React (JSX) no terminal — renderizador customizado. |
| **Componentes (`@inkjs/ui`)** | Possui `TextInput`, `Select`, `Spinner`, `StatusMessage`, `Badge`. |
| **Gráficos** | `@pppp606/ink-chart` cobre necessidades de dashboards analíticos. |
| **TS Support** | Excelente. Principal stack recomendada para transição estável. |

**Componentes Chave do `@inkjs/ui` para o SOC:**
- `Select`: Para menus de seleção (ex: "Aprovar Ação", "Escalar Incidente").
- `Spinner` e `ProgressBar`: Feedback em tempo real enquanto os agentes LangGraph rodarem em background (ex: busca em ChromaDB/pgvector).
- `TextInput`: Para injeção manual de comandos/prompts ao Supervisor.

### 3.2 Novas Alternativas TypeScript & React para TUI (Pesquisa Recente)

Há opções mais modernas e até puramente TypeScript focadas em performance e renderização em buffer para não sacrificar o throughput num SOC com muita telemetria:

1. **Storm** (Compositor-based React TUI)
   - Excelente para dashboards dinâmicos e que recebem streams de telemetria constantes. Reduz processamento no draw de tela.
   - Bom fit se as atualizações chegam violentas a partir do SIEM / OpenTelemetry Collector.

2. **Rezi** (Alta Performance, Native Bun/Node)
   - Escrito em C + interface Typescript, focadíssimo em velocidade sem o overhead de render do React puro. Não usa React, mas usa uma sintaxe JSX-like.
   - A benchmark coloca como super performance, ótimo caso haja lag ao renderizar logs ANSI.

3. **Giggles** (`zion-off/giggles`) e **Silvery** (`beorn/silvery`)
   - Alternativas experimentais de React renderer (focados em Flexbox avançado para layouts complexos de painéis no terminal).

### 3.3 Blessed / Neo-Blessed — Clássico Curses-like

| Critério | Avaliação |
|----------|-----------|
| **Maturidade** | `blessed` original está **unmaintained** desde 2017. `neo-blessed` é fork ativo. |
| **Widgets** | Extensivo: boxes, tables, forms, progress bars, logs. |

**Veredicto:** Para um projeto em 2026, **Ink (com Ink UI)** ou um framework emergente como **Storm** são infinitamente superiores ao `blessed` por causa do state-management atrelado a Hooks.

---

## 4. Integração do TUI com a Arquitetura do Agentic AI SOC

Dado que a fundação do projeto é gerida por **LangGraph** (Supervisor + Subgraphs) e monitorada de forma fina via **OpenTelemetry (OTEL)**, o frontend TUI (ou via browser embebidado) deve comportar-se da seguinte forma:

### 4.1. Comunicação com a Orquestração
- **Assinatura de Eventos (LangGraph Streaming):** A interface em Ink (ou xterm.js via browser) assina o hook de streaming do LangGraph (`astream_events`).
- **Estados Visuais (Progress/Spinners):** Durante os nós de "Detect", "Analyse", "Hunt", o TUI mapeia o nó ativo para o `Spinners` da tela. Múltiplos agentes trabalhando em paralelo podem usar componentes como `ProgressTask`.

### 4.2. Fluxo Observabilidade e Dados (RAG + Telemetria)
- A telemetria proveniente da captura OTEL chega ao Grafana e Prometheus. O TUI pode extrair via API queries em tempo real do Prometheus para renderizar no `@pppp606/ink-chart`.
- Toda injeção no prompt (human-in-the-loop) feita no TUI (por exemplo via `TextInput` do Ink) propaga um Trace ID via Langfuse e LangSmith.

O front-end se mantém **totalmente dissociado** da lógica de state do agente. Ele apenas consome os rastreios do OTEL Collector / LangSmith para a UI "ao vivo", garantindo que a tela sempre reflita a matriz de decisão em andamento do `SupervisorState`.

---

## 4. Arquitetura de Deploy Netlify (Static Site + Terminal Interativo)

### 4.1 O Desafio

Netlify é **static-first**. Não é possível manter um processo Python de longa duração em background (como `python -m scripts.dlp_proxy.main`) num deploy gratuito de site estático. A rota tradicional "backend FastAPI + frontend React" exigiria:
- Netlify Functions (serverless) para a API, ou
- um serviço separado (Render, Fly.io, Railway) para o Python backend.

Para um **tech demo 100% client-side**, sem custos de backend, a arquitetura recomendada é:

```
┌─────────────────────────────────────────────────────────────┐
│  React App (Next.js / Vite) hospedado no Netlify            │
│  ├── Seção UI: Dashboards, cards, gráficos (Recharts)       │
│  └── Seção Terminal: xterm.js embed                         │
│       └── Pyodide (WASM) rodando Python no browser          │
│            ├── Código Python do TheatreEngine (mock)        │
│            ├── Mock data carregado de JSON estático         │
│            └── Saída ANSI direcionada ao xterm.js           │
└─────────────────────────────────────────────────────────────┘
```

### 4.2 Pyodide + xterm.js — Viabilidade Técnica

**Como funciona:**
1. A página carrega `pyodide.js` via CDN (JsDelivr).
2. O runtime Python (CPython compilado para WASM) é inicializado no cliente.
3. O código do `theatre.py`, `mock_data.py` e `orchestrator.py` é carregado como strings/via fetch e executado com `pyodide.runPython()`.
4. O stdout do Python é redirecionado para o `xterm.js`.

**Limitações importantes:**
- **Textual/Rich no Pyodide:** `textual` depende de eventos de terminal reais (TTY, ioctl) que **não existem no browser**. Portanto, o TUI interativo completo do `demo_ui.py` (com tabs clicáveis, botões, etc.) **não roda diretamente** no Pyodide.
- **Solução:** rodar o `theatre.py` em modo `--quiet` (ou com um wrapper customizado) que emita logs formatados em ANSI para o xterm.js. A navegação por tabs e botões fica a cargo do React (UI web normal), enquanto o terminal mostra o "chat loop" agentic em tempo real.

**Tamanho do bundle:**
- Pyodide core: ~6.4 MB (compressed ~2.5 MB).
- Pacotes adicionais (pandas, numpy) não são necessários para o nosso caso.
- O carregamento inicial pode levar 3–8s em conexões 4G. Recomenda-se lazy-load.

### 4.3 Mock Data & "ORM" Local no Browser

Para manter o demo independente de backend, use uma estratégia de dados client-side:

| Tecnologia | Função | Quando usar |
|------------|--------|-------------|
| **JSON estático** | Datasets fixos (`mock_data.json`). | Ideal para cenários determinísticos do theatre. |
| **Dexie.js** | Wrapper IndexedDB para queries estruturadas. | Se precisar de persistência local (logs de sessão, cache de cenários). |
| **LocalStorage** | Chave-valor simples (configs, flags). | Pequeno volume de dados (< 5 MB). |

**Schema sugerido para o demo web:**

```ts
// types/demo.ts
interface DemoScenario {
  sceneId: string;
  title: string;
  eventType: string;
  expectedAction: 'blocked' | 'allowed' | 'escalated' | 'vendor_suspended';
  narration: string[];
}

interface SessionLog {
  id: number;
  timestamp: number;
  agent: string;
  type: 'THOUGHT' | 'ACTION' | 'OBSERVATION' | 'NARRATION';
  content: string;
}

interface FleetNode {
  nodeId: string;
  facility: string;
  region: string;
  status: 'online' | 'offline';
  vaccineStatus: 'up_to_date' | 'pending' | 'outdated';
}
```

### 4.4 Arquitetura Recomendada para Netlify

```
/public
  ├── pyodide/              # (opcional) self-hosted pyodide files
  └── mock-data/
        ├── scenarios.json
        └── fleet.json
/src
  ├── components/
  │     ├── Dashboard.tsx         # UI rica (Recharts, cards)
  │     ├── TerminalPanel.tsx     # xterm.js wrapper
  │     └── SceneSelector.tsx     # seleção de cenas do theatre
  ├── hooks/
  │     └── usePyodide.ts         # inicialização lazy do Pyodide
  ├── python/
  │     ├── theatre_bundle.py     # código Python combinado
  │     └── bootstrap.py          # script de entrada que redireciona stdout
  └── pages/
        └── index.tsx
/netlify.toml
```

**Config `netlify.toml` mínima:**

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "*.wasm"
  [headers.values]
    Content-Type = "application/wasm"
```

> **Nota crítica:** Netlify (e qualquer static host) precisa servir arquivos `.wasm` com o MIME type correto. O `netlify.toml` acima garante isso.

### 4.5 Alternativa: Serverless Functions (Netlify Functions)

Se for necessário executar o Python "for real" (com FastAPI) e apenas mostrar resultados no frontend:
- Criar **Netlify Functions** em Python (runtime suportado: Python 3.8+ via build image customizado).
- Limitações: timeout de 10s (planos pagos até 26s), cold starts, sem WebSocket nativo.
- Para SSE (Server-Sent Events) ou streaming, Netlify Functions não é ideal.

**Veredicto:** para um **pitch/demo** onde a interatividade e a ausência de backend são vantagens, **Pyodide no cliente é a escolha mais impactante**. Para produção real posterior, migra-se para um backend dedicado.

---

## 5. Matriz de Decisão

| Objetivo | Tecnologia Recomendada | Nível de Esforço | Impacto Visual |
|----------|------------------------|------------------|----------------|
| Terminal embed no React | `xterm.js` + `react-xtermjs` | Médio | Alto |
| Rodar Python no browser | `Pyodide` (WASM) | Médio-Alto | Alto (efeito "wow") |
| Portar TUI para Node local | `Ink` + `ink-chart` | Médio | Alto |
| Portar TUI legado curses | `neo-blessed` | Alto | Médio |
| Deploy estático gratuito | Netlify + Pyodide + xterm.js | Médio | Alto |
| Deploy com backend real | Netlify Functions (limitado) / Render | Alto | Alto |

---

## 6. Recomendações Finais

### Para o Tech Demo Web (Hackathon / Pitch)
1. **Criar um app React (Vite ou Next.js)** com duas colunas:
   - **Esquerda:** Dashboard visual em HTML/CSS (Recharts) mostrando métricas da frota, vendors, compliance.
   - **Direita:** Painel `xterm.js` que roda **Pyodide**.
2. **No Pyodide**, carregar uma versão simplificada do `theatre.py` (sem `textual`) que execute as cenas e escreva logs ANSI coloridos no terminal.
3. **Mock data** em JSON estático servido de `/public`; opcionalmente cachear sessões com `Dexie.js`.
4. **Deploy no Netlify** com `netlify.toml` configurado para WASM MIME type.

### Para a Versão Local Node.js (Portabilidade Completa)
1. **Criar um projeto `petroshield-tui-node`** usando `Ink`.
2. Replicar as 4 abas (Dashboard, Operações, Theatre, Análises) como componentes `<Box>` com `ink-table`, `ink-chart`, `ink-progress-bar`.
3. Reutilizar a lógica do `TheatreEngine` (pode ser portada para TS ou chamada via `child_process` se houver um wrapper Python).

---

## 7. Referências

- **xterm.js:** https://xtermjs.org/
- **react-xtermjs:** https://github.com/Qovery/react-xtermjs
- **xterm-react:** https://github.com/PabloLION/xterm-react
- **Ink:** https://github.com/vadimdemedes/ink
- **ink-chart:** https://github.com/pppp606/ink-chart
- **neo-blessed:** https://github.com/embarklabs/neo-blessed
- **Pyodide:** https://pyodide.org/
- **Pyodide + xterm.js issue:** https://github.com/pyodide/pyodide/issues/5760
- **Netlify WASM headers:** https://answers.netlify.com/t/how-do-i-deploy-a-python-app-using-python-3-12-and-xterm/130561

---

*Relatório gerado em 15/04/2026. Próxima ação: prototipagem do app React + xterm.js + Pyodide.*
