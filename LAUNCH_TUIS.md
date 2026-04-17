# 🚀 PetroShield TUI Local Launch Guide

> One-liners para testar todos os TUIs localmente no terminal.

---

## ⚡ Quick Start (Windows)

```batch
:: Modo interativo (menu)
launch-tuis.bat

:: Ou direto por nome
launch-tuis.bat axeguard
launch-tuis.bat classic
launch-tuis.bat harness
launch-tuis.bat all
```

---

## 🖥️ One-Liners por TUI

### AxeGuard (Ink + React + Bun)
```powershell
# Via bun.exe absoluto (evita bloqueio de ExecutionPolicy)
$C:\pinokio\bin\npm\node_modules\bun\bin\bun.exe run dev

# Ou se bun estiver no PATH
bun run dev
```
**Atalhos no terminal:**
- `[1]` Dashboard  `[2]` Operações  `[3]` Theatre
- `[←/→]` Navegar  `[Q]` Sair

---

### Classic (Blessed + Bun)
```powershell
$C:\pinokio\bin\npm\node_modules\bun\bin\bun.exe run dev
```
**Atalhos no terminal:**
- `[Q]` Sair  `[R]` Refresh
- `[L]` Injetar log sintético  `[D]` Injetar device

---

### Python Harness (Typer + Rich REPL)
```powershell
# REPL interativo
.venv\Scripts\python.exe -m scripts.manager.harness repl

# Comandos diretos
.venv\Scripts\python.exe -m scripts.manager.harness status
.venv\Scripts\python.exe -m scripts.manager.harness test --suite all
.venv\Scripts\python.exe -m scripts.manager.harness inject --count 10000
```

---

### PowerShell Manager
```powershell
# REPL
powershell -ExecutionPolicy Bypass -File .\petroshield-manager.ps1 repl

# Status rápido
powershell -ExecutionPolicy Bypass -File .\petroshield-manager.ps1 status
```

---

## 🧪 Smoke Test (Validação Rápida)

```powershell
# Build AxeGuard
cd outer-tui-axeguard-ts; bun run build

# Build Classic
cd outer-tui-classic-ts; bun run build

# Python inject test
.venv\Scripts\python.exe -m scripts.manager.harness inject --count 100
```

---

## 🌐 Deploy Web (Netlify)

```powershell
# Deploy manual via MCP (já configurado)
# Sites:
#   AxeGuard:  https://petroshield-app.netlify.app
#   Classic:   https://petroshield-classic.netlify.app
```

---

*Gerado automaticamente para testes locais PetroShield v2.6*
