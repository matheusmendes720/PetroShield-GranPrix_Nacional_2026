#!/usr/bin/env python3
"""
PetroShield Manager Harness — Typer + Rich TUI REPL
====================================================
Ferramenta CLI unificada para:
  • Gerenciar worktrees git (axeguard, classic, main)
  • Executar testes suites (TUI, Orchestrator, Theatre)
  • Promover branch para prod latest working (.V)
  • Injetar dados sintéticos em massa
  • Telemetry logging serverless-ready

Uso:
  python -m scripts.manager.harness
  python -m scripts.manager.harness test --suite all
  python -m scripts.manager.harness worktree --switch axeguard
  python -m scripts.manager.harness promote --branch tui-axeguard --version v2.6
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Optional

import os
import sys

# Forcar UTF-8 no Windows para evitar crash do Rich com cp1252
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import typer
from rich import box
from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table
from rich.text import Text

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
APP_NAME = "PetroShield Manager"
VERSION = "2.6.0-harness"
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
WORKTREES = {
    "main": PROJECT_ROOT,
    "axeguard": PROJECT_ROOT / "outer-tui-axeguard-ts",
    "classic": PROJECT_ROOT / "outer-tui-classic-ts",
    "python-core": PROJECT_ROOT / "scripts" / "dlp_proxy",
}
TEST_SUITES = {
    "tui": ("tests/test_tui.py", "TUI Integration — 16 casos"),
    "orchestrator": ("tests/test_orchestrator.py", "Orchestrator — 18 casos"),
    "theatre": ("scripts/agentic_soc/theatre.py", "Theatre Agentic — smoke test"),
}
TELEMETRY_LOG = PROJECT_ROOT / ".local" / "telemetry.jsonl"
TELEMETRY_LOG.parent.mkdir(parents=True, exist_ok=True)

console = Console()
app = typer.Typer(
    name="petroshield",
    help="PetroShield AxeGuard — Manager Harness CLI",
    rich_markup_mode="rich",
    add_completion=False,
)


# ---------------------------------------------------------------------------
# Telemetry & Logging Serverless-Ready
# ---------------------------------------------------------------------------

def emit_telemetry(
    event: str,
    payload: dict,
    level: str = "INFO",
    source: str = "harness",
) -> None:
    """Emite evento de telemetria estruturado (JSON Lines).
    Pronto para ingestão via Netlify Function / Vercel Edge / S3 + Athena.
    """
    entry = {
        "ts": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "source": source,
        "event": event,
        "payload": payload,
        "host": os.environ.get("COMPUTERNAME", "unknown"),
        "version": VERSION,
    }
    with open(TELEMETRY_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    # Também loga no console se verbose
    style = {
        "DEBUG": "dim",
        "INFO": "cyan",
        "WARN": "yellow",
        "ERROR": "red bold",
    }.get(level, "white")
    console.print(f"[telemetry] [{level}] {event}", style=style)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def run_cmd(cmd: list[str], cwd: Optional[Path] = None, capture: bool = True) -> subprocess.CompletedProcess:
    """Executa comando shell com Rich spinner."""
    cwd = cwd or PROJECT_ROOT
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]{task.description}"),
        console=console,
        transient=True,
    ) as progress:
        task = progress.add_task(description=f"Running: {' '.join(cmd[:3])}...", total=None)
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd,
                capture_output=capture,
                text=True,
                encoding="utf-8",
                check=False,
            )
            progress.update(task, completed=1)
            return result
        except FileNotFoundError as e:
            console.print(f"[red]Comando não encontrado: {cmd[0]}[/red]")
            raise typer.Exit(1) from e


def get_git_worktrees() -> list[dict]:
    """Lista worktrees ativas."""
    result = run_cmd(["git", "worktree", "list", "--porcelain"], capture=True)
    trees: list[dict] = []
    current: dict = {}
    for line in result.stdout.splitlines():
        if line.startswith("worktree "):
            if current:
                trees.append(current)
            current = {"path": line[9:], "branch": "", "head": ""}
        elif line.startswith("branch "):
            current["branch"] = line[7:]
        elif line.startswith("HEAD "):
            current["head"] = line[5:]
    if current:
        trees.append(current)
    return trees


# ---------------------------------------------------------------------------
# REPL
# ---------------------------------------------------------------------------

def repl_loop() -> None:
    """Modo interativo REPL para gerenciamento contínuo."""
    console.print(Panel.fit(
        f"[bold green]{APP_NAME} v{VERSION}[/bold green]\n"
        "[cyan]Comandos:[/cyan] test, worktree, promote, inject, status, exit\n"
        "[dim]Ex: test --suite tui | worktree --switch axeguard | promote --branch main[/dim]",
        title="REPL Harness",
        border_style="green",
    ))
    while True:
        try:
            raw = Prompt.ask("[bold green]petroshield>[/bold green]").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[yellow]Saindo...[/yellow]")
            break
        if not raw:
            continue
        if raw in ("exit", "quit", "q"):
            break
        parts = raw.split()
        cmd, args = parts[0], parts[1:]
        try:
            if cmd == "test":
                suite = args[1] if len(args) >= 2 and args[0] == "--suite" else "all"
                run_test_suite(suite)
            elif cmd == "worktree":
                if len(args) >= 2 and args[0] == "--switch":
                    switch_worktree(args[1])
                else:
                    show_worktrees()
            elif cmd == "promote":
                branch = args[1] if len(args) >= 2 and args[0] == "--branch" else "main"
                ver = args[3] if len(args) >= 4 and args[2] == "--version" else None
                promote_branch(branch, ver)
            elif cmd == "inject":
                n = int(args[1]) if len(args) >= 2 else 100
                inject_synthetic(n)
            elif cmd == "status":
                show_status()
            else:
                console.print(f"[yellow]Comando desconhecido: {cmd}[/yellow]")
        except Exception as e:
            console.print(f"[red]Erro: {e}[/red]")
            emit_telemetry("repl_error", {"cmd": raw, "error": str(e)}, level="ERROR")


# ---------------------------------------------------------------------------
# Comandos Implementados
# ---------------------------------------------------------------------------

def show_status() -> None:
    """Mostra status geral do ecossistema."""
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body"),
    )
    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right"),
    )

    # Header
    header_text = Text()
    header_text.append(f"{APP_NAME} ", style="bold green")
    header_text.append(f"v{VERSION}", style="cyan")
    layout["header"].update(Panel(header_text, style="green"))

    # Worktrees
    trees = get_git_worktrees()
    tbl = Table(title="Worktrees Git", box=box.ROUNDED, border_style="cyan")
    tbl.add_column("Path", style="green")
    tbl.add_column("Branch", style="magenta")
    tbl.add_column("HEAD", style="dim")
    for t in trees:
        tbl.add_row(t.get("path", "")[-40:], t.get("branch", "").split("/")[-1], t.get("head", "")[:8])
    layout["left"].update(tbl)

    # Test Suites
    tbl2 = Table(title="Test Suites", box=box.ROUNDED, border_style="orange3")
    tbl2.add_column("Suite", style="cyan")
    tbl2.add_column("Arquivo", style="green")
    tbl2.add_column("Descrição", style="white")
    for key, (path, desc) in TEST_SUITES.items():
        full = PROJECT_ROOT / path
        status = "[green]✓" if full.exists() else "[red]✗"
        tbl2.add_row(f"{status} {key}", path, desc)
    layout["right"].update(tbl2)

    console.print(layout)
    emit_telemetry("status_viewed", {"worktrees": len(trees)})


def show_worktrees() -> None:
    show_status()


def switch_worktree(name: str) -> None:
    """Troca para worktree especificada."""
    path = WORKTREES.get(name)
    if not path:
        console.print(f"[red]Worktree '{name}' não encontrada. Opções: {list(WORKTREES.keys())}[/red]")
        raise typer.Exit(1)
    if not path.exists():
        console.print(f"[red]Diretório não existe: {path}[/red]")
        raise typer.Exit(1)
    console.print(f"[green]→ Entrando em worktree {name}: {path}[/green]")
    os.chdir(path)
    emit_telemetry("worktree_switch", {"target": name, "path": str(path)})


def run_test_suite(suite: str) -> None:
    """Executa suite de testes com relatório Rich."""
    targets = list(TEST_SUITES.keys()) if suite == "all" else [suite]
    invalid = [t for t in targets if t not in TEST_SUITES]
    if invalid:
        console.print(f"[red]Suites invalidas: {invalid}[/red]")
        raise typer.Exit(1)

    results: list[dict] = []
    for key in targets:
        path, desc = TEST_SUITES[key]
        full = PROJECT_ROOT / path
        if not full.exists():
            console.print(f"[yellow]Arquivo nao encontrado: {path}[/yellow]")
            continue

        console.rule(f"[bold cyan]Suite: {key}[/bold cyan]")
        cmd = [sys.executable, "-m", "pytest", str(full), "-v", "--tb=short"]
        if key == "theatre":
            # smoke test via execucao direta
            cmd = [sys.executable, str(PROJECT_ROOT / "scripts" / "agentic_soc" / "theatre.py"), "--mode", "mock", "--verbose"]

        start = time.time()
        result = run_cmd(cmd, cwd=PROJECT_ROOT, capture=True)
        elapsed = time.time() - start

        passed = result.returncode == 0
        results.append({"suite": key, "passed": passed, "elapsed": elapsed, "stdout": result.stdout[-500:], "stderr": result.stderr[-300:]})

        style = "green" if passed else "red"
        icon = "[OK]" if passed else "[FAIL]"
        console.print(f"[{style}]{icon} {key} em {elapsed:.2f}s (rc={result.returncode})[/{style}]")
        if not passed and result.stderr:
            console.print(Panel(result.stderr[-500:], title="stderr", border_style="red"))

    # Resumo
    tbl = Table(title="Resumo de Testes", box=box.DOUBLE_EDGE, border_style="green")
    tbl.add_column("Suite", style="cyan")
    tbl.add_column("Status", style="bold")
    tbl.add_column("Tempo", justify="right", style="white")
    total_pass = 0
    for r in results:
        ok = "[green]PASS" if r["passed"] else "[red]FAIL"
        if r["passed"]:
            total_pass += 1
        tbl.add_row(r["suite"], ok, f"{r['elapsed']:.2f}s")
    console.print(tbl)
    emit_telemetry("test_suite_run", {"suite": suite, "results": results, "total_pass": total_pass, "total": len(results)})


def promote_branch(branch: str, version: Optional[str]) -> None:
    """Promove branch para latest working version (.V)."""
    ver = version or datetime.now().strftime("v%Y.%m.%d-%H%M")
    tag = f"prod-{ver}"
    console.print(f"[cyan]Promovendo branch '{branch}' → tag '{tag}'[/cyan]")

    # Checkout branch
    r1 = run_cmd(["git", "checkout", branch], capture=True)
    if r1.returncode != 0:
        console.print(f"[red]Falha ao checkout {branch}:\n{r1.stderr}[/red]")
        raise typer.Exit(1)

    # Tag
    r2 = run_cmd(["git", "tag", "-a", tag, "-m", f"Prod latest working {ver}"], capture=True)
    if r2.returncode != 0:
        console.print(f"[red]Falha ao criar tag:\n{r2.stderr}[/red]")
        raise typer.Exit(1)

    # Push tag
    r3 = run_cmd(["git", "push", "origin", tag], capture=True)
    if r3.returncode != 0:
        console.print(f"[yellow]Push tag falhou (talvez já exista): {r3.stderr}[/yellow]")

    console.print(f"[green]✅ Branch '{branch}' promovida para '{tag}'[/green]")
    console.print(f"[dim]Deploy trigger: git push origin {branch}[/dim]")
    emit_telemetry("branch_promoted", {"branch": branch, "version": ver, "tag": tag})


def inject_synthetic(count: int) -> None:
    """Injetar dados sintéticos via mock_data.py generators."""
    console.print(f"[cyan]Injetando {count} registros sintéticos...[/cyan]")
    # Import dinâmico para não quebrar se não houver deps
    try:
        sys.path.insert(0, str(PROJECT_ROOT))
        from scripts.agentic_soc.mock_data import generate_xr_devices_bulk, generate_monthly_metrics_bulk
        devices = generate_xr_devices_bulk(count)
        metrics = generate_monthly_metrics_bulk(count // 10)
        console.print(f"[green]✅ {len(devices)} devices + {len(metrics)} métricas gerados.[/green]")
        emit_telemetry("synthetic_inject", {"devices": len(devices), "metrics": len(metrics)})
    except ImportError as e:
        console.print(f"[yellow]Generators não disponíveis: {e}\nVerifique se mock_data.py possui generate_xr_devices_bulk.[/yellow]")
        emit_telemetry("synthetic_inject_error", {"error": str(e)}, level="ERROR")


# ---------------------------------------------------------------------------
# Typer CLI Definitions
# ---------------------------------------------------------------------------

@app.command()
def status() -> None:
    """Mostra status do ecossistema PetroShield."""
    show_status()


@app.command()
def test(
    suite: str = typer.Option("all", "--suite", "-s", help="Suite a executar: tui, orchestrator, theatre, all"),
) -> None:
    """Executa suites de testes integradas."""
    run_test_suite(suite)


@app.command()
def worktree(
    switch: Optional[str] = typer.Option(None, "--switch", "-w", help="Trocar para worktree: main, axeguard, classic, python-core"),
) -> None:
    """Lista ou troca worktrees."""
    if switch:
        switch_worktree(switch)
    else:
        show_worktrees()


@app.command()
def promote(
    branch: str = typer.Option(..., "--branch", "-b", help="Branch a promover"),
    version: Optional[str] = typer.Option(None, "--version", "-v", help="Versão (default: timestamp)"),
) -> None:
    """Promove branch para latest working version (.V) e cria tag."""
    promote_branch(branch, version)


@app.command()
def inject(
    count: int = typer.Option(100, "--count", "-n", help="Quantidade de registros sintéticos"),
) -> None:
    """Injeta dados sintéticos para stress-test."""
    inject_synthetic(count)


@app.command()
def repl() -> None:
    """Inicia modo REPL interativo."""
    repl_loop()


@app.command()
def telemetry(
    tail: int = typer.Option(20, "--tail", "-n", help="Últimos N eventos"),
) -> None:
    """Visualiza log de telemetria local."""
    if not TELEMETRY_LOG.exists():
        console.print("[yellow]Nenhum log de telemetria encontrado.[/yellow]")
        return
    lines = TELEMETRY_LOG.read_text(encoding="utf-8").strip().splitlines()
    tbl = Table(title="Telemetry Log", box=box.ROUNDED, border_style="purple")
    tbl.add_column("Timestamp", style="dim")
    tbl.add_column("Event", style="cyan")
    tbl.add_column("Level", style="bold")
    tbl.add_column("Payload", style="green")
    for line in lines[-tail:]:
        try:
            obj = json.loads(line)
            payload = json.dumps(obj.get("payload", {}), ensure_ascii=False)[:60]
            tbl.add_row(obj.get("ts", ""), obj.get("event", ""), obj.get("level", ""), payload)
        except json.JSONDecodeError:
            continue
    console.print(tbl)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    emit_telemetry("harness_start", {"argv": sys.argv[1:]})
    try:
        app()
    except Exception as e:
        emit_telemetry("harness_fatal", {"error": str(e)}, level="ERROR")
        raise


if __name__ == "__main__":
    main()
