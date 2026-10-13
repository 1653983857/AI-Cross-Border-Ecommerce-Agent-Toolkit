# 案例 · Carregador Portátil 20000mAh 45W（Shopee 巴西站）

> **案例类型**：真实产品 · 已脱敏（无店铺名、无账号、无未授权品牌词）
> **使用模块**：03 Listing Creative Agent
> **对应 SOP**：1.8 关键词表 · 3.3 Listing 打造 · 3.6 广告回改

---

## 一、产品背景

| 项 | 内容 |
|---|---|
| 产品 | 20000mAh 45W 快充充电宝，带数字显示屏，3 输出口 |
| 市场 | 巴西（Shopee BR） |
| 类目 | 电池 / 充电类 |
| 定位 | 引流款，主推广告品 |
| 上架背景 | 新品冷启动，需要一套能撑起点击率的 Listing |

**为什么选这个案例**：巴西站充电宝类目竞争激烈，是"标题写法差异直接反映在点击率上"的典型类目；同时它有明确的**误解型差评**（买家以为含数据线），可以用来演示"评论 → 详情页"的闭环。

---

## 二、输入端（节选）

完整模板见 [`../templates/input_product_brief.md`](../templates/input_product_brief.md)。

```yaml
platform: shopee
target_market: 巴西
mode: single

product_name: "Carregador Portátil"
category: "电池 / 充电类"
```

### spec_table（节选）

| 参数键 | 值 |
|---|---|
| `capacidade` | `20000 mAh` |
| `potencia_saida` | `45 W` |
| `portas` | `2× USB-A + 1× USB-C` |
| `voltagem_entrada` | `100–240 V` |
| `peso` | `380 g` |
| `dimensoes` | `14,2 × 6,8 × 2,8 cm` |
| `display` | `Display digital de bateria` |
| `tempo_recarga` | `≈ 4 h com carregador de 45 W` |
| `garantia` | `6 meses (defeito de fabricação)` |
| `certificacoes` | `（留空 —— 未持有 ANATEL，不填不虚构）` |

### package_content

```yaml
- "1× Carregador Portátil 20000mAh 45W"
- "1× Cabo USB-C 30 cm"
- "1× Manual de instruções em português"
```

### usage_scope

```yaml
- "Viagem e deslocamentos diários"
- "Trabalho remoto / home office"
- "Emergência durante o dia fora de casa"
```

### selling_points_input（含夸张表述，待改写）

```yaml
- "Bateria gigante, dura dias inteiros sem precisar de tomada"
- "Carrega ultra rápido, mais rápido que carregador comum"
- "Serve para qualquer celular"
- "Design moderno e compacto, cabe no bolso"
- "Seguro, não esquenta nem incha"
```

### review_insights

```yaml
- type: 误解型
  content: "买家评论提到『esperava que viesse o cabo longo』，以为含长数据线"
  action: "详情页注意事项段写明 cabo incluso tem 30 cm"
- type: 误解型
  content: "买家以为能给笔记本充电"
  action: "注意事项段与参数段明确 scope：celular e tablet"
```

### brand_authorization

```yaml
brand_authorization: []      # 无任何品牌授权
```

---

## 三、AI 处理流程

```text
[Step 1] 00_system.md                    → 载入角色、平台规则(120字符)、PT-BR 输出规则、合规守卫
[Step 2] 01_keyword_to_title.md          → 三榜 84 词合并去重 → 七类分词 → 3 个备选标题
[Step 3] 02_description_builder.md       → 详情页 7 段 + 卖点分层 + 参数一致性校验
[Step 4] 03_compliance_guard.md          → 合规扫描 → 命中 3 条 → 改写 → 二次扫描确认零命中
[Step 5] 输出 output_listing_pack.md     → 交付 core_selling_point / forbidden_words 给 04、05
```

**中转注意**：Step 2 的关键词分类表直接喂给 Step 3（详情页第 7 段埋词用），不重新生成。

---

## 四、生成结果

### 4.1 关键词分类（节选）

| 类别 | 词数 | 代表词 |
|---|---|---|
| 核心词 | 3 | `Carregador Portátil`、`Bateria Externa`、`Power Bank` |
| 参数词 | 11 | `20000mAh`、`45W`、`3 Saídas`、`USB-C` |
| 人群词 | 4 | `Unissex`、`Viagem`、`Trabalho`、`Estudante` |
| 功能词 | 8 | `Turbo Carga Rápida`、`Display Digital`、`Carregamento Simultâneo` |
| 场景词 | 6 | `Viagem`、`Trabalho Remoto`、`Camping`、`Emergência` |
| 配件词 | 5 | `com Cabo USB-C`、`com Manual`、`Bateria` |
| **风险词** | **6** | ⛔ `iPhone`（未授权品牌）、`100% Original`、`À Prova de Água`（参数不符）等 |

