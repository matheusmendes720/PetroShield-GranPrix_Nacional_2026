#!/usr/bin/env pwsh
<#
.SYNOPSIS
    PetroShield AxeGuard -- Unified Launcher for TUI, API, Theatre and Daily Routines
.DESCRIPTION
    Automates venv creation, dependency sync, and launch of:
      * TUI Dashboard (demo_ui)
      * FastAPI Backend (main)
      * Agentic Theatre (theatre)
      * Both API + TUI in split windows
.PARAMETER Mode
    Launch mode: tui | api | theatre | both
.PARAMETER Install
    Force recreate venv and install dependencies.
.PARAMETER Update
    Update dependencies inside existing venv.
.EXAMPLE
    .\launcher.ps1
    .\launcher.ps1 -Mode both
    .\launcher.ps1 -Mode theatre -Update
#>

[CmdletBinding()]
param(
    [ValidateSet("tui", "api", "theatre", "both")]
    [string]$Mode = "tui",

    [switch]$Install,
    [switch]$Update
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "Continue"

# ---------------------------------------------------------------------------
# Environment / Encoding
# ---------------------------------------------------------------------------
$env:PYTHONIOENCODING = "utf-8"
if ($null -eq $env:PYTHONUTF8) { $env:PYTHONUTF8 = "1" }

# ---------------------------------------------------------------------------
# Resolve Project Root
# ---------------------------------------------------------------------------
$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
if ([string]::IsNullOrWhiteSpace($ScriptRoot)) { $ScriptRoot = (Get-Location).Path }
Set-Location -Path $ScriptRoot

# ---------------------------------------------------------------------------
# Branding
# ---------------------------------------------------------------------------
function Write-Banner {
    $banner = @"
`n`n   ====== PETROSHIELD AXEGUARD -- LAUNCHER v2.0 ======
`n   SOC AGENTIC | Grand Prix SENAI Nacional 2026
   Project Root: $ScriptRoot
   Mode        : $Mode
"@
    Write-Host $banner -ForegroundColor DarkGreen
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
function Test-VEnv {
    return Test-Path -Path ".\.venv\Scripts\python.exe"
}

function Install-Dependencies {
    Write-Host "[+] Installing / updating dependencies..." -ForegroundColor Yellow
    $python = ".\.venv\Scripts\python.exe"
    & $python -m pip install --upgrade pip | Out-Null

    $reqFiles = @(
        "scripts\agentic_soc\requirements.txt",
        "scripts\dlp_proxy\requirements.txt"
    )
    foreach ($req in $reqFiles) {
        if (Test-Path $req) {
            Write-Host "    -> pip install -r $req" -ForegroundColor Gray
            & $python -m pip install -r $req | Out-Null
        }
    }
    Write-Host "[OK] Dependencies ready." -ForegroundColor Green
}

function Ensure-VEnv {
    if ($Install -or -not (Test-VEnv)) {
        if (Test-Path ".\.venv") {
            Write-Host "[!] Removing existing venv..." -ForegroundColor DarkYellow
            Remove-Item -Recurse -Force ".\.venv"
        }
        Write-Host "[+] Creating virtual environment (.\.venv) ..." -ForegroundColor Yellow
        python -m venv .\.venv
        if (-not (Test-VEnv)) {
            throw "Failed to create virtual environment. Ensure 'python' is on PATH."
        }
        Install-Dependencies
    }
    elseif ($Update) {
        Install-Dependencies
    }
}

# ---------------------------------------------------------------------------
# Launchers
# ---------------------------------------------------------------------------
function Start-TUI {
    Write-Host "[->] Launching PetroShield TUI Dashboard...`n" -ForegroundColor Cyan
    $python = ".\.venv\Scripts\python.exe"
    & $python -m scripts.dlp_proxy.demo_ui
}

function Start-API {
    Write-Host "[->] Launching FastAPI Backend (DLP Proxy)...`n" -ForegroundColor Cyan
    $python = ".\.venv\Scripts\python.exe"
    & $python -m scripts.dlp_proxy.main
}

function Start-Theatre {
    Write-Host "[->] Launching Agentic Theatre...`n" -ForegroundColor Cyan
    $python = ".\.venv\Scripts\python.exe"
    & $python -m scripts.agentic_soc.theatre
}

function Start-Both {
    Write-Host "[->] Starting FastAPI Backend in background window..." -ForegroundColor Cyan
    $apiCmd = "`$env:PYTHONIOENCODING='utf-8'; `\".\.venv\Scripts\python.exe\" -m scripts.dlp_proxy.main"
    Start-Process -FilePath "powershell.exe" -ArgumentList "-NoExit","-Command",$apiCmd -WindowStyle Normal -WorkingDirectory $ScriptRoot

    Start-Sleep -Seconds 2

    Write-Host "[->] Launching PetroShield TUI Dashboard...`n" -ForegroundColor Cyan
    $python = ".\.venv\Scripts\python.exe"
    & $python -m scripts.dlp_proxy.demo_ui
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
Write-Banner
Ensure-VEnv

try {
    switch ($Mode.ToLower()) {
        "tui"      { Start-TUI }
        "api"      { Start-API }
        "theatre"  { Start-Theatre }
        "both"     { Start-Both }
        default    { Start-TUI }
    }
}
catch {
    Write-Host "`n[X] ERROR: $_" -ForegroundColor Red
    Write-Host "    StackTrace: $($_.ScriptStackTrace)" -ForegroundColor DarkGray
}
finally {
    Write-Host "`n[OK] PetroShield launcher session ended." -ForegroundColor Green
    if ($Mode -eq "both") {
        Write-Host "    Remember to close the API PowerShell window manually." -ForegroundColor Yellow
    }
    Write-Host ""
    if ($Host.Name -eq 'ConsoleHost' -and -not $MyInvocation.ExpectingInput) {
        Write-Host "Press any key to exit..." -ForegroundColor Gray
        $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    }
}
