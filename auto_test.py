#!/usr/bin/env python3
import sys
import subprocess
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "test_run.log"
TEST_DIR = ROOT / "tests"
VENV_DIR = ROOT / ".venv"

def run_script(path):
    print(f"Running {path}")
    # Ensure project root is on PYTHONPATH so imports like `import app` succeed
    env = os.environ.copy()
    env_py = env.get('PYTHONPATH', '')
    env['PYTHONPATH'] = str(ROOT) + (os.pathsep + env_py if env_py else '')
    result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, env=env, cwd=str(ROOT))
    out = result.stdout
    err = result.stderr
    status = 'PASS' if result.returncode == 0 else f'FAIL ({result.returncode})'
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"=== {path.name} : {status} ===\n")
        f.write(out)
        if err:
            f.write("--- STDERR ---\n")
            f.write(err)
        f.write("\n\n")
    print(f"{path.name}: {status}")
    return result.returncode


def main():
    tests = sorted([p for p in TEST_DIR.glob('*.py') if p.is_file()])
    if not tests:
        print("No test scripts found in tests/")
        return 1
    # Clear previous log
    if LOG_FILE.exists():
        LOG_FILE.unlink()
    total_fail = 0
    for t in tests:
        rc = run_script(t)
        if rc != 0:
            total_fail += 1
    summary = f"Ran {len(tests)} tests, failures: {total_fail}\n"
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write("=== SUMMARY ===\n")
        f.write(summary)
    print(summary)

    # Append environment info to README.md
    try:
        python_ver = sys.version.replace('\n', ' ')
        pip_ver = subprocess.check_output([sys.executable, '-m', 'pip', '--version'], text=True).strip()
        env_name = VENV_DIR.name if VENV_DIR.exists() else ''
        env_path = str(VENV_DIR.resolve()) if VENV_DIR.exists() else ''
        readme = ROOT / 'README.md'
        with open(readme, 'a', encoding='utf-8') as f:
            f.write('\n')
            f.write('Environment: ' + (env_name or 'system') + '\n')
            f.write('Environment path: ' + (env_path or str(Path(sys.executable).parent.parent)) + '\n')
            f.write('Python: ' + python_ver + '\n')
            f.write('pip: ' + pip_ver + '\n')
    except Exception as e:
        print('Failed to append environment info to README.md:', e)
    return 0

if __name__ == '__main__':
    sys.exit(main())
