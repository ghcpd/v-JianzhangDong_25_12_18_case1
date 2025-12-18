#!/usr/bin/env python
"""Auto test runner that executes tests using the project's .venv
and writes results to logs/test_run.log.
"""
import subprocess
import sys
import os
from pathlib import Path

def get_venv_python():
    """Return path to python executable inside .venv if present, else system python."""
    if os.name == 'nt':
        py = Path('.venv') / 'Scripts' / 'python.exe'
    else:
        py = Path('.venv') / 'bin' / 'python'
    return str(py) if py.exists() else sys.executable


def run_tests(py_exe):
    logs_dir = Path('logs')
    logs_dir.mkdir(exist_ok=True)
    log_file = logs_dir / 'test_run.log'
    # Run each test script under tests/ with the venv/python
    overall_rc = 0
    with open(log_file, 'w') as f:
        test_files = [str(p) for p in Path('tests').glob('*.py')]
        for tf in test_files:
            f.write(f"\nRunning {tf}\n")
            env = os.environ.copy()
            env['PYTHONPATH'] = str(Path.cwd())
            rc = subprocess.run([py_exe, tf], stdout=f, stderr=subprocess.STDOUT, env=env).returncode
            overall_rc = overall_rc or rc
    return overall_rc
def main():
    py = get_venv_python()
    print(f"Using python: {py}")
    rc = run_tests(py)
    if rc == 0:
        print('All tests passed')
    else:
        print(f'Tests failed (exit code {rc}). See logs/test_run.log for details.')
    # Print environment info
    try:
        out = subprocess.check_output([py, '--version'], text=True)
    except Exception:
        out = 'Unknown'
    pip_out = ''
    try:
        pip_out = subprocess.check_output([py, '-m', 'pip', '--version'], text=True)
    except Exception:
        pip_out = 'Unknown'
    print('Python version:', out.strip())
    print('pip version:', pip_out.strip())

    # Append environment info to README.md
    try:
        readme = Path('README.md')
        if readme.exists():
            abs_path = str(Path.cwd().resolve())
            with open(readme, 'a') as r:
                r.write('\n---\n')
                r.write(f"Environment: .venv\n")
                r.write(f"Path: {abs_path}\n")
                r.write(f"Python version: {out.strip()}\n")
                r.write(f"pip version: {pip_out.strip()}\n")
    except Exception:
        pass

if __name__ == '__main__':
    main()
