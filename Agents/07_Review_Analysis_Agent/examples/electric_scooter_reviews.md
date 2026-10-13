# 案例 · Patinete Elétrico 500W 评论分析（Shopee 巴西站）

> **案例类型**：真实数据 · 已脱敏
> **使用模块**：07 Review Analysis Agent
> **对应 SOP**：1.6 竞品分析与评论分析 · 3.7 评价与售后维护
> **重点演示**：**84,6% 的差评可以靠改文案解决** · 最大卖点同时是最大误解源

**为什么选它**：这是[旗舰案例](../../../Examples/01_Patinete_Eletrico_500W/)埋下的伏笔——那份案例的详情页注意事项段预测了三类差评（承重、续航、组装）。本案例就是**用真实评论数据验证这个预测准不准**，并给出修补方案。它演示了整套流程的**回流闭环**。

---

## 一、数据概览

| 项 | 数值 | 占比 |
|---|---|---|
| 总评论数 | **128** | 100% |
| 好评（4–5 星） | 104 | **81,2%** |
| 中评（3 星） | 11 | 8,6% |
| 差评（1–2 星） | **13** | **10,2%** |
| 带图评论数 | 31 | **24,2%** |

**样本量判定**：✅ 充足（≥ 50 条）

**数据局限**：平台已删除部分评论（SOP 提到平台会删除评论过于简单、重复率过高、违规的评论），实际样本可能不完整。

---

## 二、先验证旗舰案例的预测

旗舰案例在详情页注意事项段写了四条前置说明。现在看真实差评有没有落在预测范围内：

| 旗舰案例的预测 | 实际差评是否出现 | 命中 |
|---|---|---|
| 续航虚标（"35 km 实测不符"） | ✅ 出现（见参数不符合预期 #1） | ✅ |
| 承重不符预期（"以为能载两人"） | ✅ 出现（见误解型 #1） | ✅ |
| 组装困难 | ✅ 出现（见使用困难 #1） | ✅ |
| 需核查当地上路法规 | ❌ 未出现 | — |

> **4 项预测中 3 项命中。**
>
> 这说明旗舰案例基于 `review_insights` 和 `usage_scope` 写出的注意事项段，方向是对的。**但命中的 3 项仍然发生了差评——说明"写了"不等于"有效"。** 这就是本案例要解决的核心问题。

---

## 三、好评分析

### 3.1 买家为什么满意

| # | 满意原因 | 提及次数 | 占比 | 典型原文 |
|---|---|---|---|---|
| 1 | 爬坡能力 | 38 | 36,5% | `Sobe ladeira sem esforço, achei que ia travar mas subiu tranquilo` |
| 2 | 折叠方便 | 31 | 29,8% | `Dobro em segundos e coloco no porta-malas do carro` |
| 3 | 减震效果好 | 27 | 26,0% | `Passei em cima de buraco e nem senti` |
| 4 | 电池续航 | 22 | 21,2% | `Ando 25 km por dia e ainda sobra bateria` |
| 5 | 外观设计 | 18 | 17,3% | `Muito bonito, parece de marca cara` |
| 6 | 性价比 | 14 | 13,5% | `Pelo preço, valeu muito` |
| 7 | 卖家客服 | 9 | 8,7% | `Vendedor respondeu rápido e ajudou na montagem` |

> ⚠️ **第 4 条值得注意**：好评里说的是"25 km 还有电"，差评里说的是"只跑了 20 km"。**同一块电池，两种结论——差异来自载重。** 这条对照是后面识别续航类差评的关键线索。

### 3.2 卖点有效性核对

| 卖点 | 提及次数 | 现有 Listing 是否突出 | 建议 |
|---|---|---|---|
| 爬坡能力 | 38 | ⚠️ **标题有 `500W`，但主图未突出爬坡** | 主图 + 视频强化爬坡画面 |
| 折叠方便 | 31 | ✅ 标题有 `Dobrável`，图 5 专图 | 保持 |
| 减震效果好 | 27 | ✅ 标题有 `e Suspensão`，图 6 特写 | 保持 |
| 电池续航 | 22 | ⚠️ 只在参数表里，参数图上排第 3 位 | 参数图前置 + 标注测试条件 |
| **客服响应** | **9** | ❌ **Listing 里完全没提** | ⚠️ **这是空白机会** |

