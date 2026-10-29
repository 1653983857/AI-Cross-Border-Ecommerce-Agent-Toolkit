"""Behavioral numerical invariants; all inputs synthetic."""
from pathlib import Path
import copy
import importlib.util
import json
import math
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import allocate as a

class AllocationTests(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'examples/synthetic.json').read_text(encoding='utf-8'))
    def run_case(self,data=None):
        data=data or self.data
        prep=a.prepare(data,ROOT/'examples')
        return a.solve(data,prep),prep
    def test_money_conservation_and_reserve(self):
        result,prep=self.run_case()
        self.assertEqual(result['status'],'plan_ready')
        ev=result['rounded_validation']
        target=sum(r['rounded_target_amount'] for r in result['positions'])
        self.assertAlmostEqual(target+ev['cash_amount']+ev['fee_amount'],prep['gross'],places=4)
        self.assertGreaterEqual(ev['cash_amount']+1e-5,prep['reserve'])
        self.assertTrue(ev['feasible'])
        self.assertLessEqual(ev['worst_stress_loss'],self.data['profile']['max_stress_loss']+2e-7)
    def test_no_broker_authorization(self):
        r,_=self.run_case()
        self.assertFalse(r['execution_authorized'])
        self.assertIsNone(r['probability_of_profit'])
    def test_immediate_buys_never_spend_pending_sales(self):
        self.data['profile']['cash_available']=50000
        self.data['funds'][0]['current_value']=60000
        self.data['funds'][0]['sellable_value']=60000
        r,_=self.run_case()
        if not r.get('trade_plan_ready_for_human_execution'): return
        required=sum(max(0,x['immediate_trade_amount']) for x in r['positions'])
        self.assertLessEqual(required,10000+1e-6)
        self.assertTrue(all(not x['sell_proceeds_available_today'] for x in r['positions']))
    def test_all_cash_when_opportunity_cost_is_higher(self):
        for f in self.data['funds']:
            f.update(forward_return_low=-.01,forward_return_base=0,forward_return_high=.01)
        r,_=self.run_case()
        self.assertEqual(r['status'],'plan_ready')
        self.assertLess(sum(x['rounded_target_amount'] for x in r['positions']),30)
    def test_suspended_purchase(self):
        self.data['funds'][0]['buy_allowed']=False
        r,_=self.run_case()
        self.assertLessEqual(r['positions'][0]['planned_trade_amount'],0)
    def test_unavailable_market_does_not_prevent_liquidation(self):
        self.data['funds'][1]['market']='US'
        r,_=self.run_case()
        self.assertLessEqual(r['positions'][1]['planned_trade_amount'],0)
    def test_locked_holdings_cannot_be_sold(self):
        f=self.data['funds'][1];f['sell_allowed']=False;f['sellable_value']=0
        r,_=self.run_case()
        self.assertGreaterEqual(r['positions'][1]['rounded_target_amount']+.01,f['current_value'])
    def test_infeasible_risk_not_silently_relaxed(self):
        for f in self.data['funds']: f['sell_allowed']=False
        self.data['profile']['max_stress_loss']=.01
        r,_=self.run_case()
        self.assertIn(r['status'],['infeasible','infeasible_inaccurate'])
        self.assertNotIn('positions',r)
    def test_high_water_mark_reduces_remaining_budget(self):
        self.data['profile']['high_water_mark']=190000
        r,_=self.run_case()
        self.assertAlmostEqual(r['remaining_stress_budget'],(180000-190000*.86)/180000)
    def test_cap_on_lookthrough_exposure(self):
        self.data['exposure_caps']['us']=.10
        r,_=self.run_case()
        self.assertLessEqual(r['positions'][1]['rounded_target_amount']/r['gross_assets']*.95,.10+2e-7)
    def test_buy_quota(self):
        self.data['funds'][2]['max_buy_amount']=1000
        r,_=self.run_case()
        self.assertLessEqual(r['positions'][2]['planned_trade_amount'],1000.01)
    def test_missing_profile_rejected(self):
        del self.data['profile']['emergency_reserve']
        with self.assertRaises(a.InputError): self.run_case()
    def test_raw_nav_rejected(self):
        self.data['history']['kind']='unit_nav'
        with self.assertRaises(a.InputError): self.run_case()
    def test_currency_mismatch_rejected(self):
        self.data['history']['base_currency']='USD'
        with self.assertRaises(a.InputError): self.run_case()
    def test_stale_quote_rejected(self):
        self.data['funds'][0]['quote_as_of']='2025-01-01'
        with self.assertRaises(a.InputError): self.run_case()
    def test_future_quote_rejected(self):
        self.data['funds'][0]['quote_as_of']='2026-11-01'
        with self.assertRaises(a.InputError): self.run_case()
    def test_missing_stress_component_rejected(self):
        self.data['stress_scenarios'][0]['returns'].pop(self.data['funds'][0]['id'])
        with self.assertRaises(a.InputError): self.run_case()
    def test_unknown_exposure_not_assumed_zero(self):
        self.data['funds'][0]['exposures'].pop('us')
        with self.assertRaises(a.InputError): self.run_case()
    def test_nonfinite_fee_rejected(self):
        self.data['funds'][0]['buy_fee_rate']=float('nan')
        with self.assertRaises(a.InputError): self.run_case()
    def test_bad_return_interval_rejected(self):
        self.data['funds'][0]['forward_return_low']=.5
        with self.assertRaises(a.InputError): self.run_case()
    def test_large_lot_rounding_never_violates_risk(self):
        f=self.data['funds'][0];f.update(instrument_type='etf',lot_size=100,price_base_currency=100)
        r,_=self.run_case()
        if r['trade_plan_ready_for_human_execution']:
            self.assertTrue(r['rounded_validation']['feasible'])
            self.assertTrue(r['intermediate_validation']['feasible'])
        else:
            self.assertTrue(all(x['immediate_trade_amount'] is None for x in r['positions']))
    def test_minimum_buy_is_respected(self):
        self.data['funds'][2]['min_buy_amount']=1000000
        r,_=self.run_case()
        self.assertLessEqual(r['positions'][2]['planned_trade_amount'],0)
    def test_baselines_are_checked_not_assumed_feasible(self):
        r,_=self.run_case()
        self.assertIn('violations',r['comparisons']['equal_weight'])
        self.assertIn('feasible',r['comparisons']['all_cash'])
    def test_do_nothing_when_turnover_forbidden(self):
        self.data['profile']['max_turnover']=0
        r,_=self.run_case()
        self.assertEqual(r['status'],'plan_ready')
        self.assertTrue(all(x['action']=='HOLD' for x in r['positions']))
    def test_money_cannot_be_counted_twice(self):
        self.data['profile']['emergency_reserve']=200000
        with self.assertRaises(a.InputError): self.run_case()
    def test_id_and_share_class_are_unique(self):
        self.data['funds'][1]['id']=self.data['funds'][0]['id']
        with self.assertRaises(a.InputError): self.run_case()
    def test_gross_purchase_limit_includes_fee(self):
        self.data['funds'][2].update(max_buy_amount=1000,buy_fee_rate=.15)
        r,_=self.run_case()
        self.assertLessEqual(r['positions'][2]['planned_trade_amount'],1000+1e-5)
        row=r['positions'][2]
        if row['action']=='BUY':
            self.assertAlmostEqual(row['planned_trade_amount'],row['net_position_change']*1.15,places=4)
    def test_post_rounding_does_not_underperform_feasible_hold(self):
        self.data['funds'][2]['min_buy_amount']=1000000
        r,_=self.run_case()
        if r['comparisons']['no_trade']['feasible'] and r['rounded_validation']['feasible']:
            self.assertGreaterEqual(r['rounded_validation']['annual_growth_objective']+1e-9,r['comparisons']['no_trade']['annual_growth_objective'])
    def test_frequency_cannot_hide_daily_risk_as_monthly(self):
        self.data['history']['observations_per_year']=12
        with self.assertRaises(a.InputError): self.run_case()

if __name__=='__main__': unittest.main(verbosity=2)
