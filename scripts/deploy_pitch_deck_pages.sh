#!/usr/bin/env bash
# Publica o pitch deck (06_Entregas/pitch_deck/) no GitHub Pages — SEMPRE no mesmo link:
#   https://matheusmendes720.github.io/PetroShield-GranPrix_Nacional_2026/
#
# A branch `gh-pages` do repositório é a fonte do Pages (source = gh-pages, path = /).
# Este script reescreve essa branch com o conteúdo atual do deck e dá push.
# Uso:  bash scripts/deploy_pitch_deck_pages.sh   ["mensagem de commit"]
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_ROOT/06_Entregas/pitch_deck"
BRANCH="gh-pages"
REMOTE="origin"
MSG="${1:-Publish pitch deck to GitHub Pages}"
URL="https://matheusmendes720.github.io/PetroShield-GranPrix_Nacional_2026/"

cd "$REPO_ROOT"
git fetch "$REMOTE" "$BRANCH"

WT="$(mktemp -d)"
cleanup() { git worktree remove --force "$WT" >/dev/null 2>&1 || rm -rf "$WT"; }
trap cleanup EXIT

git worktree add --force "$WT" "$BRANCH" >/dev/null

# limpa a branch mantendo apenas o conteúdo publicável
find "$WT" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +
cp "$SRC/index.html" "$WT/index.html"
cp -r "$SRC/assets" "$WT/assets"
mkdir -p "$WT/diagrams"
cp "$SRC"/diagrams/*.svg "$WT/diagrams/" 2>/dev/null || true

git -C "$WT" add -A
if git -C "$WT" diff --cached --quiet; then
  echo "GH Pages: nada novo para publicar."
else
  git -C "$WT" -c user.name="$(git config user.name || echo matheusmendes720)" \
                 -c user.email="$(git config user.email || echo noreply@github.com)" \
                 commit -qm "$MSG"
  git -C "$WT" push "$REMOTE" "$BRANCH"
  echo "GH Pages: push feito -> $BRANCH ($MSG)"
fi

CODE=$(curl -s -o /dev/null -w '%{http_code}' "$URL" || true)
echo "URL: $URL (HTTP $CODE — Pages pode levar ~1 min para propagar)"
