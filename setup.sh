#!/usr/bin/env bash
set -e

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Upgrade pip and install requirements
python -m pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

# Run tests
python -m pytest -q
