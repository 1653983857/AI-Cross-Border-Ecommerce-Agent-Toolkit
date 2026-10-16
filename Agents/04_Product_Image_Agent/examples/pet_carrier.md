# 案例 · Bolsa Transportadora para Pets（Mercado Livre 巴西站）

> ⚠️ **规则更新说明（2026-10）**：本案例写作时 ML 要求主图纯白底。
> **现行规则已放宽**——白/纯色/实景按类目，但「背景干净 + 首图禁促销文字」不变。
> 本案例的白底方案仍是宠物用品类目的**最安全选择**，可继续使用；
> 最新规则见 [`../references/platform-mercadolivre.md`](../references/platform-mercadolivre.md)。

> **案例类型**：真实产品 · 已脱敏
> **使用模块**：04 Product Image Agent（上游依赖 03 Listing Creative）
> **对应 SOP**：3.3 9 张电商图片生成逻辑
> **重点演示**：ML 与 Shopee 的**主图规范冲突**处理

---

## 一、产品背景

| 项 | 内容 |
|---|---|
| 产品 | 宠物外出便携包，可折叠软箱式，透气网面，肩背两用 |
| 市场 | 巴西（站点：Mercado Livre） |
| 类目 | 母婴 / 宠物 |
| 定位 | 常规款 |
| 视觉调性 | 温柔、软质、浅色系 |

**为什么选这个案例**：宠物类目是典型的「尺寸不符预期」差评高发区——买家对"能装多大的狗/猫"没有概念，尺寸图做不好直接退货。同时 ML 首图禁促销文字与平台属性词（比 Shopee 严），和 Shopee 的常规做法直接冲突，正好演示 `platform_variant`。

---

## 二、输入端（从 03 继承）

```yaml
platform: mercadolivre
target_market: 巴西
mode: standard
prompt_language: en
has_product_photo: true

# ── 03 的输出（阻塞项，全部齐备）──
core_selling_point: "Ventilação em 3 lados com tela reforçada — seu pet respira e enxerga durante todo o trajeto"

secondary_points:
  - "Dobrável e plana para guardar — ocupa pouco espaço"
  - "Alça de ombro ajustável + alça de mão"
  - "Base rígida removível e lavável"
  - "Mosquetão interno para prender a coleira"

spec_table:
  dimensoes_externas: "41 × 25 × 26 cm"
  dimensoes_internas: "38 × 23 × 23 cm"
  peso: "1,2 kg"
  capacidade_peso: "até 8 kg"
  material: "Poliéster 600D + tela de nylon respirável"
  cor: "Cinza mescla com detalhes em azul"
  fechamento: "Zíper duplo com trava de segurança"

usage_scope_confirmed:
  - "Transporte de pets de pequeno porte em consultas veterinárias"
  - "Deslocamentos curtos de carro e transporte público"
  - "Viagens de ônibus de curta distância"

forbidden_words:
  - "À Prova d'Água"          # 参数不符：面料仅防泼水，不是防水
  - "Grau de Companhia Aérea"  # 无认证，不可宣称
  - "100% Seguro"
  - "Irresistível"
  - "Gucci"                    # 未授权品牌

visual_tone_hint: "Suave e acolhedor — fundo claro, tons pastel, sem elementos agressivos"
certifications: []             # 留空 → 不生成任何认证图
```

---

## 三、AI 处理流程

```text
[依赖检查] core_selling_point / secondary_points / spec_table / forbidden_words / usage_scope 全部齐备 ✅
[Step 1] 01_image_plan_9grid.md        → 9 图规划 + 图内文案
[Step 2] 检测到 platform = mercadolivre → 触发 platform_variant，输出两套主图方案
[Step 3] 02_image_prompt_generator.md  → 逐图出图 Prompt + 负面词
[Step 4] IMAGE COMPLIANCE GUARD I1–I8  → 扫描 → 命中 3 条 → 处理
```

---

## 四、生成结果

### 4.1 9 图内容规划