> **客服被 9 条好评主动称赞，但 Listing 里一个字都没提。**
> 评价数量少、信任度不足是转化率的主要阻力（见 [06 广告案例](../../06_Advertising_Optimization_Agent/examples/powerbank_20000mah_ads.md) 的结论），而**"卖家响应快"恰好是买家在下单前最想确认的事之一**。把这一点写进详情页是零成本动作。

### 3.3 物流与售后

| 维度 | 正面提及 | 负面提及 | 净情感 |
|---|---|---|---|
| 发货速度 | 12 | 1 | ✅ 正面 |
| 包装完整度 | 8 | 1 | ✅ 正面 |
| 客服响应 | 9 | 0 | ✅ 正面 |

### 3.4 价格感知

| 类型 | 提及次数 | 典型原文 |
|---|---|---|
| 觉得划算 | 14 | `Custo-benefício excelente para o que entrega` |
| 觉得偏贵 | 2 | `Achei um pouco caro, mas a qualidade compensa` |

---

## 四、差评归因

### 4.1 归因分布

| # | 归因类型 | 数量 | 占比 | 责任方 | 可否靠文案修复 |
|---|---|---|---|---|---|
| 1 | **误解型** ⭐ | **5** | **38,5%** | 我方（详情页） | ✅ 可 |
| 2 | 产品质量问题 | 0 | 0,0% | 供应商 | ❌ |
| 3 | 参数不符合预期 | **3** | 23,1% | 我方 | ✅ 可 |
| 4 | 配件缺失 | **2** | 15,4% | 我方（包装清单） | ✅ 可 |
| 5 | 发货慢 | 1 | 7,7% | 物流 | ❌ |
| 6 | 使用困难 | **1** | 7,7% | 我方（说明书） | ✅ 可 |
| 7 | 售后差 | 0 | 0,0% | 我方 | ✅ 可 |
| 8 | 破损 / 故障 / 退货 | 1 | 7,7% | 物流 / 供应商 | ❌ |
| | **合计** | **13** | 100% | | |

### 4.2 ⭐ 本案例最重要的一个数字

```
可修复项 = 误解型 5 + 参数不符 3 + 配件缺失 2 + 使用困难 1 + 售后差 0
        = 11 条

占差评总数 = 11 ÷ 13 = 84,6%
```

> ### **84,6% 的差评可以通过修改文案和图片解决，不需要动产品、不需要换供应商、不需要换物流。**
>
> 而且这类修复的**成本接近于零、周期是"改完立即生效"**。
>
> 对比一下另外 15,4%：一条是物流慢（要换物流），一条是破损故障（要改包装或换供应商）——这两类修复周期是数周到数月。
>
> **所以正确的动作顺序是：先花一天改文案消除 11 条，再去处理剩下 2 条。**

### 4.3 逐类明细

#### 误解型（5 条）

| # | 原文 | 买家以为 | 实际 | 判定 |
|---|---|---|---|---|
| 1 | `Pensei que dava para duas pessoas, mas é só para uma mesmo` | 能载两人 | `capacidade_carga = 150 kg`（未说明"单人乘坐"） | 说明不醒目 |
| 2 | `Não sobe ladeira forte como no vídeo, aqui tem um morro íngreme` | 任意坡道 | `usage_scope` 仅含 `vias planas e pavimentadas` | 说明不醒目 |
| 3 | `Imaginai que fosse mais leve, é difícil de subir no ônibus` | 更轻便 | `peso_produto = 18 kg`（写在参数表第 12 行） | 说明不醒目 |
| 4 | `O farol é fraco à noite, quase não ilumina a rua` | 可用作夜间照明 | 未说明灯光用途限于提示可见性 | **缺失说明** |
| 5 | `Pensei que a garantia era de 1 ano, mas é 6 meses` | 保修 1 年 | `warranty = 6 meses (motor e bateria)` | 说明不醒目 |

