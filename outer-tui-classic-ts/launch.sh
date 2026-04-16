#!/usr/bin/env bash
# launch.sh — PetroShield Classic TUI Launcher
set -euo pipefail

cd "$(dirname "$0")"

if ! command -v bun &>/dev/null; then
  echo "[ERRO] Bun não encontrado no PATH."
  exit 1
fi

echo "=== PetroShield Classic TUI ==="

if [[ "${1:-}" == "--build" ]]; then
  echo "Building..."
  bun run build
  echo "Build completo. Artefatos em ./dist"
  exit 0
fi

if [[ "${1:-}" == "--dev" ]]; then
  echo "Modo DEV (hot reload via bun)..."
  bun run dev
else
  if [[ ! -f "dist/index.js" ]]; then
    echo "Binário não encontrado. Compilando primeiro..."
    bun run build
  fi
  echo "Launching TUI..."
  bun run launch
fi
