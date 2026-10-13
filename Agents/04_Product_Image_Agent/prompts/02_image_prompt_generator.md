# TASK · 出图 Prompt 生成

> 配套使用：`00_system.md` + `01_image_plan_9grid.md` 的输出（9 图规划 + 图内文案）

本任务的产出是**可直接粘贴到图像生成工具**的 Prompt。

---

# INPUT

| 字段 | 来源 | 说明 |
|---|---|---|
| `platform` | 人工 | 决定主图规范 |
| `target_market` | 人工 | 决定图内文案语言 |
| `prompt_language` | 人工 | `en`（默认，通用模型）/ `zh`（中文模型如即梦、通义万相） |
| `image_plan` | **01 的输出** | 9 图规划表 |
| `image_copy` | **01 的输出** | 图内文案明细 |
| `visual_tone_confirmed` | **01 的输出** | 视觉调性 |
| `spec_table` | 03 | 参数校验用 |
| `forbidden_words[]` | 03 | 图内文字拦截 |
| `has_product_photo` | 人工 | `true` / `false`——是否有实拍图作为参考 |

---

# Prompt 结构公式

每张图的 Prompt 由 **七个槽位**构成，缺一不可：

```
[SUBJECT]     主体：是什么，什么形态，什么颜色材质
[MATERIAL]    材质与表面处理：哑光/亮面/金属/织物，纹理细节
[COMPOSITION] 构图：角度、位置、占画比例、留白区
[LIGHTING]    光位：主光方向、柔硬、色温、阴影
[BACKGROUND]  背景：纯白/场景/渐变，具体描述
[STYLE]       风格：写实/产品摄影/3D 渲染，参考质感
[PARAMETERS]  技术参数：比例、尺寸、（真实渲染时）相机参数
```

## 关键原则

| 原则 | 说明 |
|---|---|
| **越具体越可控** | `白色背景` → `纯白无缝背景，RGB 255,255,255，无阴影投射` |
| **不要说"好看"** | 用可执行的视觉描述替代主观评价 |
| **图内文字单独处理** | 文字**不要**写进出图 Prompt，而是标注为「后期叠字」。原因：当前图像模型渲染文字仍不稳定，尤其葡语变音符号（ã ç õ é）极易出错 |
| **一个 Prompt 出一个镜头** | 不要试图让一张 Prompt 生成"组合图" |

> **图内文字的处理建议**：本模块输出**不带文字的产品画面 Prompt** + **独立的图内文案**，由设计工具（Figma / Canva / Photoshop）后期叠字。这样文字一定准确、一定清晰、一定不会出现变音符号错误。

---

# 输出格式

对 9 张图逐一输出：

```markdown
### 图 <n> · <图位>

**出图 Prompt（<prompt_language>）**
```text
<完整 Prompt，七个槽位齐备>
```

**负面 Prompt**
```text
<需要排除的元素>
```

**图内文案（后期叠字）**
- 主文案：`<母语>`
- 副文案：`<母语>`
- 位置：<居中偏上 / 左下 / ...>
- 字号建议：<主文案高度 ≥ 图高 4%>

**渲染参数**
- 比例：1:1（或按平台）
- 建议尺寸：<1024×1024 / 1000×1000 / 1080×1920>
- 参考图需求：<需要 / 不需要>

**校验**
- 数值一致性：✅ / ❌ <逐项>
- 禁用词：✅ 无命中 / ❌ <列出>
- 场景范围：✅ 在范围内 / ❌ <越界>
```

---

# 负面 Prompt 标准库

按平台按情况拼装：

## 通用负面词

```text
text, watermark, logo, signature, stamp, border, frame, label,
low resolution, blurry, jpeg artifacts, oversaturated,
distorted proportions, extra objects, cluttered background,
plastic look, cartoon, illustration, 3d render (unless intended)
```

## Mercado Livre 主图专用（必须加）

```text
text of any kind, letters, numbers printed on the image, watermark,
logo, badge, ribbon, colored block, frame, border, background gradient,
additional props, accessories not included in the package
```

## Shopee 主图（可保留商品本身标签）

```text
watermark, extra props, cluttered background, distracting elements
```

## 场景图专用

```text
indoors with wrong context, rain, water, swimming pool (for non-waterproof items),
medical setting, exaggerated dramatic lighting, unrealistic physics
```

> 最后一行对**不防水产品**尤其重要——画面里出现水，等于暗示产品防水，属虚假宣传。

---

# 分图位的 Prompt 侧重

| 图位 | Prompt 侧重 |
|---|---|
| 图 1 主图 | `[BACKGROUND]` 必须是纯白无缝；无任何道具；构图最严格 |
| 图 2 卖点图 | 需要**强化卖点对应的视觉元素**（如快充 → 能量流动光效、接口特写） |
| 图 3 参数图 | 一般是**设计排版图**，不是 AI 生成图——输出「版式规格」而非出图 Prompt |
| 图 4/5 场景图 | 需要**人物/环境**，注意 I6 肖像约束（建议不露脸：手部、背影、远景） |
| 图 6 细节图 | 需要**微距质感**，Prompt 强调材质与纹理 |
| 图 7 尺寸图 | 一般是**含参照物的实拍或设计图**——输出「版式规格」 |
| 图 8 包装清单图 | **必须实拍**，AI 生成包装清单会导致买家收到实物不符 |
| 图 9 售后图 | **设计排版图**——输出「版式规格」 |

> ⚠️ **重要判断**：图 3、7、8、9 本质上是**信息排版图**，不是 AI 出图。对这些图位，输出「版式规格」（尺寸、字体、层级、配色）比输出出图 Prompt 更有用。
> **图 8 尤其必须实拍**——AI 生成的包装清单与实际不符，会直接引发"配件缺失"差评。

---

# 输出结构

```markdown
## 1. 出图 Prompt 清单
### 图 1 · 主图
### 图 2 · 核心卖点图
...
### 图 9 · 售后/保修图

## 2. 非 AI 图位的版式规格
（图 3 / 7 / 9，以及需要实拍的图 8）

## 3. 出图工作流建议
- 批量出图顺序
- 后期叠字流程
- 品控检查点

## 4. 图片合规扫描
（按 00_system.md 的 I1–I8 输出；无命中写"无命中"）

## 5. 交付给下游的字段
- hero_visual:
- key_visual_moments: []
- visual_tone_confirmed:
```

---

# SELF-CHECK

- [ ] 每张 AI 出图 Prompt 都齐备七个槽位
- [ ] 每张图都配了负面 Prompt
- [ ] ML / Amazon 主图 Prompt 的负面词包含 `text of any kind`
- [ ] 不防水产品的场景 Prompt 负面词包含 `rain, water, swimming pool`
- [ ] 图内文字**未写进**出图 Prompt，而是标注为后期叠字
- [ ] 图 8 已标注「必须实拍」
- [ ] 图 3 / 7 / 9 已输出「版式规格」而非出图 Prompt
- [ ] 场景图人物构图已避开可识别面孔
- [ ] 所有数值与 `spec_table` 一致
- [ ] 末尾已附图片合规扫描
