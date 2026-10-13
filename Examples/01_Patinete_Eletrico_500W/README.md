# 案例 01 · Patinete Elétrico 500W（电动滑板车）· 端到端全链路

> **案例类型**：旗舰案例 · 真实产品 · 已脱敏
> **覆盖模块**：03 Listing Creative → 04 Product Image → 05 Product Video
> **市场**：Shopee 巴西站（主）+ Mercado Livre（对照）
> **对应 SOP**：1.8 关键词表 · 3.3 Listing + 9 图 + 详情页结构 · 3.4 多链接启动

**为什么这是旗舰案例**：SOP 1.8 拿它当标题公式的示例产品（原文：`Patinete Elétrico Adulto 500W 150kg com Banco Dobrável para Mobilidade Urbana`），制作说明把它列在五款案例产品里（Electric Scooter），而且它**天然横跨三个模块**——参数多（适合做参数图）、有强场景（适合做场景视频）、有明确安全风险（适合演示合规守卫）。

---

## 一、产品背景

| 项 | 内容 |
|---|---|
| 产品 | 500W 电动滑板车，成人款，带座椅、可折叠、前后双减震 |
| 市场 | 巴西（Shopee BR 主力，ML 对照） |
| 类目 | 电动出行 |
| 定位 | 主推款 |
| 视觉调性 | 力量感、城市动感、冷色调 |

**类目特性**（决定了整个内容策略）：

| 特性 | 影响 |
|---|---|
| 参数多（功率/续航/承重/轮胎/减震…） | 参数图必须做，且不能堆一起 |
| 买家最怕"承重虚标""续航虚标" | 详情页必须解释测试条件 |
| 涉及安全（刹车、灯光、夜间骑行） | **合规红线最密集的类目** |
| 巴西对电动滑板车有地方性上路规定 | 场景表述不能承诺"合法上路" |

---

## 二、市场分析（简版）

详细版由 01 Market Research Agent 承担（Phase 2）。此处只给案例所需的结论：

| 维度 | 结论 | 对内容的影响 |
|---|---|---|
| 价格带 | 目标区间 `R$ 1.800 – R$ 2.600` | 标题参数词按此价位段配置 |
| 主流配置 | 350–500W、10–15Ah、8–10 寸轮胎、承重 100–150kg | 标题必须含 `500W` `150kg`（差异化于 350W 竞品） |
| 竞品短板 | 多数竞品**不写续航测试条件**、不写减震细节 | 我方详情页把这两点讲透 |
| 高退货原因 | 承重/续航不符预期、组装困难 | 详情页注意事项段必须覆盖 |
| 关键词 | 高频词集中在 `Patinete Elétrico` + `Adulto` + 功率 + `Dobrável` + `Mobilidade Urbana` | 标题结构直接对齐 SOP 公式 |

---

## 三、模块 03 · Listing Creative

### 3.1 输入（节选）

```yaml
platform: shopee
target_market: 巴西
mode: single
product_name: "Patinete Elétrico"
category: "电动出行"

spec_table:
  potencia: "500 W"
  bateria: "12 Ah / 48 V"
  autonomia: "até 35 km"
  velocidade_max: "30 km/h"
  capacidade_carga: "150 kg"
  pneu: "8 polegadas, câmara de ar"
  freio: "Freio a disco dianteiro + freio elétrico traseiro"
  suspensao: "Suspensão dianteira e traseira"
  banco: "Banco removível com haste ajustável"
  dobravel: "Sim — sistema de dobra em 3 segundos"
  tempo_recarga: "5 a 6 horas"
  iluminacao: "Farol LED dianteiro + lanterna traseira"
  peso_produto: "18 kg"
  peso_max_usuario: "150 kg"
  garantia: "6 meses (motor e bateria)"

usage_scope_confirmed:
  - "Deslocamento urbano em vias planas e pavimentadas"
  - "Lazer em parques e ciclovias"
  - "Trajeto casa-trabalho em distâncias curtas"

forbidden_words:            # 由合规扫描产出
  - "Anda a 60 km/h"        # 参数不符（实际 30 km/h）
  - "Autonomia de 60 km"    # 参数不符（实际 35 km）
  - "Pode Andar em Qualquer Via"  # 合规风险：上路规定因地区而异，不可承诺
  - "O Melhor Patinete do Brasil" # 绝对化
  - "Xiaomi"                # 未授权品牌
```