#### 参数不符合预期（3 条）

| # | 原文 | 买家预期 | 实际值 | 判定 |
|---|---|---|---|---|
| 1 | `Diz 35 km mas só fez 20 km comigo` | 35 km | `autonomia = até 35 km`（测试条件：70 kg 骑手） | **描述不清**——买家体重明显高于测试条件 |
| 2 | `A velocidade não chega a 30 km/h nem no plano` | 30 km/h | `velocidade_max = 30 km/h` | **描述不清**——未说明是"最高速度"而非"持续速度" |
| 3 | `Demorou mais de 7 horas para carregar` | 5–6 h | `tempo_recarga = 5 a 6 horas`（配原装充电器） | **描述不清**——买家用了非原装充电器 |

> **这三条都不是虚标，是"测试条件没写清楚"。** 三条都应当归入"描述不清"而非"描述错误"——**处理方式是补充条件说明，不是改数值。**
>
> 这是很重要的一次区分：如果误判为"描述错误"而把标称值改成 20 km，就等于主动放弃了一个真实的优势（轻载时确实能跑 35 km）。

#### 配件缺失（2 条）

| # | 原文 | 买家以为含 | `package_content` 实际 | 判定 |
|---|---|---|---|---|
| 1 | `Achei que vinha com capacete` | 头盔 | **不含** | 误解 → 需明确标注 |
| 2 | `Não veio a bomba de ar para os pneus` | 打气筒 | **不含** | 误解 → 需明确标注 |

> ⚠️ **这两条都是误解，不是缺件。** 对照 `package_content` 确认产品本就不含这两样。
> **正确动作是在包装清单图上明确标注"不含什么"，不是补发配件。**
> 补发配件是错误的——它会让成本上升，而且下一批买家依然会误解。

#### 发货慢（1 条）

| # | 原文 | 问题 |
|---|---|---|
| 1 | `Demorou 12 dias para chegar` | 物流时效 |

**不可靠文案修复**。动作：核实是否需要调整发货承诺的表述，或与物流商沟通。

#### 使用困难（1 条）

| # | 原文 | 问题 |
|---|---|---|
| 1 | `Difícil de montar, o manual não explica bem a parte do guidão` | 说明书对车把部分说明不清 |

**可靠文案修复**。动作：补一张组装指引图（回流 04）。

#### 破损 / 故障 / 退货（1 条）

| # | 原文 | 问题 |
|---|---|---|
| 1 | `Veio com um risco na carenagem e a lanterna traseira não acende` | 运输划痕 + 尾灯故障 |

**不可靠文案修复**。动作：改包装（防划痕）+ 出货前检查尾灯。

---

## 五、⭐ 最关键的发现：最大卖点 = 最大误解源

把好评卖点排序和差评归因放在一起看：

| 卖点 | 好评提及 | 排名 | 相关差评 | 差评归因 |
|---|---|---|---|---|
| **爬坡能力** | **38 次** | **🥇 第 1** | **1 条** | 误解型 #2（以为能上陡坡） |
| 折叠方便 | 31 次 | 🥈 第 2 | 0 条 | — |
| 减震效果好 | 27 次 | 🥉 第 3 | 0 条 | — |
| **电池续航** | 22 次 | 第 4 | **1 条** | 参数不符 #1（实测低于标称） |
| 外观设计 | 18 次 | 第 5 | 0 条 | — |

> ### **排名第 1 的卖点，同时也是差评来源之一。**
>
> 这不是巧合，而是一个**规律**：
>
> **你在详情页和视频里强调得越强的卖点，买家的预期就越高；预期越高，落差的可能性就越大。**
>
> 旗舰案例在视频里拍了"上坡镜头"、在标题里写了 `500W`、在图 2 里打了 `Motor 500W`——把爬坡讲成了第一卖点。买家因此产生了"这车什么坡都能上"的预期，然后在自家门口的陡坡上失望了。

