"""Evidence-input, long-only, cost-aware convex allocation. Never submits orders."""
from __future__ import annotations

import argparse
import csv
from datetime import date
import json
import math
from pathlib import Path
import sys

from _runtime import activate
activate()
import numpy as np
import pandas as pd
import cvxpy as cp
from pypfopt import HRPOpt, risk_models


class InputError(ValueError):
    pass


def number(value, name, low=None, high=None):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise InputError(f'{name}: finite numeric value required')
    value = float(value)
    if low is not None and value < low or high is not None and value > high:
        raise InputError(f'{name}: outside [{low}, {high}]')
    return value


def required(obj, key):
    if key not in obj or obj[key] is None:
        raise InputError(f'missing required field: {key}')
    return obj[key]


def source(value, name):
    if not isinstance(value, str) or not value.strip():
        raise InputError(f'{name}: non-empty provenance required')
    return value


def dated(value, name, as_of):
    try:
        parsed = date.fromisoformat(value)
    except (TypeError, ValueError):
        raise InputError(f'{name}: YYYY-MM-DD required') from None
    if parsed > as_of:
        raise InputError(f'{name}: future information is not allowed')
    return parsed


def validate_input(data):
    try:
        as_of = date.fromisoformat(required(data, 'as_of'))
    except (TypeError, ValueError):
        raise InputError('as_of: YYYY-MM-DD required') from None
    p = required(data, 'profile')
    for key in ['base_currency', 'allowed_markets']:
        if not required(p, key):
            raise InputError(f'{key}: must not be empty')
    if not isinstance(p['allowed_markets'], list):
        raise InputError('allowed_markets: list required')
    for key in ['cash_available', 'emergency_reserve', 'near_term_reserve', 'min_trade_amount']:
        number(required(p, key), key, 0)
    for key in ['max_stress_loss', 'max_annual_volatility', 'max_single_fund_weight']:
        number(required(p, key), key, 0, 1)
    number(required(p, 'max_turnover'), 'max_turnover', 0, 2)
    number(required(p, 'horizon_years'), 'horizon_years', 0.001, 100)
    number(required(p, 'cash_annual_return'), 'cash_annual_return', -0.99, 5)
    for key in ['max_history_lag_days', 'max_quote_lag_days']:
        number(required(p, key), key, 0, 366)
    funds = required(data, 'funds')
    if not isinstance(funds, list) or not 1 <= len(funds) <= 40:
        raise InputError('funds: 1 to 40 researched candidates/holdings required')
    seen = set()
    caps = data.get('exposure_caps', {})
    for key, val in caps.items():
        number(val, f'exposure_caps.{key}', 0, 1)
    for f in funds:
        fid = required(f, 'id')
        if not isinstance(fid, str) or not fid or fid in seen or fid == 'date':
            raise InputError('fund IDs must be non-empty, unique, and not date')
        seen.add(fid)
        for key in ['name', 'market', 'currency', 'instrument_type', 'return_source', 'data_source']:
            source(required(f, key), f'{fid}.{key}')
        if f['instrument_type'] not in ['mutual_fund', 'etf', 'lof', 'reit', 'stock']:
            raise InputError(f'{fid}: unsupported instrument_type')
        for key in ['current_value', 'sellable_value', 'max_buy_amount', 'min_buy_amount']:
            number(required(f, key), f'{fid}.{key}', 0)
        if f['sellable_value'] > f['current_value'] + 1e-7:
            raise InputError(f'{fid}: sellable_value exceeds current_value')
        for key in ['buy_fee_rate', 'sell_fee_rate']:
            number(required(f, key), f'{fid}.{key}', 0, 0.99)
        for key in ['buy_allowed', 'sell_allowed']:
            if not isinstance(required(f, key), bool):
                raise InputError(f'{fid}.{key}: boolean required')
        quotes = dated(required(f, 'quote_as_of'), fid + '.quote_as_of', as_of)
        if (as_of - quotes).days > p['max_quote_lag_days']:
            raise InputError(f'{fid}: valuation quote is stale')
        low, base, high = [number(required(f, k), fid + '.' + k, -0.99, 5)
                           for k in ['forward_return_low', 'forward_return_base', 'forward_return_high']]
        if not low <= base <= high:
            raise InputError(f'{fid}: forward-return interval is not ordered')
        if 'max_weight' in f:
            number(f['max_weight'], fid + '.max_weight', 0, 1)
        for key in caps:
            number(required(f.get('exposures', {}), key), fid + '.exposures.' + key, 0, 1)
        for key in ['buy_increment', 'redemption_increment']:
            number(f.get(key, 0.01), fid + '.' + key, 0.000001)
        if f['instrument_type'] in ['etf', 'lof', 'reit', 'stock']:
            number(required(f, 'lot_size'), fid + '.lot_size', 0.000001)
            number(required(f, 'price_base_currency'), fid + '.price_base_currency', 0.000001)
        number(f.get('sell_settlement_days', 1), fid + '.sell_settlement_days', 0)
    scenarios = required(data, 'stress_scenarios')
    if not isinstance(scenarios, list) or len(scenarios) < 2:
        raise InputError('at least two explicit stress scenarios required')
    for s in scenarios + data.get('return_regimes', []):
        source(required(s, 'name'), 'scenario.name')
        source(required(s, 'source'), 'scenario.source')
        for fid in seen:
            number(required(required(s, 'returns'), fid), 'scenario.' + fid, -1, 5)
        number(s.get('cash_return', 0), 'stress.cash_return', -1, 5)
    gross = p['cash_available'] + sum(f['current_value'] for f in funds)
    if gross <= 0:
        raise InputError('cash plus holdings must be positive')
    reserve = p['emergency_reserve'] + p['near_term_reserve']
    if reserve > gross:
        raise InputError('protected reserves exceed all funds; no investment capacity')
    if 'high_water_mark' in p:
        number(p['high_water_mark'], 'high_water_mark', gross)
    return as_of, gross, reserve


