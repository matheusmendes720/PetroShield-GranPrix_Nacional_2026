@echo off
chcp 65001 >nul
REM PetroShield TUI Local Launcher (Windows Batch)
REM Uso: launch-tuis.bat [axeguard|classic|harness|all]

set BUN=C:\pinokio\bin\npm\node_modules\bun\bin\bun.exe
set PYTHON=.venv\Scripts\python.exe

if "%1"=="axeguard" goto :axeguard
if "%1"=="classic" goto :classic
if "%1"=="harness" goto :harness
if "%1"=="all" goto :all
if "%1"=="" goto :menu

echo [ERRO] Uso: launch-tuis.bat [axeguard ^| classic ^| harness ^| all]
exit /b 1

:menu
echo =========================================
echo   PetroShield TUI Local Launcher
echo =========================================
echo 1. AxeGuard  (Ink/React terminal)
echo 2. Classic   (Blessed terminal)
echo 3. Harness   (Typer+Rich REPL)
echo 4. ALL       (sequencial)
echo =========================================
set /p choice="Escolha (1-4): "
if "%choice%"=="1" goto :axeguard
if "%choice%"=="2" goto :classic
if "%choice%"=="3" goto :harness
if "%choice%"=="4" goto :all
goto :menu

:axeguard
echo [LAUNCH] AxeGuard TUI...
cd /d "%~dp0outer-tui-axeguard-ts"
start "AxeGuard TUI" cmd /k "%BUN% run dev"
cd /d "%~dp0"
goto :eof

:classic
echo [LAUNCH] Classic TUI...
cd /d "%~dp0outer-tui-classic-ts"
start "Classic TUI" cmd /k "%BUN% run dev"
cd /d "%~dp0"
goto :eof

:harness
echo [LAUNCH] PetroShield Harness REPL...
cd /d "%~dp0"
start "Harness REPL" cmd /k "%PYTHON% -m scripts.manager.harness repl"
goto :eof

:all
echo [LAUNCH] Iniciando todos os TUIs...
call :axeguard
call :classic
call :harness
echo [OK] Todos os terminais foram abertos.
goto :eof
