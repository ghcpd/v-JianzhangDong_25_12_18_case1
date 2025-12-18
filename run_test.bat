@echo off
setlocal

if not exist .venv\Scripts\python.exe (
    python -m venv .venv
)

call .venv\Scripts\activate

python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

python -m pytest -q
