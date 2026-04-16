# PetroShield TUI — Node/TS + Bun + Netlify Deploy

> Guia rápido de setup para os dois trabalhos TUI externos e seus pipelines CI/CD.

---

## 🚀 Estrutura Criada

```text
outer-tui-axeguard-ts/    # TUI moderno com Ink (React para terminal)
outer-tui-classic-ts/     # TUI clássico com Blessed (estilo retro cyber-ops)
.github/workflows/        # Pipelines GitHub Actions → Netlify
```

## 🖥 Como rodar localmente

### AxeGuard (Ink)
```powershell
cd outer-tui-axeguard-ts
bun install
bun run dev
```
Atalhos: `[1]` Dashboard | `[2]` Operações | `[3]` Theatre | `[←/→]` Navegar | `[Q]` Sair

### Classic (Blessed)
```powershell
cd outer-tui-classic-ts
bun install
bun run dev
```
Atalhos: `[Q]` Sair | `[R]` Refresh | `[L]` Injetar log | `[D]` Injetar device

## 🔧 Build & Launch scripts

Cada pasta contém `launch.ps1` e `launch.sh`:
```powershell
.\launch.ps1 -Dev      # modo desenvolvimento
.\launch.ps1 -Build    # gera bundle em dist/
```

## 🌐 Projetos Netlify

| App | Site ID | URL Primária |
|-----|---------|--------------|
| AxeGuard | `a0be275a-293d-4aa0-b61e-9df9d9119730` | https://petroshield-app.netlify.app |
| Classic | `c8fb18d0-a002-4437-b9eb-f81320ec8609` | https://petroshield-classic.netlify.app |

## 🔐 Secrets do GitHub (Settings → Secrets and variables → Actions)

Configure os seguintes secrets no repositório para os workflows funcionarem:

- `NETLIFY_AUTH_TOKEN` — seu Personal Access Token do Netlify
- `NETLIFY_SITE_ID_AXEGUARD` — `a0be275a-293d-4aa0-b61e-9df9d9119730`
- `NETLIFY_SITE_ID_CLASSIC` — `c8fb18d0-a002-4437-b9eb-f81320ec8609`

## 📦 Mock Data Sintética

Os arquivos `src/mocks/data.ts` e `src/mocks/generators.ts` contêm datasets empresariais espelhados do Python (`scripts/agentic_soc/mock_data.py`) e geradores expansíveis para stress-test visual.

## 🔄 CI/CD Trigger

Os workflows rodam em:
- Push para `main`, `tui-axeguard` ou `tui-classic`
- Pull Requests para `main` (deploy preview)