| # | 图位 | 承载信息 | 类型 | 画面构成 | 图内文案 | 字数 |
|---|---|---|---|---|---|---|
| **1** | 主图 | 这是一个宠物外出包 | 识别 | 纯白底，包体 3/4 正面角度，肩带自然垂落 | **无文字**（ML 强制） | 0 |
| **2** | 核心卖点图 | 三面透气网，宠物能呼吸能看见 | 说服 | 包内一只小型犬侧脸贴近网面，光线透过网孔 | `Ventilação em 3 lados` | 22 |
| **3** | 参数规格图 | 尺寸与承重 | 信息 | 白色背景排版图 | 内部尺寸 / 承重 / 重量 / 面料 | — |
| **4** | 场景图 A | 带去宠物医院 | 代入 | 主人手提包在医院走廊，不露脸（手部 + 背景） | （无文字） | 0 |
| **5** | 场景图 B | 车内短途出行 | 代入 | 包放在汽车后座，包内宠物探出头 | （无文字） | 0 |
| **6** | 细节特写图 | 内部挂扣 + 双层拉链 | 说服 | 微距特写，金属扣与拉链齿清晰 | `Mosquetão interno incluso` | 25 |
| **7** | 尺寸/对比图 | 41×25×26 cm 有多大 | 消除疑虑 | 包体旁放置成年女性手掌与前臂作为参照 | 尺寸数值 | — |
| **8** | 包装清单图 | 含什么 / 不含什么 | 消除纠纷 | **实拍**平铺俯拍 | `Não incluso: comedouro` | 22 |
| **9** | 售后/保修图 | 保修与客服 | 信任 | 深灰底排版图 | `3 meses · Garantia legal` | — |

**关键判断**：图 1 在 ML 上必须是**零文字**——这是本案例和 Shopee 版本最大的差异。

### 4.2 平台差异方案

| 方案 | 适用平台 | 主图 | 说明 |
|---|---|---|---|
| **A** | **Mercado Livre** / Amazon | 纯白底，**无任何文字** | ✅ 本案例采用 |
| B | Shopee / TikTok Shop | 白底 + 文字徽章（`3 Lados de Tela`） | 站内提升点击率的常见做法 |

⚠️ **冲突点**：Shopee 版本的主图如果直接上传到 ML，会被判违规（主图含文字）→ 可能被下架或要求整改。**两套素材必须分开管理。**

### 4.3 出图 Prompt（节选三张）

#### 图 1 · 主图（ML 版，无文字）

```text
[SUBJECT] A soft-sided pet carrier bag, rectangular box shape with rounded corners,
light grey mélange polyester body with subtle blue trim accents,
carrying handle on top and adjustable shoulder strap draped naturally alongside.

[MATERIAL] 600D polyester with visible fine woven texture, matte finish,
two breathable mesh panels clearly distinguishable by their slight sheen,
metal zipper pulls with a slight brushed metallic reflection.

[COMPOSITION] Three-quarter front view, product centered, occupying approximately
70% of frame width, floating with no support, no props, generous even white margin
on all four sides.

[LIGHTING] Soft diffused studio lighting from upper-left at 45 degrees,
large softbox, minimal contact shadow directly beneath the product,
neutral white color temperature (5500K).

[BACKGROUND] Pure seamless white background, RGB 255,255,255,
completely shadowless outside the product area.

[STYLE] Professional e-commerce product photography, photorealistic,
high detail, sharp focus across the entire product, commercial catalog quality.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, no text or graphics anywhere.
```

**负面 Prompt**

```text
text of any kind, letters, numbers printed on the image, watermark, logo, badge,
ribbon, colored block, frame, border, background gradient, additional props,
accessories not included in the package, animals outside the carrier,
low resolution, blurry, oversaturated, distorted proportions, cluttered background
```

#### 图 2 · 核心卖点图

