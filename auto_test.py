#!/usr/bin/env python3
"""
Run all tests in tests/ using the Python interpreter from .venv if present.
Write results to logs/test_run.log and append environment info to README.md.
"""
import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
LOGS = ROOT / "logs"
LOGS.mkdir(exist_ok=True)
LOGFILE = LOGS / "test_run.log"

# Detect python in .venv
venv_py = None
if (ROOT / ".venv" / "bin" / "python").exists():
    venv_py = str((ROOT / ".venv" / "bin" / "python").resolve())
elif (ROOT / ".venv" / "Scripts" / "python.exe").exists():
    venv_py = str((ROOT / ".venv" / "Scripts" / "python.exe").resolve())
else:
    # fall back to current interpreter
    venv_py = sys.executable

env_name = ".venv" if (ROOT / ".venv").exists() else "system"

def run_cmd(cmd, capture=True):
    print(f"Running: {cmd}")
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return proc.returncode, proc.stdout

# Write header
with LOGFILE.open("a", encoding="utf-8") as fh:
    fh.write(f"Test run: {os.getlogin() if hasattr(os, 'getlogin') else 'user'}@{ROOT} - using {env_name}\n")
    try:
        rc, out = run_cmd(f'"{venv_py}" --version')
        fh.write(out + "\n")
        rc, out = run_cmd(f'"{venv_py}" -m pip --version')
        fh.write(out + "\n")
    except Exception as e:
        fh.write(f"Could not determine python/pip versions: {e}\n")

# Run each test script in tests/
tests_dir = ROOT / "tests"
if not tests_dir.exists():
    print("No tests/ directory found.")
    sys.exit(1)

exit_code = 0
for py in sorted(tests_dir.glob("*.py")):
    # Run each test file in a Python process that has the project ROOT on sys.path
    # This allows `from app...` imports to resolve without modifying tests or source.
    cmd = (
        f'"{venv_py}" -c "import sys; sys.path.insert(0, {str(ROOT)!r}); ' 
        f'exec(open({str(py)!r}).read())"'
    )
    rc, out = run_cmd(cmd)
    with LOGFILE.open("a", encoding="utf-8") as fh:
        fh.write("="*40 + "\n")
        fh.write(f"Test file: {py.name}\n")
        fh.write(out + "\n")
    if rc != 0:
        exit_code = rc

# Append environment metadata to README.md
readme = ROOT / "README.md"
try:
    with readme.open("a", encoding="utf-8") as fh:
        fh.write("\n---\n")
        fh.write(f"Environment used: {env_name}\n")
        fh.write(f"Environment absolute path: {str(ROOT / ('.venv' if env_name=='.venv' else ''))}\n")
        rc, out = run_cmd(f'"{venv_py}" --version')
        fh.write(out + "\n")
        rc, out = run_cmd(f'"{venv_py}" -m pip --version')
        fh.write(out + "\n")
except Exception as e:
    print(f"Warning: could not append to README.md: {e}")

sys.exit(exit_code)
