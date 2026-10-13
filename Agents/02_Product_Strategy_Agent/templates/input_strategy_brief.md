# 输入模板 · 产品策略简报

> **前置要求**：
> 1. 已跑完 [01 Market Research](../../01_Market_Research_Agent/)（提供市场结论）
> 2. 已由人确认"这个产品决定做"（`decision_approved`）

---

## 0. 决策确认 ★ 阻塞项

```yaml
decision_approved*: false      # ⚠️ 必须由人改为 true
approved_by: ""                # 决策人
approved_date: ""              # YYYY-MM-DD
decision_notes: ""             # 决策依据备注
```

> **为什么这是阻塞项**：本模块**不做选品决策**，只做"把已决策的产品规格化"。
> 未确认就往下跑，等于让 Agent 替你做商业决策 —— 这涉及公司战略、资金与风险偏好，Agent 无法代劳。

---

## 1. 任务配置

```yaml
platform*: shopee
target_market*: 巴西
category*: ""
```

---

## 2. 上游字段 · 01 的交付 ★ 阻塞项

```yaml
# ── 从 01 输出的「交付给 02 Product Strategy 的字段」区块直接粘贴 ──

target_price_range*: [0, 0]
main_price_zone: [0, 0]
cost_floor_price: 0.00         # 01 反算的成本可行价（无则填 null）

recommended_config*: {}
mainstream_config: {}
opportunity_config: {}

brand_barrier: ""              # low | medium | high
seller_barrier: ""             # low | medium | high
competitor_weakness*: []
competitor_review_insights: []

benchmark_for_launch:
  days_to_ramp: null
  reviews_needed_before_ramp: null
  sales_needed_before_ramp: null
  ad_dependency: null

pending_confirmations: []
```

---

## 3. 成本结构 ★ 阻塞项

> **不同配置的成本不同，请逐 SKU 填。** 用一个成本套所有 SKU 会算错毛利。

```yaml
cost_structure*:
  commission_rate: 0.14        # ⚠️ 按实际类目查
  return_rate: 0.02            # SOP 规定 2%
  ad_rate: 0.05                # 大件 ~5% / 小件 5–10%
  target_margin_rate: 0.32     # 大件 30–35% / 小件 25–30%
  tax_rate: 0.00               # ⚠️ 巴西税费；填 0 时报告会标注"未含税费"

sku_costs*:
  - sku_role: "引流款"
    product_cost: 0.00
    shipping: 0.00
    warehouse: 0.00
  - sku_role: "主推款"
    product_cost: 0.00
    shipping: 0.00
    warehouse: 0.00
  - sku_role: "高配款"
    product_cost: 0.00
    shipping: 0.00
    warehouse: 0.00
  - sku_role: "套装款"
    product_cost: 0.00          # 含配件包
    shipping: 0.00
    warehouse: 0.00
```

---

## 4. 公司能力与约束

```yaml
company_capabilities:
  can_do_config: true           # 能否实现市场推荐的配置
  config_limitations: ""        # 做不到的配置，如"承重件供应商最高支持 150kg"
  supply_lead_time_days: 0
  moq: 0                        # 最小起订量

after_sales_capacity*:          # 决定能写什么售后承诺
  can_repair: false
  can_replace: true
  has_local_warranty_point: false
  can_provide_parts: true
  warranty_months: 0
  notes: ""
```

> ⚠️ `after_sales_capacity` 直接决定详情页段 5（售后承诺）能写什么。
> **能力之外的一律不能写** —— 写了就是给自己制造差评。

---

## 5. 运营约束（影响定价策略）

```yaml
cash_flow_constraint: ""        # 现金流约束，如"前期最多承受 4 周低毛利"
inventory_level: 0              # 当前库存
can_stock_for_promo: true       # 能否为活动备货
# ⚠️ 虾皮活动一旦参加无法退出，报名时必须核对库存
```

---

## 6. 竞品价格锚点（可选）

```yaml
competitor_price_points:
  - label: "A"
    price: 0.00
    config: ""
  - label: "B"
    price: 0.00
    config: ""
```

---

## 填写自检

- [ ] `decision_approved` 已由人确认改为 true
- [ ] 01 的交付字段已粘贴完整（尤其 `opportunity_config` 与 `cost_floor_price`）
- [ ] `sku_costs` **逐 SKU** 填了，不是用同一个成本
- [ ] `commission_rate` 按实际类目查的，不是套用 14%
- [ ] 税费已计入（未计入时接受报告里的"未含税费"标注）
- [ ] `after_sales_capacity` 如实填写（这决定售后承诺能写什么）
- [ ] 我理解：**采购决策由我做**，Agent 只输出规格与依据
