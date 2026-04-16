#!/usr/bin/env pwsh
<#
.SYNOPSIS
    PetroShield Test Runner -- Orchestrator + TUI Integration Tests
.DESCRIPTION
    Runs the full test suite for:
      * scripts.agentic_soc.orchestrator
      * scripts.dlp_proxy.demo_ui (TUI)
    Creates venv automatically if missing.
.PARAMETER Install
    Force recreate venv and install dependencies before testing.
.PARAMETER Update
    Update dependencies before testing.
.PARAMETER Fast
    Skip TUI tests (orchestrator only) for faster feedback.
.EXAMPLE
    .\run_tests.ps1
    .\run_tests.ps1 -Install
    .\run_tests.ps1 -Fast
#>

[CmdletBinding()]
param(
    [switch]$Install,
    [switch]$Update,
    [switch]$Fast
)

$ErrorActionPreference = "Stop"

# Encoding guard
$env:PYTHONIOENCODING = "utf-8"
if ($null -eq $env:PYTHONUTF8) { $env:PYTHONUTF8 = "1" }

$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
if ([string]::IsNullOrWhiteSpace($ScriptRoot)) { $ScriptRoot = (Get-Location).Path }
Set-Location -Path $ScriptRoot

Write-Host ""
Write-Host "===============================================================" -ForegroundColor DarkCyan
Write-Host "     PETROSHIELD AXEGUARD -- TEST RUNNER v1.0                 " -ForegroundColor DarkCyan
Write-Host "===============================================================" -ForegroundColor DarkCyan
Write-Host ""

# -- Ensure venv ------------------------------------------------------------
function Ensure-VEnv {
    if ($Install -or -not (Test-Path ".\.venv\Scripts\python.exe")) {
        if (Test-Path ".\.venv") { Remove-Item -Recurse -Force ".\.venv" }
        Write-Host "[+] Creating virtual environment..." -ForegroundColor Yellow
        python -m venv .\.venv
        $Update = $true
    }
    if ($Update) {
        Write-Host "[+] Updating dependencies..." -ForegroundColor Yellow
        .\.venv\Scripts\python.exe -m pip install --upgrade pip | Out-Null
        $reqFiles = @(
            "scripts\agentic_soc\requirements.txt",
            "scripts\dlp_proxy\requirements.txt"
        )
        foreach ($req in $reqFiles) {
            if (Test-Path $req) {
                Write-Host "    -> $req" -ForegroundColor Gray
                .\.venv\Scripts\python.exe -m pip install -r $req | Out-Null
            }
        }
        # Optional: skip heavy editable install to keep tests fast
        # if (Test-Path "pyproject.toml") {
        #     Write-Host "    -> pip install -e ." -ForegroundColor Gray
        #     .\.venv\Scripts\python.exe -m pip install -e . | Out-Null
        # }
    }
}

Ensure-VEnv

$python = ".\.venv\Scripts\python.exe"
$exitCodes = @()

# -- Orchestrator Tests -----------------------------------------------------
Write-Host ""
Write-Host "> TEST SUITE 1: Orchestrator Data Flows" -ForegroundColor Cyan
Write-Host "-----------------------------------------" -ForegroundColor Gray
& $python -m unittest tests.test_orchestrator -v
$exitCodes += $LASTEXITCODE

# -- Orchestrator Self-Test -------------------------------------------------
Write-Host ""
Write-Host "> TEST SUITE 2: Orchestrator Self-Test (flag --test)" -ForegroundColor Cyan
Write-Host "------------------------------------------------------" -ForegroundColor Gray
& $python -m scripts.agentic_soc.orchestrator --test
$exitCodes += $LASTEXITCODE

# -- TUI Tests --------------------------------------------------------------
if (-not $Fast) {
    Write-Host ""
    Write-Host "> TEST SUITE 3: TUI Integration (demo_ui.py)" -ForegroundColor Cyan
    Write-Host "----------------------------------------------" -ForegroundColor Gray
    & $python -m unittest tests.test_tui -v
    $exitCodes += $LASTEXITCODE
} else {
    Write-Host ""
    Write-Host "> TEST SUITE 3: TUI Integration SKIPPED (-Fast)" -ForegroundColor DarkYellow
}

# -- Theatre Engine Smoke Tests ---------------------------------------------
Write-Host ""
Write-Host "> TEST SUITE 4: Theatre Engine Smoke Tests" -ForegroundColor Cyan
Write-Host "--------------------------------------------" -ForegroundColor Gray
$theatreSmokePy = Join-Path $env:TEMP "theatre_smoke_test.ps1tmp.py"
@'
from scripts.agentic_soc.theatre import TheatreEngine
engine = TheatreEngine(quiet=True)
workflows = [w['scene_id'] for w in engine.scenarios]
assert len(workflows) >= 12, 'Expected 12+ workflows'
for wf in workflows:
    result = engine.run_scene(wf)
    assert result['final_state'] is not None, '%s: no final state' % wf
    print('  [OK] %s -> %s' % (wf, result['final_state'].get('dlp_action', 'N/A')))
print('  [PASS] All workflow smoke tests passed')
'@ | Set-Content -Path $theatreSmokePy -Encoding UTF8
& $python $theatreSmokePy
$exitCodes += $LASTEXITCODE

# -- Summary ----------------------------------------------------------------
Write-Host ""
Write-Host "===============================================================" -ForegroundColor DarkCyan
if ($exitCodes -contains 1) {
    Write-Host "  RESULT: SOME TESTS FAILED" -ForegroundColor Red
    exit 1
} else {
    Write-Host "  RESULT: ALL TESTS PASSED" -ForegroundColor Green
    exit 0
}
