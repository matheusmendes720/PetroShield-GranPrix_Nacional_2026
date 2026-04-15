# AGENTS.md — Guia do Agente para o Repositório GP SENAI 2026

> Este arquivo é destinado a agentes de IA. Leia-o antes de qualquer modificação no repositório.

---

## 1. Visão Geral do Projeto

Este repositório é a **base de conhecimento e prototipagem tática** de uma escuderia para o **Grand Prix SENAI de Inovação 2026**. Não se trata de um monolito de software enterprise tradicional, mas de um **centro de inteligência competitiva** que combina:

- Documentação estratégica e técnica (Markdown + Mermaid);
- Pesquisa de mercado e OSINT corporativo;
- Protótipos de código Python (FastAPI e scripts de automação);
- Assets visuais gerados por IA (identidade cyberpunk da marca **PetroShield** / **Camaçari Shield**).

**Foco da competição:** Cibersegurança e Ética Digital, com ênfase em proteção industrial (Petrobras, PMEs baianas, IoT/SCADA) e conformidade LGPD.

**Idioma oficial:** Português (Brasil). Todo novo documento, comentário de código e mensagem de commit deve preferencialmente ser em português.

---

## 2. Stack Tecnológico

| Camada | Tecnologia / Ferramenta | Observação |
| :--- | :--- | :--- |
| **Documentação** | Markdown, Mermaid, PDFs | Diagramas de arquitetura e fluxos de processo |
| **Protótipo Backend** | Python 3.11+, FastAPI, Pydantic v2 | Middleware DLP (`scripts/dlp_proxy/`) |
| **Automação / BI** | Python puro (`json`, `re`, `random`, `sys`) | `dorking_engine.py` e `econometric_pipeline.py` |
| **Frontend (planejado)** | React / Next.js, Tailwind CSS | Nenhum código de frontend foi iniciado ainda |
| **Agentic AI (planejado)** | LangGraph, LangChain | Apenas documentação conceitual e schemas de estado |
| **Observabilidade (planejada)** | OpenTelemetry, Langfuse, Prometheus, Grafana | Documentada em `base/Agentic AI SOC Playground Architecture.md` |
| **Design** | Figma (planejado), imagens geradas por IA (JPG/PNG) | Pasta `design/` |

**NÃO EXISTE** no repositório: `pyproject.toml`, `package.json`, `Cargo.toml`, `Makefile`, `Dockerfile`, ou qualquer arquivo de build/CI centralizado na raiz.

---

## 3. Organização de Pastas e Módulos

```text
/
├── 00_Regulamento/              # Regras oficiais da competição e extrações de PDF
├── 01_Intel_OSINT/              # Inteligência em fontes abertas (Petrobras, CIMATEC, recrutamento)
├── 02_Estrategia_Vencedora/     # Táticas de pontuação, templates de proposta
├── 03_Arquitetura_Projeto/      # Especificações técnicas, padrões de segurança, skills da equipe
├── 04_BI_Ofensivo/              # Lean Canvas, KPIs C-Level, propostas estratégicas
├── 05_Market_Intelligence/      # Análises econométricas, TAM/SAM/SOM, sumários executivos
├── 06_Entregas/                 # Entregas oficiais da competição (E1, E2, E3)
│   └── E1_Ideacao/              # Lean Canvas final submetido no dia 13/04
├── base/                        # Documentos-base, planos de implementação, requisitos
├── design/                      # Identidade visual PetroShield (imagens, logo, paleta cyberpunk)
├── scripts/                     # Código executável de protótipos e automações
│   ├── dlp_proxy/               # API FastAPI: proxy DLP com OAuth Device Flow mockado
│   └── research_automation/     # Scripts de geração de dorks e pipeline econométrico
├── README.md                    # Índice navegável para humanos
├── Hackathon OS.md              # Cronograma e regras do evento
├── INDEX_GP_NACIONAL_2026.md    # Visão holística da campanha nacional
└── Rules_and_Winning_Strategies_GP.md  # "Grimório" de estratégia competitiva
```

### Convenções de nomenclatura
- Pastas numeradas (`00_`, `01_`, ...) representam fases ou domínios de conhecimento fixos.
- Arquivos Markdown usam `Snake_Case_Descritivo.md`.
- Scripts Python usam `snake_case_descritivo.py`.
- Assets de design mantêm os nomes originais gerados pela ferramenta de IA.

---

## 4. Como Executar o Código Existente

### 4.1 DLP Proxy (FastAPI)
Local: `scripts/dlp_proxy/`

