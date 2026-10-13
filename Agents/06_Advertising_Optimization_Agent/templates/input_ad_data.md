# 输入模板 · 广告数据与成本结构

> **数据质量决定诊断质量。** 曝光不足 1,000 或周期不足 3 天的数据，Agent 会直接拒绝分析——这不是刁难，是样本不足时指标波动会大于信号。

---

## 0. 任务配置

```yaml
platform*: shopee              # shopee | mercadolivre
ad_type*: keyword              # keyword | product | shop（Shopee）/ Mercado Ads
test_window_days*: 7           # 数据覆盖天数
target_market: 巴西
target_market_timezone: "UTC-3"

# 可选但建议填
current_title: ""
current_main_image_desc: ""
```

---

## 1. 定价与成本结构 ★ 阻塞项

> **缺这一块，Agent 拒绝输出任何 ROI 结论**——因为算不出盈亏线，所有"ROI 好不好"的判断都是空谈。

```yaml
price*: 0.00                   # 售价

cost_structure*:
  unit_cost: 0.00              # 产品成本（含头程分摊）
  shipping: 0.00               # 尾程物流（实测值）
  warehouse: 0.00              # 仓储 / 操作费
  commission_rate: 0.14        # 平台佣金率（⚠️ 按实际类目查）
  return_rate: 0.02            # 退货损耗率（SOP 规定 2%）
  # 巴西站提醒：税费未含在此处，若有独立税率请另加字段

target_margin_rate: 0.28       # 目标毛利率（大件 30–35% / 小件 25–30%）
ad_cost_rate_assumed: 0.075    # 定价时预留的广告成本率（小件 5–10%）
```

---

## 2. 广告组数据

> **每个广告组一行。** 指标口径必须与平台后台一致——特别是"加购"的统计口径。

```yaml
ad_groups:
  - keyword_or_target*: ""     # 关键词 / 商品 / 店铺名
    match_type*: ""            # amplo(广泛) | exato(精准) | concorrente(竞品词) | cenario(场景词) | produto(商品)
    impressions*: 0
    clicks*: 0
    add_to_cart*: 0
    orders*: 0
    spend*: 0.00
    # 以下由 Agent 计算，不需要填（填了也会被重算）
    # ctr / atc_rate / cvr / cpc / cpa / roas

  - keyword_or_target*: ""
    match_type*: ""
    impressions*: 0
    clicks*: 0
    add_to_cart*: 0
    orders*: 0
    spend*: 0.00
```

### 数据填写注意

| 项 | 注意 |
|---|---|
| `impressions` | 用**平台后台的曝光数**，不要用"估算曝光" |
| `add_to_cart` | ⚠️ **确认平台的加购口径**——是"加购商品数"还是"加购人数"？各平台不同 |
| `orders` | 用**广告归因订单**，不是总订单 |
| `spend` | 用**实际扣费**，不是预算 |
| 异常广告组 | 若某组曝光极低（花不出钱），也**照常填**——Agent 会识别并走解 bug 流程 |

---

## 3. 预算现状

```yaml
daily_budget_current: 0.00     # 当前日预算
budget_mode: "manual"          # manual | auto（ML 前 7 天建议 manual）
roi_setting_current: 0.00      # 当前 ROI 设置（若有）
bid_strategy: ""               # 出价策略描述
```

---

## 4. 竞品推广数据（可选，用于反推阶段目标）

> 来源：SOP 1.10。填了它，Agent 会反推"新链接多久起量、起量前要多少评价"。

```yaml
competitor_benchmark:
  - name: ""                   # 竞品标识（不要填真实店铺名，用 A/B/C）
    listing_age_days: 0        # 上架天数
    monthly_sales: 0
    last_30d_sales: 0
    review_count: 0
    review_with_image_count: 0
    has_ad_slot: false         # 是否出现在广告位
```

---

## 5. 外部干扰声明（可选但建议）

> 用途：复测时判断指标变化是**动作带来的**还是**外部因素带来的**。

```yaml
external_events:
  - date: ""
    event: ""                  # 例："参加了平台大促" / "竞品降价 15%" / "库存断货 2 天"
```

---

## 填写自检

- [ ] 成本结构完整（缺则无法算盈亏线）
- [ ] `commission_rate` 是按**实际类目**查的，不是套用 14%
- [ ] 每个广告组的曝光/点击/加购/订单/花费都填了
- [ ] 已确认平台"加购"的统计口径
- [ ] 测试周期 ≥ 3 天，总曝光 ≥ 1,000
- [ ] 曝光异常低的广告组也填了（不要删掉不填）
- [ ] 竞品标识已脱敏（用 A/B/C，不用真实店铺名）
- [ ] 已声明外部干扰事件
