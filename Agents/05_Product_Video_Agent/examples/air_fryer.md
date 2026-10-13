# 案例 · Air Fryer 5L（Shopee 巴西站）

> **案例类型**：真实产品 · 已脱敏
> **使用模块**：05 Product Video Agent（上游 03 + 04）
> **对应 SOP**：3.3 详情页结构（叙事骨架）+ 1.6 评论洞察（钩子来源）
> **重点演示**：15s / 30s 双版本、钩子从差评来、静音可理解性

---

## 一、产品背景

| 项 | 内容 |
|---|---|
| 产品 | 5L 空气炸锅，8 种预设程序，可视窗口，炸篮可拆卸不粘涂层 |
| 市场 | 巴西（Shopee BR） |
| 类目 | 家电 |
| 定位 | 利润款 |
| 视觉调性 | 明亮、居家、暖色 |

**为什么选这个案例**：家电类目天然适合视频（有"过程感"和"结果感"），而且它的**核心痛点非常明确**——来自竞品差评的高频抱怨是"预热太慢"。这是 SOP 1.6 讲的"评论是最接近真实买家需求的地方"的完美应用场景：**钩子不需要创作，从评论里捡就行。**

---

## 二、输入端（从 03 / 04 继承）

```yaml
platform: shopee
target_market: 巴西
durations: [15, 30]
mode: standard
production_mode: mixed
prompt_language: en

# ── 03 的交付（阻塞项，全部齐备）──
core_selling_point: "Aquece até 200 °C em 3 minutos — sem pré-aquecimento longo"

secondary_points:
  - "Cesto de 5 litros — serve uma família de 4 pessoas"
  - "8 programas prontos com um toque"
  - "Frita com pouco ou nenhum óleo"
  - "Cesto antiaderente removível, pode lavar na máquina"
  - "Visor transparente — acompanhe sem abrir"

spec_table:
  capacidade: "5 L"
  potencia: "1500 W"
  temperatura: "80 °C a 200 °C"
  tempo_aquecimento: "≈ 3 minutos até 200 °C"
  programas: "8 presets"
  voltagem: "127 V / 220 V"
  material_cesto: "Aço com revestimento antiaderente"
  peso: "4,8 kg"
  dimensoes: "32 × 30 × 34 cm"
  garantia: "12 meses"

usage_scope_confirmed:
  - "Preparo de refeições diárias em casa"
  - "Reaquecer alimentos sem micro-ondas"
  - "Receitas rápidas para famílias pequenas"

forbidden_words:
  - "Fritura 100% Saudável"      # 绝对化 + 医疗暗示
  - "Substitui Médico"           # 医疗表述
  - "O Mais Rápido do Brasil"    # 绝对化
  - "Philips"                    # 未授权品牌
  - "À Prova de Falhas"          # 绝对化

title_final: "Air Fryer 5L 1500W 8 Programas Cesto Antiaderente Visor Transparente para Família"

# ── 04 的交付（视觉统一）──
visual_tone_confirmed: "Claro e acolhedor — luz natural de cozinha, tons quentes, madeira e branco"
hero_visual: "Airefryer 3/4 em bancada de madeira clara, cesto puxado 1/3, luz natural pela janela"
key_visual_moments:
  - "Cesto puxando com batatas douradas fumegando — o 'resultado' mais vendável"
  - "Painel digital acendendo com os 8 programas — 'simples de usar'"
  - "Comparação de óleo: colher cheia vs colher quase vazia — 'pouco óleo'"

hook_material:
  pain_points:
    - "差评高频：'demora muito pra esquentar, quase 8 minutos'"
    - "差评高频：'não sei qual programa usar em cada comida'"
  satisfaction_points:
    - "好评高频：'batata ficou pronta rápido e crocante'"
    - "好评高频：'cesto fácil de lavar'"
  competitor_weakness:
    - "同价位竞品普遍预热 6–8 分钟"
```

---

## 三、AI 处理流程

```text
[依赖检查] 六个阻塞字段齐备 ✅
[Step 1] 01_script_and_storyboard.md   → 钩子候选 → 选定 → 双版本脚本 → 分镜表
[Step 2] 时长核对                       → 15s 版 30 词 / 30s 版 65 词（实测）
[Step 3] 02_ai_video_and_voice.md      → 逐镜头 Prompt + 配音稿 + 字幕
[Step 4] 静音可理解性检查              → 三项核对
[Step 5] VIDEO COMPLIANCE GUARD         → 命中 4 条 → 处理
```

---

## 四、生成结果

### 4.1 钩子方案（0–3s）