### 这不是"不该强调"，而是"强调时要加边界"

| 做法 | 结果 |
|---|---|
| ❌ 削弱爬坡宣传 | 丢掉第 1 卖点，得不偿失 |
| ❌ 不写任何限定 | 差评持续发生 |
| ✅ **强化爬坡 + 同时明确边界** | **既拿到卖点的说服力，又管住预期** |

**具体动作**：

```text
原来（旗舰案例现状）：图 2 只打 "Motor 500W"
改成：图 2 打 "Motor 500W" + 小字 "Indicado para ladeiras leves"
```

> **一行小字，同时保住了卖点、消除了误解。** 这就是本模块的核心手法——**不是让描述更保守，而是让描述更精确。**

同样的逻辑适用于续航：

```text
参数图原来： "Autonomia: até 35 km"
改成：       "Autonomia: até 35 km (piloto de 70 kg, piso plano)"
```

---

## 六、详情页修补建议

### 6.1 新增/修改条目（→ 03 Listing）

| # | 对应差评 | 写入位置 | 文案（PT-BR） | 中文说明 |
|---|---|---|---|---|
| 1 | 误解型 #1 | 段 6 · **首条** | `Indicado para 1 pessoa. Capacidade máxima de 150 kg (piloto + bagagem).` | 明确单人乘坐 |
| 2 | 误解型 #2 | 段 6 · 首条 | `Indicado para vias planas e pavimentadas e ladeiras leves.` | 从 `usage_scope` 前置 |
| 3 | 误解型 #3 | 段 6 | `Peso do produto: 18 kg. Recomendamos duas pessoas para transportá-lo em escadas ou ônibus.` | 重量 + 使用建议 |
| 4 | 误解型 #4 | 段 6 | `O farol LED é para sinalização e visibilidade. Não substitui iluminação de via pública.` | 说明灯光用途边界 |
| 5 | 误解型 #5 | 段 5 · 售后 | `Garantia de 6 meses para motor e bateria.` | 保修写到段 5（原本只在参数表） |
| 6 | 参数不符 #1 | 段 4 · 参数注 | `Autonomia de até 35 km medida com piloto de 70 kg, em piso plano, a 20 km/h.` | 补齐测试条件 |
| 7 | 参数不符 #2 | 段 4 · 参数注 | `Velocidade máxima de 30 km/h. A velocidade média de uso é menor.` | 区分最高与平均 |
| 8 | 参数不符 #3 | 段 4 · 参数注 | `Tempo de recarga de 5 a 6 horas com o carregador original incluso.` | 限定原装充电器 |
| 9 | 使用困难 #1 | 段 6 | `A montagem do guidão leva cerca de 15 minutos. Veja o guia ilustrado abaixo.` | 组装说明 |

### 6.2 需要补的图（→ 04 Product Image）

| # | 对应差评 | 图位 | 图内文案（PT-BR） | 说明 |
|---|---|---|---|---|
| 1 | 配件缺失 #1 #2 | 图 8 · 包装清单图 | `Não incluso: capacete, bomba de ar` | **用图代替文字**——文字说明会被跳过 |
| 2 | 使用困难 #1 | 新增图 10 · 组装指引图 | 分步图 `1 · 2 · 3` | ML 允许 12 张，Shopee 需替换低价值图 |
| 3 | 误解型 #2 | 图 4 · 场景图 | 小字 `Vias pavimentadas` | 场景图加边界说明 |
| 4 | 参数不符 #1 | 图 3 · 参数图 | 续航项下加 `(piloto 70 kg, piso plano)` | 参数图补测试条件 |

> **第 1 条是最优解**：配件类误解用**文字永远说不清**，因为买家不读参数表也没读注意事项段。但**平铺图上一句 `Não incluso`，没有人会看漏。**

