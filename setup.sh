#!/usr/bin/env bash
set -euo pipefail
# Create or replace .venv, install requirements
if [ -d ".venv" ]; then
  echo "Removing existing .venv/"
  rm -rf .venv
fi
python -m venv .venv
# shellcheck disable=SC1091
. .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
echo "Environment created at $(pwd)/.venv"
