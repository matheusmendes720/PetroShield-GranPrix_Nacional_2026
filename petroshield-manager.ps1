#Requires -Version 5.1
<#
  petroshield-manager.ps1 — PetroShield AxeGuard TUI Manager
  ==========================================================
  Orquestrador unificado em PowerShell para:
    • Gerenciar worktrees git (axeguard, classic, main, python-core)
    • Executar testes suites (TUI, Orchestrator, Theatre)
    • Promover branch para prod latest working (.V)
    • Injetar dados sintéticos em massa
    • Telemetry logging serverless-ready
    • Build e deploy para Netlify

  Uso:
    .\petroshield-manager.ps1 status
    .\petroshield-manager.ps1 test -Suite all
    .\petroshield-manager.ps1 worktree -Switch axeguard
    .\petroshield-manager.ps1 promote -Branch tui-axeguard -Version v2.6
    .\petroshield-manager.ps1 inject -Count 10000
    .\petroshield-manager.ps1 build-netlify -App axeguard
    .\petroshield-manager.ps1 repl

  Requisitos:
    • git, python, bun (no PATH)
    • venv Python em .\.venv ou .venv
#>

[CmdletBinding()]
param(
  [Parameter(Mandatory = $false, Position = 0)]
  [ValidateSet("status", "test", "worktree", "promote", "inject", "build-netlify", "deploy-netlify", "repl", "telemetry", "help")]
  [string]$Command = "status",

  [Parameter(Mandatory = $false)]
  [ValidateSet("tui", "orchestrator", "theatre", "all")]
  [string]$Suite = "all",

  [Parameter(Mandatory = $false)]
  [ValidateSet("main", "axeguard", "classic", "python-core")]
  [string]$Switch,

  [Parameter(Mandatory = $false)]
  [string]$Branch = "main",

  [Parameter(Mandatory = $false)]
  [string]$Version,

  [Parameter(Mandatory = $false)]
  [int]$Count = 100,

  [Parameter(Mandatory = $false)]
  [ValidateSet("axeguard", "classic")]
  [string]$App = "axeguard",

  [Parameter(Mandatory = $false)]
  [int]$Tail = 20,

  [Parameter(Mandatory = $false)]
  [switch]$Verbose
)

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
$ErrorActionPreference = "Stop"
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'

$Script:ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Script:TelemetryLog = Join-Path $Script:ProjectRoot ".local\telemetry_ps.jsonl"
$Script:Worktrees = @{
  main        = $Script:ProjectRoot
  axeguard    = Join-Path $Script:ProjectRoot "outer-tui-axeguard-ts"
  classic     = Join-Path $Script:ProjectRoot "outer-tui-classic-ts"
  python-core = Join-Path $Script:ProjectRoot "scripts\dlp_proxy"
}
$Script:TestSuites = @{
  tui          = @{ File = "tests\test_tui.py"; Desc = "TUI Integration — 16 casos"; Cmd = "pytest" }
  orchestrator = @{ File = "tests\test_orchestrator.py"; Desc = "Orchestrator — 18 casos"; Cmd = "pytest" }
  theatre      = @{ File = "scripts\agentic_soc\theatre.py"; Desc = "Theatre Agentic — smoke"; Cmd = "python" }
}

# Cores para console
function Write-Color($Text, $Color = "White") {
  Write-Host $Text -ForegroundColor $Color
}
function Write-Success($Text) { Write-Color "[✅] $Text" "Green" }
function Write-Warn($Text)  { Write-Color "[⚠️] $Text" "Yellow" }
function Write-Error($Text) { Write-Color "[❌] $Text" "Red" }
function Write-Info($Text)  { Write-Color "[ℹ️] $Text" "Cyan" }

# ---------------------------------------------------------------------------
# Telemetry
# ---------------------------------------------------------------------------
function Emit-Telemetry {
  param([string]$Event, [hashtable]$Payload, [string]$Level = "INFO")
  $entry = @{
    ts      = (Get-Date -Format "o")
    level   = $Level
    source  = "petroshield-manager.ps1"
    event   = $Event
    payload = $Payload
    host    = $env:COMPUTERNAME
    version = "2.6.0"
  } | ConvertTo-Json -Compress -Depth 3
  $dir = Split-Path -Parent $Script:TelemetryLog
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Path $dir -Force | Out-Null }
  Add-Content -Path $Script:TelemetryLog -Value $entry
  if ($Verbose) { Write-Color "[telemetry][$Level] $Event" $(if($Level -eq "ERROR"){"Red"}else{"DarkGray"}) }
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
function Invoke-GitCmd {
  param([string[]]$Args)
  $proc = Start-Process git -ArgumentList $Args -WorkingDirectory $Script:ProjectRoot -PassThru -NoNewWindow -Wait
  return $proc.ExitCode
}

