@echo off
REM ---------------------------------------------------------------------------
REM  Super Gold - Jewellery ERP.  Double-click this file to start the software.
REM
REM  Needs Python 3.10 or newer installed (python.org -> "Add python.exe to PATH").
REM  The first run installs the required packages; later runs start immediately.
REM ---------------------------------------------------------------------------
setlocal
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found on this computer.
    echo Install Python 3.10+ from https://www.python.org/downloads/
    echo and tick "Add python.exe to PATH" during setup, then run this file again.
    pause
    exit /b 1
)

REM Install/refresh dependencies only when something is missing.
python -c "import PySide6" >nul 2>nul
if errorlevel 1 (
    echo Installing required packages, please wait...
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Package installation failed. Check your internet connection.
        pause
        exit /b 1
    )
)

echo Starting Super Gold...
python main.py
if errorlevel 1 pause
endlocal
