@echo off
REM Activate .venv and run tests on Windows
IF NOT EXIST ".venv\Scripts\activate.bat" (
  echo No .venv found. Run setup.sh or create .venv first.
  exit /b 1
)
call .venv\Scripts\activate.bat
python auto_test.py >> logs\test_run.log 2>&1
echo Test run complete. See logs\test_run.log