### 3.2 关键词七类分词（节选）

| 类别 | 词数 | 代表词 |
|---|---|---|
| 核心词 | 4 | `Patinete Elétrico`、`Scooter Elétrico`、`Patinete Adulto` |
| 参数词 | 12 | `500W`、`150kg`、`12Ah`、`8 Polegadas`、`30 km/h` |
| 人群词 | 4 | `Adulto`、`Unissex`、`Iniciante` |
| 功能词 | 10 | `Dobrável`、`com Banco`、`com Suspensão`、`Freio a Disco` |
| 场景词 | 6 | `Mobilidade Urbana`、`Ciclovia`、`Parque`、`Casa-Trabalho` |
| 配件词 | 5 | `Bateria`、`Carregador`、`Banco Removível` |
| **风险词** | **5** | ⛔ 见 `forbidden_words` |

### 3.3 标题（实测字符数）

| # | 标题 | 字符数 | 侧重 |
|---|---|---|---|
| **A** | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável e Suspensão para Mobilidade Urbana` | **89/120** | 参数驱动 ✅ 推荐 |
| B | `Patinete Elétrico Adulto 500W 150kg Dobrável com Banco para Mobilidade Urbana e Lazer` | **85/120** | 场景驱动 |
| C | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável Pneus 8 Polegadas Mobilidade Urbana` | **90/120** | 功能驱动 |

**与 SOP 原例的差异**：

| | 标题 | 字符数 |
|---|---|---|
| SOP 原例 | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável para Mobilidade Urbana` | **77** |
| 本案例 A | 在原例基础上加 `e Suspensão`（SOP 原例未含的差异化卖点） | **89** |

> SOP 原例只用了 77/120 字符，**还有 43 字符空间没用**。本案例的 A 方案把「双减震」这个竞品普遍不强调的点补进标题——**在不堆砌的前提下补真实卖点，是标题优化的正确做法；为凑字数加 `Novo` `Promoção` 才是堆砌。**

### 3.4 详情页 7 段（结构示意）

| 段 | 内容要点 | 本案例的特殊处理 |
|---|---|---|
| 1 · 欢迎语 | 产品一句话定位 | — |
| 2 · 核心卖点 | 5 条，每条含量化支撑 | 核心：`500W 电机 + 150kg 承重` |
| 3 · 使用场景 | 3 个场景 | ⚠️ **只写"vias planas e pavimentadas"**，不承诺任何路况都能骑 |
| 4 · 详细参数 | 表格，14 项 | 续航必须写测试条件 |
| 5 · 售后 | 6 个月（电机+电池） | 明确范围 |
| 6 · 注意事项 | 由 `review_insights` 驱动 | 见下方 |
| 7 · 关键词标签 | 10–15 个 | 风险词零命中 |

**段 6 注意事项的内容来源**（关键段落）：

```text
- A autonomia de até 35 km foi medida com piloto de 70 kg, em piso plano,
  velocidade média de 20 km/h e temperatura de 25 °C. Autonomia varia com
  peso do piloto, relevo, velocidade e calibragem dos pneus.
- A capacidade máxima é de 150 kg (piloto + bagagem).
- O tempo de recarga completo é de 5 a 6 horas.
- Regras de circulação de patinetes elétricos variam por cidade e estado.
  Verifique a legislação local antes de circular em vias públicas.
- É obrigatório o uso de capacete.
- O produto vem parcialmente montado; a montagem final leva cerca de 15 minutos.
```

> **最后三条是本案例最有价值的部分**：
> - 「上路规定因地区而异，请自行核查」——**既规避了合规风险，又显得专业**。直接写"可以合法上路"是危险的。
> - 「必须戴头盔」——安全提示，也降低售后纠纷。
> - 「需自行完成部分组装」——**组装困难是这类产品的高频退货原因**，前置说明能直接减少退货。
>
> 前两条则直接对冲"续航虚标""承重虚标"这两类高发差评。

### 3.5 卖点分层与交付字段

```yaml
core_selling_point: "Motor de 500W com capacidade para 150 kg — sobe ladeiras leves com estabilidade"