def prepare(data, input_dir):
    as_of, gross, reserve = validate_input(data)
    hist = required(data, 'history')
    if required(hist, 'kind') != 'total_return_base_currency':
        raise InputError('history must be verified total_return_base_currency, not raw NAV')
    if required(hist, 'base_currency') != data['profile']['base_currency']:
        raise InputError('history and profile currency mismatch')
    source(required(hist, 'source'), 'history.source')
    declared_as_of = dated(required(hist, 'as_of'), 'history.as_of', as_of)
    freq = number(required(hist, 'observations_per_year'), 'observations_per_year', 1, 366)
    min_obs = number(required(hist, 'min_observations'), 'min_observations', 30)
    path = Path(required(hist, 'path'))
    if not path.is_absolute():
        path = Path(input_dir) / path
    df = pd.read_csv(path)
    if len(df) == 0:
        raise InputError('history contains no observations')
    if 'date' not in df:
        raise InputError('history must contain date column')
    try:
        dates = pd.to_datetime(df.pop('date'), format='%Y-%m-%d', errors='raise')
    except (ValueError, TypeError):
        raise InputError('invalid history dates') from None
    if dates.isna().any() or dates.duplicated().any() or not dates.is_monotonic_increasing:
        raise InputError('history dates must be valid, unique, and increasing')
    if any(d.date() > as_of for d in dates):
        raise InputError('history contains future observations')
    if dates.iloc[-1].date() != declared_as_of:
        raise InputError('history as_of does not match last CSV observation')
    cols = [f.get('history_id', f['id']) for f in data['funds']]
    if any(col not in df for col in cols):
        raise InputError('history missing fund columns')
    try:
        prices = df[cols].apply(pd.to_numeric, errors='raise')
    except (ValueError, TypeError):
        raise InputError('history contains non-numeric values') from None
    prices.index = dates
    missing = len(prices) - len(prices.dropna())
    if missing / max(len(prices), 1) > 0.1:
        raise InputError('over 10% history rows lack a common observation')
    prices = prices.dropna()
    if len(prices) < min_obs + 1:
        raise InputError('insufficient common total-return observations')
    span_days = (prices.index[-1]-prices.index[0]).days
    empirical_frequency = (len(prices)-1)*365.25/span_days if span_days > 0 else 0
    if not 0.75 <= empirical_frequency/freq <= 1.25:
        raise InputError('declared history frequency conflicts with common observation dates')
    if not np.isfinite(prices.to_numpy()).all() or (prices <= 0).any().any():
        raise InputError('history prices must be finite and positive')
    lag = (as_of - prices.index[-1].date()).days
    if lag > data['profile']['max_history_lag_days']:
        raise InputError('common-date total-return history is stale')
    if lag < 0:
        raise InputError('future common observations')
    prices.columns = [f['id'] for f in data['funds']]
    returns = prices.pct_change(fill_method=None).dropna()
    raw_cov = risk_models.sample_cov(prices, frequency=freq).to_numpy()
    cov = 0.8 * raw_cov + 0.2 * np.diag(np.diag(raw_cov))
    cov = (cov + cov.T) / 2
    eig = np.linalg.eigvalsh(cov)
    if not np.isfinite(cov).all() or eig.min() < -1e-9:
        raise InputError('invalid risk covariance')
    cov += np.eye(len(cov)) * max(0, 1e-12 - eig.min())
    return {'gross': gross, 'reserve': reserve, 'cov': cov, 'returns': returns,
            'history_rows': len(prices), 'dropped_rows': missing, 'history_lag_days': lag,
            'declared_observations_per_year': freq, 'empirical_observations_per_year': empirical_frequency}


