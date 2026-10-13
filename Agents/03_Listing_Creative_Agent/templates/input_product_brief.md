# 输入模板 · 产品资料与关键词三榜

> **使用方法**：复制本文件 → 填写 → 与 `prompts/00_system.md` + 对应任务 Prompt 一起提交给 LLM。
> **带 `*` 的字段为必需项**，缺失会导致对应输出无法生成（详见各 Prompt 的 INPUT CONTRACT）。

---

## 0. 任务配置

```yaml
platform*: shopee              # shopee | mercadolivre | amazon | tiktokshop | shopify
target_market*: 巴西            # 决定输出语言：巴西→PT-BR / 墨西哥→ES
mode*: single                  # single | variant | iterate
variant_count: 3               # mode=variant 时必填，2–4
```

---

## 1. 产品基础信息

```yaml
product_name*: "Carregador Portátil"        # 产品通用名（目标语言）
category*: "电池 / 充电类"
sku_internal: ""                            # 内部 SKU 编码（可选）
```

---

## 2. 参数表（spec_table）★ 最关键

> **所有输出中出现的数值，都必须能在本表找到对应项。** 本表是唯一数值来源。
> **不确定的参数：留空，不要编。** 留空只会少一个卖点，编错会导致退货和罚分。

| 参数键 | 值（含单位） | 备注 |
|---|---|---|
| `marca` | | 无品牌授权则留空 |
| `modelo` | | |
| `cor` | | |
| `material` | | |
| `peso` | | 公制：`380 g` |
| `dimensoes` | | 公制：`14,2 × 6,8 × 2,8 cm` |
| `capacidade` | | 如 `20000 mAh` |
| `potencia_saida` | | 如 `45 W` |
| `voltagem_entrada` | | 如 `100–240 V` |
| `portas` | | 如 `2× USB-A + 1× USB-C` |
| `tempo_recarga` | | 注明测试条件 |
| `garantia` | | **巴西站必需** |
| `certificacoes` | | ⚠️ 仅填**实际持有**的认证，虚构属高危违规 |
| `_custom_1` | | 类目特有参数，按需增删 |
| `_custom_2` | | |

**包装清单**（`package_content`）— ⚠️ **差评第一大来源，务必填全**：

```yaml
package_content*:
  - "1× Carregador Portátil 20000mAh"
  - "1× Cabo USB-C"
  # 不含什么也要写明，例如：
  # - "（注意：Adaptador de tomada NÃO incluso）"
```

---

## 3. 使用场景范围（usage_scope）★ 合规必需

> 只有列在这里的场景，才允许出现在详情页的"使用场景"段。超出范围的会被删除。

```yaml
usage_scope*:
  - "Viagem e deslocamentos diários"
  - "Trabalho remoto / home office"
  - "Camping e atividades ao ar livre"
  # 不要写产品做不到的场景
```

**不要写在这些场景里**（示例）：不防水产品不写"水上活动"；非医用产品不写"医疗急救援"。

---

## 4. 卖点输入（可含夸张表述）

> 这里可以随便写，甚至可以写得夸张。Agent 会按「卖点真实化映射表」改写成可验证表达。
> 但**每条卖点都必须有真实依据**，否则改不出来。

```yaml
selling_points_input:
  - "Turbo carga: carrega muito mais rápido que carregador comum"
  - "Bateria gigante, dura dias"
  - "Serve para qualquer celular"
  - "Design compacto e moderno"
  - "Seguro, não esquenta"
```

---

## 5. 品牌与合规声明 ★

```yaml
brand_authorization: []      # 已获授权的品牌名列表。无授权写 []
                             # 例：["Anker"]  ← 只有真的拿到授权才填

competitor_weakness: []      # 竞品短板（用于差异化表达，可选）
  # 例：["竞品普遍 18W 输出", "竞品无数字显示"]

review_insights: []          # 来自 07 Review Analysis 的差评归因（可选，强烈建议）
  # 例：
  # - type: 误解型
  #   content: "买家以为含数据线"
  #   action: "详情页注意事项段写明 cabo não incluso"

notes_required*: true        # 是否生成"注意事项"段
                             # 有误解型差评时建议设为 true
```

---

## 6. 关键词三榜 ★ 必需

> 来源：虾多拉 / 平台搜索词工具 / 卖家中心关键词分析。
> **格式**：每榜一行一个词，或用逗号分隔。
> ⚠️ Agent **不产生关键词**，只做分类和组合。三榜缺失则无法执行关键词分类。

### 6.1 搜索量前 30

```text
<词1>
<词2>
...
```

### 6.2 供需比前 30

```text
<词1>
<词2>
...
```

### 6.3 增长率前 30

```text
<词1>
<词2>
...
```

---

## 7. 竞品参考（可选但建议）

| 竞品 | 价格 | 月销量 | 标题 | 主图特点 | 核心卖点 | 差评高频点 |
|---|---|---|---|---|---|---|
| | | | | | | |

> 填了它，Agent 的"差异化表达"部分会更具体；不填也不影响基础输出。

---

## 8. mode 专属字段

### mode = variant

```yaml
variant_directions: []       # 留空则由 Agent 按三种方向自动分配
  # 例：["参数驱动", "场景驱动", "人群驱动"]
```

### mode = iterate（对应 SOP 3.6 广告跑不动时回改）

```yaml
existing_title: ""
symptom: ""                  # 例："有曝光没点击，CTR 1.2%（低于 3% 基准）"
constraints: ""              # 例："只改主图位置的关键词，不要动参数部分"
```

---

## 填写自检

- [ ] 所有 `*` 必填项已填
- [ ] `spec_table` 中所有数值都是我**能举证的真实值**
- [ ] `package_content` 已完整列出，包含"不含什么"
- [ ] `usage_scope` 里的场景产品**真的能做到**
- [ ] `brand_authorization` 没有填入未授权的品牌
- [ ] `certificacoes` 只填**实际持有**的认证
- [ ] 三榜关键词已填（共 90 个词）
- [ ] 我理解：**参数真实性由我负责**，Agent 只能保证"输出与输入一致"