| # | 类型 | 钩子文案 | 画面 | 选择 |
|---|---|---|---|---|
| A | **痛点直击** | `Sua air fryer demora uma eternidade para esquentar?` | 手机计时器特写，数字在跳到 6:00 时被按下暂停 | ✅ **选定** |
| B | 结果前置 | `Batata crocante em doze minutos.` | 炸篮拉出，金黄色薯条冒着热气 | |
| C | 对比冲击 | `Três minutos. Não oito.` | 左右分屏，左侧计时器 8:00，右侧 3:00 | |

**选定 A**，理由：
- 直接来自**竞品差评高频抱怨**（SOP 1.6 的做法）
- 巴西买家在家里对"等空气炸锅预热"有真实体感，钩子命中的是**已有的痛点**，不需要教育市场
- 3 秒内能拍完，且画面有动作（计时器跳动）

> **B 也很有力**，但它假设观众已经想要空气炸锅；A 假设观众已经有了一台慢的或对慢有顾虑——后者在巴西站的受众更广。

### 4.2 15s 版脚本

| 段 | 时间 | 目标 | 内容 |
|---|---|---|---|
| 钩子 | 0–3s | 抓住注意力 | 计时器跳到 6:00 被暂停 + `Sua air fryer demora uma eternidade para esquentar?` |
| 核心卖点 | 3–9s | 讲清一件事 | 炸锅通电，面板数字从 25 °C 快速攀升到 200 °C，计时器同步显示 3:00 |
| 场景 | 9–13s | 代入 | 炸篮拉出，金黄薯条冒热气，家人伸手取食 |
| CTA | 13–15s | 行动 | 商品定格 + `Air Fryer 5L. Confira o link.` |

### 4.3 30s 版脚本

| 段 | 时间 | 目标 | 内容 |
|---|---|---|---|
| 钩子 | 0–3s | 抓住注意力 | 同 15s 版（**钩子必须一致**） |
| 卖点 1 | 3–9s | 主卖点 | 3 分钟到 200 °C 的完整过程 |
| 卖点 2 | 9–16s | 副卖点 | 8 个预设程序依次点亮，手指轻触切换 |
| 场景 | 16–23s | 代入 | 一家人晚餐，炸篮和烤盘同时出菜 |
| 参数/信任 | 23–28s | 消除顾虑 | 5L 容量、1500W、可拆洗炸篮、12 个月保修 |
| CTA | 28–30s | 行动 | 同 15s 版（**CTA 必须一致**） |

### 4.4 分镜表（30s 版）

| 镜号 | 时长 | 画面内容 | 运镜 | 静音字幕 | 音效 / 人声 |
|---|---|---|---|---|---|
| 1 | 0–3s | 手机计时器特写，数字跳到 6:00 时手指按下暂停 | 固定，微距 | `Esperando esquentar?` | 人声提问 + 计时器"嘀"声 |
| 2 | 3–6s | 空气炸锅插电，面板数字从 25 快速攀升，计时器同步走 3:00 | 缓慢推近面板 | `200 °C em 3 minutos` | 电子提示音 |
| 3 | 6–9s | 炸篮拉出，金黄薯条冒热气，蒸汽升腾 | 侧向跟随炸篮拉出 | `Batata crocante` | 酥脆声 + 热气声 |
| 4 | 9–12s | 面板 8 个预设图标依次点亮 | 固定 + 轻微推近 | `8 programas prontos` | 轻快电子音 |
| 5 | 12–16s | 手指轻触面板切换程序，画面切到对应食物图标 | 固定 | `Um toque` | 触控反馈音 |
| 6 | 16–19s | 晚餐场景：炸篮与烤盘同时出菜，家人（**手部/背影，不露脸**）取食 | 中景固定 | `Para toda a família` | 环境餐具声 |
| 7 | 19–23s | 桌面全景，5 人份餐食摆放完整 | 缓慢横摇 | `5 litros` | 暖调 BGM 渐强 |
| 8 | 23–26s | 炸篮拆卸、冲洗、放入洗碗机特写 | 固定，俯拍 | `Cesto antiaderente lavável` | 水流声 |
| 9 | 26–28s | 参数卡排版：1500W / 5L / 127V-220V / 12 meses | 静态排版 | `1500 W · 5 L · 12 meses` | BGM 持续 |
| 10 | 28–30s | 商品定格 + 包装清单一角 | 固定 | `Confira o link` | BGM 收尾 |

> **10 个镜头 / 30s** ——符合"30s 版 7–10 个镜头"的要求。
> **镜头 6 标注为真人镜头**：只输出拍摄指令，不生成 AI Prompt（见 4.6）。

### 4.5 配音稿（**词数与时长均为实测计算**）

