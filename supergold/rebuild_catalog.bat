@echo off
REM Re-generate the converted definitions from a PowerBuilder export:
REM   data\menu.json  data\windows.json  data\schema.sql
REM Usage:  rebuild_catalog.bat "C:\path\to\folder\with\gmine*\folders"
setlocal
cd /d "%~dp0"
if "%~1"=="" (
    echo Usage: rebuild_catalog.bat "path to the PowerBuilder export folder"
    pause
    exit /b 1
)
python tools\build_catalog.py --source "%~1" --out data
python tools\build_schema.py --source "%~1" --out data\schema.sql --scripts
python tools\build_layouts.py --source "%~1"
pause
endlocal