secondary_points:
  - "Suspensão dianteira e traseira — menos impacto em piso irregular"
  - "Dobrável em 3 segundos — cabe no porta-malas"
  - "Banco removível com haste ajustável"
  - "Freio a disco dianteiro + freio elétrico traseiro"
  - "Farol LED dianteiro e lanterna traseira"
  - "Autonomia de até 35 km (condições de teste no item 6 da descrição)"

forbidden_words: [同 spec_table 上方的 5 条]

visual_tone_hint: "Urbano e dinâmico — luz natural de fim de tarde, asfalto e ciclovia, tons frios com destaque no produto"

usage_scope_confirmed:
  - "Deslocamento urbano em vias planas e pavimentadas"
  - "Lazer em parques e ciclovias"
  - "Trajeto casa-trabalho em distâncias curtas"

title_final: "Patinete Elétrico Adulto 500W 150kg com Banco Dobrável e Suspensão para Mobilidade Urbana"
```

### 3.6 合规扫描结果

| 规则 | 命中 | 处理 |
|---|---|---|
| R1 绝对化用语 | 1 | `O Melhor Patinete do Brasil` → 删除 |
| R2 未授权品牌词 | 1 | `Xiaomi` → 删除 |
| R3 参数虚标 | **3** | `60 km/h` `60 km 续航` `350W 型号混入` → 全部删除并记录 `[PARAM_DROPPED]` |
| R4 促销词入标题 | 1 | 标题初稿含 `Promoção` → 移入详情页段 1 |
| R5 敏感表述 | 1 | `Pode Andar em Qualquer Via` → 改为"请核查当地法规" |
| R6 场景超范围 | 1 | 输入的 `Trilhas e Off-Road` 不在 `usage_scope` 内 → 删除并记录 `[SCENE_DROPPED]` |
| R7 伪造证明 | 0 | — |

**结论**：命中 8 条，其中 R3 有 3 条高危。全部处理，二次扫描零命中。

> **R3 命中 3 次是本案例最值得注意的地方。** 参数虚标往往不是故意编造，而是**关键词表里带着竞品的参数词**（竞品是 60km/h、60km 续航），如果直接拿来用就变成虚标。这证明了 `spec_table` 作为唯一数值来源的必要性。

---

## 四、模块 04 · Product Image

### 4.1 9 图内容规划

| # | 图位 | 承载信息 | 图内文案 | 字数 |
|---|---|---|---|---|
| 1 | **主图** | 车体完整 3/4 侧前角度 | **无文字**（ML 版）/ `500W · 150kg`（Shopee 版） | 0 / 14 |
| 2 | 核心卖点图 | 500W 电机 + 150kg 承重 | `Motor 500W · Suporta 150 kg` | 28 |
| 3 | 参数规格图 | 关键参数可视化 | 功率/电池/续航/速度/承重 | — |
| 4 | 场景图 A | 城市通勤 | `Mobilidade urbana` | 17 |
| 5 | 场景图 B | 折叠后放入后备箱 | `Dobra em 3 segundos` | 19 |
| 6 | 细节图 | 减震器 + 碟刹特写 | `Suspensão + freio a disco` | 25 |
| 7 | 尺寸/对比图 | 整车尺寸 + 折叠尺寸 | 数值标注 | — |
| 8 | 包装清单图 | **实拍**平铺 | `Não incluso: capacete` | 21 |
| 9 | 售后/保修图 | 6 个月电机与电池 | `6 meses · motor e bateria` | 26 |

### 4.2 平台冲突处理

| 方案 | 平台 | 主图 |
|---|---|---|
| **A** | Mercado Livre / Amazon | 纯白底 + **零文字**（ML 禁止主图出现文字） |
| **B** | Shopee / TikTok Shop | 白底 + `500W · 150kg`（站内提升点击率） |

⚠️ **不可复用**。ML 主图带文字会被判违规。

### 4.3 出图 Prompt（图 2 · 核心卖点图）

```text
[SUBJECT] A black and dark-grey adult electric scooter with a removable padded
seat, standing upright on flat asphalt. A slender LED headlight is on.
The deck is wide and textured with grip tape; 8-inch pneumatic tires are clearly visible.

[MATERIAL] Matte powder-coated aluminum frame with subtle brushed metal accents
on the folding hinge; rubber tires with visible tread; textured grip tape on the deck.