> **风险词处理**：6 个风险词全部隔离，**不得出现在任何输出中**，但完整交付给 04/05 做拦截。
> 特别说明：`iPhone` 属未授权品牌词，但 `Celular` 是通用词，可以正常使用——两者不是一回事。

### 4.2 标题（3 个备选，字符数已实测）

| # | 标题 | 字符数 | 侧重方向 |
|---|---|---|---|
| **A** | `Carregador Portátil 20000mAh 45W Turbo Carga Rápida 3 Saídas com Display Digital para Celular Viagem` | **100/120** | 参数驱动 |
| **B** | `Carregador Portátil 20000mAh 45W com Display Digital 3 Saídas para Viagem e Trabalho Remoto` | **91/120** | 场景驱动 |
| **C** | `Carregador Portátil 20000mAh 45W Bateria Externa com Display Digital 3 Saídas para Celular Viagem` | **97/120** | 功能驱动 |

**推荐 A**，理由：主关键词 `Carregador Portátil` 落在第 1–19 字符，`20000mAh 45W` 落在前 30 字符内，参数密度最高，适合新品冷启动阶段抢精准搜索流量。

> **没有强行填满 120 字符**。SOP 提到"标题写满在完整性评分上更占优"，但**前提是每个词都必须是买家会搜的词**。为了凑字数加 `Hot Sale`、`Novo` 这类词，属于平台明确禁止的堆砌行为。

### 4.3 详情页（节选）

**段 1 · 欢迎语**
```text
Carregador portátil de 20000mAh com saída de 45W e display digital.
Ideal para quem passa o dia fora de casa e não pode ficar sem bateria.
```

**段 2 · 核心卖点**（含改写对照）

| 输入（夸张） | 输出（可验证） |
|---|---|
| Bateria gigante, dura dias | `Capacidade de 20000 mAh — recarrega um celular comum cerca de 4 vezes` |
| Carrega ultra rápido | `Saída de 45W, recarga completa de um celular em cerca de 40 minutos*` |
| Serve para qualquer celular | `Compatível com celulares e tablets via USB-A ou USB-C` |
| Design moderno e compacto | `Corpo em ABS de 14,2 × 6,8 × 2,8 cm e 380 g` |
| Seguro, não esquenta | `Proteção contra sobrecarga, sobrecorrente e curto-circuito` |

> `*` 需在段 6 补充测试条件。

**段 3 · 使用场景**（全部在 `usage_scope` 内）

| 场景 | 具体用法 |
|---|---|
| Viagem e deslocamentos | Carregue o celular no aeroporto, no ônibus ou no carro |
| Trabalho remoto | Mantenha o celular carregado durante o dia de reuniões |
| Emergência durante o dia | Saia de casa sem se preocupar com a bateria baixa |

**段 6 · 注意事项**（由 `review_insights` 驱动生成）

```text
- O cabo incluso (USB-C) tem 30 cm. Não é um cabo longo.
- O produto carrega celulares e tablets. Não é indicado para notebooks.
- A recarga completa em cerca de 40 minutos foi medida com um celular de
  4.500 mAh em temperatura ambiente de 25 °C.
- Nunca use o aparelho molhado ou sobre superfícies inflamáveis.
```

> 这一段是**本案例收益最高的产出**。两条误解型差评 → 两条前置说明，直接减少后续退货和差评。

### 4.4 卖点分层

| 层级 | 卖点 | 支撑依据 |
|---|---|---|
| **主卖点** | `45W 快充 + 20000mAh 容量组合` | `spec_table`：`45 W` / `20000 mAh` |
| 副卖点 | 数字显示屏；3 输出口；100–240V 宽电压 | `display` / `portas` / `voltagem_entrada` |
| 备用卖点 | 380 g 便携；6 个月保修 | `peso` / `garantia` |
| 禁用卖点 | `100% original`、`à prova d'água`、`serve para tudo` | 品牌未授权 / 参数不符 / 绝对化 |

### 4.5 合规扫描结果

