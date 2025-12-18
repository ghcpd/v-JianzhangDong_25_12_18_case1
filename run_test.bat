@echo off

REM Run tests script for Windows

echo Running tests...

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Run test scripts
for %%f in (tests\*.py) do (
    echo Running %%f...
    python %%f
)

echo Tests completed.