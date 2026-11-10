@echo off
cd /d "%~dp0"
py -3 update-vault-catalog.py
if errorlevel 1 python update-vault-catalog.py
pause
