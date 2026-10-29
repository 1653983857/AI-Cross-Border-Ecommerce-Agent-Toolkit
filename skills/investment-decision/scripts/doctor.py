"""Read-only runtime and offline source-library check."""
import importlib.metadata
import json
from pathlib import Path
from _runtime import activate
activate()

def check():
    modules = ['numpy', 'scipy', 'pandas', 'cvxpy', 'pypfopt']
    result = {}
    for mod in modules:
        try:
            module = __import__(mod)
            result[mod] = {'ok': True, 'version': getattr(module, '__version__', 'unknown')}
        except Exception as exc:
            result[mod] = {'ok': False, 'error': str(exc)}
    try:
        import cvxpy as cp
        result['solvers'] = cp.installed_solvers()
    except ImportError:
        result['solvers'] = []
    try:
        import pandas as pd
        from pypfopt import HRPOpt
        sample = pd.DataFrame({'a':[.01,-.01,.02,.005], 'b':[-.005,.007,.003,.001]})
        result['hrp_smoke'] = bool(HRPOpt(returns=sample).optimize())
    except Exception as exc:
        result['hrp_smoke'] = False
        result['hrp_error'] = str(exc)
    result['library_present'] = (Path(__file__).resolve().parents[1] / 'assets/upstream-reference.zip').is_file()
    result['ready'] = all(result[m]['ok'] for m in modules) and 'CLARABEL' in result['solvers'] and result['hrp_smoke'] and result['library_present']
    result['missing_dependencies_command'] = 'python scripts/bootstrap.py'
    return result

if __name__ == '__main__':
    result = check()
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['ready'] else 2)
