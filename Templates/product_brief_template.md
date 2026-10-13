# 模板 · 标准中间产物（Product Brief）

> **这是三个模块之间的通信契约。** 03 产出它，04 和 05 消费它。
> 它不是"某个 Agent 的输入模板"，而是**模块间的数据接口定义**。

---

## 为什么需要它

没有中间产物会发生什么：

```text
❌ 无契约
运营跑完 03 得到一堆文案
→ 拿给 04 出图，04 自己"理解"了一遍卖点（理解偏了）
→ 拿给 05 做视频，05 又自己理解了一遍（理解又偏了）
→ 三处卖点不一致，观众觉得是拼凑的
```

```text
✅ 有契约
03 输出结构化的 product_brief
→ 04 直接读 core_selling_point（零解释损耗）
→ 05 直接读同一份 core_selling_point
→ 三处完全一致
```

---

## 字段定义

### 必填字段（阻塞项）

| 字段 | 类型 | 定义 | 谁产出 | 谁消费 |
|---|---|---|---|---|
| `product_name` | string | 产品通用名（目标语言） | 人工 | 03/04/05 |
| `target_market` | string | 目标市场 | 人工 | 03/04/05 |
| `platform` | enum | 目标平台 | 人工 | 03/04/05 |
| **`core_selling_point`** | string | **一句话主卖点**，必须可验证 | 03 | **04/05** |
| **`secondary_points[]`** | array | 副卖点 3–5 条 | 03 | **04/05** |
| **`spec_table`** | object | 参数表（唯一数值来源） | 人工 → 03 校验 | **04/05** |
| **`forbidden_words[]`** | array | 禁用词清单 | 03（合规扫描） | **04/05** |
| **`usage_scope_confirmed[]`** | array | 确认可用的场景 | 人工 → 03 确认 | **04/05** |
| `package_content[]` | array | 包装清单（含"不含什么"） | 人工 | 04 |
| `warranty` | string | 保修信息 | 人工 | 04/05 |

> **加粗的六个字段为空时，04/05 必须拒绝执行。** 这不是"建议"，是硬拦截。

### 可选字段

| 字段 | 类型 | 定义 | 用途 |
|---|---|---|---|
| `title_final` | string | 最终标题 | 05 的结尾 CTA |
| `keyword_classified` | object | 七类分词结果 | 04 主图卖点、05 字幕埋词 |
| `visual_tone_hint` | string | 视觉调性 | 04/05 风格统一 |
| `review_insights[]` | array | 差评归因 | 03 的注意事项段、05 的场景选择 |
| `brand_authorization[]` | array | 已授权品牌 | 合规拦截基准 |

---

## 模板

```yaml
# ─────────────────────────────────────────────
# PRODUCT BRIEF · 模块间通信契约
# ─────────────────────────────────────────────
meta:
  brief_id: ""                 # 便于追踪，如 PB-20261013-001
  created_at: ""               # YYYY-MM-DD
  source_agent: "03-Listing-Creative"
  version: "v0.1"

# ── 基础信息 ──
identity:
  product_name*: ""
  product_name_local: ""       # 目标市场语言版本
  category*: ""
  platform*: ""                # shopee | mercadolivre | amazon | tiktokshop | shopify
  target_market*: ""

# ── 核心输出（下游阻塞项）──
core:
  core_selling_point*: ""      # 一句话，必须可验证
  secondary_points*: []        # 3–5 条
  usage_scope_confirmed*: []   # 场景白名单

# ── 参数（唯一数值来源）──
params:
  spec_table*: {}              # 所有输出中的数值都必须来自这里
  package_content*: []
  warranty*: ""

# ── 合规 ──
compliance:
  forbidden_words*: []
  brand_authorization: []
  certifications: []           # ⚠️ 仅填实际持有的

# ── 视觉与关键词 ──
creative:
  keyword_classified: {}
  title_final: ""
  visual_tone_hint: ""

# ── 评论洞察 ──
insights:
  review_insights: []
  # - type: 误解型 | 质量型 | 物流型 | 参数型
  #   content: ""
  #   action: ""
```

---

## 使用方式

### 03 怎么产出它

跑完 `02_description_builder.md` + `03_compliance_guard.md` 后，从输出的「交付给下游模块的字段」区块直接拷贝。

### 04 / 05 怎么消费它

**执行前的依赖检查**（必须做）：

```text
1. 读取 product_brief
2. 检查六个阻塞字段是否为非空
3. 任一为空 → 输出报错并停止：

   [UPSTREAM_MISSING]
   缺失字段：<字段名>
   影响：<无法完成哪部分>
   请先完成 03 Listing Creative Agent 并补齐上述字段。
```

**绝对不允许**在阻塞字段缺失时用推测值填充。

---

## 数据一致性检查

三个模块跑完后，做一次横向比对：

| 字段 | 03 输出 | 04 输出 | 05 输出 | 一致 |
|---|---|---|---|---|
| `core_selling_point` 的数值 | | | | ✅ / ❌ |
| `spec_table` 关键参数 | | | | ✅ / ❌ |
| `forbidden_words` 命中数 | | | | ✅ / ❌ |
| 视觉调性描述 | | | | ✅ / ❌ |

> **参数漂移是这套流程最常见的翻车点。** 03 写 `20000mAh`，04 的图里写成 `20.000mAh`，05 配音说"两万毫安时"——单看都没错，放一起就是拼凑感。跑完必须比对一次。

---

**相关文档**：[架构拆解](../docs/00_Architecture_SOP_to_Agent.md) · [自检清单](../docs/04_Result_Checklist.md)