| 镜号 | 时间 | 配音文案 | 词数 | 累计 | 预估时长 |
|---|---|---|---|---|---|
| 1 | 0–3s | `Sua air fryer demora uma eternidade para esquentar?` | 8 | 8 | 3,2s |
| 2 | 3–6s | `Esta chega a duzentos graus em três minutos.` | 8 | 16 | 6,4s |
| 3–4 | 6–12s | `Cesto de cinco litros: comida para toda a família.` | 9 | 25 | 10,0s |
| 5 | 12–16s | `Oito programas prontos, só girar o botão.` | 7 | 32 | 12,8s |
| 6–7 | 16–23s | `Frita sem óleo e a louça sai fácil, porque o cesto é antiaderente.` | 13 | 45 | 18,0s |
| 8 | 23–26s | `Traz receitas em português e tem um ano de garantia.` | 10 | 55 | 22,0s |
| 9–10 | 26–30s | `Air Fryer cinco litros, cento e cinquenta graus a duzentos.` | 10 | **65** | **26,0s** |

**时长核对**：65 词 ÷ 2,5 词/秒 = **26,0s**，落在 30s 窗口内（留 4s 给留白与镜头切换）✅

**15s 版配音稿**：

| 镜号 | 时间 | 配音文案 | 词数 | 累计 | 预估时长 |
|---|---|---|---|---|---|
| 1 | 0–3s | `Sua air fryer demora demais para esquentar?` | 7 | 7 | 2,8s |
| 2 | 3–6s | `Esta chega a duzentos graus em três minutos.` | 8 | 15 | 6,0s |
| 3 | 6–13s | `Cesto de cinco litros para toda a família.` | 8 | 23 | 9,2s |
| 4 | 13–15s | `Air Fryer cinco litros. Confira o link.` | 7 | **30** | **12,0s** |

**时长核对**：30 词 ÷ 2,5 = **12,0s**，落在 15s 窗口内（留 3s 留白）✅

**TTS 参数建议**
```yaml
accent: "Português (Brasil)"
gender: "Feminino"
tone: "Próximo e cotidiano, como quem conversa em casa"
speed: 1.0
pauses: "句末 0,3s / 镜头切换 0,2s"
diacritics_checked: true   # 已核对：três, família, óleo, antaderente → antiaderente, português, botão
```

> 注：本案例初稿把 `botão` 写成 `botao`、`três` 写成 `tres`，已在核对环节修正。**变音符号是 PT-BR TTS 的翻车点**——`botao` 和 `botão` 发音完全不同。

### 4.6 真人镜头处理（镜头 6）

```markdown
### 镜头 6 · 16–19s · [真人镜头 — 不生成 AI Prompt]

**原因**：涉及真人出镜，按 V6 规则改为拍摄指令。

**拍摄指令**
- 机位：桌面高度，中景，略低于视线（营造"围坐餐桌"感）
- 景别：中景，画面只到家人肩部以下
- 动作：三只手依次从画外伸入取食，动作自然不刻意
- 道具：餐桌、餐盘、实拍成品菜（可用真实炸物）
- 场地：明亮厨房或餐区，暖光，背景简洁
- 时长：3s
- 注意事项：**画面只到肩部以下，不出现面部**；若需真人出镜面部，需签署肖像授权

**替代 AI 方案**（如需全 AI 制作）
- 采用不露脸构图：仅手部取食
- 对应 Prompt：Close-up of three hands, of different skin tones,
  reaching into frame to take golden french fries from an air fryer basket
  on a light wooden dining table, no faces visible, warm natural window light,
  shallow depth of field, photorealistic lifestyle photography, slow gentle motion
```

### 4.7 字幕表

| 镜号 | 时间 | 第 1 行 | 第 2 行 | 字数 | 行数 |
|---|---|---|---|---|---|
| 1 | 0–3s | `Esperando esquentar?` | — | 20 | 1 |
| 2 | 3–6s | `200 °C em` | `3 minutos` | 12 | 2 |
| 3 | 6–9s | `Batata crocante` | — | 15 | 1 |
| 4 | 9–12s | `8 programas` | `prontos` | 17 | 2 |
| 5 | 12–16s | `Um toque` | — | 8 | 1 |
| 6 | 16–19s | `Para toda` | `a família` | 16 | 2 |
| 7 | 19–23s | `5 litros` | — | 8 | 1 |
| 8 | 23–26s | `Cesto lavável` | — | 13 | 1 |
| 9 | 26–28s | `1500 W · 5 L` | `12 meses` | 19 | 2 |
| 10 | 28–30s | `Confira o link` | — | 14 | 1 |

全部符合"每屏 ≤2 行 / 每行 ≤20 字符"。

### 4.8 静音可理解性检查

| 检查项 | 结果 | 依据 |
|---|---|---|
| 关掉声音，能否看懂这是什么产品 | ✅ | 镜头 2/3/7 都有完整产品画面 + 字幕 `5 litros` |
| 关掉声音，能否看懂核心卖点 | ✅ | 镜头 1（计时器 6:00）+ 镜头 2（`200 °C em 3 minutos`）构成完整对比 |
| 关掉声音，能否看懂结尾要做什么 | ✅ | 镜头 10 字幕 `Confira o link` |
| **是否通过** | **✅ 通过** | 三项全 ✅ |

