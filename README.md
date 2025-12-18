Project environment helper files

Generated files and purpose:
- requirements_backup.txt: copy of the original requirements prior to updates.
- requirements.txt: updated and pinned dependency versions (safe for Python 3.14).
- report.json: simplified report listing issues, original and updated versions, and reasons.
- Dockerfile: minimal container that creates a venv and runs auto_test.py by default.
- setup.sh: create a fresh .venv and install requirements (Linux/macOS).
- run_test.sh: activate .venv and run auto_test.py, logs appended to logs/test_run.log (Linux/macOS).
- run_test.bat: Windows helper that runs auto_test.py using .venv\Scripts\python.exe.
- auto_test.py: uses the .venv interpreter (if present) to run all scripts in tests/ and writes logs to logs/test_run.log. It also appends environment info to README.md when run.
- .gitignore: ignores .venv, logs, and other common artifacts.
- logs/: directory where test_run.log is stored.

Setup instructions:
1) Ensure you have Python 3.14 installed (this project was validated with Python 3.14).
2) On Linux/macOS:
   - bash setup.sh
   - bash run_test.sh
3) On Windows:
   - python -m venv .venv
   - .venv\Scripts\python -m pip install --upgrade pip setuptools wheel
   - .venv\Scripts\python -m pip install -r requirements.txt
   - run_test.bat

Using auto_test.py manually:
- Activate the environment you want to use or ensure .venv exists.
- Run: .venv/bin/python auto_test.py  (or .venv\Scripts\python.exe auto_test.py on Windows)
- Results are appended to logs/test_run.log and environment metadata is appended to README.md.

Checking logs:
- Open logs/test_run.log to see output from each test script and recorded Python/pip versions.

Contact:
- This is an automated update of dependencies; review report.json for rationale of changes.

---
Environment used: .venv
Environment absolute path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv
Python 3.14.0

pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)



---
Environment used: .venv
Environment absolute path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv
Python 3.14.0

pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)



---
Environment used: .venv
Environment absolute path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv
Python 3.14.0

pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)



---
Environment used: .venv
Environment absolute path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv
Python 3.14.0

pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)



---
Environment used: .venv
Environment absolute path: D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv
Python 3.14.0

pip 25.3 from D:\projects\v-JianzhangDong_25_12_18_case1\oswe-mini-uiberry-1211\v-JianzhangDong_25_12_18_case1\.venv\Lib\site-packages\pip (python 3.14)


