#!/usr/bin/env bash
set -euo pipefail

# Activate .venv and run auto_test.py
if [ ! -d ".venv" ]; then
  echo ".venv not found. Run ./setup.sh first." >&2
  exit 1
fi

. .venv/bin/activate
python auto_test.py
