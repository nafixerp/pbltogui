@echo off
REM Launch the Jewellery ERP (development run).
cd /d "%~dp0"
python -m pip install -r requirements.txt
python main.py
