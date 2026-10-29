"""Install only this skill's locked calculation packages into .runtime."""
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[1]
target = root / '.runtime'
if __name__ == '__main__':
    subprocess.run([sys.executable, '-m', 'pip', 'install', '--only-binary=:all:',
                    '--target', str(target), '-r', str(root / 'requirements.txt')], check=True)
    subprocess.run([sys.executable, str(root / 'scripts' / 'doctor.py')], check=True)