```powershell
cd scripts/dlp_proxy
pip install -r requirements.txt
python main.py
# ou, para desenvolvimento:
# uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

- Endpoint raiz: `GET /`
- Endpoint protegido: `POST /api/v1/secure-prompt` (requer header `Authorization: Bearer jwt_token_xr_session_9942`)
- Endpoint de simulação OAuth: `GET /api/v1/auth/device-flow-status?device_id=...`

### 4.2 Motor de Dorks (OSINT)
Local: `scripts/research_automation/dorking_engine.py`

```powershell
python scripts/research_automation/dorking_engine.py petrobras.com.br
```

### 4.3 Pipeline Econométrico
Local: `scripts/research_automation/econometric_pipeline.py`

```powershell
python scripts/research_automation/econometric_pipeline.py
```

Gera o arquivo `c_level_dashboard_feed.json` com métricas de risco financeiro simuladas.

### 4.4 Extrator de PDF do Regulamento
Local: `00_Regulamento/extract.py`

```powershell
cd 00_Regulamento
python extract.py
```

Dependência dinâmica: instala `pypdf` automaticamente se não estiver presente.

---

## 5. Diretrizes de Estilo e Qualidade

### 5.1 Markdown
- Use emojis de seção de forma consistente com os documentos existentes (ex: `## 📁`, `> [!IMPORTANT]`).
- Diagramas Mermaid são fortemente encorajados para fluxos e arquiteturas.
- Tabelas em Markdown devem ter alinhamento explícito (`:---`, `:---:`, `---:`).

### 5.2 Python
- Comentários e docstrings em **português**.
- Evite adicionar dependências pesadas. Prefira a biblioteca padrão quando possível (regra do hackathon: "sujo, rápido e barato, mas premium").
- Se for necessário adicionar uma biblioteca, atualize o `requirements.txt` correspondente e documente a justificativa em um comentário acima da importação.
- Não altere a lógica dos mocks existentes sem garantir que a "demonstração do pitch" ainda funcione (os tokens mockados e respostas fixas são intencionais para apresentação).

### 5.3 Design / Visual
A identidade visual PetroShield possui tokens fixos. Ao criar qualquer asset ou referência visual, respeite:
- **Neon Matrix Green:** `#00FF41`
- **Fire Petroleum Orange:** `#FF6200`
- **Deep Void Black:** `#0A0A0A`
- **Tipografia terminal:** VT323, Courier New Bold

---

## 6. Estratégia de Testes

**Não existe suite de testes automatizada neste repositório.** A validação é feita por inspeção manual e demonstração:

1. **DLP Proxy:** envie requisições de teste via `curl` ou Postman contendo CPFs, nomes de poços (`Poço Tupi-10`) ou senhas. Verifique se o log de resposta mostra o mascaramento (`[CPF_BLOQUEADO]`, `[ATIVO_RESTRITO]`).
2. **Pipeline Econométrico:** execute o script e valide o JSON gerado (`c_level_dashboard_feed.json`).
3. **Documentação:** verifique renderização de Mermaid no preview do GitHub ou VS Code.

Se você criar novos scripts Python, adicione um bloco `if __name__ == "__main__":` com um exemplo executável mínimo.

---

## 7. Considerações de Segurança

### 7.1 Proteção de Informações Sensíveis
O `.gitignore` já exclui arquivos de OSINT de recrutamento e engenharia social (`CIMATEC_Intel_Report.md`, `OSINT_Recruitment_Playbook.md`, etc.). **Nunca remova essas regras nem force o commit desses arquivos.**

### 7.2 Segredos e Mocks
- Tokens JWT mockados (ex: `jwt_token_xr_session_9942`) são **apenas para demonstração de hackathon**. Se o projeto evoluir para produção real, esses tokens devem ser substituídos por um fluxo OAuth2.0 legítimo.
- Não commite arquivos `.env` ou credenciais reais.

### 7.3 LGPD e Ética Digital
Qualquer código ou documentação que mencione dados pessoais (CPF, credenciais) deve fazê-lo no contexto de:
- **Conformidade LGPD** (mascaramento, notificação de breach);
- **Educação em cibersegurança** (exemplos fictícios).

Nunca use dados pessoais reais de terceiros.

---

## 8. Convenções para Agentes de IA

Ao modificar este repositório:

1. **Mantenha a estrutura de pastas numerada.** Não crie novas pastas de topo sem justificativa tática clara.
2. **Preserve o tom e o vocabulário dos documentos existentes.** O projeto usa uma linguagem de "inteligência ofensiva", "BI agressivo" e "hacking virtuoso". Não banalize esse tom em documentos estratégicos.
3. **Atualize o `README.md` raiz** se você adicionar um novo documento de destaque em qualquer pasta numerada.
4. **Verifique conflitos de versão.** Como este é um repositório colaborativo de equipe, evite alterações massivas em múltiplos arquivos de estratégia sem consultar o contexto.
5. **Documente no próprio arquivo** qualquer código gerado por IA, incluindo uma breve nota sobre o propósito e limitações.

---

*Última atualização: 13/04/2026 — gerado após auditoria completa da estrutura do repositório.*
