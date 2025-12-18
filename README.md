# Environment and Test Automation

This project includes auto-generated files to make environment setup and test execution reproducible.

Generated files:
- requirements_backup.txt: Backup of the original requirements.txt
- requirements.txt: Updated, pinned dependencies (secure and compatible versions)
- report.json: Summary of dependency updates and reasons
- Dockerfile: Docker image that installs requirements and runs tests
- setup.sh: Create a fresh .venv virtual environment and install requirements (Linux/macOS)
- run_test.sh: Activate .venv and run tests via auto_test.py (Linux/macOS)
- run_test.bat: Windows test runner to execute auto_test.py
- auto_test.py: Script to run all test scripts in tests/, write logs to logs/test_run.log, and append environment info to README.md
- logs/: Directory created by auto_test.py to store test_run.log
- .gitignore: Updated to ignore .venv/ and logs/

Setup instructions (Linux/macOS):
1. Ensure Python 3.14+ is installed.
2. Run: bash setup.sh
3. Run tests: bash run_test.sh

Setup instructions (Windows):
1. Ensure Python 3.14+ is installed.
2. Create venv: python -m venv .venv
3. Activate: .venv\Scripts\activate.bat
4. Install: python -m pip install --upgrade pip && pip install -r requirements.txt
5. Run tests: run_test.bat

Docker:
1. Build image: docker build -t project-test .
2. Run container: docker run --rm project-test

Using auto_test.py directly:
- With .venv active (recommended) or system Python, run: python auto_test.py
- Test logs are written to logs/test_run.log and environment info is appended to README.md

Checking logs:
- Open logs/test_run.log to view individual test outputs and the summary.

Notes:
- The original requirements.txt has been saved as requirements_backup.txt.
- The updated requirements.txt was chosen to address security and dependency compatibility.

Important compatibility note (Python 3.14):
- Some compiled scientific packages (notably numpy and scipy) may not have pre-built binary wheels for Python 3.14 on all platforms (especially Windows). Pip may attempt to build from source which requires a C/C++ build toolchain.
- If pip install fails during compilation, recommended options:
  - Use Python 3.11 or 3.12 which have broader wheel support for the scientific stack.
  - Use a conda/miniforge environment which provides pre-built binaries for these packages.
  - Install platform build tools (MSVC on Windows) to allow building from source.

Environment: .venv
Environment path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv
Python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
pip: pip 25.3 from D:\python\Lib\site-packages\pip (python 3.14)

Environment: .venv
Environment path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv
Python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
pip: pip 25.3 from D:\python\Lib\site-packages\pip (python 3.14)

Environment: .venv
Environment path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv
Python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Environment path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv
Python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Environment path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv
Python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-m22a5s330\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)
