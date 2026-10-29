"""Load isolated optional dependencies without changing global Python."""
from pathlib import Path
import os
import sys

def activate():
    paths = [Path(__file__).resolve().parents[1] / '.runtime']
    if os.environ.get('INVESTMENT_SKILL_PACKAGES'):
        paths.insert(0, Path(os.environ['INVESTMENT_SKILL_PACKAGES']))
    for path in reversed(paths):
        if path.is_dir():
            sys.path.insert(0, str(path))