[COMPOSITION] Three-quarter front-left view, scooter occupying 70% of frame height,
slightly low camera angle to emphasize stability and power, clean empty space on the
right third reserved for text overlay.

[LIGHTING] Late afternoon directional natural light from camera-right, long soft
shadow cast to the left on the asphalt, warm-neutral tone (4800K).

[BACKGROUND] Smooth clean asphalt with a subtle cyclist lane line blurred in the
far background, shallow depth of field, horizon line below the frame center.

[STYLE] Commercial e-mobility advertising photography, photorealistic, crisp focus
on the scooter, dynamic but stable mood.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, reserve right 35% for text overlay.
```

**负面 Prompt**

```text
text rendered by the model, watermark, logo, brand names, rider, human figure,
helmet, exaggerated speed blur, sparks, off-road mud, wet road, rain,
damaged scooter, broken parts, low resolution, distorted proportions,
cluttered background, traffic, visible license plate
```

> **`rider, human figure` 是必加的**：主图如果出现人物，注意力会从产品上移开，且在 ML 上可能被判定为"展示不出售的内容"。

### 4.4 图片合规扫描（本案例命中项）

| 规则 | 命中 | 处理 |
|---|---|---|
| I1 伪造认证标志 | **1** | 图 9 初稿拟加 `INMETRO` 标志 → 商品未持证，**删除**，改为纯文字保修说明 |
| I2 伪造评价 / 销量 | 0 | — |
| I3 未授权品牌 | 1 | 负面 Prompt 加入 `logo, brand names`，拦截 `Xiaomi` |
| I4 参数不一致 | **2** | 图 3 初稿写 `35km` / `30km/h`（无空格）→ 统一为 `35 km` / `30 km/h` |
| I5 场景超范围 | **1** | 图 4 原方案为"山地越野场景"→ 不在 `usage_scope` 内，改为城市通勤场景 |
| I6 真人肖像 | 0 | 场景图采用骑行者剪影/背影，不露可识别面部 |
| I7 绝对化用语 | 0 | — |
| I8 对比图约束 | **1** | 图 7 初稿拟与某竞品同框对比 → 改为与**通用车身尺寸轮廓**对比 |

**结论**：命中 6 条，全部处理。

> **I1 和 I5 这两条最能说明合规守卫的价值**：一个差点生成虚假认证标志，一个差点用"越野场景"暗示产品能做它做不到的事。**这两类问题在电动出行类目里极其常见，且都属于高危。**

---

## 五、模块 05 · Product Video

### 5.1 钩子选择

| # | 类型 | 钩子 | 选择 |
|---|---|---|---|
| A | 痛点直击 | `Trânsito parado e você ainda de ônibus?` | ✅ 选定 |
| B | 反常识 | `Chega ao trabalho sem suar.` | |
| C | 场景代入 | `Seis quilômetros. Doze minutos.` | |

### 5.2 分镜（30s 版，节选）

| 镜号 | 时长 | 画面 | 运镜 | 静音字幕 |
|---|---|---|---|---|
| 1 | 0–3s | 拥堵车道，镜头从车流摇到旁边空着的自行车道 | 横摇 | `Trânsito parado?` |
| 2 | 3–7s | 滑板车从画面右侧滑入自行车道，匀速前行 | 侧向跟随 | `Patinete Elétrico 500W` |
| 3 | 7–12s | 上坡路段，车体稳定爬升，电机声平稳 | 低角度跟随 | `Sobe ladeiras leves` |
| 4 | 12–17s | 承重展示：骑行者（背影/剪影）+ 字幕标注 `150 kg` | 固定中景 | `Suporta 150 kg` |
| 5 | 17–22s | 折叠动作：3 秒内完成，放入汽车后备箱 | 固定俯拍 | `Dobra em 3 segundos` |
| 6 | 22–26s | 减震器与碟刹特写 | 微距固定 | `Suspensão + freio a disco` |
| 7 | 26–30s | 商品定格 + 参数卡 | 静态 | `Confira o link` |

**7 个镜头 / 30s** ✅

### 5.3 真人镜头处理（镜头 4）

```markdown
### 镜头 4 · 12–17s · [真人镜头 — 不生成 AI Prompt]

**拍摄指令**
- 机位：低角度，中景，略仰视
- 构图：**骑行者背影或剪影，不出现面部**
- 动作：匀速直线骑行，上身挺直
- 注意事项：**必须戴头盔**（安全合规 + 内容真实），需签署肖像授权或采用剪影
- 时长：5s

