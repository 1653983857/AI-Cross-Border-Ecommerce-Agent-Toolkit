# Validation record — 2026-10-29

Scope: local numerical implementation, skill format, dependency compatibility and synthetic behavior. No live brokerage, paid data API, real holdings, transaction or out-of-sample investment performance was tested.

- 29 unit tests passed: cash/fees conservation, protected reserves, pending settlements, no implied trade authorization, cash alternative, purchase suspension, inaccessible-market reduction, locked holdings, infeasible risk, high-water budget, lookthrough caps, gross payment quota/minimum, missing profile, wrong NAV/currency, stale/future data, missing shocks/exposure, non-finite costs, ordered estimates, lot rounding, hold comparison, turnover, reserves, IDs and history frequency.
- Independent synthetic forward checks: unaffordable minimum purchase does not trigger an inferior liquidation; missing cash profile rejected; daily history declared monthly rejected. The reviewer did not edit implementation.
- Offline library: 5 pinned sources, 89 text files, SHA-256 integrity check passed.
- Runtime: Python 3.12, NumPy 2.5.4, SciPy 1.17.1, pandas 3.1.0, CVXPY 1.9.3, PyPortfolioOpt 1.6.0; CLARABEL and HRP smoke checks passed. SciPy is deliberately pinned below 1.18 because that release removes a private linkage constant referenced by this PyPortfolioOpt version.
- A full synthetic 180,000 CNY case produced a feasible cost-aware target and separate immediate/deferred gross payments, preserving 40,000 CNY in protected reserves. All names, total-return histories and forward estimates were synthetic.

Skill formatting, local reference links, packaging and installed hashes are also checked by the release workflow. These checks establish reproducibility and constraint enforcement; they do not establish future return, accuracy of forecasts, a probability of profit, a guaranteed drawdown ceiling or superiority to simple investing.
