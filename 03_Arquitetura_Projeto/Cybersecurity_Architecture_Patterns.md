# 📁 Arquitetura de Pastas e Padrão de Projeto Escalonável
**Área Temática:** Cibersegurança e Ética Digital
**Foco:** Preparação Ofensiva de BI e Desenvolvimento Rápido (MVP "Sujo e Premium")

Para garantir velocidade absurda durante as 48h críticas de prototipagem e evitar conflitos de versão na Escuderia, o repositório oficial da equipe será padronizado.

---

## Estrutura Árvore do Repositório (`/ciberseguranca-gp-2026`)

```text
/
├── 📁 .cursor/                  # Configurações locais da IDE e Agentes IA
│   ├── rules/                   # (.mdc) Regras do projeto, UI/UX (Styles-Guard), Compliance
│   └── skills/                  # Scripts e prompts dos agentes
│
├── 📁 01_Intel_BI/              # PREPARAÇÃO OFENSIVA DE BI (Business Intelligence)
│   ├── datasets/                # CSVs e JSONs de mercado (ex: estatísticas de fraudes, LGPD)
│   ├── dashboards/              # Templates de Looker Studio / Power BI pré-montados
│   ├── lean_canvas/             # Rascunhos e blocos de texto otimizados para a IA (Prompt Reverso)
│   └── concorrentes/            # Análise de soluções de mercado existentes (Threat Intelligence)
│
├── 📁 02_Design_UX/             # "SUJO, RÁPIDO E BARATO, MAS PREMIUM"
│   ├── design_system/           # Tokens de design globais (design-tokens.css), Dark Mode Cyber
│   ├── figma_exports/           # SVGs, assets, e mockups de alta fidelidade
│   └── pitch_assets/            # Roteiros do Pitch, Logos, Mograph elements e IA Videos (Sora/Runway)
│
├── 📁 03_Frontend/              # O Rosto da Solução (A "Caixa Preta" Bonita)
│   ├── public/                  # Favicons, assets estáticos
│   ├── src/
│   │   ├── components/          # Botões Neumórficos, Gráficos de Radares D3.js (Impacto Visual)
│   │   ├── pages/               # Views estáticas principais (Landing Page de Venda + Dashboard Falso)
│   │   ├── styles/              # STYLES-GUIDE.md aplicado estritamente
│   │   └── utils/               # Conexão Mockada (falsa) ou rápida com APIs externas
│   ├── package.json
│   └── tailwind.config.ts       # Apenas se absolutamente necessário (Priorizar vanilla css tokens)
│
├── 📁 04_Backend_Engine/        # A Máquina (Apenas o estritamente necessário para validar)
│   ├── core/                    # O Algoritmo principal (A teoria abstrata mencionada no regulamento)
│   ├── api/                     # Rotas simples (FastAPI ou Express) para consumir os datasets do BI
│   └── docs/                    # OpenAPI/Swagger para o Tech Lead impressionar os jurados técnicos
│
└── 📋 README.md                 # Pitch de Vendas em formato de documentação
```

---

## 🚀 Como a Arquitetura Potencializa a Vitória

### 1. Preparação Ofensiva de BI (A pasta `01_Intel_BI`)
Antes mesmo do evento começar no dia 13, esta pasta já deve estar cheia de dados do Banco Central, Febraban, e relatórios globais de Ransomware. Quando o desafio for revelado, a equipe de base (Técnico/Médio) só precisa ligar os pontos e preencher o *Lean Canvas*. A métrica de "Atratividade de Mercado" vai gabaritar porque é embasada em dados reais e volumosos, enquanto as outras equipes ainda estarão pesquisando no Google.

### 2. Barreira de Proteção de IP (A separação 03_Frontend vs 04_Backend)
Como dita a nossa estratégia perante a regra 9.3 (Apropriação da ideia), a pasta `03_Frontend` é o que será enviado no repositório final e linkado no vídeo. Ela é linda, perfomática e vende a ideia com maestria. O verdadeiro segredo industrial quântico ou de machine learning contido na pasta `04_Backend_Engine/core` pode ser documentado via API Rest genérica nos slides, não expondo 100% da lógica proprietária que o Arquiteto de Nível Superior construir, impedindo o roubo silencioso do núcleo do IP após a competição.

### 3. Foco Absoluto em Compliance e Estilo (A pasta `.cursor/rules`)
Com painéis de IA gerando código e design durante o tempo escasso, uma regra `styles-guard.mdc` e o `design-tokens.css` amarram os agentes de forma inflexível. Se a paleta foca na Ética Digital com tons de #0D1117 (Dark) com acentos de #00FF41 (Matrix Green) e #0052FF (Trust Blue), a IA não terá permissão de fugir disso, garantindo consistência visual cirúrgica para a gravação do pitch, poupando a equipe de perder horas corrigindo CSS.
