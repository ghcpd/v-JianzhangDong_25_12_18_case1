@echo off
REM Activate venv and run auto_test.py
if not exist ".venv\Scripts\python.exe" (
  echo .venv not found. Run setup.bat or setup.sh first.
  exit /b 1
)
.venv\Scripts\python.exe auto_test.py