function Invoke-PythonCmd {
  param([string]$Args)
  $python = if (Test-Path "$Script:ProjectRoot\.venv\Scripts\python.exe") { "$Script:ProjectRoot\.venv\Scripts\python.exe" }
            elseif (Test-Path "$Script:ProjectRoot\venv\Scripts\python.exe") { "$Script:ProjectRoot\venv\Scripts\python.exe" }
            else { "python" }
  $cmd = "$python $Args"
  if ($Verbose) { Write-Info "Running: $cmd" }
  Invoke-Expression $cmd
}

function Invoke-BunCmd {
  param([string]$Args, [string]$Cwd)
  $dir = if ($Cwd) { $Cwd } else { $Script:ProjectRoot }
  $cmd = "bun $Args"
  if ($Verbose) { Write-Info "Running in $dir`: $cmd" }
  Push-Location $dir
  try { Invoke-Expression $cmd } finally { Pop-Location }
}

# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------
function Show-Status {
  Write-Color "=== PetroShield AxeGuard Manager v2.6 ===" "Green"
  Write-Color "Project Root: $Script:ProjectRoot" "DarkGray"
  Write-Color ""

  # Git worktrees
  Write-Color "Git Worktrees:" "Cyan"
  $trees = git -C $Script:ProjectRoot worktree list --porcelain 2>$null
  if ($trees) {
    $trees | Select-String "worktree|branch|HEAD" | ForEach-Object { Write-Color "  $_" "White" }
  } else {
    Write-Warn "Nenhuma worktree listada"
  }

  Write-Color ""
  Write-Color "Test Suites:" "Cyan"
  foreach ($key in $Script:TestSuites.Keys) {
    $s = $Script:TestSuites[$key]
    $full = Join-Path $Script:ProjectRoot $s.File
    $ok = if (Test-Path $full) { "[✅]" } else { "[❌]" }
    Write-Color "  $ok $key — $($s.Desc)" $(if(Test-Path $full){"Green"}else{"Red"})
  }

  Write-Color ""
  Write-Color "Netlify Sites:" "Cyan"
  Write-Color "  AxeGuard:  https://petroshield-app.netlify.app" "Green"
  Write-Color "  Classic:   https://petroshield-classic.netlify.app" "Green"

  Emit-Telemetry -Event "status_viewed" -Payload @{ worktrees = ($trees -split "`n" | Measure-Object).Count }
}

function Invoke-TestSuite {
  param([string]$SuiteName)
  $targets = if ($SuiteName -eq "all") { @("tui", "orchestrator", "theatre") } else { @($SuiteName) }
  foreach ($key in $targets) {
    $s = $Script:TestSuites[$key]
    $full = Join-Path $Script:ProjectRoot $s.File
    if (-not (Test-Path $full)) { Write-Error "Arquivo não encontrado: $($s.File)"; continue }

    Write-Color "--- Suite: $key ---" "Cyan"
    $sw = [System.Diagnostics.Stopwatch]::StartNew()
    try {
      if ($s.Cmd -eq "pytest") {
        Invoke-PythonCmd "-m pytest `"$full`" -v --tb=short"
      } else {
        Invoke-PythonCmd "`"$full`" --mode mock --verbose"
      }
      $sw.Stop()
      Write-Success "$key concluído em $($sw.Elapsed.TotalSeconds.ToString("F2"))s"
      Emit-Telemetry -Event "test_passed" -Payload @{ suite = $key; elapsed_sec = $sw.Elapsed.TotalSeconds }
    } catch {
      $sw.Stop()
      Write-Error "$key falhou: $_"
      Emit-Telemetry -Event "test_failed" -Payload @{ suite = $key; error = $_.Exception.Message } -Level "ERROR"
    }
  }
}

