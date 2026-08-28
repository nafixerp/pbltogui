@echo off
REM Build a standalone Windows executable: dist\SuperGold.exe
setlocal
cd /d "%~dp0"
python -m pip install -r requirements-dev.txt
pyinstaller JewelleryERP.spec
echo.
echo Built: dist\SuperGold.exe
pause
endlocal