def context(data, prep):
    fs, p, g = data['funds'], data['profile'], prep['gross']
    cur = np.array([f['current_value'] / g for f in fs])
    fee_buy = np.array([f['buy_fee_rate'] for f in fs])
    fee_sell = np.array([f['sell_fee_rate'] for f in fs])
    caps = np.array([min(p['max_single_fund_weight'], f.get('max_weight', 1)) for f in fs])
    max_buy = np.array([f['max_buy_amount'] / (1+f['buy_fee_rate']) / g if f['buy_allowed'] and f['market'] in p['allowed_markets'] else 0 for f in fs])
    max_sell = np.array([f['sellable_value'] / g if f['sell_allowed'] else 0 for f in fs])
    for i, f in enumerate(fs):
        funding_upper_bound = max(0, p['cash_available'] - prep['reserve'] +
                                  sum(max_sell[j]*g*(1-fs[j]['sell_fee_rate']) for j in range(len(fs)) if j != i))
        minimum = f['min_buy_amount']
        if f['instrument_type'] in ['etf','lof','reit','stock']:
            minimum = max(minimum, f['lot_size']*f['price_base_currency']*(1+f['buy_fee_rate']))
        if min(f['max_buy_amount'],funding_upper_bound) + 1e-7 < minimum:
            max_buy[i] = 0
    shocks = np.array([[s['returns'][f['id']] for f in fs] for s in data['stress_scenarios']])
    shock_cash = np.array([s.get('cash_return', 0) for s in data['stress_scenarios']])
    regimes = data.get('return_regimes') or [{'name': 'conservative_forward', 'source': 'per-fund estimates',
                                             'returns': {f['id']: f['forward_return_low'] for f in fs}}]
    mu = np.array([[s['returns'][f['id']] for f in fs] for s in regimes])
    risk_budget = p['max_stress_loss']
    if 'high_water_mark' in p:
        risk_budget = max(0, (g - p['high_water_mark'] * (1 - p['max_stress_loss'])) / g)
    exposures = {k: np.array([f['exposures'][k] for f in fs]) for k in data.get('exposure_caps', {})}
    return dict(cur=cur, fee_buy=fee_buy, fee_sell=fee_sell, caps=caps, max_buy=max_buy,
                max_sell=max_sell, shocks=shocks, shock_cash=shock_cash, mu=mu,
                risk_budget=risk_budget, exposures=exposures)


