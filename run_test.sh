#!/usr/bin/env bash
set -euo pipefail
# Activate .venv and run tests
if [ -d ".venv" ]; then
  source .venv/bin/activate
else
  echo "No .venv found. Run setup.sh first."
  exit 1
fi
mkdir -p logs
python auto_test.py | tee -a logs/test_run.log
