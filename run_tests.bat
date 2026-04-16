@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

:: PetroShield Test Runner — Batch Edition
:: Runs orchestrator + TUI tests using the project venv

cd /d "%~dp0"

set "PYTHONIOENCODING=utf-8"
set "PYTHONUTF8=1"

echo.
echo ╔══════════════════════════════════════════════════════════════╗
echo ║     PETROSHIELD AXEGUARD — TEST RUNNER (BATCH)              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.

:: Check for venv
if not exist ".\.venv\Scripts\python.exe" (
    echo [+] Creating virtual environment...
    python -m venv .\.venv
    if errorlevel 1 (
        echo [X] Failed to create venv. Ensure python is on PATH.
        pause
        exit /b 1
    )
    echo [+] Installing dependencies...
    .\.venv\Scripts\python.exe -m pip install --upgrade pip >nul
    if exist "scripts\agentic_soc\requirements.txt" (
        .\.venv\Scripts\python.exe -m pip install -r "scripts\agentic_soc\requirements.txt" >nul
    )
    if exist "scripts\dlp_proxy\requirements.txt" (
        .\.venv\Scripts\python.exe -m pip install -r "scripts\dlp_proxy\requirements.txt" >nul
    )
    if exist "pyproject.toml" (
        .\.venv\Scripts\python.exe -m pip install -e . >nul
    )
)

set "PYTHON=.\.venv\Scripts\python.exe"
set "FAILED=0"

echo.
echo ▶ TEST SUITE 1: Orchestrator Data Flows
echo ─────────────────────────────────────────
%PYTHON% -m unittest tests.test_orchestrator -v
if errorlevel 1 set FAILED=1

echo.
echo ▶ TEST SUITE 2: Orchestrator Self-Test (--test)
echo ─────────────────────────────────────────────────
%PYTHON% -m scripts.agentic_soc.orchestrator --test
if errorlevel 1 set FAILED=1

echo.
echo ▶ TEST SUITE 3: TUI Integration (demo_ui.py)
echo ──────────────────────────────────────────────
%PYTHON% -m unittest tests.test_tui -v
if errorlevel 1 set FAILED=1

echo.
echo ▶ TEST SUITE 4: Theatre Engine Smoke Tests
echo ────────────────────────────────────────────
%PYTHON% -c "from scripts.agentic_soc.theatre import TheatreEngine; engine = TheatreEngine(quiet=True); workflows=[w['scene_id'] for w in engine.scenarios]; assert len(workflows)>=12; [engine.run_scene(w) for w in workflows]; print('  [PASS] All workflow smoke tests passed')"
if errorlevel 1 set FAILED=1

echo.
echo ═══════════════════════════════════════════════════════════════
if "%FAILED%"=="1" (
    echo   RESULT: SOME TESTS FAILED
    exit /b 1
) else (
    echo   RESULT: ALL TESTS PASSED
    exit /b 0
)
