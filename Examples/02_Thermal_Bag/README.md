# 案例 02 · Bolsa Térmica 20L（保温包）· iterate 模式的回改闭环

> ⚠️ **规则更新说明（2026-10）**：案例中「ML 主图纯白底」为旧规。
> 现行：白/纯色/实景**按类目**，但背景必须干净、首图禁促销文字。
> 见 [`../Agents/04_Product_Image_Agent/references/platform-mercadolivre.md`](../../Agents/04_Product_Image_Agent/references/platform-mercadolivre.md)。

> **案例类型**：真实产品 · 已脱敏
> **覆盖模块**：03 Listing Creative（`mode = iterate`）+ 06 Advertising（预演）
> **市场**：Shopee 巴西站
> **对应 SOP**：3.6 广告调整逻辑 · 3.5 广告与评价节奏

---

## 一、这个案例和案例 01 有什么不同

案例 01 演示的是**从零到一**（`mode = single`）。本案例演示的是**跑起来之后发现问题、回头改**（`mode = iterate`）。

| | 案例 01 | 案例 02 |
|---|---|---|
| 触发场景 | 新品上架 | 已上架，广告数据不健康 |
| 输入 | 空 | **现有 Listing + 症状描述** |
| 输出 | 完整素材包 | **只改必要部分**，其余不动 |
| 核心能力 | 生成 | **诊断 + 最小改动** |

> **为什么会需要 iterate 模式**：SOP 3.6 把"有曝光没点击""有点击没加购"等现象写成了可判定的规则。这意味着**回改不该靠感觉**——症状是可诊断的，改动是可定位的。

---

## 二、产品背景

| 项 | 内容 |
|---|---|
| 产品 | 20L 保温包，防水面料，加厚铝箔内衬，可折叠，带加宽加固提手 |
| 市场 | 巴西（Shopee BR） |
| 类目 | 箱包 |
| 定位 | 引流款 |
| 上架时长 | 3 周 |

**为什么选它**：SOP 3.6 给的健康基准线是「点击率 3–5%」。保温包这类**主图差异度低**的类目，最容易出现的问题就是"有曝光没点击"——主图看起来都差不多，买家为什么点你？这是最典型、也最好验证的 iterate 场景。

---

## 三、SOP 3.6 的健康基准线

先把基准线摆出来，因为**诊断需要基准**：

| 指标 | 基准（SOP） | 本案例实际 | 判定 |
|---|---|---|---|
| 点击率（CTR） | **3–5%** | **1,4%** | ❌ 低于下限一半以上 |
| 转化率 | 稳定 **1% 以上** | 2,1% | ✅ 达标 |
| 加购率 | **> 8%** | 11,3% | ✅ 达标 |

**症状定位**：**有曝光没点击**（曝光量正常、CTR 严重偏低、但转化与加购都健康）。

> 这个组合非常关键：**转化率正常说明产品本身没问题、价格也没问题**——问题出在"买家点进来之前的环节"，也就是**主图和标题**。如果转化率也低，那才要考虑详情页和价格。

---

## 四、SOP 3.6 的诊断规则

SOP 对"有曝光没点击"给出的优先检查清单：

| 优先检查项 | 本案例现状 | 诊断 |
|---|---|---|
| 主图 | 一张白底产品图，无任何文字，与其他竞品主图**几乎无法区分** | 🔴 **主因** |
| 标题 | 参数齐备但缺少"点进来的理由" | 🟡 次因 |
| 价格展示 | 与同类持平 | ✅ 无问题 |
| 核心卖点 | 详情页有，但**主图上完全没有** | 🔴 **主因** |
| 是否有明显优惠 | 无 | 🟡 可选优化 |

**SOP 给出的优化方向**：换主图 → 优化标题关键词 → 强化价格优势 → 主图加卖点 → 调整广告词

---

## 五、iterate 模式的输入

```yaml
platform: shopee
target_market: 巴西
mode: iterate                  # ← 关键：只改必要部分

# ── 现状 ──
existing_title: "Bolsa Térmica 20L Impermeável para Delivery e Supermercado com Alça Reforçada"
                                    # 77 字符

existing_main_image_desc: "Bolsa térmica em fundo branco puro, vista frontal 3/4,
                           sem texto, sem elementos gráficos, produto centralizado"

symptom: "有曝光没点击。CTR 1,4%（SOP 基准 3–5%）。曝光量正常 12.400/周，
          转化率 2,1% 与加购率 11,3% 均达标。"

# ── 约束 ──
constraints: "不改变产品定位和价格。主图需要改动，标题允许小幅优化。
              详情页与视频保持不动（转化率已达标，不需动）。"

# ── 从 03 的原始输出继承（保持一致性）──
core_selling_point: "Conserva a temperatura por até 8 horas com forro de alumínio duplo"
spec_table:
  capacidade: "20 L"
  material_externo: "Poliéster 600D impermeável"
  forro: "Alumínio duplo"
  tempo_conservacao: "até 8 horas"
  carga_suportada: "até 15 kg"
  dimensoes: "40 × 30 × 22 cm"
  medida_fechada: "40 × 30 × 6 cm"
  peso: "620 g"
forbidden_words: ["100% Impermeável", "A Melhor do Mercado", "Vedação Absoluta", "Termo Rei"]
usage_scope_confirmed: ["Transporte de compras do supermercado", "Entrega de comida por entregadores", "Transporte de bebidas geladas para eventos"]
```