```text
[SUBJECT] The same grey and blue pet carrier bag with a small short-haired dog
(approximately 5 kg, brown and white) inside, head and front paws visible behind
the breathable mesh panel, looking calmly toward camera-left.

[MATERIAL] Mesh panel rendered with a visible hexagonal weave, light passing through
creating a soft glow; polyester body retains matte woven texture.

[COMPOSITION] Eye-level side view, slightly angled toward the viewer, carrier fills
75% of frame, dog's face positioned on the upper third, empty space on the right
reserved for text overlay.

[LIGHTING] Bright soft daylight, large window light from the right, gentle fill
from the left, soft natural shadows, warm-neutral tone (5200K).

[BACKGROUND] Seamless light beige studio background, subtle vertical gradient,
no visible floor line.

[STYLE] Warm lifestyle product photography, photorealistic, shallow depth of field
on background, crisp focus on the mesh and the dog's face.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, reserve right 35% for text overlay.
```

**负面 Prompt**

```text
watermark, logo, brand names, rain, water, wet fur, swimming pool, outdoor storm,
medical setting, hospital equipment, exaggerated dramatic lighting,
text rendered by the model, multiple animals, distressed animal, aggressive dog
```

> **`rain, water, wet fur` 是必加的**：本产品面料仅防泼水、不防水。画面里出现水，等于暗示产品防水——属虚假宣传（对应 `forbidden_words` 中的 `À Prova d'Água`）。

#### 图 4 · 使用场景图 A

```text
[SUBJECT] A person's hand and forearm carrying the grey pet carrier by its top
handle, walking through a bright veterinary clinic waiting area.
The carrier is the visual focus; the person is cropped at the shoulder — no face visible.

[MATERIAL] Same carrier as main image; clinic interior with light wood flooring,
white walls, simple bench seating blurred in the background.

[COMPOSITION] Over-the-shoulder perspective, carrier in sharp foreground at lower-left,
background corridor receding to upper-right, intentional blur on the surroundings.

[LIGHTING] Bright even indoor lighting, large windows out of frame to the left,
soft ambient bounce, neutral-cool tone (5000K).

[BACKGROUND] Clean modern veterinary clinic interior, uncluttered, no signage,
no readable text on walls.

[STYLE] Documentary lifestyle photography, photorealistic, natural candid feel,
moderate depth of field.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, no face visible, no text.
```

**负面 Prompt**

```text
visible human face, recognizable person, rain, water, swimming pool,
large breed dog, multiple animals, cluttered background, readable signage,
medical equipment, syringes, distressed pets, watermark
```

### 4.4 非 AI 图位的版式规格

| 图位 | 类型 | 处理方式 |
|---|---|---|
| 图 3 | 参数排版图 | 设计工具制作。白底，4 行参数（`Dimensões internas 38 × 23 × 23 cm` / `Peso suportado até 8 kg` / `Peso do produto 1,2 kg` / `Poliéster 600D + tela respirável`），无衬线字体，主文案高度 ≥ 图高 4% |
| 图 7 | 尺寸对比图 | **实拍**：包体旁放成年女性手掌 + 前臂，标出 `41 × 25 × 26 cm`（逐字符等于 `spec_table.dimensoes_externas`） |
| 图 8 | 包装清单图 | **必须实拍**：平铺俯拍，含 `1× Bolsa` / `1× Alça de ombro` / `1× Base rígida removível` / `1× Manual`，并在角落明确标注 **`Não incluso: comedouro e coleira`** |
| 图 9 | 售后排版图 | 设计工具制作。深灰底，含保修时长 `3 meses`、范围、客服通道。**不得生成仿 ML 官方标识的图形** |

> **图 8 为什么必须实拍**：AI 生成的包装清单图容易"多画一件"或少画一件。买家收到实物后对照图片发现不符 → 直接差评"配件缺失"。这是最容易避免、也最不值得冒的险。

### 4.5 图片合规扫描结果

