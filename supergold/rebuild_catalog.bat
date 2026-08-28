@echo off
REM Re-generate data\menu.json and data\windows.json from a PowerBuilder export.
REM Point --source at the folder that holds the gmine* source folders.
setlocal
cd /d "%~dp0"
python tools\build_catalog.py --source "%~1" --out data
pause
endlocal
