# Agents · 模块索引

7 个 Agent 模块，统一结构：

```text
<NN>_<Name>_Agent/
├── README.md        # 解决什么问题 / 输入输出 / 使用方法 / 已知限制
├── prompts/         # 系统 Prompt + 任务 Prompt
├── templates/       # 标准输入模板 + 标准输出模板
└── examples/        # 真实产品跑通记录
```

---

## 已完成

### v0.1 · 创意簇

| 编号 | 模块 | 职责 | 依赖 | 目录 |
|---|---|---|---|---|
| **03** | **Listing Creative Agent** | 关键词分类 → 标题 → 详情页 → 卖点/参数 → 合规自检 | 无（入口模块） | [→](./03_Listing_Creative_Agent/) |
| **04** | **Product Image Agent** | 9 图内容规划 + 每张图的出图 Prompt + 图片合规校验 | **03**（需 `core_selling_point`） | [→](./04_Product_Image_Agent/) |
| **05** | **Product Video Agent** | 15s/30s 脚本 → 分镜 → AI 视频 Prompt → 配音字幕 | **03**（需 `core_selling_point`） | [→](./05_Product_Video_Agent/) |

### v0.2 · 运营簇

| 编号 | 模块 | 职责 | 依赖 | 目录 |
|---|---|---|---|---|
| **06** | **Advertising Optimization Agent** | 四类漏斗诊断（曝光→点击→加购→转化）+ 盈亏线核算 + 预算/ROI 模型 | 广告数据 + 成本结构 | [→](./06_Advertising_Optimization_Agent/) |
| **07** | **Review Analysis Agent** | 好评/差评分类 → 八类归因 → 误解型识别 → 详情页修补建议 | 评论数据 + `spec_table` | [→](./07_Review_Analysis_Agent/) |

### v0.3 · 分析簇（前置链路）

| 编号 | 模块 | 职责 | 依赖 | 目录 |
|---|---|---|---|---|
| **01** | **Market Research Agent** | 类目前置判断 / 容量 / 集中度 / 价格带（含波谷检测）/ 配置组合 · **带数据解析与指标计算脚本** | 类目导出数据 + 公司资源 + 成本结构 | [→](./01_Market_Research_Agent/) |
| **02** | **Product Strategy Agent** | 产品定位 / 核心配置 / 主推卖点收敛 / 风险规避 / 定价模型 / SKU 四角色结构 | **01** + `decision_approved` | [→](./02_Product_Strategy_Agent/) |

✅ **7 个模块全部完成。**

---

## 编号说明

原始规划为 `01` 市场 → `02` 产品策略 → `03` Listing → `04` 广告 → `05` 评论 → `06` 视频。
v0.1 按**工作簇**重排为 `03-04-05`（创意簇：文案→图→视频）与 `06-07`（运营簇：广告→评论），让天然串联的模块编号连续。变更记录见根目录 [CHANGELOG.md](../CHANGELOG.md)。

---

## 交接契约

```text
01 Market Research ──► 02 Product Strategy ──► 03 Listing Creative
（要不要做、什么价位）  （做成什么样）           （怎么表达）
                                                    │
                              ┌─────────────────────┼─────────────────────┐
                              ▼                     ▼                     ▼
                     04 Product Image      05 Product Video        上架 → 平台运行
                                                                        │
                                          ┌─────────────────────────────┴──────────┐
                                          ▼                                        ▼
                                 06 Advertising                           07 Review Analysis
                                 （广告数据）                              （评论数据）
                                          │                                        │
                                          └────────► 回流 03/04（iterate）◄────────┘
                                                             │
                                                             ▼
                                                          复测 → 达标放量 / 未达标回诊断
```

### 正向契约

| 上游 | 必须提供 | 下游 | 缺失时的行为 |
|---|---|---|---|
| 01 | `target_price_range` / `recommended_config` / `opportunity_config` / `cost_floor_price` | 02 | 02 无法定价与确认配置 → 报错 |
| 02 | `core_selling_point`（唯一）/ `secondary_points` / `forbidden_words_seed` / `after_sales_commitment` | 03 | 03 无法收敛卖点 → 报错 |
| 02 | `breakeven_roas_by_sku` | 06 | 06 无法判断广告是否赚钱 → 拒绝输出 ROI 结论 |
| 03 | `core_selling_point` / `spec_table` / `forbidden_words` / `title_final` | 04 / 05 | **阻塞**，04/05 不许开工 |

### 回流契约（06 / 07 → 03 / 04）

| 上游 | 输出字段 | 回流目标 | 约束 |
|---|---|---|---|
| **06** | `symptom_by_group` / `ctr_fail_groups` / `atc_fail_groups` / `cvr_fail_groups` / `breakeven_roas` | 03（iterate）、04（iterate） | **只改症状指向的环节**，其余不动 |
| **07** | `review_patch_suggestions` / `forbidden_words_candidates` / `selling_points_ranked` / `packaging_clarity_needed` | 03（iterate）、04（iterate） | 修补文案须为**目标市场母语**且可直接粘贴 |

**闭环纪律**（前文各模块反复强调）：
1. 一次只改一个**病因**（指向同一病因的动作可同批）
2. 不属于症状的环节**不许动**
3. 未达标**不加码同一动作**，回诊断重新定位

完整闭环演示见 [`../Examples/03_Closed_Loop/`](../Examples/03_Closed_Loop/)。完整前置链路见 [`01`](./01_Market_Research_Agent/examples/patinete_eletrico_market.md) → [`02`](./02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md) → [`03`](./03_Listing_Creative_Agent/examples/powerbank_20000mah.md)。

---

**文档**：[SOP→Agent 拆解](../docs/00_Architecture_SOP_to_Agent.md) · [Prompt 规范](../docs/01_Prompt_Design_Guide.md) · [平台字段规范](../docs/02_Platform_Output_Spec.md) · [合规红线](../docs/03_Compliance_Guard.md) · [自检清单](../docs/04_Result_Checklist.md)