def evaluate(w, data, prep, ctx):
    """Independent recomputation of net fees, cash and constraints."""
    p, g = data['profile'], prep['gross']
    w = np.asarray(w, dtype=float)
    b, s = np.maximum(w - ctx['cur'], 0), np.maximum(ctx['cur'] - w, 0)
    fees = float(ctx['fee_buy'] @ b + ctx['fee_sell'] @ s)
    cash = float(1 - w.sum() - fees)
    variance = max(0, float(w @ prep['cov'] @ w))
    volatility = math.sqrt(variance)
    losses = fees - ctx['shocks'] @ w - ctx['shock_cash'] * cash
    objective = float(np.min(ctx['mu'] @ w) + p['cash_annual_return'] * cash
                      - 0.5 * variance - fees / p['horizon_years'])
    tolerance = 2e-7
    violations = []
    def check(ok, reason):
        if not ok:
            violations.append(reason)
    check(np.all(w >= -tolerance), 'negative_position')
    check(np.all(w <= ctx['caps'] + tolerance), 'single_fund_cap')
    check(np.all(b <= ctx['max_buy'] + tolerance), 'purchase_status_or_quota')
    check(np.all(s <= ctx['max_sell'] + tolerance), 'redemption_status_or_locked_units')
    check(cash >= prep['reserve'] / g - tolerance, 'protected_cash_reserve')
    check(float((b+s).sum()) <= p['max_turnover'] + tolerance, 'turnover_cap')
    check(volatility <= p['max_annual_volatility'] + tolerance, 'annual_volatility_budget')
    check(np.all(losses <= ctx['risk_budget'] + tolerance), 'stress_loss_budget')
    for k, exposure in ctx['exposures'].items():
        check(float(exposure @ w) <= data['exposure_caps'][k] + tolerance, 'exposure_cap:' + k)
    return {'feasible': not violations, 'violations': violations,
            'cash_amount': round(cash * g, 6), 'fee_amount': round(fees * g, 6),
            'volatility': volatility, 'worst_stress_loss': float(max(losses)),
            'stress_losses': {s['name']: float(x) for s, x in zip(data['stress_scenarios'], losses)},
            'annual_growth_objective': objective, 'turnover': float((b+s).sum()),
            'weights_before_cost_nav': {f['id']: float(x) for f, x in zip(data['funds'], w)}}


