# Project Environment & Reproduction

This repository contains the project's dependency maintenance artifacts and test automation helpers.

## 🔧 Generated files
- `requirements.txt` — pinned, updated, non-vulnerable dependencies.
- `requirements_backup.txt` — backup of the original requirements before modification.
- `report.json` — summary of dependency issues and the applied version updates.
- `auto_test.py` — helper to run the project's tests using the `.venv` and write results to `logs/test_run.log`.
- `Dockerfile` — Docker image for reproducing the environment.
- `setup.sh` — Linux/macOS convenience script to set up and run tests.
- `run_test.sh` / `run_test.bat` — platform-specific scripts to (re)create `.venv`, install deps, and run tests.

## 🧭 How to set up the environment

### Linux / macOS
```bash
bash setup.sh
```

### Windows (PowerShell)
```powershell
# Create or recreate .venv, install deps, and run tests
.\run_test.bat
```

## ▶ How to run tests
- **Using the helper script**: `python auto_test.py` (will use `.venv` if it exists).
- **Using the provided scripts**: `bash run_test.sh` / `run_test.bat`.

## 📄 Logs
Test output is written to `logs/test_run.log`.

---

This README will be appended with environment information by `auto_test.py` after creation.

---
Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_18_case1\fast-oswe-1206\v-JianzhangDong_25_12_18_case1
Python version: Python 3.14.0
pip version: pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\fast-oswe-1206\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)