**替代 AI 方案**
- 采用逆光剪影构图
- Prompt：Silhouette of an adult riding an electric scooter from behind at dusk,
  wearing a helmet, riding on a flat asphalt bike lane, low camera angle,
  warm golden backlight, no facial features visible, photorealistic, gentle forward motion
```

### 5.4 配音稿（实测时长）

| 镜号 | 配音文案 | 词数 | 累计 | 预估时长 |
|---|---|---|---|---|
| 1 | `Trânsito parado e você ainda de ônibus?` | 7 | 7 | 2,8s |
| 2 | `Este patinete tem motor de quinhentos watts.` | 7 | 14 | 5,6s |
| 3 | `Sobe ladeiras leves sem esforço.` | 5 | 19 | 7,6s |
| 4 | `Suporta até cento e cinquenta quilos.` | 6 | 25 | 10,0s |
| 5 | `Dobra em três segundos e cabe no porta-malas.` | 8 | 33 | 13,2s |
| 6 | `Suspensão nas duas rodas e freio a disco na frente.` | 9 | 42 | 16,8s |
| 7 | `Patinete Elétrico 500W. Confira o link.` | 6 | **48** | **19,2s** |

> 30s 版只用了 48 词（19,2s）→ **留有大量留白**。对电动出行类目这是合适的：**激烈口播会削弱"稳定可靠"的观感**，慢节奏 + 留白更契合产品调性。
> 若平台要求填满时长，应补**画面**而不是补**文案**。

### 5.5 视频合规扫描（本案例命中项）

| 规则 | 命中 | 处理 |
|---|---|---|
| V1 伪造证明 | 0 | — |
| V2 参数不一致 | **1** | 字幕初稿 `500W` 无空格 → 改为 `500 W` |
| V3 场景超范围 | **1** | 镜头 3 原为"越野爬坡"→ 不在 `usage_scope`，改为"缓坡 urban 路况" |
| V4 绝对化用语 | 0 | — |
| V5 未授权品牌 | 0 | — |
| V6 真人肖像 | **1** | 镜头 4 从正面出镜 → 改为背影/剪影 |
| V7 危险演示 | **1** | 初稿含"双手离把展示平衡"→ **删除**（危险操作） |
| V8 音效版权 | 0 | 已标注可商用要求 |

> **V7 值得特别注意**：危险操作镜头是这类内容里最容易"顺手加"的——做视频的人会觉得"双手离把"很酷、有传播力。但这既违规也传递了危险示范。**这条规则必须硬拦。**

---

## 六、跨平台对照：标题从 120 字符压到 60 字符

| 平台 | 标题 | 字符数 |
|---|---|---|
| Shopee | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável e Suspensão para Mobilidade Urbana` | **89/120** |
| **Mercado Livre** | `Patinete Elétrico Adulto 500W 150kg com Banco Dobrável` | **54/60** |

**ML 的砍词过程**（按 ML 的砍词优先级：场景词 → 人群词 → 主关键词与核心参数永不砍）：

| 步骤 | 动作 | 被砍成分 | 剩余字符 |
|---|---|---|---|
| 1 | 起点 | — | 89 |
| 2 | 砍场景词 | `Mobilidade Urbana`、`para` | 69 |
| 3 | 砍并列功能词 | `e Suspensão` | 57 |
| 4 | 加回必要连接词 | `com` 保留 | **54** |

**保留的**：`Patinete Elétrico`（核心词）+ `Adulto`（人群词，ML 上必要）+ `500W` `150kg`（核心参数）+ `com Banco Dobrável`（核心功能）。
**一个核心参数都没砍**——这正符合 SOP 的砍词原则。

---

## 七、跨模块一致性校验

这是本案例最该被复制的一步。

