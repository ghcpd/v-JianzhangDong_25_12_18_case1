@echo off
REM Test execution script for Windows
REM Runs all test files in the tests/ directory

setlocal enabledelayedexpansion

echo ========================================
echo Running Tests (Windows)
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\" (
    echo Error: Virtual environment not found at .venv\
    echo Please run setup.bat or configure_env.bat first to create and configure the environment.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Create logs directory if it doesn't exist
if not exist "logs\" (
    echo Creating logs directory...
    mkdir logs
)

REM Display environment information
echo Environment Information:
for /f "tokens=*" %%i in ('python --version') do echo   Python Version: %%i
for /f "tokens=*" %%i in ('pip --version') do echo   Pip Version: %%i
echo   Environment Path: %cd%\.venv
echo.

REM Run all test files
echo Running test files...
python -m pytest tests/ -v --tb=short > logs\test_run.log 2>&1
type logs\test_run.log

REM Display test summary
echo.
echo ========================================
echo Test Execution Complete!
echo ========================================
echo Test results saved to: logs\test_run.log
echo.
pause