---

## 六、回改方案

### 6.1 主图迭代（核心改动）

**诊断**：原主图的问题不是"拍得不好"，而是**"看不出和别的保温包有什么不同"**。搜索列表里 20 张几乎一样的白底保温包，买家没有任何理由点你这一张。

```markdown
## 主图迭代方案

- 现状：纯白底 + 无文字 + 正面 3/4 角度
- 症状：CTR 1,4%（基准 3–5%），曝光正常
- 诊断：主图在搜索结果中「无差异度」。转化率与加购率均达标 → 产品与价格无问题，
        问题在点击环节。对应 SOP 3.6「有曝光没点击 → 优先检查主图」。
- 修改点（最小化）：
    1. 保留白底与产品角度（不推翻重拍）
    2. 增加**视觉差异元素**：把产品置于「半打开状态」，露出内部铝箔层 + 一瓶冰饮
    3. 增加**一行卖点文字**：`8h de conservação`（不超过 20 字符，Shopee 允许图内文字）
- 不改动：产品本身、拍摄角度、背景色、价格展示
- 预期效果：搜索列表中出现「能看懂的差异点」，目标 CTR 提升至 3% 以上
```

**为什么这样改**：
- **露出内衬 + 冰饮** = 一张图同时回答了"这是什么"和"它能干什么"，这是原主图没做到的
- **`8h de conservação`** 直接来自 `core_selling_point`，且是竞品详情页才讲、主图没讲的信息——**把详情页的差异化搬到主图上，是提升点击率最直接的办法**

### 6.2 迭代后主图 Prompt（Shopee 版）

```text
[SUBJECT] A grey and navy thermal delivery bag, 20L, partially unzipped and open
to about 40 degrees, revealing a shiny silver aluminum-lined interior.
A chilled glass bottle with visible condensation stands beside the bag's base.

[MATERIAL] Water-resistant 600D polyester outer with visible fine weave texture,
matte finish; bright reflective silver aluminum foil lining inside,
slightly wrinkled to show thickness and flexibility.

[COMPOSITION] Three-quarter front view, bag centered occupying 65% of frame,
slightly elevated camera angle looking down into the open bag,
empty space on the top right reserved for text overlay.

[LIGHTING] Clean studio lighting from upper-left with large softbox,
crisp specular highlights on the aluminum lining to convey the insulation property,
neutral white temperature (5500K).

[BACKGROUND] Pure seamless white background, RGB 255,255,255, no shadow outside
the product and bottle area.

[STYLE] Commercial product photography, photorealistic, high detail,
crisp focus across bag and bottle, category-leading clarity.

[PARAMETERS] 1:1 square aspect ratio, 1024x1024, reserve top-right 30% for text overlay.
```

**负面 Prompt**

```text
text rendered by the model, watermark, logo, brand names, melted ice, water puddle,
wet fabric, visible human hands, food items other than the bottle,
cluttered background, low resolution, distorted proportions, dark or moody lighting
```

> **`melted ice, water puddle, wet fabric` 必加**：产品是"防泼水"不是"完全防水"（`forbidden_words` 里明确禁了 `100% Impermeável`）。画面出现水渍或融冰，等于暗示防水能力超出实际。

### 6.3 标题微调

**原则**：`mode = iterate` 下标题只做**小幅优化**，不重写。因为转化率已达标，说明标题带来的流量质量没问题，问题在点击率——**标题的作用是"让对的人搜到你"，不是"让人想点你"**。

| | 标题 | 字符数 |
|---|---|---|
| 现状 | `Bolsa Térmica 20L Impermeável para Delivery e Supermercado com Alça Reforçada` | **77/120** |
| 迭代后 | `Bolsa Térmica 20L Impermeável 8 Horas de Conservação para Delivery e Supermercado` | **81/120** |

**改动说明**：
- **加入** `8 Horas de Conservação`（核心差异化卖点，且是买家的真实搜索意图）
- **移除** `com Alça Reforçada`（次要功能，已在详情页说明）
- 主关键词 `Bolsa Térmica` 位置不变，仍在最前
- 改动幅度：4 个字符的净增，**结构未变**

### 6.4 明确不改动的部分

| 项 | 不动 | 理由 |
|---|---|---|
| 详情页 | ❌ 不动 | 转化率 2,1% 已达标 → 详情页是有效的 |
| 价格 | ❌ 不动 | 转化与加购达标 → 价格不是瓶颈 |
| 视频 | ❌ 不动 | 同上 |
| 其余 8 张图 | ❌ 不动 | 点击率只与主图有关 |
| SKU 结构 | ❌ 不动 | 加购率 11,3% 达标 → SKU 设计有效 |

