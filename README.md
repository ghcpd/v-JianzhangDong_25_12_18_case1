# Project Environment & Test Helpers ✅

## Generated files and purpose 🔧

- `requirements_backup.txt` — Original dependencies (backup).
- `requirements.txt` — Updated, pinned dependency versions suitable for **Python 3.14**.
- `report.json` — Summary of dependency updates and reasons.
- `Dockerfile` — Container setup that installs `requirements.txt` and can run `auto_test.py`.
- `setup.sh` — Convenience script to create `.venv` and install requirements (Linux/macOS).
- `run_test.sh` / `run_test.bat` — Cross-platform scripts to run `auto_test.py`.
- `.gitignore` — Excludes `.venv`, `logs/`, and common artifacts.
- `auto_test.py` — Automatically runs all `tests/*.py` using the `.venv` Python, writes results to `logs/test_run.log`, and appends environment info to this README.
- `logs/test_run.log` — Test run logs (created after running `auto_test.py`).

---

## Quick setup (Linux/macOS) 💡

1. Create a fresh virtual environment and install deps:

   ./setup.sh

2. Run tests:

   ./run_test.sh

---

## Quick setup (Windows) 💡

1. Create a fresh virtual environment and install deps (PowerShell):

   python -m venv .venv
   .\.venv\Scripts\python.exe -m pip install --upgrade pip
   .\.venv\Scripts\pip.exe install --no-cache-dir -r requirements.txt

2. Run tests:

   run_test.bat

---

## Using `auto_test.py` (automatic detection) ⚙️

- `auto_test.py` will:
  - Use `.venv`'s Python to execute each script in `tests/` (so tests execute in the correct environment).
  - Create `logs/test_run.log` with results (stdout/stderr, timestamps).
  - Append the environment name, absolute path, and Python/pip versions to this README.

Example (Linux/macOS):

  . .venv/bin/activate && python auto_test.py

Example (Windows):

  .venv\Scripts\python.exe auto_test.py

---

## Inspect logs 📋

- Test run output is appended to `logs/test_run.log`.
- Look for `=== Test run:` entries and per-test `RETURN CODE` and stderr/stdout blocks.

---

*Note: `auto_test.py` appends environment details to this README each time it runs.*