### 6.3 需要补的卖点（→ 03）

| # | 发现 | 动作 |
|---|---|---|
| 1 | 客服响应被 9 条好评主动称赞，但 Listing 未提 | 段 5 售后承诺中加入：`Atendimento pelo chat com resposta em até 24 horas` |

> **这是零成本的信任要素**：买家在下单前最想确认"出问题找谁"，而这条正好是本品被真实买家验证过的强项。**评论分析最大的价值就是发现这类"被验证过但没写进 Listing 的优点"。**

---

## 七、参数红线

| # | 被投诉参数 | 买家预期 | 实际值 | 禁用词候选 | 理由 |
|---|---|---|---|---|---|
| 1 | 续航 | 60 km | 35 km | `60 km` `autonomia longa` `dura o dia todo` | 竞品词表里有 60km，拿来用即虚标 |
| 2 | 承重 | 200 kg | 150 kg | `200 kg` | 超载有安全风险 |
| 3 | 上坡 | 任意坡 | 缓坡 | `qualquer ladeira` `sobe tudo` `off-road` | 未限定表述会被理解为全场景 |
| 4 | 夜间照明 | 替代路灯 | 仅提示可见性 | `iluminação noturna` `farol potente` | 涉及安全承诺 |
| 5 | 速度 | 60 km/h | 30 km/h | `60 km/h` `alta velocidade` | 竞品词表混入 |
| 6 | 保修 | 1 年 | 6 个月 | `garantia de 1 ano` | 避免预期落差 |

```yaml
forbidden_words_candidates:
  - "60 km"
  - "60 km/h"
  - "200 kg"
  - "autonomia longa"
  - "dura o dia todo"
  - "qualquer ladeira"
  - "sobe tudo"
  - "off-road"
  - "iluminação noturna"
  - "farol potente"
  - "garantia de 1 ano"
```

> **红线 1、5 特别值得注意**：`60 km` `60 km/h` 很可能出现在**竞品的关键词表里**（竞品标称 60 km 续航、60 km/h 极速）。如果 SEO 导向地把这些词写进标题，就等于主动制造虚标。
> **评论分析是发现这类红线最直接的途径**——因为买家会拿竞品的参数来质问你。

---

## 八、卖点排序（含情感强度）

| 排名 | 卖点 | 提及次数 | 情感强度 | 综合分 | 建议动作 |
|---|---|---|---|---|---|
| 1 | 爬坡能力 | 38 | 强（×3） | **114** | 主图 + 视频（**同时加边界说明**） |
| 2 | 折叠方便 | 31 | 强（×3） | **93** | 已突出，保持 |
| 3 | 减震效果好 | 27 | 中（×2） | **54** | 已突出，保持 |
| 4 | 电池续航 | 22 | 中（×2） | **44** | 参数图前置 + 补测试条件 |
| 5 | 外观设计 | 18 | 中（×2） | **36** | 详情页保持 |
| 6 | 性价比 | 14 | 中（×2） | **28** | 段 2 卖点中强化 |
| 7 | **卖家客服** | 9 | 强（×3） | **27** | ⭐ **新增到详情页段 5** |

**情感强度判定标准**：强（`excelente` / `perfeito` / `superou` / `recomendo`，权重 3）· 中（`bom` / `funciona bem` / `satisfeito`，权重 2）· 弱（`ok` / `razoável`，权重 1）

> **对照 Listing 现状**：
> - 排名前 2 的卖点（爬坡、折叠）都在标题或主图里 ✅
> - 排名第 7 的**客服**完全没提 ⚠️ → 这是**新发现的优化点**，且成本为零
> - 排名第 4 的**续航**只在参数表第 3 行 → 可前置

---

## 九、分析目标回答（SOP 1.6 七问）

