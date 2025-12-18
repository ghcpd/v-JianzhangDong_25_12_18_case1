# Dependency Maintenance and Testing Framework

This project contains a complete dependency maintenance system with automated testing scripts and environment management tools.

## Overview

This framework provides:
- Updated and secure Python dependencies compatible with Python 3.14
- Automated virtual environment setup and management
- Multi-platform test execution scripts
- Comprehensive dependency analysis and vulnerability reporting
- Environment replication through Docker and shell scripts

## Generated Files and Their Purpose

### Dependency Management Files
- **requirements.txt** - Updated Python package dependencies with stable, secure versions pinned for reproducibility
- **requirements_backup.txt** - Original backup of dependencies before updates
- **report.json** - Detailed analysis of each dependency update including CVE/vulnerability information and reasons for updates

### Environment Setup Files
- **setup.sh** - Automated environment setup script for Linux/macOS (creates .venv and installs dependencies)
- **Dockerfile** - Docker container definition for complete environment replication with all dependencies
- **run_test.sh** - Linux/macOS test execution script that runs all tests and logs results
- **run_test.bat** - Windows test execution script with the same functionality
- **auto_test.py** - Cross-platform Python test runner that auto-detects the virtual environment

### Configuration Files
- **.gitignore** - Git ignore rules to exclude virtual environment, logs, and build artifacts
- **README.md** - This file

