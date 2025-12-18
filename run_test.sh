#!/usr/bin/env bash
set -euo pipefail
# Activate .venv and run test scripts in tests/
if [ ! -d ".venv" ]; then
  echo ".venv not found. Run setup.sh first to create it." >&2
  exit 2
fi
. .venv/bin/activate
mkdir -p logs
LOGFILE=logs/test_run.log
echo "Test run: $(date -u)" >> "$LOGFILE"
python -u auto_test.py 2>&1 | tee -a "$LOGFILE"
echo "Finished. See $LOGFILE"
