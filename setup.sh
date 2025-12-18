#!/usr/bin/env bash
set -euo pipefail
# Create a fresh .venv, install dependencies
if [ -d ".venv" ]; then
  echo "Removing existing .venv..."
  rm -rf .venv
fi
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
echo "Environment ready in .venv"