function Switch-Worktree {
  param([string]$Name)
  $path = $Script:Worktrees[$Name]
  if (-not $path) {
    Write-Error "Worktree '$Name' desconhecida. Use: $($Script:Worktrees.Keys -join ', ')"
    exit 1
  }
  if (-not (Test-Path $path)) {
    Write-Error "Diretório não existe: $path"
    exit 1
  }
  Set-Location $path
  Write-Success "Worktree ativa: $Name → $path"
  Emit-Telemetry -Event "worktree_switch" -Payload @{ target = $Name; path = $path }
}

function Promote-Branch {
  param([string]$BranchName, [string]$Ver)
  $tagVer = if ($Ver) { $Ver } else { (Get-Date -Format "vyyyy.MM.dd-HHmm") }
  $tag = "prod-$tagVer"
  Write-Info "Promovendo '$BranchName' → tag '$tag'"

  $rc = Invoke-GitCmd @("checkout", $BranchName)
  if ($rc -ne 0) { Write-Error "Checkout falhou"; exit 1 }

  $rc = Invoke-GitCmd @("tag", "-a", $tag, "-m", "Prod latest working $tagVer")
  if ($rc -ne 0) { Write-Error "Tag falhou"; exit 1 }

  $rc = Invoke-GitCmd @("push", "origin", $tag)
  if ($rc -ne 0) { Write-Warn "Push tag falhou (talvez já exista)" }

  Write-Success "Branch '$BranchName' promovida para '$tag'"
  Emit-Telemetry -Event "branch_promoted" -Payload @{ branch = $BranchName; version = $tagVer; tag = $tag }
}

