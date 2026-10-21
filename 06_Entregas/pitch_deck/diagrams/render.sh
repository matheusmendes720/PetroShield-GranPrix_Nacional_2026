#!/usr/bin/env bash
# Render all pitch_deck diagrams to SVG with the deck background.
# Uso: bash render.sh
set -euo pipefail
cd "$(dirname "$0")"

BG="#0A0E27"   # --bg-primary (Option D Holographic)

for src in *.d2; do
  out="${src%.d2}.svg"
  d2 "$src" "$out"
  # D2 emite um <rect> de fundo branco; no deck o fundo é o próprio slide.
  python - "$out" "$BG" <<'PY'
import re, sys
path, bg = sys.argv[1], sys.argv[2]
svg = open(path, encoding="utf-8").read()
svg = re.sub(r'(<rect[^>]*?)fill="#FFFFFF"', rf'\1fill="{bg}"', svg, count=1)
open(path, "w", encoding="utf-8").write(svg)
PY
  printf '  %-28s %s\n' "$out" "$(grep -o 'viewBox="0 0 [0-9]* [0-9]*"' "$out" | head -1)"
done