| 规则 | 命中 | 处理 |
|---|---|---|
| I1 伪造认证标志 | 0 | `certifications` 为空，未生成认证图 ✅ |
| I2 伪造评价 / 销量 | 0 | 无任何评价截图、销量角标 ✅ |
| I3 未授权品牌 | **1** | 输入的 `forbidden_words` 含 `Gucci`，已在全部 Prompt 与图内文案中拦截；主图 Prompt 负面词加入 `logo, brand names` |
| I4 参数不一致 | **1** | 图 7 尺寸标注初稿写成 `41 x 25 x 26 cm`（半角 x），已修正为 `41 × 25 × 26 cm`（与 `spec_table` 逐字符一致） |
| I5 场景超范围 | **1** | 场景图原计划包含"航空托运"，不在 `usage_scope_confirmed` 内 → 删除并记录 `[SCENE_DROPPED]` |
| I6 真人肖像 | 0 | 场景图均采用不露脸构图（手部 / 背影） ✅ |
| I7 绝对化用语 | 0 | 图内文案无绝对化表述 ✅ |
| I8 对比图约束 | 0 | 尺寸图参照物为手掌与前臂（通用形态） ✅ |

**结论**：命中 3 条，全部处理完毕，**二次扫描零命中**。

---

## 五、交付给 05 Product Video Agent

```yaml
visual_tone_confirmed: "Suave e acolhedor — fundo claro, tons pastel, sem elementos agressivos"
hero_visual: "包体 3/4 正面角度，浅灰混色面料配蓝色细节，三面透气网清晰可见"
key_visual_moments:
  - "宠物隔着网面向外看的侧脸 —— 直观传达'能呼吸能看见'"
  - "内部金属挂扣特写 —— 传达安全细节"
  - "折叠后平放的状态 —— 传达收纳便利"
forbidden_words:            # 透传给 05，做字幕硬拦截
  - "À Prova d'Água"
  - "Grau de Companhia Aérea"
  - "100% Seguro"
  - "Irresistível"
  - "Gucci"
```

---

## 六、优化建议

| # | 建议 | 依据 |
|---|---|---|
| 1 | 图 2 作为**视频首帧**候选 | 宠物隔网看镜头是本案例最有情绪张力的画面 |
| 2 | 图 7 的参照物换成**实物同框**（如 5 kg 标准砝码或常见宠物） | 手掌参照对"能装多大的狗"帮助有限，买家真正的疑问是承重 |
| 3 | ML 的 `Ficha Técnica` 字段**逐项填满** | 公开测试数据显示完整填写的 listing 自然流量获取概率显著更高 |
| 4 | 补拍**折叠状态图**作为候选第 10 张 | ML 允许 12 张，折叠收纳是差异化卖点，目前只在文案里 |
| 5 | 主图两套素材**分开命名存放**（`ML_` / `SP_` 前缀） | 防止误传导致 ML 主图违规下架 |
| 6 | 上线后监测"尺寸不符"类差评 | 验证图 7 是否真的起到了消除疑虑的作用 |

---

## 七、这个案例证明了什么

| 结论 | 证据 |
|---|---|
| **平台规范冲突必须显式处理** | ML 零文字 vs Shopee 带卖点，同一商品两套主图 |
| **有些图不能用 AI 生成** | 图 8 包装清单必须实拍，AI 生成=配件缺失差评 |
| **负面 Prompt 是防御手段** | `rain, water, wet fur` 直接挡住了"暗示防水"的虚假宣传风险 |
| **信息排版图 ≠ AI 出图** | 图 3/7/9 输出「版式规格」比输出 Prompt 更有用 |
| **参数一致性要到字符级** | 半角 `x` 与全角 `×` 都要统一——买家不会在意，但一致性是专业度的底线 |
| **阻塞机制真的会触发** | 场景"航空托运"因不在 `usage_scope_confirmed` 内被删除，证明 R6/I5 守卫生效 |

---

**相关文件**：[模块说明](../README.md) · [9 图规划 Prompt](../prompts/01_image_plan_9grid.md) · [出图 Prompt 生成](../prompts/02_image_prompt_generator.md) · [输出模板](../templates/output_image_prompt_pack.yaml) · [平台字段规范](../../../docs/02_Platform_Output_Spec.md)
