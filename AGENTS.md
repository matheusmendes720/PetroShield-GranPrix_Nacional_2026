# AGENTS.md

Single-team competition dossier for **Grand Prix SENAI Nacional 2026** (Apr 13–17, 2026, 100% online). Currently branded **AxeGuard / PetroShield** in the README and **Camaçari Shield** in the E1 deliverable. This file is a cross-agent summary. The detailed **`CLAUDE.md`** (Claude-Code specific) is the canonical source of truth for strategy, conventions, and the project "big picture" — read it before any non-trivial edit.

## What this repository is

It is **not a product codebase**. It is a competition dossier: ~95% Markdown strategy, ~5% Python tooling. Most "architecture" decisions live as Mermaid diagrams and prose, not code.

The product being pitched — a *Zero-Trust cybersecurity middleware (DLP proxy + Edge AI)* that blocks ransomware lateral movement on industrial SMEs, optionally extending to secure LLM access from smart-glasses — is a **demo**, not a deployment plan. Per the team's IP-trap strategy (Art. 9.3 of the edital), the frontend is the public asset and the backend is the moat.

## Setup & run

There is **no `package.json`, no `pyproject.toml`, no test runner**. Python is short scripts, not a package.

- **DLP demo:** `cd scripts/dlp_proxy && uvicorn main:app --reload` (serves `:8000`; Swagger at `/docs`). Pins: fastapi 0.110.0, uvicorn 0.27.1, pydantic 2.6.2. **Note:** `main.py:86` binds the `if __name__ == "__main__":` path to `0.0.0.0:8000`, but `uvicorn main:app --reload` (which reloads the module) listens only on `127.0.0.1:8000` by default. To reach the demo from a smart-glasses companion phone on the LAN, run `uvicorn main:app --reload --host 0.0.0.0`.
- **OSINT/econometric:** `python scripts/research_automation/econometric_pipeline.py` and `dorking_engine.py <domain>`.
- **Edital PDF → text:** `python 00_Regulamento/extract.py` — auto-installs `pypdf` on first run, so no separate `pip install` step is needed.

Full setup, demo bearer token (`jwt_token_xr_session_9942`), and endpoint walkthrough live in **`CLAUDE.md` § "Run / build commands"**.

## Project layout

Folder numbering (`00_Regulamento/` … `06_Entregas/`) is by **phase of preparation**, not by component. The full table is in **`CLAUDE.md` § "Repository layout (top-level)"**.

Sub-repo-specific deltas not covered in CLAUDE.md:

- **`scripts/`** splits into `dlp_proxy/` (FastAPI demo — layer 3 of the Zero-Trust cut: MDM endpoint → OAuth2 Device Flow IAM → FastAPI DLP proxy → Azure OpenAI VNet enclave) and `research_automation/` (Dorks + econometric engine that produces `c_level_dashboard_feed.json` for the C-level pitch slides).
- **`01_Intel_OSINT/`** carries social-engineering / recruitment material. `.gitignore` only matches **6 specific filenames** — the directory itself is **not** ignored. The four currently-present files (`Corporate_OSINT_Strategy.md`, `Advanced_Deep_Research_Pipeline.md`, `Latest_Intelligence_Brief_April_2026.md`, `Petrobras_Supply_Chain_Vendor_Intelligence.md`) **would be tracked if committed**.

## Deliverables status

See **`CLAUDE.md` § "Deliverables status"** for the table (E1 ✅ submitted; E2/E3/submission consolidation pending).

When generating E2/E3 deliverables, **mirror the tone, structure, and C-level jargon** of the E1 PDF — that is what the AI-judge scoring layer was trained on. The branding is currently inconsistent across files (**AxeGuard** in README, **PetroShield** in some strategy docs, **Camaçari Shield** in the E1 PDF) — surface this to the user before changing it.

## Conventions

- **Markdown is the deliverable format**, not docs about deliverables. Don't bloat strategy files with meta-commentary.

Language, color tokens (`#0D1117` / `#00FF41` / `#0052FF`), no-`Co-Authored-By`-trailer, and the rest of the conventions are in **`CLAUDE.md` § "Conventions specific to this repo"**.

## Branching & commits

- Default branch: `master`.
- Conventional commits where it makes sense (`feat:` / `fix:` / `docs:` / `refactor:`); the repo already uses this style.

## Security

- The DLP proxy `RedactionEngine` regex patterns (`\d{3}\.\d{3}\.\d{3}-\d{2}`, `\bp-\d{2,3}\b`, spoken-password pattern) are part of what the judges will read in the source-code deliverable. Treat them as public IP — extend cautiously.

Art. 9.3 IP-trap guidance (frontend = public asset, backend = moat) is in **`CLAUDE.md` § "Where the big picture actually lives"** and the parent workspace `AGENTS.md`.

## Key reference files

For non-trivial edits, read these first:

- `INDEX_GP_NACIONAL_2026.md` — canonical folder map + Mermaid timelines.
- `Rules_and_Winning_Strategies_GP.md` — the "grimório" for judge/AI scoring. Treat as binding.

The rest of the reference files (`README.md`, `base/problem.txt`, `00_Regulamento/regulamento_extracted_clean.txt`, `03_Arquitetura_Projeto/Project_Rules_and_Skills.md`) are listed in **`CLAUDE.md` § "Key reference files (read these before non-trivial edits)"**.