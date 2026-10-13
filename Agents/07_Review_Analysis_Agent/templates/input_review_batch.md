# 输入模板 · 评论批量导入

> ⚠️ **导入前必须脱敏**：删除买家昵称、订单号、头像 URL、可识别的个人信息。
> 评论原文**保留原始语言**（葡语/西语），不要预先翻译——翻译会丢失表达线索（如"esperava que"这类误解型特征词）。

---

## 0. 任务配置

```yaml
platform*: shopee
target_market*: 巴西
product_name*: ""
analysis_scope*: own          # own（仅我方）| competitor（仅竞品）| both（对比）
```

---

## 1. 基准数据 ★ 阻塞项

> **缺这两块，Agent 无法判断"参数不符"和"配件缺失"是真问题还是误解。** 会直接拒绝执行。

```yaml
# ── 从 03 Listing Creative 的输出粘贴 ──

spec_table*: {}
# 例：
#   autonomia: "até 35 km"
#   capacidade_carga: "150 kg"
#   peso_produto: "18 kg"
#   tempo_recarga: "5 a 6 horas"

package_content*: []
# 例：
#   - "1× Patinete Elétrico"
#   - "1× Carregador 42V"
#   - "1× Manual em português"
#   - "（Não incluso: capacete）"     ← 明确"不含什么"极其重要

usage_scope*: []
# 例：
#   - "Deslocamento urbano em vias planas e pavimentadas"
#   - "Lazer em parques e ciclovias"
#   - "Trajeto casa-trabalho em distâncias curtas"

warranty*: ""                 # 例："6 meses (motor e bateria)"
```

---

## 2. 现有 Listing（用于判断"说明缺失"还是"说明不醒目"）

```yaml
current_title: ""
current_description: ""        # 详情页全文（或分段粘贴，标注段落序号）
current_image_plan: []         # 04 的 9 图规划（可选）
# 例：
#   - {slot: 1, role: "主图"}
#   - {slot: 8, role: "包装清单图"}
```

> 有了这两项，Agent 才能区分：
> - 完全没提 → **缺失说明** → 新增条目
> - 提了但埋得深 → **说明不醒目** → 前置
> - 很醒目仍被误解 → **买家未阅读** → 换表达方式（改成图）

---

## 3. 评论数据

> **格式**：用 JSON 数组或 CSV。每条至少含 `text` / `rating` / `source`。

```json
[
  {
    "id": "R001",
    "text": "<原文，保留原始语言>",
    "rating": 5,
    "has_image": true,
    "source": "own",
    "date": "2026-09-15"
  },
  {
    "id": "R002",
    "text": "",
    "rating": 1,
    "has_image": false,
    "source": "own",
    "date": "2026-09-20"
  }
]
```

### 字段说明

| 字段 | 必需 | 说明 |
|---|---|---|
| `id` | ✅ | 自编号（**不要用平台评论 ID**，避免可追溯） |
| `text` | ✅ | 评论原文，**保留原始语言与错别字** |
| `rating` | ✅ | 星级（用于好评/差评分组） |
| `has_image` | ✅ | 是否带图（用于评价质量评估、SOP 提到的"带图评价数"） |
| `source` | ✅ | `own` / `competitor_A` / `competitor_B`（**用代号，不要真实店铺名**） |
| `date` | ⭕ | 便于看时间趋势（如某个问题是否集中出现在某个批次） |

### 评论选择建议

| 建议 | 原因 |
|---|---|
| **优先导入全部差评** | 差评的信息密度远高于好评 |
| 好评可抽样（如近 50 条） | 好评同质化高，抽够样本即可判断高频点 |
| 中评（3 星）不要丢 | 中评最能反映"差一点就满意"的具体缺口 |
| 竞品评论导入同类目头部 | 用于对比"竞品靠什么卖" |
| 保留原始错别字 | `nao` / `não` 的写法差异反映买家语言习惯 |

---

## 4. 分析重点（可选）

```yaml
focus:
  - "为什么差评集中在爬坡能力"     # 有具体疑问时填，Agent 会专项回答
  - ""
```

---

## 填写自检

- [ ] 已脱敏（无昵称、订单号、头像 URL）
- [ ] `spec_table` 与 `package_content` 已填（缺则 Agent 拒绝执行）
- [ ] `usage_scope` 已填（用于判断场景类误解）
- [ ] 评论原文**保留原始语言**，未预先翻译
- [ ] 竞品来源用代号（`competitor_A`），未填真实店铺名
- [ ] 差评已全部导入，好评可抽样
- [ ] 中评（3 星）未丢弃
- [ ] 每条评论都有 `rating` 和 `has_image`
- [ ] 评论总数 ≥ 20（低于此值 Agent 会标注"样本不足"）