function Invoke-SyntheticInject {
  param([int]$N)
  Write-Info "Injetando $N registros sintéticos..."
  $py = @"
import sys
sys.path.insert(0, r'$Script:ProjectRoot')
from scripts.agentic_soc.mock_data import generate_xr_devices_bulk, generate_monthly_metrics_bulk
devs = generate_xr_devices_bulk($N)
metrics = generate_monthly_metrics_bulk(max(1, $N // 10))
print(f'✅ {len(devs)} devices + {len(metrics)} métricas gerados.')
"@
  try {
    Invoke-PythonCmd "-c `"$py`""
    Emit-Telemetry -Event "synthetic_inject" -Payload @{ count = $N }
  } catch {
    Write-Error "Falha na injeção: $_"
    Emit-Telemetry -Event "synthetic_inject_error" -Payload @{ error = $_.Exception.Message } -Level "ERROR"
  }
}

function Build-Netlify {
  param([string]$AppName)
  $dir = if ($AppName -eq "axeguard") { $Script:Worktrees.axeguard } else { $Script:Worktrees.classic }
  Write-Info "Buildando $AppName em $dir..."
  try {
    Invoke-BunCmd -Args "install" -Cwd $dir
    Invoke-BunCmd -Args "run build" -Cwd $dir
    Write-Success "Build $AppName completo. Artefatos em $dir\dist"
    Emit-Telemetry -Event "build_success" -Payload @{ app = $AppName }
  } catch {
    Write-Error "Build $AppName falhou: $_"
    Emit-Telemetry -Event "build_failed" -Payload @{ app = $AppName; error = $_.Exception.Message } -Level "ERROR"
  }
}

function Deploy-Netlify {
  param([string]$AppName)
  $dir = if ($AppName -eq "axeguard") { $Script:Worktrees.axeguard } else { $Script:Worktrees.classic }
  $siteId = if ($AppName -eq "axeguard") { "a0be275a-293d-4aa0-b61e-9df9d9119730" } else { "c8fb18d0-a002-4437-b9eb-f81320ec8609" }
  Write-Info "Deployando $AppName para Netlify..."
  try {
    # Assumimos que netlify-cli está instalado globalmente ou via bunx
    $cmd = "netlify deploy --prod --dir=`"$dir\web`" --site=$siteId"
    Invoke-Expression $cmd
    Write-Success "Deploy $AppName completo."
    Emit-Telemetry -Event "deploy_success" -Payload @{ app = $AppName; site_id = $siteId }
  } catch {
    Write-Error "Deploy $AppName falhou: $_"
    Emit-Telemetry -Event "deploy_failed" -Payload @{ app = $AppName; error = $_.Exception.Message } -Level "ERROR"
  }
}

function Show-Telemetry {
  param([int]$Lines)
  if (-not (Test-Path $Script:TelemetryLog)) {
    Write-Warn "Nenhum log de telemetria encontrado."
    return
  }
  $last = Get-Content $Script:TelemetryLog -Tail $Lines
  Write-Color "=== Últimos $Lines eventos de telemetria ===" "Cyan"
  foreach ($line in $last) {
    try {
      $obj = $line | ConvertFrom-Json
      $color = switch ($obj.level) { "ERROR" { "Red" } "WARN" { "Yellow" } default { "Green" } }
      Write-Color "[$($obj.ts)] [$($obj.level)] $($obj.event) — $($obj.payload | ConvertTo-Json -Compress -Depth 2)" $color
    } catch {
      Write-Color $line "DarkGray"
    }
  }
}

function Start-Repl {
  Write-Color "=== PetroShield Manager REPL ===" "Green"
  Write-Color "Comandos: status, test, worktree, promote, inject, build-netlify, deploy-netlify, telemetry, exit" "DarkGray"
  while ($true) {
    $raw = Read-Host "petroshield>"
    if (-not $raw) { continue }
    $parts = $raw -split '\s+'
    $cmd = $parts[0].ToLower()
    $rest = $parts[1..$parts.Length]

    switch ($cmd) {
      "exit"   { break }
      "quit"   { break }
      "q"      { break }
      "status" { Show-Status }
      "test"   { Invoke-TestSuite -SuiteName ($rest[0] -replace "^--suite=","" -replace "^-s=","" -or "all") }
      "worktree" {
        if ($rest[0]) { Switch-Worktree -Name ($rest[0] -replace "^--switch=","" -replace "^-w=","") }
        else { Show-Status }
      }
      "promote" {
        $b = ($rest -match "^--branch=(.+)$")[0] -replace "^--branch=","" -or "main"
        $v = ($rest -match "^--version=(.+)$")[0] -replace "^--version=",""
        Promote-Branch -BranchName $b -Ver $v
      }
      "inject" {
        $n = [int](($rest -match "^--count=(\d+)$")[0] -replace "^--count=","" -or 100)
        Invoke-SyntheticInject -N $n
      }
      "build-netlify" {
        $a = ($rest -match "^--app=(.+)$")[0] -replace "^--app=","" -or "axeguard"
        Build-Netlify -AppName $a
      }
      "deploy-netlify" {
        $a = ($rest -match "^--app=(.+)$")[0] -replace "^--app=","" -or "axeguard"
        Deploy-Netlify -AppName $a
      }
      "telemetry" {
        $n = [int](($rest -match "^--tail=(\d+)$")[0] -replace "^--tail=","" -or 20)
        Show-Telemetry -Lines $n
      }
      default { Write-Warn "Comando desconhecido: $cmd" }
    }
    if ($cmd -in @("exit","quit","q")) { break }
  }
  Write-Color "Saindo do REPL..." "Yellow"
}

# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------
switch ($Command) {
  "status"        { Show-Status }
  "test"          { Invoke-TestSuite -SuiteName $Suite }
  "worktree"      { if ($Switch) { Switch-Worktree -Name $Switch } else { Show-Status } }
  "promote"       { Promote-Branch -BranchName $Branch -Ver $Version }
  "inject"        { Invoke-SyntheticInject -N $Count }
  "build-netlify" { Build-Netlify -AppName $App }
  "deploy-netlify"{ Deploy-Netlify -AppName $App }
  "telemetry"     { Show-Telemetry -Lines $Tail }
  "repl"          { Start-Repl }
  "help"          {
    Write-Color @"
PetroShield Manager v2.6
========================
Comandos:
  status          — Status do ecossistema
  test            — Executar suites de teste (-Suite tui|orchestrator|theatre|all)
  worktree        — Listar ou trocar worktree (-Switch main|axeguard|classic)
  promote         — Promover branch para prod (-Branch, -Version)
  inject          — Injetar dados sintéticos (-Count N)
  build-netlify   — Build para Netlify (-App axeguard|classic)
  deploy-netlify  — Deploy para Netlify (-App axeguard|classic)
  telemetry       — Ver logs de telemetria (-Tail N)
  repl            — Modo interativo
  help            — Esta mensagem
"@ "Cyan"
  }
}

Emit-Telemetry -Event "manager_invoked" -Payload @{ command = $Command; suite = $Suite; branch = $Branch }
