#!/usr/bin/env python3

import os
import sys
import subprocess
import logging
from pathlib import Path

# Set up logging
logs_dir = Path('logs')
logs_dir.mkdir(exist_ok=True)
logging.basicConfig(filename=logs_dir / 'test_run.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_env_info():
    env_name = '.venv'
    env_path = Path('.venv').resolve()
    python_version = sys.version
    try:
        pip_version = subprocess.check_output([sys.executable, '-m', 'pip', '--version']).decode().strip()
    except:
        pip_version = 'Unknown'
    return env_name, str(env_path), python_version, pip_version

def run_tests():
    test_dir = Path('tests')
    if not test_dir.exists():
        logging.error("Tests directory not found.")
        return

    for test_file in test_dir.glob('*.py'):
        logging.info(f"Running {test_file}")
        try:
            env = dict(os.environ, PYTHONPATH=os.getcwd())
            result = subprocess.run([sys.executable, str(test_file)], capture_output=True, text=True, env=env)
            logging.info(f"STDOUT: {result.stdout}")
            if result.stderr:
                logging.error(f"STDERR: {result.stderr}")
            logging.info(f"Return code: {result.returncode}")
        except Exception as e:
            logging.error(f"Error running {test_file}: {e}")

def append_to_readme(env_info):
    readme_path = Path('README.md')
    with open(readme_path, 'a') as f:
        f.write("\n## Environment Information\n")
        f.write(f"- Environment Name: {env_info[0]}\n")
        f.write(f"- Absolute Path: {env_info[1]}\n")
        f.write(f"- Python Version: {env_info[2]}\n")
        f.write(f"- Pip Version: {env_info[3]}\n")

if __name__ == "__main__":
    env_info = get_env_info()
    logging.info("Starting auto test.")
    run_tests()
    append_to_readme(env_info)
    logging.info("Auto test completed.")