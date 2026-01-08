#!/usr/bin/env python3
import sys
import os
import subprocess
import glob
import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / '.venv'
LOG_DIR = ROOT / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / 'test_run.log'
TESTS_DIR = ROOT / 'tests'


def venv_python():
    if os.name == 'nt':
        return VENV_DIR / 'Scripts' / 'python.exe'
    else:
        return VENV_DIR / 'bin' / 'python'


def venv_pip():
    if os.name == 'nt':
        return VENV_DIR / 'Scripts' / 'pip.exe'
    else:
        return VENV_DIR / 'bin' / 'pip'


def run_tests():
    vpy = venv_python()
    if not vpy.exists():
        print('.venv not found or missing python executable. Please run setup.sh or create the .venv first.', file=sys.stderr)
        sys.exit(1)

    test_files = sorted(glob.glob(str(TESTS_DIR / '*.py')))
    results = []
    for tf in test_files:
        start = datetime.datetime.utcnow()
        # Execute test within project root by inserting the project root to sys.path and running the file
        cmd = [str(vpy), "-c", (
            "import sys, runpy; sys.path.insert(0, r'" + str(ROOT) + "'); runpy.run_path(r'" + str(tf) + "', run_name='__main__')"
        )]
        proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT))
        end = datetime.datetime.utcnow()
        results.append({
            'test': os.path.relpath(tf, ROOT),
            'returncode': proc.returncode,
            'stdout': proc.stdout,
            'stderr': proc.stderr,
            'start': start.isoformat() + 'Z',
            'end': end.isoformat() + 'Z'
        })
    return results


def write_log(results):
    with open(LOG_FILE, 'a', encoding='utf-8') as fh:
        fh.write(f"=== Test run: {datetime.datetime.utcnow().isoformat()}Z ===\n")
        for r in results:
            fh.write(f"TEST: {r['test']}\n")
            fh.write(f"START: {r['start']}\nEND: {r['end']}\n")
            fh.write(f"RETURN CODE: {r['returncode']}\n")
            fh.write("--- STDOUT ---\n")
            fh.write(r['stdout'] or '')
            fh.write("\n--- STDERR ---\n")
            fh.write(r['stderr'] or '')
            fh.write("\n\n")


def append_env_info_to_readme():
    vpy = venv_python()
    vpip = venv_pip()
    try:
        py_ver = subprocess.run([str(vpy), '--version'], capture_output=True, text=True).stdout.strip()
    except Exception:
        py_ver = 'unknown'
    try:
        pip_ver = subprocess.run([str(vpip), '--version'], capture_output=True, text=True).stdout.strip()
    except Exception:
        pip_ver = 'unknown'

    readme = ROOT / 'README.md'
    env_name = '.venv'
    abs_path = str(VENV_DIR.resolve())
    with open(readme, 'a', encoding='utf-8') as fh:
        fh.write('\n')
        fh.write('---\n')
        fh.write(f'Environment: {env_name}\n')
        fh.write(f'Path: {abs_path}\n')
        fh.write(f'Python: {py_ver}\n')
        fh.write(f'pip: {pip_ver}\n')


def main():
    results = run_tests()
    write_log(results)
    append_env_info_to_readme()

    # exit non-zero if any test failed
    failed = [r for r in results if r['returncode'] != 0]
    if failed:
        print(f"{len(failed)} test(s) failed; see {LOG_FILE} for details.")
        sys.exit(2)
    else:
        print(f"All tests passed. Logs written to {LOG_FILE}.")


if __name__ == '__main__':
    main()
