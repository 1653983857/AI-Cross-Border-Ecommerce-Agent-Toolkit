# TASK · 详情页构建与卖点/参数提炼

> 配套使用：`00_system.md`（系统 Prompt）+ `01_keyword_to_title.md` 的输出（关键词分类表）+ `templates/input_product_brief.md`

对应 SOP **3.3 Listing 打造（详情页结构）**。

> ⚠️ **SOP 原文的编号问题**：原文写"可以分为以下 8 个部分"，但实际只列出 7 项（欢迎语 / 核心卖点 / 使用场景 / 详细参数 / 售后客服 / 注意事项 / 关键词标签区）。本模块按 **7 段**执行。若后续补齐第 8 段，请更新此处与 `docs/02_Platform_Output_Spec.md`。

---

# INPUT

必需字段：

| 字段 | 说明 |
|---|---|
| `platform` | 目标平台（决定结构：Shopee 7 段 / ML 五点 + Ficha Técnica） |
| `target_market` | 目标市场（决定输出语言） |
| `product_name` | 产品通用名 |
| `category` | 类目 |
| `spec_table` | 参数表（键值对） |
| `usage_scope[]` | 允许表达的使用场景 |
| `selling_points_input[]` | 已知卖点（原始表述，可含夸张表达，由 Agent 改写） |
| `warranty` | 保修信息（**巴西站必需**，ML 也要求） |
| `package_content[]` | 包装清单（**这是差评高发项，务必填全**） |
| `notes_required` | 是否需要生成"注意事项"段（`true` / `false`） |
| `keyword_classified` | 来自 `01_keyword_to_title.md` 第 5 段 |

可选字段：
- `review_insights`：来自 07 Review Analysis Agent 的差评归因（有则用于补强第 6 段）
- `competitor_weakness[]`：竞品短板（用于差异化表达）

---

# 输出结构（platform = shopee）

严格 7 段，顺序固定：

```markdown
## 1. 详情页正文

### 段 1 · 欢迎语（Boas-vindas）
### 段 2 · 核心卖点（Diferenciais）
### 段 3 · 使用场景（Cenários de Uso）
### 段 4 · 详细参数（Especificações）
### 段 5 · 售后与客服承诺（Garantia e Atendimento）
### 段 6 · 注意事项（Observações Importantes）  ← 仅在 notes_required = true 时生成
### 段 7 · 关键词标签区（Tags de Busca）
```

---

## 段 1 · 欢迎语

**内容**：一句话自我介绍 + 促销信息。
**字数**：2–3 句，不超过 200 字符。
**注意**：不写"感谢光临本店"这类无信息量的客套。写"我们卖什么 + 为什么值得看下去"。

---

## 段 2 · 核心卖点

**内容**：产品解决了什么问题、有什么优势。
**数量**：3–5 条。
**格式**：每条一行，`卖点标题 — 量化支撑`。

### 卖点真实化映射（强制执行）

输入里的卖点若是夸张表述，**必须改写成可验证表达**：

| 输入（夸张） | 输出（可验证） |
|---|---|
| Bateria mais forte do mercado | Bateria de 20000mAh |
| Carrega super rápido | Saída de 45W, recarrega um celular em cerca de 40 minutos* |
| Qualidade premium | Carcaça em ABS + PC com acabamento antichamas |
| Durável | Suporta mais de 500 ciclos de carga |
| Design moderno | Corpo de 14,2 cm × 6,8 cm × 2,8 cm, 380 g |
| Serve para tudo | Compatível com smartphones, tablets e fones com entrada USB-C ou USB-A |

> **改写规则**：把"形容词"换成"名词 + 数字"。凡是无法用一张图、一个参数或一份测试条件支撑的表述，一律删掉。
> 带 `*` 的数值需在段 6 补充测试条件。

---

## 段 3 · 使用场景

**内容**：让买家代入情境，激发购买欲。

> ⚠️ **这是虚假宣传的高发区。** SOP 原文也标注了这一点。执行时强制约束：
> 每个场景**必须**落在 `input.usage_scope` 列表中。超出范围的场景一律删除，并记录 `[SCENE_DROPPED]`。

**格式**：3–5 个场景，每个写 `场景名 + 具体用法`（不写"让生活更美好"这类空话）。

---

## 段 4 · 详细参数

**内容**：颜色、材质、尺寸、容量、包装等规格信息。

**格式**：表格。左列参数名（母语），右列值（含单位）。