| # | 问题 | 结论 | 依据 |
|---|---|---|---|
| 1 | 竞品靠什么卖 | （本案例为 `own` 范围，未导入竞品评论） | — |
| 2 | 买家真正关心什么 | **爬坡能力**（38 次，排名第 1）> 折叠便利 > 减震 | 128 条评论 |
| 3 | **哪些卖点必须写** | 爬坡能力、折叠、减震、续航、**客服响应** | 好评频次排序 |
| 4 | **哪些参数不能乱写** | 续航（35 km 限定条件）、承重（150 kg 单人）、速度（30 km/h 最高）、保修（6 个月） | 差评归因 3 条+误解 2 条 |
| 5 | **哪些问题需要提前解释** | 单人乘坐 / 上坡边界 / 18 kg 重量 / 灯光用途 / 保修期 / 续航测试条件 / 组装耗时 | 11 条可修复差评 |
| 6 | 我方应该突出什么差异化 | 爬坡能力（竞品少强调且我方被验证有效）+ **客服响应**（被验证但未宣传） | 好评排序 |
| 7 | 我方需要避开什么售后风险 | 续航期望落差、上坡期望落差、配件误解、灯光用途误解 | 差评归因 |

---

## 十、可修复性评估

| 项 | 数量 | 占比 |
|---|---|---|
| 差评总数 | 13 | 100% |
| **可由改描述/改图修复** | **11** | **84,6%** |
| 需改产品 / 供应商 | 0 | 0% |
| 需改物流 / 包装 | 2 | 15,4% |

**优先修复顺序**（按「出现频次 ÷ 修复成本」排序）：

| 顺序 | 动作 | 覆盖差评 | 成本 | 见效 |
|---|---|---|---|---|
| 1 | 包装清单图明确 `Não incluso` | 2 条（15,4%） | 1 张图 | 立即 |
| 2 | 段 6 补 5 条边界说明 | 5 条（38,5%） | 改文案 | 立即 |
| 3 | 参数段补测试条件 | 3 条（23,1%） | 改文案 | 立即 |
| 4 | 补组装指引图 | 1 条（7,7%） | 1 张图 | 立即 |
| 5 | 改包装 / 出货检查 | 1 条（7,7%） | 需供应链 | 数周 |
| 6 | 物流沟通 | 1 条（7,7%） | 需外部 | 数周 |

> **前 4 项覆盖 11 条差评（84,6%），全部是"改文案 + 补两张图"，一天内可完成。**

---

## 十一、分析合规扫描

`分析合规扫描：无命中`

（本案例未涉及：诱导删评、组织性举报、虚假评价、臆断评论真伪、泄露买家隐私。所有结论基于文本内容与字段对照，未对评论真实性下判断。）

---

## 十二、交付给其他模块的字段

```yaml
selling_points_ranked:
  - {rank: 1, point: "爬坡能力", mentions: 38, strength: "强", score: 114, action: "主图+视频（加边界说明）"}
  - {rank: 2, point: "折叠方便", mentions: 31, strength: "强", score: 93, action: "保持"}
  - {rank: 3, point: "减震效果好", mentions: 27, strength: "中", score: 54, action: "保持"}
  - {rank: 4, point: "电池续航", mentions: 22, strength: "中", score: 44, action: "参数图前置+补测试条件"}
  - {rank: 7, point: "卖家客服", mentions: 9, strength: "强", score: 27, action: "⭐新增到段5"}

forbidden_words_candidates:
  ["60 km", "60 km/h", "200 kg", "autonomia longa", "dura o dia todo",
   "qualquer ladeira", "sobe tudo", "off-road", "iluminação noturna",
   "farol potente", "garantia de 1 ano"]

review_patch_suggestions:             # → 03 详情页
  - {location: "段6首条", copy: "Indicado para 1 pessoa. Capacidade máxima de 150 kg (piloto + bagagem)."}
  - {location: "段6首条", copy: "Indicado para vias planas e pavimentadas e ladeiras leves."}
  - {location: "段6", copy: "Peso do produto: 18 kg. Recomendamos duas pessoas para transportá-lo em escadas ou ônibus."}
  - {location: "段6", copy: "O farol LED é para sinalização e visibilidade. Não substitui iluminação de via pública."}
  - {location: "段5售后", copy: "Garantia de 6 meses para motor e bateria."}
  - {location: "段5售后", copy: "Atendimento pelo chat com resposta em até 24 horas."}
  - {location: "段4参数注", copy: "Autonomia de até 35 km medida com piloto de 70 kg, em piso plano, a 20 km/h."}
  - {location: "段4参数注", copy: "Velocidade máxima de 30 km/h. A velocidade média de uso é menor."}
  - {location: "段4参数注", copy: "Tempo de recarga de 5 a 6 horas com o carregador original incluso."}
  - {location: "段6", copy: "A montagem do guidão leva cerca de 15 minutos. Veja o guia ilustrado abaixo."}

packaging_clarity_needed: true         # → 04 补包装清单图（明确 Não incluso）
scene_limit_image_needed: true         # → 04 场景图加边界说明

# 关键统计（供复测对标）
negative_review_count: 13
misunderstanding_count: 5
fixable_count: 11
fixable_ratio: 0.846
image_review_ratio: 0.242
```

