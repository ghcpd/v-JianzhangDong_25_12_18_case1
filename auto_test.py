#!/usr/bin/env python3
"""
Auto Test Script
================
Automatic test runner that detects the virtual environment and runs all tests.

Features:
- Auto-detects .venv environment
- Collects and runs all test files from tests/ directory
- Logs all output to logs/test_run.log
- Displays environment information
"""

import os
import sys
import subprocess
import logging
from pathlib import Path
from datetime import datetime

# Set encoding for console output
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def setup_logging(log_dir: str = "logs") -> logging.Logger:
    """Setup logging to both console and file."""
    Path(log_dir).mkdir(exist_ok=True)
    
    log_file = Path(log_dir) / "test_run.log"
    
    # Create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    # File handler with UTF-8 encoding
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Formatter (removed unicode characters for Windows compatibility)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def find_venv() -> Path:
    """Find the virtual environment directory."""
    venv_path = Path(".venv")
    if not venv_path.exists():
        raise EnvironmentError("Virtual environment not found at .venv/. Please run setup.sh or setup.bat first.")
    return venv_path

def get_python_executable(venv_path: Path) -> Path:
    """Get the Python executable from the virtual environment."""
    if sys.platform == "win32":
        python_exe = venv_path / "Scripts" / "python.exe"
    else:
        python_exe = venv_path / "bin" / "python"
    
    if not python_exe.exists():
        raise FileNotFoundError(f"Python executable not found at {python_exe}")
    
    return python_exe

def get_environment_info(python_exe: Path, pip_exe: Path) -> dict:
    """Get Python and pip version information."""
    info = {}
    
    try:
        result = subprocess.run(
            [str(python_exe), "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        info["python_version"] = result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        info["python_version"] = "Unknown"
    
    try:
        result = subprocess.run(
            [str(pip_exe), "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        info["pip_version"] = result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        info["pip_version"] = "Unknown"
    
    info["venv_path"] = str(Path(".venv").absolute())
    info["working_directory"] = str(Path.cwd())
    
    return info

def find_test_files(tests_dir: str = "tests") -> list:
    """Find all test files in the tests directory."""
    tests_path = Path(tests_dir)
    if not tests_path.exists():
        raise FileNotFoundError(f"Tests directory not found at {tests_dir}/")
    
    test_files = sorted(tests_path.glob("test_*.py")) + sorted(tests_path.glob("*_test.py"))
    return list(set(test_files))  # Remove duplicates

def run_tests(python_exe: Path, test_files: list, logger: logging.Logger) -> bool:
    """Run all test files."""
    success = True
    
    for test_file in test_files:
        logger.info(f"\nRunning test: {test_file}")
        logger.info("=" * 70)
        
        try:
            result = subprocess.run(
                [str(python_exe), str(test_file)],
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.stdout:
                logger.info(result.stdout)
            if result.stderr:
                logger.warning(result.stderr)
            
            if result.returncode != 0:
                success = False
                logger.error(f"Test {test_file.name} failed with return code {result.returncode}")
            else:
                logger.info(f"[PASS] Test {test_file.name} passed")
        
        except Exception as e:
            success = False
            logger.error(f"Error running test {test_file.name}: {str(e)}")
    
    return success

def main():
    """Main test runner function."""
    print("=" * 70)
    print("Auto Test Runner - Environment Detection and Testing")
    print("=" * 70)
    print()
    
    logger = setup_logging()
    
    try:
        # Find virtual environment
        logger.info("Detecting virtual environment...")
        venv_path = find_venv()
        logger.info(f"[OK] Virtual environment found at {venv_path.absolute()}")
        
        # Get Python and pip executables
        python_exe = get_python_executable(venv_path)
        if sys.platform == "win32":
            pip_exe = venv_path / "Scripts" / "pip.exe"
        else:
            pip_exe = venv_path / "bin" / "pip"
        
        logger.info(f"[OK] Python executable: {python_exe}")
        logger.info(f"[OK] Pip executable: {pip_exe}")
        
        # Get environment information
        logger.info("\nCollecting environment information...")
        env_info = get_environment_info(python_exe, pip_exe)
        
        logger.info("Environment Information:")
        logger.info(f"  Python Version: {env_info['python_version']}")
        logger.info(f"  Pip Version: {env_info['pip_version']}")
        logger.info(f"  Virtual Environment: {env_info['venv_path']}")
        logger.info(f"  Working Directory: {env_info['working_directory']}")
        
        # Append to README
        logger.info("\nUpdating README.md with environment information...")
        append_to_readme(env_info, logger)
        
        # Find test files
        logger.info("\nScanning for test files...")
        test_files = find_test_files()
        
        if not test_files:
            logger.warning("[!] No test files found in tests/ directory")
            logger.info("Looking for test files matching patterns: test_*.py or *_test.py")
        else:
            logger.info(f"[OK] Found {len(test_files)} test file(s):")
            for test_file in test_files:
                logger.info(f"  - {test_file.name}")
        
        # Run tests
        logger.info("\n" + "=" * 70)
        logger.info("Running Tests...")
        logger.info("=" * 70)
        
        if test_files:
            success = run_tests(python_exe, test_files, logger)
        else:
            logger.warning("No test files to run. Skipping test execution.")
            success = True
        
        # Summary
        logger.info("\n" + "=" * 70)
        if success:
            logger.info("[OK] All tests completed successfully!")
        else:
            logger.warning("[!] Some tests failed. Check the log for details.")
        logger.info("=" * 70)
        logger.info(f"Test results logged to: logs/test_run.log")
        
        return 0 if success else 1
    
    except Exception as e:
        logger.error(f"Fatal error: {str(e)}", exc_info=True)
        print(f"\n[ERROR] Error: {str(e)}")
        return 1

def append_to_readme(env_info: dict, logger: logging.Logger):
    """Append environment information to README.md."""
    readme_file = Path("README.md")
    
    env_section = f"""
## Environment Information

**Generated on:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

- **Python Version:** {env_info['python_version']}
- **Pip Version:** {env_info['pip_version']}
- **Virtual Environment Path:** {env_info['venv_path']}
- **Working Directory:** {env_info['working_directory']}
"""
    
    if readme_file.exists():
        try:
            content = readme_file.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            try:
                content = readme_file.read_text(encoding='gbk')
            except UnicodeDecodeError:
                content = readme_file.read_text(encoding='latin-1')
        
        if "## Environment Information" not in content:
            with open(readme_file, "a", encoding='utf-8') as f:
                f.write(env_section)
            logger.info("[*] README.md updated with environment information")
        else:
            logger.info("Environment information already present in README.md")
    else:
        logger.info("README.md not found; environment information not appended")

if __name__ == "__main__":
    sys.exit(main())
