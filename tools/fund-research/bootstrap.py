"""Create an isolated environment and install the two upstream packages."""
from pathlib import Path
import subprocess
import sys
import venv

root = Path(__file__).resolve().parent
if sys.version_info < (3, 12):
    raise SystemExit("Use Python 3.12 or newer (validated with Python 3.12).")
env = root / ".venv"
venv.EnvBuilder(with_pip=True).create(env)
python = env / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
requirements = root / "requirements-lock.txt"
if not requirements.exists():
    requirements = root / "requirements.txt"
subprocess.run([str(python), "-m", "pip", "install", "-r", str(requirements)], check=True)
subprocess.run([str(python), str(root / "fund_cli.py"), "doctor"], check=True)
print(f"Ready: {python} {root / 'fund_cli.py'} --help")