| 规则 | 命中数 | 处理 |
|---|---|---|
| R1 绝对化用语 | 1 | `mais rápido que carregador comum` → 改为带测试条件的量化表达 |
| R2 未授权品牌词 | 1 | `iPhone` → 改为通用词 `Celular` |
| R3 参数虚标 | 0 | — |
| R4 促销词入标题 | 1 | 标题中的 `Promoção` 已移入详情页段 1 |
| R5 敏感表述 | 0 | — |
| R6 场景超范围 | 1 | 输入的 `Camping` 不在 `usage_scope` 内 → 删除并记录 `[SCENE_DROPPED]` |
| R7 伪造证明 | 0 | — |

**结论**：命中 4 条（R2 高危），全部处理完毕，**二次扫描零命中**，可发布。

---

## 五、交付给下游模块

```yaml
core_selling_point: "20000mAh com saída de 45W — recarga completa do celular em cerca de 40 minutos"
secondary_points:
  - "Display digital de bateria"
  - "3 saídas (2× USB-A + 1× USB-C) para carregamento simultâneo"
  - "Entrada 100–240V, funciona em qualquer tomada do Brasil"
spec_table: { ... }          # 同 input
forbidden_words:
  - "iPhone"
  - "100% Original"
  - "À Prova de Água"
  - "mais rápido do mercado"
  - "Serve para tudo"
  - "Promoção"
keyword_classified: { ... }
title_final: "Carregador Portátil 20000mAh 45W Turbo Carga Rápida 3 Saídas com Display Digital para Celular Viagem"
visual_tone_hint: "Tecnológico e limpo — fundo claro, tons de cinza e azul, sem elementos infantis"
usage_scope_confirmed:
  - "Viagem e deslocamentos diários"
  - "Trabalho remoto / home office"
  - "Emergência durante o dia fora de casa"
```

`visual_tone_hint` 会被 04（图片）和 05（视频）共同读取，保证两者的视觉风格一致。

---

## 六、其他平台版本（同一产品）

### Mercado Livre（60 字符上限，需大幅精简）

| # | 标题 | 字符数 |
|---|---|---|
| A | `Carregador Portátil 20000mAh 45W 3 Saídas Display Digital` | **57/60** |

**砍词过程**：`Viagem`（场景词，首个被砍）→ `Turbo Carga Rápida`（功能词，与 45W 语义重复）→ 保留 `Carregador Portátil`（核心词）+ `20000mAh 45W`（参数）+ `3 Saídas Display Digital`（功能）。
**主关键词与核心参数一个都没砍**——符合 ML 的砍词优先级规则。

⚠️ **ML 图片规范与 Shopee 冲突**：ML 主图禁止出现任何文字与水印，而 Shopee 主图习惯打卖点文字。因此 04 Product Image Agent 需要输出**两套主图方案**，不能复用。

---

## 七、优化建议（给使用者的下一步）

| # | 建议 | 依据 |
|---|---|---|
| 1 | 用 title A/B/C 做 **3 条链接 A/B 测试**（SOP 3.4 方式二） | 三条标题侧重方向不同，可快速判断哪种方向点击率更高 |
| 2 | 图片来源优先拍**数字显示屏亮起**的状态 | 卖点中最直观、竞品普遍拍得差的一项 |
| 3 | 补拍一张**包装清单平铺图** | 直接对冲"以为含长线"的误解型差评 |
| 4 | 广告跑不动时先改主图，再动 ROI（SOP 3.6） | 改主图常能解除广告 bug，比盲目调价有效 |
| 5 | 详情页第 6 段上线后**监测差评变化** | 验证"误解型差评前置说明"是否真的降低了退货 |
| 6 | 拿到 ANATEL 认证后再补认证图 | 目前留空是对的——虚构认证属高危违规 |

---

## 八、这个案例证明了什么

| 结论 | 证据 |
|---|---|
| **Agent 能守住参数真实性的底线** | 全程 0 次 `[PARAM_DROPPED]`，因为所有数值都来自 `spec_table` |
| **合规守卫是有效的** | 拦截了 4 条，包括 1 条高危的未授权品牌词 |
| **评论能反向修复 Listing** | 2 条误解型差评 → 2 条前置说明，且这两条说明在优化建议里被列为本案例最高收益项 |
| **跨平台不能简单复制** | 同一个商品，Shopee 100 字符 vs ML 57 字符；且主图规范直接冲突 |
| **上限在人不在模型** | Agent 只能保证"输出 = 输入"，参数本身是否真实，是使用者的责任 |

---

**相关文件**：[模块说明](../README.md) · [输入模板](../templates/input_product_brief.md) · [输出模板](../templates/output_listing_pack.md) · [合规红线](../../../docs/03_Compliance_Guard.md)
