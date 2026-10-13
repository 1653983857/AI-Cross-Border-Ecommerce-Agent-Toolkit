# 输入模板 · 类目调研

> **前置步骤**：先跑 `scripts/` 下的两个脚本产出 `metrics_report`，再来填这个模板。
> 脚本跑不通 / 数据进不来时，**不要手工估算指标** —— 那是本模块最想避免的事。

---

## 0. 任务配置

```yaml
platform*: shopee
target_market*: 巴西
category*: ""                  # 类目名
sample_size: 0                 # 样本商品数（从 metrics_report 读）
data_date: ""                  # 数据日期 YYYY-MM-DD
```

---

## 1. 指标报告 ★ 阻塞项

> 由 `market_metrics.py` 产出。**直接把 `.md` 内容粘贴过来，或给 `.json` 路径。**

```yaml
metrics_report_source: ""      # 文件路径，或标注"见下方粘贴内容"
metrics_json_path: ""
```

```text
（在此粘贴 metrics.md 的完整内容，或说明 JSON 路径）
```

### 可选：多期数据（用于判断趋势）

SOP 1.2 要求判断"是否处于增长期/下滑期"。**单期快照无法判断**，需要 2 期以上：

| 期次 | 数据日期 | 月总销量 | 月总销售额 | 备注 |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

---

## 2. 公司资源能力 ★ 阻塞项（前置判断必需）

> 缺这一块，前置判断无法执行 —— Agent 不允许替公司假设能力。

```yaml
company_capabilities:
  has_stock_or_incoming: false        # 是否有现货或即将到货
  has_stable_supplier: false          # 是否有稳定供应商
  has_cost_advantage: false           # 成本是否有优势
  fits_target_market: false           # 是否适合目标市场
  fits_warehouse_logistics: false     # 体积重量是否适合当前仓储物流
  can_handle_after_sales: false       # 是否有能力处理售后/维修/配件/退换货
  after_sales_notes: ""               # 补充说明（如"只能处理换货，不做维修"）
```

### 产品画像（用于风险判定）

```yaml
product_profile:
  weight_kg: 0
  volume_cm: ""                       # 如 "90 × 25 × 110"
  is_fragile: false                   # 是否易碎
  needs_certification: []             # 需认证，如 ["ANATEL", "INMETRO"]
  contains_battery: false
  is_liquid_or_magnet: false
  high_virtual_spec_risk: false       # 是否容易参数虚标
  ip_risk: ""                         # 知识产权风险描述
```

---

## 3. 成本结构（价格带判断"有没有利润"必需）

```yaml
cost_structure:
  unit_cost: 0.00
  shipping: 0.00
  warehouse: 0.00
  commission_rate: 0.14
  return_rate: 0.02
  after_sales_cost_per_unit: 0.00     # 高风险类目需填（维修/配件/罚分摊分）
target_margin_rate: 0.30              # 大件 30–35% / 小件 25–30%
```

---

## 4. 竞品数据（SOP 1.6 要求 2–3 个）

> 筛选标准：价格区间接近 / 配置接近 / 目标用户接近 / 销量较高 / 评价较多 / 近期仍有销量 / **与我方计划做的产品存在直接竞争关系**。

```yaml
competitors:
  - label: "A"                        # ⚠️ 用代号，不要填真实店铺名
    price: 0.00
    monthly_sales: 0
    monthly_revenue: 0.00
    sales_growth_rate: 0.00
    listing_age_days: 0
    rating: 0.0
    review_count: 0
    review_with_image_count: 0
    core_config: ""                   # 核心配置
    title: ""
    main_image_points: []             # 主图打出的卖点
    detail_page_notes: ""             # 详情页特点
    in_ad_slot: false                 # 是否出现在广告位
  - label: "B"
    # ... 同结构
```

### 竞品评论（可选，浅层即可）

```yaml
competitor_reviews:
  - competitor: "A"
    text: ""                          # 保留原文语言
    rating: 0
```

> **深度评论归因交给 [`07 Review Analysis`](../../07_Review_Analysis_Agent/)。** 这里只填"竞品靠什么卖"够用的量级。

---

## 5. 配置维度（用于脚本抽取）

```yaml
config_dimensions: []
# 例：["功率", "承重", "电池容量", "是否可折叠"]
# 已在脚本里用 --config-fields 指定过，这里仅作记录
```

---

## 填写自检

- [ ] `metrics_report` 来自脚本，不是手工估算
- [ ] `company_capabilities` 六项都填了（含 `after_sales_notes`）
- [ ] `product_profile` 填了体积重量与认证需求
- [ ] 高风险类目填了 `after_sales_cost_per_unit`
- [ ] 竞品用代号（A/B/C），未填真实店铺名
- [ ] 评论保留原文语言，未翻译
- [ ] 若只有单期数据，已准备接受"无法判断趋势"的结论
- [ ] 我理解：**最终选品决策由我做**，Agent 只输出分析与依据