def solve(data, prep):
    ctx = context(data, prep)
    p, fs, n = data['profile'], data['funds'], len(data['funds'])
    w, b, s = cp.Variable(n), cp.Variable(n, nonneg=True), cp.Variable(n, nonneg=True)
    c, growth = cp.Variable(), cp.Variable()
    fee = ctx['fee_buy'] @ b + ctx['fee_sell'] @ s
    cash0 = p['cash_available'] / prep['gross']
    constraints = [w == ctx['cur'] + b - s, w >= 0, w <= ctx['caps'],
                   b <= ctx['max_buy'], s <= ctx['max_sell'],
                   c == cash0 - cp.sum(b) + cp.sum(s) - fee,
                   c >= prep['reserve'] / prep['gross'],
                   cp.sum(b+s) <= p['max_turnover'],
                   cp.quad_form(w, cp.psd_wrap(prep['cov'])) <= p['max_annual_volatility']**2,
                   fee - ctx['shocks'] @ w - ctx['shock_cash'] * c <= ctx['risk_budget']]
    for key, exposure in ctx['exposures'].items():
        constraints.append(exposure @ w <= data['exposure_caps'][key])
    for mu in ctx['mu']:
        constraints.append(growth <= mu @ w + p['cash_annual_return'] * c
                           - 0.5 * cp.quad_form(w, cp.psd_wrap(prep['cov']))
                           - fee / p['horizon_years'])
    problem = cp.Problem(cp.Maximize(growth - 1e-9 * cp.sum(b+s)), constraints)
    try:
        problem.solve(solver='CLARABEL', max_iter=300)
    except cp.error.SolverError as exc:
        return {'status': 'solver_error', 'reason': str(exc), 'execution_authorized': False}
    if problem.status != cp.OPTIMAL:
        return {'status': problem.status, 'execution_authorized': False,
                'constraint_summary': {'reserve': prep['reserve'], 'position_caps': ctx['caps'].tolist(),
                                       'locked_values': ((ctx['cur']-ctx['max_sell'])*prep['gross']).tolist(),
                                       'stress_budget': ctx['risk_budget'],
                                       'action': 'Identify conflicting reserve/locked/cap/risk constraints; do not relax silently.'}}
    target = np.maximum(np.asarray(w.value).ravel(), 0)
    validation = evaluate(target, data, prep, ctx)
    if not validation['feasible']:
        return {'status': 'failed_independent_validation', 'validation': validation,
                'execution_authorized': False}
    comparisons = {'no_trade': evaluate(ctx['cur'], data, prep, ctx),
                   'all_cash': evaluate(np.zeros(n), data, prep, ctx)}
    equal = np.repeat(max(0, 1-prep['reserve']/prep['gross']) / n, n)
    comparisons['equal_weight'] = evaluate(equal, data, prep, ctx)
    try:
        hrp = HRPOpt(returns=prep['returns']).optimize()
        weights = np.array([hrp[f['id']] for f in fs]) * max(0, 1-prep['reserve']/prep['gross'])
        comparisons['hrp'] = evaluate(weights, data, prep, ctx)
    except (ValueError, FloatingPointError, KeyError, AttributeError) as exc:
        comparisons['hrp'] = {'available': False, 'reason': str(exc)}
    return build_plan(data, prep, ctx, target, validation, comparisons)


def floor_increment(amount, increment):
    return max(0, math.floor((amount + 1e-9) / increment) * increment)