> **`mode = iterate` 最大的价值就在这里：明确地"不改什么"。** 很多运营在点击率低的时候会顺手改价格、改详情页、加优惠券——把本来没问题的环节改坏，反而看不出是哪个动作起了作用。

---

## 七、SOP 3.6 的另一条建议

SOP 还提到一个解除广告 bug 的技巧：

> 当广告出现跑不动的情况，不只是单单调整 ROI 和预算，这个时候把主图、标题、详情页稍微改一下，一般改一下主图即可，解除广告的 bug，广告就能跑起来了。

**本案例的适用性判断**：

| 情况 | 是否适用 |
|---|---|
| 广告**跑不动**（花不出钱、拿不到曝光） | ✅ 适用——改主图常能解除 |
| 广告**跑得动但不点击**（本案例） | ✅ 同样适用——改主图是首要动作 |
| 广告**跑得动、有点击、没转化** | ❌ 不适用——问题在详情页与价格 |

**本案例的额外观察**：改主图这个动作，在 SOP 里被同时用于两个目的——**解除广告 bug** 和 **提升点击率**。这说明主图在这套方法论里的权重极高：**它既是流量入口，也是技术层面的"触发开关"**。

---

## 八、验证方法

改完之后必须有验证，否则不知道改动是否有效。

| 验证项 | 方法 | 观察周期 |
|---|---|---|
| CTR 是否提升 | 改主图后对比同期 CTR | **7 天**（SOP 的测试区间） |
| 曝光是否变化 | 确认曝光量未因改动而下降 | 7 天 |
| 转化率是否保持 | 确认 2,1% 未下滑（防止点击来的流量变差） | 7 天 |
| 广告是否能正常花费 | 确认预算消耗正常 | 3 天 |

**对照原则**：**一次只改一个变量**。本案例同时改了主图和标题，如果 CTR 提升，无法确定是哪个起的作用。

> ⚠️ **这是一个已知的方法论瑕疵**，也是本案例的诚实说明：为了压缩案例篇幅，这里把主图和标题一起改了。
> **实操中应该分两步**：先改主图（7 天）→ 有提升就停手；无提升再加标题优化（再 7 天）。这样每一步的效果都可归因。
> 这个原则和 SOP 里"广告模型要跑 7 天测试区间"是同一个逻辑——**改动需要测试区间，不能同时动多个变量**。

---

## 九、优化建议

| # | 建议 | 依据 |
|---|---|---|
| 1 | **本次实操应分两步**：先改主图 → 观察 7 天 → 再决定是否改标题 | 同时改两个变量无法归因 |
| 2 | 主图的冰饮道具要**真实拍摄或真实合成**，不要画一个 | 画出来的冰饮会削弱可信度 |
| 3 | 若 7 天后 CTR 仍未达 3%，考虑 **B 方案**：把保温包放进真实使用场景（外卖骑手背着） | 白底主图在箱包类目同质化严重，场景化主图是另一条路 |
| 4 | 补一个**打开状态的对照主图做 A/B 测试** | 验证"露出内衬"是否是提升点击的关键 |
| 5 | 详情页保持不动，但要**记录改动前的时间点** | 便于日后回溯是哪次改动带来了提升 |
| 6 | 若 CTR 提升但转化率下滑，说明新主图吸引错了人 | 需要重新校准卖点表达 |

---

## 十、这个案例证明了什么

| 结论 | 证据 |
|---|---|
| **诊断需要基准线** | 没有 SOP 的「CTR 3–5%」基准，1,4% 这个数字没有任何意义 |
| **指标组合能定位环节** | CTR 低但转化/加购达标 → 问题在点击环节，不在产品与价格 |
| **iterate 的核心是"不改什么"** | 明确列出详情页/价格/视频/SKU 四项不动，避免改坏没问题的环节 |
| **`mode = iterate` 输出的是最小改动集** | 主图改 3 处、标题改 2 个词，其余全部保留 |
| **改动必须可归因** | 同时改两个变量的做法被明确标注为瑕疵，并给出分步方案 |
| **禁用词会反向约束视觉** | `100% Impermeável` 被禁 → 主图负面词必须加 `water puddle, wet fabric` |
| **同一动作服务两个目的** | 改主图既提升 CTR，也是 SOP 里解除广告 bug 的手段 |

---

**关联案例**：[案例 01 · Patinete Elétrico 端到端](../01_Patinete_Eletrico_500W/) · [Power Bank](../../Agents/03_Listing_Creative_Agent/examples/powerbank_20000mah.md) · [Pet Carrier](../../Agents/04_Product_Image_Agent/examples/pet_carrier.md) · [Air Fryer](../../Agents/05_Product_Video_Agent/examples/air_fryer.md)

**相关文档**：[架构拆解](../../docs/00_Architecture_SOP_to_Agent.md) · [06 Advertising Agent](../../Agents/06_Advertising_Optimization_Agent/)（Phase 2） · [自检清单](../../docs/04_Result_Checklist.md)