---

## 十三、复测方案

| 项 | 内容 |
|---|---|
| 复测时点 | 改动生效后 **14–30 天**（评论积累需要时间，比广告复测周期长） |
| **主要观察指标** | **误解型差评占差评总数的比例**（当前 38,5%） |
| 次要指标 | 配件缺失类差评数（当前 2）、参数不符类差评数（当前 3） |
| 通过标准 | 误解型占比降至 **20% 以下** |
| 未通过处理 | 检查是"判定类型错了"（该用图却用了文字）还是"位置不醒目" |
| 需排除的干扰 | 是否换了物流 / 换了批次 / 是否赶上大促带来的新客群 |

> **为什么主指标选"误解型占比"而不是"差评数"？**
> 因为差评总数受销量、物流、大促等外部因素影响，**不是文案能控制的**。而误解型占比几乎完全由文案决定——**它是能验证"改文案有没有用"的最干净的指标。**

---

## 十四、这个案例证明了什么

| 结论 | 证据 |
|---|---|
| **绝大多数差评是文案问题，不是产品问题** | 84,6%（11/13）的差评可由改描述/改图修复 |
| **最大卖点同时是最大误解源** | 爬坡能力好评排名第 1（38 次），同时产生 1 条误解型差评 |
| **"写了"不等于"有效"** | 旗舰案例已预测 3 类差评并写了说明，仍全部发生 → 说明位置/形式不对 |
| **配件误解用文字说不清** | 2 条配件差评都因买家未读参数表 → 必须用平铺图 + `Não incluso` |
| **"描述不清" ≠ "描述错误"** | 3 条参数差评都是测试条件缺失，**不是虚标** → 补条件而非改数值 |
| **好评能发现被埋没的优点** | 客服响应被 9 条好评称赞但 Listing 未提 → 零成本优化点 |
| **竞品参数会变成自己的红线** | `60 km` `60 km/h` 来自竞品词表 → 必须列入 `forbidden_words` |
| **让描述更精确，而不是更保守** | 加"缓坡"边界说明，既保住第 1 卖点又管住预期 |
| **复测指标要选文案能控制的那个** | 用"误解型占比"而非"差评总数" |
| **闭环成立** | 03 写注意事项 → 上架 → 07 分析评论 → 回流 03 改文案 → 再复测 |

---

**关联文件**：[模块说明](../README.md) · [误解题识别 Prompt](../prompts/02_misunderstanding_detector.md) · [分类归因 Prompt](../prompts/01_classify_and_attribute.md) · [旗舰案例](../../../Examples/01_Patinete_Eletrico_500W/) · [闭环案例](../../../Examples/03_Closed_Loop/) · [广告诊断案例](../../06_Advertising_Optimization_Agent/examples/powerbank_20000mah_ads.md)
