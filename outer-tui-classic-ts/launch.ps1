#Requires -Version 5.1
<#
  launch.ps1 — PetroShield Classic TUI Launcher
  Uso: .\launch.ps1 [-Dev] [-Build]
#>
param(
  [switch]$Dev,
  [switch]$Build
)

$ErrorActionPreference = "Stop"
$dir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $dir

if (-not (Get-Command bun -ErrorAction SilentlyContinue)) {
  Write-Host "[ERRO] Bun não encontrado no PATH." -ForegroundColor Red
  exit 1
}

Write-Host "=== PetroShield Classic TUI ===" -ForegroundColor Cyan

if ($Build) {
  Write-Host "Building..." -ForegroundColor Yellow
  bun run build
  Write-Host "Build completo. Artefatos em ./dist" -ForegroundColor Green
  exit 0
}

if ($Dev) {
  Write-Host "Modo DEV (hot reload via bun)..." -ForegroundColor Green
  bun run dev
} else {
  if (-not (Test-Path "dist/index.js")) {
    Write-Host "Binário não encontrado. Compilando primeiro..." -ForegroundColor Yellow
    bun run build
  }
  Write-Host "Launching TUI..." -ForegroundColor Green
  bun run launch
}