def build_plan(data, prep, ctx, target, validation, comparisons):
    fs, p, g = data['funds'], data['profile'], prep['gross']
    deltas = (target - ctx['cur']) * g
    rounded = []
    for f, delta in zip(fs, deltas):
        if abs(delta) < p['min_trade_amount']:
            delta = 0
        if f['instrument_type'] in ['etf', 'lof', 'reit', 'stock']:
            increment = f['lot_size'] * f['price_base_currency']
        else:
            increment = f.get('buy_increment' if delta >= 0 else 'redemption_increment', 0.01)
        if delta > 0 and f['instrument_type'] == 'mutual_fund':
            payment = floor_increment(delta*(1+f['buy_fee_rate']), increment)
            amount = payment/(1+f['buy_fee_rate'])
        else:
            amount = floor_increment(abs(delta), increment)
        if delta > 0 and amount*(1+f['buy_fee_rate']) < f['min_buy_amount']:
            amount = 0
        rounded.append(amount if delta >= 0 else -amount)
    rounded = np.array(rounded)
    executable_w = ctx['cur'] + rounded / g
    rounded_validation = evaluate(executable_w, data, prep, ctx)
    selection_reason = 'rounded_continuous_solution'
    hold = comparisons['no_trade']
    if hold['feasible'] and (not rounded_validation['feasible'] or
            rounded_validation['annual_growth_objective'] < hold['annual_growth_objective'] - 1e-9):
        selection_reason = 'hold_dominates_or_repairs_rounded_plan'
        rounded = np.zeros(len(fs))
        executable_w = ctx['cur'].copy()
        rounded_validation = hold.copy()
    execution_ok = rounded_validation['feasible']
    cost_need = float(sum(max(x, 0)*(1+f['buy_fee_rate']) for f, x in zip(fs, rounded)))
    immediate_cash = max(0, p['cash_available'] - prep['reserve'])
    fraction = min(1, immediate_cash / cost_need) if cost_need > 0 else 1
    rows, immediate_changes = [], []
    for f, delta, ideal in zip(fs, rounded, target):
        immediate = delta
        if delta > 0:
            increment = f['lot_size']*f['price_base_currency'] if f['instrument_type'] in ['etf','lof','reit','stock'] else f.get('buy_increment', 0.01)
            if f['instrument_type'] == 'mutual_fund':
                immediate = floor_increment(delta*fraction*(1+f['buy_fee_rate']),increment)/(1+f['buy_fee_rate'])
            else:
                immediate = floor_increment(delta*fraction, increment)
            if immediate*(1+f['buy_fee_rate']) < f['min_buy_amount']:
                immediate = 0
        immediate_changes.append(immediate)
        payment = delta*(1+f['buy_fee_rate']) if delta > 0 else delta
        immediate_payment = immediate*(1+f['buy_fee_rate']) if immediate > 0 else immediate
        row = {'id': f['id'], 'name': f['name'], 'current_amount': f['current_value'],
               'ideal_target_amount': round(float(ideal*g), 2),
               'rounded_target_amount': round(float(f['current_value']+delta), 6),
               'target_weight_of_gross': float((f['current_value']+delta)/g),
               'action': 'BUY' if delta > 0 else 'SELL' if delta < 0 else 'HOLD',
               'net_position_change': round(float(delta), 6),
               'planned_trade_amount': round(float(payment), 6),
               'immediate_trade_amount': round(float(immediate_payment), 6),
               'deferred_buy_amount': round(float(max(0, payment-immediate_payment)), 6),
               'estimated_fee_amount': round(float(abs(delta)*f['buy_fee_rate' if delta > 0 else 'sell_fee_rate']), 6),
               'amount_semantics': 'BUY: gross cash payment including fee; SELL: gross redemption before fee',
               'sell_proceeds_available_today': False,
               'source': f['data_source'], 'quote_as_of': f['quote_as_of']}
        if not execution_ok:
            row['immediate_trade_amount'] = None
            row['deferred_buy_amount'] = None
        rows.append(row)
    intermediate = evaluate(ctx['cur']+np.array(immediate_changes)/g, data, prep, ctx)
    if not intermediate['feasible']:
        execution_ok = False
        for row in rows:
            row['immediate_trade_amount'] = None
            row['deferred_buy_amount'] = None
    interval = {}
    for key in ['low', 'base', 'high']:
        forward = np.array([f['forward_return_'+key] for f in fs])
        w = executable_w if rounded_validation['feasible'] else target
        ev = rounded_validation if rounded_validation['feasible'] else validation
        interval[key] = float(forward @ w + p['cash_annual_return']*ev['cash_amount']/g)
    return {'status': 'plan_ready' if execution_ok else 'blocked_rounding_or_sequence',
            'synthetic': bool(data.get('synthetic', False)), 'as_of': data['as_of'],
            'base_currency': p['base_currency'], 'execution_authorized': False,
            'trade_plan_ready_for_human_execution': execution_ok,
            'solver': 'CLARABEL', 'solver_status': 'optimal', 'selection_reason': selection_reason,
            'objective': 'worst_forward_approximate_log_growth_after_cost',
            'gross_assets': g, 'protected_reserve': prep['reserve'],
            'investable_capacity': g-prep['reserve'], 'remaining_stress_budget': ctx['risk_budget'],
            'settled_cash_now': p['cash_available'],
            'reserve_shortfall_now': max(0,prep['reserve']-p['cash_available']),
            'pending_sale_proceeds': float(sum(max(-x,0)*(1-f['sell_fee_rate']) for f,x in zip(fs,rounded))),
            'cash_after_all_settlements': rounded_validation['cash_amount'],
            'history': {k: prep[k] for k in ['history_rows','dropped_rows','history_lag_days','declared_observations_per_year','empirical_observations_per_year']},
            'ideal_validation': validation, 'rounded_validation': rounded_validation,
            'intermediate_validation': intermediate, 'comparisons': comparisons,
            'forward_annual_return_assumptions': interval,
            'probability_of_profit': None,
            'positions': rows,
            'limitations': ['Scenario bounds are assumptions, not calibrated probabilities.',
                           'Stress budget is not a guaranteed drawdown limit.',
                           'Deferred purchases require confirmed settlement and a refreshed calculation.',
                           'Amounts use current valuations; OTC dealing price/units are not guaranteed.',
                           'No brokerage connection or order submission exists.']}