### Logging and Reports
- **logs/** - Directory containing test execution logs
- **logs/test_run.log** - Complete test execution results and environment information

## Dependency Updates Summary

All dependencies have been updated from 2021-2022 versions to the latest stable 2025 versions, with Python 3.14 compatibility.

### Key Updates:
| Package | Old Version | New Version | Reason |
|---------|------------|-------------|--------|
| numpy | 1.24.0 | 2.3.5 | Python 3.14 support, performance improvements |
| pandas | 1.5.0 | 2.3.3 | Python 3.14 support, major bug fixes |
| matplotlib | 3.5.0 | 3.10.8 | Python 3.14 support, enhanced rendering |
| requests | 2.25.0 | 2.32.5 | Multiple CVE fixes |
| pyyaml | 5.3.1 | 6.0.3 | Critical security fixes (arbitrary code execution vulnerability) |
| scipy | 1.9.0 | 1.16.3 | Python 3.14 support, performance improvements |
| regex | 2021.4.4 | 2025.11.3 | Major regex engine improvements |
| tqdm | 4.32.0 | 4.67.1 | Bug fixes and improvements |
| lxml | 4.6.1 | 6.0.2 | Python 3.14 support, critical security fixes |
| typing_extensions | 3.7.4 | 4.15.0 | Modern Python type hinting support |

## Environment Information

**Generated on:** 2025-12-18

- **Python Version:** Python 3.14.0
- **Pip Version:** pip 25.3
- **Virtual Environment Path:** d:\vscoderprojects\v-JianzhangDong_25_12_18_case1\haiku-4.5\v-JianzhangDong_25_12_18_case1\.venv
- **Working Directory:** d:\vscoderprojects\v-JianzhangDong_25_12_18_case1\haiku-4.5\v-JianzhangDong_25_12_18_case1

## Getting Started

### Step 1: Choose Your Platform

#### For Windows Users:
```bash
# Run the batch script to set up the environment and install dependencies
run_test.bat
```

#### For Linux/macOS Users:
```bash
# Make scripts executable
chmod +x setup.sh run_test.sh auto_test.py

# Run the setup script
./setup.sh

# Run tests
./run_test.sh
```

### Step 2: Activate the Virtual Environment (Manual Setup)

#### Windows:
```bash
.venv\Scripts\activate.bat
```

#### Linux/macOS:
```bash
source .venv/bin/activate
```

### Step 3: Install Dependencies (if not auto-installed)

```bash
pip install -r requirements.txt
```

## Running Tests

### Option 1: Using Platform-Specific Scripts (Recommended)

**Windows:**
```bash
run_test.bat
```

**Linux/macOS:**
```bash
./run_test.sh
```

### Option 2: Using auto_test.py (Cross-Platform)

```bash
# Activate virtual environment first
# Windows
.venv\Scripts\python auto_test.py

# Linux/macOS
.venv/bin/python auto_test.py
```

The auto_test.py script will:
- Auto-detect the virtual environment at .venv/
- Display Python and pip version information
- Collect and run all test files from the tests/ directory
- Log all output to logs/test_run.log
- Append environment information to README.md

### Option 3: Using Docker

Build and run the Docker container:

```bash
# Build the Docker image
docker build -t python-env:latest .

# Run tests in the container
docker run --rm python-env:latest
```

## Directory Structure

```
.
├── .venv/                          # Virtual environment directory (created by setup)
├── .gitignore                      # Git ignore rules
├── app/                            # Application source code
│   ├── __init__.py
│   ├── data_loader.py
│   ├── text_processor.py
│   └── visualizer.py
├── tests/                          # Test directory
│   ├── case_1.py
│   ├── case_2.py
│   └── case_3.py
├── logs/                           # Test execution logs (created by test runner)
│   └── test_run.log
├── Dockerfile                      # Docker container definition
├── requirements.txt                # Updated Python dependencies
├── requirements_backup.txt         # Original dependencies backup
├── setup.sh                        # Linux/macOS setup script
├── run_test.sh                     # Linux/macOS test runner
├── run_test.bat                    # Windows test runner
├── auto_test.py                    # Cross-platform test runner
├── report.json                     # Dependency update analysis
└── README.md                       # This file
```

## Checking Test Results

After running tests, view the detailed results:

```bash
# On Windows
type logs\test_run.log

# On Linux/macOS
cat logs/test_run.log

# Or in any text editor
```

The log file contains:
- Environment information (Python version, pip version, paths)
- Test execution timestamps
- Individual test results
- Error messages and tracebacks if any tests failed

## Dependency Vulnerability Report

For detailed information about each dependency update, including security vulnerabilities and reasons for updates, see:

```bash
# View the dependency analysis report
cat report.json
```

The report includes:
- Original package version
- Updated package version
- Detailed reason for update including CVE information
- Security vulnerability details where applicable

## Virtual Environment Management

### Recreating the Virtual Environment

If you need to completely recreate the virtual environment:

**Windows:**
```bash
rmdir /s /q .venv
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
```

**Linux/macOS:**
```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Updating Dependencies

To update all dependencies to the latest versions:

**Windows:**
```bash
.venv\Scripts\pip install --upgrade -r requirements.txt
```

**Linux/macOS:**
```bash
source .venv/bin/activate
pip install --upgrade -r requirements.txt
```

### Freezing Current Dependencies

To save the current installed packages:

```bash
# Windows
.venv\Scripts\pip freeze > requirements_current.txt

# Linux/macOS
.venv/bin/pip freeze > requirements_current.txt
```

## Troubleshooting

### Virtual Environment Not Found
If you get an error about `.venv` not found:
- Run `setup.sh` (Linux/macOS) or the platform-specific setup script
- This will create the virtual environment and install all dependencies

### Python Version Mismatch
If tests fail with version errors:
- Ensure Python 3.14.0 is installed
- Check with `python --version`
- Verify the virtual environment is using Python 3.14

### Permission Denied (Linux/macOS)
If you get permission denied errors on shell scripts:
```bash
chmod +x setup.sh run_test.sh auto_test.py
```

### Dependencies Installation Fails
If pip install fails:
1. Ensure your internet connection is working
2. Try upgrading pip: `pip install --upgrade pip`
3. Check that you're using the virtual environment
4. Try installing packages individually to identify the problematic package

## Security Notes

- **PyYAML**: Updated from 5.3.1 to 6.0.3 to fix arbitrary code execution vulnerability (CVE-2020-14343)
- **requests**: Updated from 2.25.0 to 2.32.5 to fix multiple security issues
- **lxml**: Updated from 4.6.1 to 6.0.2 to fix XML external entity (XXE) vulnerabilities

All dependencies are pinned to specific versions to ensure reproducibility and prevent unexpected updates that could introduce vulnerabilities.

## Platform Compatibility

This framework has been tested and is compatible with:
- **Python:** 3.14.0
- **Windows:** Windows 10/11 with PowerShell or Command Prompt
- **Linux:** Ubuntu 20.04+, Debian 10+, CentOS 7+
- **macOS:** 10.14+
- **Docker:** Any Docker version supporting Python 3.14 base images

## Next Steps

1. **Run Setup:** Execute the setup script for your platform
2. **Run Tests:** Use one of the test runner methods to validate the environment
3. **Review Reports:** Check report.json for dependency details and logs/test_run.log for test results
4. **Deploy:** Use the Dockerfile for containerized deployment or setup.sh for direct installation

## Support and Maintenance

For dependency updates and security patches:
- Check PyPI for new versions: https://pypi.org/
- Review security advisories: https://pypi.org/project/pip-audit/
- Regularly update dependencies: `pip list --outdated`

---

**Framework Version:** 1.0  
**Last Updated:** 2025-12-18  
**Python Target Version:** 3.14.0