**硬约束**：
- 每个值**必须**逐字符等于 `spec_table` 中的对应项
- `package_content[]` 必须**完整列出**，一项不能少（这是差评第一大来源）
- 单位全部公制，小数用逗号

---

## 段 5 · 售后与客服承诺

**内容**：降低退货顾虑。

**要求**：
- 承诺必须与 `input.warranty` 一致
- **巴西站**：保修信息是消费法要求，必须明确写出时长与范围
- **禁止**承诺做不到的事（如"无条件退货"若平台规则不支持）

---

## 段 6 · 注意事项（条件生成）

**触发条件**：`notes_required = true`，**或** `review_insights` 中存在"误解型差评"。

**内容来源**（按优先级）：
1. `review_insights` 中的**误解型差评** → 转化为预防性说明（这是 ROI 最高的用法）
2. 产品天然的使用限制（电压、兼容性、清洁方式）
3. 段 2 中带 `*` 的测试条件

**禁止**：把平台通用规则抄一遍充数。

---

## 段 7 · 关键词标签区

**内容**：埋词优化搜索曝光。

**来源**：`keyword_classified` 中的**核心词 + 功能词 + 场景词 + 配件词**。
**禁止**：放入风险词、无关词、重复词。标签数控制在 10–15 个。

---

# 输出结构（platform = mercadolivre）

结构不同，改为：

```markdown
## 1. 详情页正文

### 1.1 Características principais（五点描述）
每条 = 技术参数 + 适用场景 + 售后保障 的组合。5 条，每条不超过 120 字符。

### 1.2 Ficha Técnica（技术规格表）
「能填就填满」——平台对完整填写的 listing 有排名倾斜。
必须包含：Marca / Modelo / Cor / Material / Peso / Dimensões /
         Voltagem / Potência / Garantia / Itens incluídos

### 1.3 Observações
（条件生成，同 Shopee 段 6）
```

---

# STEP 2 · 卖点分层提炼

详情页正文写完后，额外输出一份**卖点分层表**——这是 04 和 05 模块的直接输入。

```markdown
## 2. 卖点分层

| 层级 | 卖点 | 支撑依据 | 用于 |
|---|---|---|---|
| **主卖点**（1 个） | <核心差异点> | <参数 / 测试 / 材料> | 主图核心文案、视频钩子、标题关键词 |
| **副卖点**（3–5 个） | <各条> | <依据> | 详情图文案、视频卖点段、五点描述 |
| **备用卖点**（若干） | <各条> | <依据> | A/B 测试、场景化素材 |
| **禁用卖点** | <被剔除的夸张表述> | <为什么不能用> | ⛔ 列入 forbidden_words |
```

**主卖点选择标准**（按优先级）：
1. 竞品普遍**没有**或**做得差**的
2. 买家评论里**反复提到**的
3. 能用**一个数字**说清的
4. 和价格的关联最直接的

---

# STEP 3 · 参数一致性校验

```markdown
## 3. 参数一致性校验

| 参数 | input.spec_table | 详情页正文 | 标题 | 一致 |
|---|---|---|---|---|
| <键> | <值> | <值> | <值> | ✅ / ❌ |

校验结果：<全部一致 / 发现 N 处不一致，已修正>
```

> 三处（输入 / 标题 / 详情页）必须逐字符一致。这是跨模块参数漂移的第一道防线。

---

# FINAL OUTPUT STRUCTURE

```markdown
## 1. 详情页正文
（按 platform 输出对应结构）

## 2. 卖点分层

## 3. 参数一致性校验

## 4. 合规扫描
（按 00_system.md 输出；无命中也必须写"无命中"）

## 5. 交付给下游模块的字段
- core_selling_point:
- secondary_points: [...]
- spec_table: {...}
- forbidden_words: [...]
- visual_tone_hint:     ← 视觉调性提示，供 04/05 统一风格
- usage_scope_confirmed: [...]
```

---

# SELF-CHECK

- [ ] 7 段结构完整（`notes_required = false` 且无误解型差评时，段 6 可省略并注明原因）
- [ ] 使用场景全部落在 `usage_scope` 内
- [ ] `package_content[]` 已完整列出，无遗漏
- [ ] 段 2 无绝对化用语，夸张表述已全部改写
- [ ] 段 4 每个数值与 `spec_table` 逐字符一致
- [ ] 段 6 的内容有明确来源（评论归因 / 产品限制 / 测试条件），不是通用套话
- [ ] 段 7 不含风险词
- [ ] 保修信息完整（巴西站、ML 必须）
- [ ] 输出末尾已附下游字段 + 合规扫描