def markdown(result):
    lines = ['# 投资配置决策', '', f"状态：{result['status']}", '']
    if result.get('synthetic'):
        lines += ['**合成案例：所有名称、数据与估计均非真实投资建议。**', '']
    if 'positions' not in result:
        return '\n'.join(lines + ['未生成可执行交易。', '', '```json', json.dumps(result,ensure_ascii=False,indent=2),'```'])
    lines += [f"决策日 {result['as_of']}；币种 {result['base_currency']}。全部资金 {result['gross_assets']:,.2f}，保护储备 {result['protected_reserve']:,.2f}，可承担投资风险的容量 {result['investable_capacity']:,.2f}。", '',
              '| 产品 | 当前金额 | 目标金额 | 买入支付/卖出赎回金额 | 今日金额 | 待到账后支付额 |',
              '|---|---:|---:|---:|---:|---:|']
    for r in result['positions']:
        lines.append(f"| {r['name']} ({r['id']}) | {r['current_amount']:,.2f} | {r['rounded_target_amount']:,.2f} | {r['action']} {r['planned_trade_amount']:,.2f} | {r['immediate_trade_amount']} | {r['deferred_buy_amount']} |")
    ev = result['rounded_validation']
    lines += ['', f"计划后现金 {ev['cash_amount']:,.2f}；估计一次性费用 {ev['fee_amount']:,.2f}；年化波动模型估计 {ev['volatility']:.2%}；最差已建模压力损失 {ev['worst_stress_loss']:.2%}。", '',
              f"当前已到账现金 {result['settled_cash_now']:,.2f}；当前储备缺口 {result['reserve_shortfall_now']:,.2f}；计划赎回净收入 {result['pending_sale_proceeds']:,.2f} 尚未计入今日买入能力。买入列是含前端费用的现金预算，卖出列是扣赎回费前金额。", '',
              '以上压力损失和前瞻收益均是模型条件下估计，不是最大亏损保证或获利概率。计划不代表成交。', '',
              '若状态为 blocked，金额仅是研究目标，不能按今日交易列执行；查看 JSON 约束冲突。', '',
              '完整数据质量、对照方案、舍入后和分阶段约束检查见同名 JSON。']
    return '\n'.join(lines) + '\n'


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, type=Path)
    parser.add_argument('--output-dir', required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.input.read_text(encoding='utf-8-sig'))
        prep = prepare(data, args.input.parent)
        result = solve(data, prep)
    except (InputError, OSError, json.JSONDecodeError) as exc:
        result = {'status': 'invalid_input', 'reason': str(exc), 'execution_authorized': False}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir/'decision.json').write_text(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    (args.output_dir/'decision.md').write_text(markdown(result),encoding='utf-8')
    print(json.dumps({'status':result['status'],'output':str(args.output_dir.resolve())},ensure_ascii=False))
    return 0 if result['status'] == 'plan_ready' else 2


if __name__ == '__main__':
    raise SystemExit(main())