| 字段 | 03 Listing | 04 Image | 05 Video | 一致 |
|---|---|---|---|---|
| 功率 | `500 W` | `500 W` | `500 W` | ✅ |
| 承重 | `150 kg` | `150 kg` | `150 kg` | ✅ |
| 续航 | `até 35 km` | `35 km` | 未提及 | ✅ |
| 折叠时间 | `3 segundos` | `3 segundos` | `3 segundos` | ✅ |
| 保修 | `6 meses (motor e bateria)` | `6 meses · motor e bateria` | 未提及 | ✅ |
| 核心卖点 | `Motor de 500W … 150 kg` | 图 2 文案同源 | 镜头 2/4 同源 | ✅ |
| 视觉调性 | `Urbano e dinâmico` | 4.3 的 Prompt 用词一致 | 分镜画面一致 | ✅ |
| 禁用词命中 | 5 条 | 5 条通用 + 1 条场景 | 同 | ✅ |

**发现的 4 处不一致（已修正）**：

| # | 问题 | 位置 | 修正 |
|---|---|---|---|
| 1 | `35km` 无空格 | 图 3 初稿 | → `35 km` |
| 2 | `500W` 无空格 | 视频字幕初稿 | → `500 W` |
| 3 | 保修表述不统一 | 图 9 vs 详情页 | 统一为 `6 meses · motor e bateria` |
| 4 | 视觉调性描述不一致 | 04 写"暖色"、05 分镜写"冷色" | 统一为 03 的 `Urbano e dinâmico`（冷调 + 暖光） |

> **第 4 条最能说明问题**：同一个产品，图片用暖色、视频用冷色，单看都好看，放一起就是拼凑感。**视觉调性必须由 03 定义，04 和 05 共同服从。**

---

## 八、优化建议

| # | 建议 | 依据 |
|---|---|---|
| 1 | 用 A/B/C 三个标题做**多链接测试**（SOP 3.4 方式二） | 三个标题侧重方向不同，可快速判断哪种方向点击率更高 |
| 2 | 优先拍**上坡镜头**作为视频主力素材 | "能爬坡"是这类产品最难被竞品模仿的直观证据 |
| 3 | 补拍**折叠全过程 3 秒完整长镜头** | 可剪出多版本、可做竖版、也是详情页补图素材 |
| 4 | 图 3 参数图把「续航测试条件」也画进去 | 直接对冲"续航虚标"类差评 |
| 5 | 上线后监测「承重」「续航」「组装」三类差评 | 验证段 6 前置说明是否真的降低了退货 |
| 6 | ML 的 `Ficha Técnica` **逐项填满**（14 项参数全部录入） | 完整填写的 listing 有排名倾斜 |
| 7 | 拿到 INMETRO 认证后再补认证图 | 目前不生成是对的——虚构认证是高危违规 |

---

## 九、这个案例证明了什么

| 结论 | 证据 |
|---|---|
| **端到端串联是可行的** | 03 的 `core_selling_point` 被 04 和 05 直接消费，零信息损耗 |
| **`spec_table` 作为唯一数值来源是必要的** | R3 命中 3 次——关键词表里混着竞品的 60km/h、60km 参数，没有 `spec_table` 就会变成虚标 |
| **合规守卫在电动出行类目里命中率最高** | 03 命中 8 条、04 命中 6 条、05 命中 4 条，其中多条高危 |
| **SOP 标题公式直接可用** | SOP 原例 77 字符，本案例在其基础上补真实卖点扩到 89 字符，未堆砌 |
| **跨平台必须重新压缩** | 89 → 54 字符，砍词有明确优先级，核心参数一个没丢 |
| **视觉调性必须由上游定义** | 发现的第 4 处不一致就是 04 和 05 各自定调性导致的 |
| **危险镜头会被顺手加进来** | V7 拦截的"双手离把"是内容吸引力与合规冲突的典型 |
| **事项段是最高收益的产出** | 续航测试条件、承重说明、组装说明、头盔提示——四条全部直接对冲高退货原因 |

---

**关联案例**：[案例 02 · Thermal Bag](../02_Thermal_Bag/)（iterate 模式回改闭环） · [Power Bank](../../Agents/03_Listing_Creative_Agent/examples/powerbank_20000mah.md) · [Pet Carrier](../../Agents/04_Product_Image_Agent/examples/pet_carrier.md) · [Air Fryer](../../Agents/05_Product_Video_Agent/examples/air_fryer.md)

**相关文档**：[架构拆解](../../docs/00_Architecture_SOP_to_Agent.md) · [平台字段规范](../../docs/02_Platform_Output_Spec.md) · [合规红线](../../docs/03_Compliance_Guard.md) · [自检清单](../../docs/04_Result_Checklist.md)
