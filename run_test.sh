#!/usr/bin/env bash
set -e

if [ ! -d ".venv" ]; then
  python -m venv .venv
fi

source .venv/bin/activate

pip install --upgrade pip
pip install --no-cache-dir -r requirements.txt

python -m pytest -q
