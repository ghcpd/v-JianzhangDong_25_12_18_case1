@echo off
REM Activate .venv and run tests (Windows)
if not exist .venv\Scripts\python.exe (
  echo .venv not found. Run setup.sh or create a virtual env first.
  exit /b 2
)
.venv\Scripts\python.exe -u auto_test.py
if %ERRORLEVEL% neq 0 (
  echo Tests finished with errors. See logs\test_run.log
) else (
  echo Tests completed successfully. See logs\test_run.log
)
