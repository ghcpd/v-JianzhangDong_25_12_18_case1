#!/usr/bin/env bash
set -euo pipefail

# Create virtual environment in .venv and install dependencies
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

echo "Virtual environment created in .venv and dependencies installed." 
