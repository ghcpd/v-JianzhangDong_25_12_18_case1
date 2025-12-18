#!/bin/bash

# Setup script for Linux and macOS environments
# Creates virtual environment and installs dependencies

set -e  # Exit on error

echo "========================================"
echo "Environment Setup Script (Linux/macOS)"
echo "========================================"

# Check if .venv exists and remove it if it does
if [ -d ".venv" ]; then
    echo "Removing existing virtual environment..."
    rm -rf .venv
fi

# Check Python version
echo "Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
echo "Python version: $PYTHON_VERSION"

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip, setuptools, and wheel
echo "Upgrading pip, setuptools, and wheel..."
pip install --upgrade pip setuptools wheel

# Install dependencies from requirements.txt
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Display installation summary
echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo "Environment Path: $(pwd)/.venv"
echo "Python Executable: $(which python)"
python --version
echo "Pip Version: $(pip --version)"
echo ""
echo "To activate the environment, run:"
echo "  source .venv/bin/activate"
echo ""
