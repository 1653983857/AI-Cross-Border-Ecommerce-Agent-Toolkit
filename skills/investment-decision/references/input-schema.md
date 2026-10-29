# 输入规范

脚本读取 JSON 和一份总回报历史 CSV。数值比例统一为小数，例如 0.15=15%；金额统一为基准币种。基础模型限 long-only、无杠杆、线性买卖费，最多 40 个经过研究的候选基金。它不会自动推荐示例代码。

## 顶层

- `as_of`：YYYY-MM-DD，本次决策日。
- `profile`：下表全部字段必须由用户或已知记录确认。
- `funds`：持仓及候选。所有已有持仓必须进入输入，不能只放想买的基金。
- `history`：`path` 为相对本 JSON 的 CSV 路径或绝对路径；`kind` 必须 `total_return_base_currency`；`base_currency` 必须与画像一致；`observations_per_year` 通常 252/52/12，按真实频率；`min_observations` 至少 30、实际建议 >=252；`source` 与 `as_of` 必填。
- `stress_scenarios`：至少两个场景，每个有 `name`、`source`、`returns`（所有基金 ID 到小数收益的映射），`cash_return` 可设为 0 并写明假设。它们是瞬间冲击，不是年度收益预测。
- `exposure_caps`：可选，`{"equity":0.7,"us":0.4,"technology":0.2}`；每个基金必须明确相应穿透暴露。已知前十持仓不等于完整暴露，缺失不填 0。
- `return_regimes`：可选，多个有来源的前瞻情景 `{name,source,returns:{ID:annual_return}}`；若提供，优化所有场景中的最差近似增长；默认使用每基金的 forward_return_low。

## profile

| 字段 | 含义 |
|---|---|
| base_currency | CNY/USD 等 |
| cash_available | 已到账、可用现金，含本次实际到账新增资金；不要再次叠加计划中的月收入 |
| emergency_reserve | 应急储备；和其他储备不能重叠计算 |
| near_term_reserve | 投资期内确定要花的钱 |
| horizon_years | 本次目标投资期限，>0 |
| max_stress_loss | 可接受的本期组合压力损失比例，不是保证的最大回撤 |
| max_annual_volatility | 年化波动预算 |
| max_single_fund_weight | 占全部资金的单基金上限；现金不受此上限 |
| max_turnover | 买入+卖出金额/全部资金上限，0–2 |
| cash_annual_return | 经核实、扣费后的现金年化收益估计 |
| min_trade_amount | 基准币种最小有意义交易额 |
| allowed_markets | 实际可购买市场的非空列表，如 CN/HK/US/EU |
| max_history_lag_days | 允许总回报序列落后决策日的自然日数，按市场假期/净值延迟确认 |
| max_quote_lag_days | 允许用于估值和金额计算的价格/净值落后天数 |
| high_water_mark | 可选，真实资金流调整后的历史高水位；否则不推断已发生回撤 |

## 每个 fund

必填：`id`（唯一代码含份额）、`name`、`market`（购买载体市场，不是底层国家）、`instrument_type`（mutual_fund/etf/lof/reit/stock）、`currency`（计价币种）、`current_value`（基准币种现值）、`sellable_value`（已确认可卖现值）、`buy_allowed`/`sell_allowed`（布尔值）、`buy_fee_rate`/`sell_fee_rate`（本笔扣费/税/价差估计，0–1）、`max_buy_amount`（本期申购/账户额度，基准币种）、`min_buy_amount`、`forward_return_low`/`forward_return_base`/`forward_return_high`（同基准币种、扣持续费后的年化估计，必须有序）、`return_source`、`data_source`、`quote_as_of`（YYYY-MM-DD）。

申购口径：`max_buy_amount`、`min_buy_amount` 和场外 `buy_increment` 均指平台支付总额（含前端申购费）。`buy_fee_rate` 定义为新增净资产的费率，支付额=新增净资产×(1+费率)。若平台按支付额扣费，先换算成本模型费率。输出买入金额为支付额，`net_position_change` 为净增加持仓；卖出金额为扣赎回费前的赎回额，另列费用。海外交易额/报价先用核验汇率换算到基准币种，实际外币支付需按当时汇率复核。

可选：`max_weight` 覆盖为更严格单品上限；`exposures` 穿透风险字典；`sell_settlement_days`（默认正值，不把卖出收入当今日现金）；`buy_increment`（场外支付金额增量，默认 0.01）；`redemption_increment`（按现值折算金额，默认 0.01，仅预算口径）；`lot_size` 与 `price_base_currency`（场内必须提供，并据其计算整手净成交预算）；`history_id`（相同份额共享总回报列时显式指定）；`holding_period_notes`（赎回费精算依据）。

因暂停买入/不可准入，脚本允许现有持仓保留并按可卖部分降仓，绝不新增。暂停卖出或锁定份额形成持仓下界，冲突会报 infeasible。A/C 类、美元/人民币类必须不同 id。非线性赎回费需要先按实际持有批次汇总出本笔成本，无法线性近似时不运行金额执行建议。

## 历史 CSV

首列 `date`，其余列为基金 id/history_id，值为同币种、分红再投资的总回报指数或调整价格。日期递增且唯一，不允许前视日期。不得把累计净值无条件视为复投总回报；必须核实提供方定义。不同币种先做 `TR_base(t)=TR_local(t)*FX_base_per_local(t)` 再对齐共同日期。缺值只做交集，不前向填补跨时区净值。

所有金额和估计都应保留来源。示例 `examples/synthetic.json` 与 CSV 仅为合成测试，无真实代码、行情或建议。