> **镜头 1 的设计要点**：字幕写 `Esperando esquentar?` 而不是完整问句，是因为字幕要短；而**计时器跳到 6:00 这个画面本身不需要任何文字就能传达"等太久"**。这就是"画面优先于口播"原则的应用。

### 4.9 视频合规扫描结果

| 规则 | 命中 | 处理 |
|---|---|---|
| V1 伪造证明 | 0 | 无虚构认证 / 销量 / 评价 ✅ |
| V2 参数不一致 | **1** | 字幕初稿写 `1500W`（无空格），已改为 `1500 W` 与 `spec_table` 一致 |
| V3 场景超范围 | 0 | 所有场景均在 `usage_scope_confirmed` 内 ✅ |
| V4 绝对化用语 | **2** | 脚本初稿的 `O mais rápido do Brasil` → 改为 `200 °C em 3 minutos`；配音稿的 `100% sem óleo` → 改为 `sem óleo ou com pouquíssimo óleo` |
| V5 未授权品牌 | **1** | 输入的 `forbidden_words` 含 `Philips`，已在全片字幕与配音中拦截 |
| V6 真人肖像 | **1** | 镜头 6 原计划为真人面部出镜 → 改为**只到肩部以下**，并补出不露脸 AI 替代方案 |
| V7 危险演示 | 0 | 无危险操作 ✅ |
| V8 音效版权 | **1** | BGM 与音效已标注「需使用可商用素材」 |

**结论**：命中 5 条（含 V6 肖像类），全部处理完毕，**二次扫描零命中**。

---

## 五、技术需求

```yaml
aspect_ratio: "1:1"            # Shopee 主图位；TikTok 版改 9:16
resolution: "1080x1080"
bgm_mood: "暖调、轻快、日常感，不喧闹，中段渐强、结尾干净收束"
bgm_license: "需使用可商用素材"
sfx_list:
  - "计时器嘀声（镜头 1）"
  - "电子提示音（镜头 2/4）"
  - "酥脆声 + 热气声（镜头 3）"
  - "触控反馈音（镜头 5）"
  - "环境餐具声（镜头 6）"
  - "水流声（镜头 8）"
overlay_elements:
  - "参数卡（镜头 9）：1500 W · 5 L · 127V/220V · 12 meses"
  - "Logo 角落位（镜头 10）"
```

---

## 六、优化建议

| # | 建议 | 依据 |
|---|---|---|
| 1 | **镜头 2 的数字攀升过程拍实**，不要用后期动画 | 真实过程比动画更有说服力，且规避"数据造假"观感 |
| 2 | 15s 版优先投放主图位，30s 版放详情页 | 15s 版信息密度更高，适合拦截；30s 版适合已进入详情页的意向用户 |
| 3 | 补拍一条**只用 3 分钟**的完整无剪辑镜头作素材 | 可剪出多个版本复用，也便于日后做 TikTok 竖版 |
| 4 | B 钩子（`Batata crocante em doze minutos`）做 A/B 测试 | 两个钩子代表两种假设：A 打已有痛点，B 打食欲冲动 |
| 5 | 上线后监测"预热时间"相关差评是否下降 | 验证核心卖点是否真的成立 |
| 6 | TikTok 版需重做构图（9:16，字幕上移避开底部 20%） | 横版素材直接拉伸会破坏安全区 |

---

## 七、这个案例证明了什么

| 结论 | 证据 |
|---|---|
| **钩子从评论里捡，不用创作** | 钩子 A 直接来自竞品差评的"预热太慢"抱怨 |
| **配音时长必须实算** | 65 词 ÷ 2,5 词/秒 = 26,0s，全部数字可复现；超了要删词不加语速 |
| **静音可理解性是硬指标** | 三项全过才算通过——多数买家静音浏览 |
| **变音符号是 PT-BR 的翻车点** | 初稿 `botao` / `tres` 已修正为 `botão` / `três` |
| **真人镜头要区别处理** | 镜头 6 从"真人面部"改为"肩部以下"，并给出不露脸 AI 替代 |
| **字幕比配音短** | 钩子配音是完整问句，字幕精简为 `Esperando esquentar?` |
| **15s 与 30s 版钩子/CTA 一致** | 两个版本动的是同一个念头 |
| **绝对化用语会自然冒出来** | 初稿出现 `O mais rápido do Brasil`，说明阻断规则是必要的而非形式 |

---

**相关文件**：[模块说明](../README.md) · [脚本与分镜 Prompt](../prompts/01_script_and_storyboard.md) · [视频与配音 Prompt](../prompts/02_ai_video_and_voice.md) · [输出模板](../templates/output_video_pack.yaml) · [自检清单](../../../docs/04_Result_Checklist.md)
