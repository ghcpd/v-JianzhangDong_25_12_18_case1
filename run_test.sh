#!/bin/bash

# Test execution script for Linux and macOS
# Runs all test files in the tests/ directory

set -e  # Exit on error

echo "========================================"
echo "Running Tests (Linux/macOS)"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found at .venv/"
    echo "Please run setup.sh first to create and configure the environment."
    exit 1
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Create logs directory if it doesn't exist
if [ ! -d "logs" ]; then
    echo "Creating logs directory..."
    mkdir -p logs
fi

# Display environment information
echo "Environment Information:"
echo "  Python Version: $(python --version)"
echo "  Pip Version: $(pip --version)"
echo "  Environment Path: $(pwd)/.venv"
echo ""

# Run all test files
echo "Running test files..."
python -m pytest tests/ -v --tb=short 2>&1 | tee logs/test_run.log

# Display test summary
echo ""
echo "========================================"
echo "Test Execution Complete!"
echo "========================================"
echo "Test results saved to: logs/test_run.log"
echo ""
