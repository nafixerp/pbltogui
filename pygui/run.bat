@echo off
REM ---------------------------------------------------------------------------
REM  Jewellery ERP - PowerBuilder to Python (PySide6) launcher (Windows)
REM ---------------------------------------------------------------------------
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo Python was not found on PATH. Install Python 3.10+ and try again.
    pause
    exit /b 1
)

if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
    call .venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
) else (
    call .venv\Scripts\activate.bat
)

python main.py
pause
