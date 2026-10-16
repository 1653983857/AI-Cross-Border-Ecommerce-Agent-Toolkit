# 9 图场景库（Shopee 序列 × 平台差异）

> 每个图位给出：**目的 / 构图 / prompt 骨架 / 平台差异**。
> 用法：按 `planning_mode` 选序列 → 逐图位套模板 → 把「产品身份锁定」字段填进
> `[PRODUCT]` → 平台差异段决定叠字与背景。
>
> prompt 里的占比、颜色、留白**必须数字化**（见 SKILL.md 七条铁律）。

---

## 通用 Prompt 骨架（五槽位）

```text
[PRODUCT 身份块]
{product_type}, {shape}, body color {hex}, {materials},
logo/text "{logo_text}" rendered exactly as in reference image,
{ports_layout}

[场景与构图]
{scene}, {camera_angle}, product occupies {n}% of frame,
{margin} even margin on all sides

[光影]
{lighting}, soft shadows, accurate colors, sRGB

[平台技术参数]
square 1:1, {min_px}px or larger, clean {background_type} background

[否定清单]
no text overlay (except {allowed_text}), no watermark, no border, no collage,
no extra objects, keep {must_not_change} unchanged
```

---

## 图位 1 · 首图 / 白底正面图

| 项 | 内容 |
|---|---|
| 目的 | 搜索结果里的点击率 —— 决定生死的唯一一张 |
| 构图 | 正面平视，商品占 **Shopee 70–85% / ML 85–95%**，居中 |
| 骨架 | `studio packshot of [PRODUCT], front view, on {bg}, soft studio lighting` |
| **Shopee** | 白底 + **PT-BR 叠字**（主标语 ≤4 词，总文字 ≤画面 20%，右上留 12% 给角标） |
| **ML** | 背景**干净即可**（白/纯色/实景按类目），❌ 禁一切无关文字 |
| Amazon | 纯白 `#FFFFFF`，零文字 |

**Shopee BR 叠字模板**：

```text
top banner text "{主标语 ≤4 词}" in bold {color} PT-BR typography,
occupying less than 20% of the image area, never covering the product
```

---

## 图位 2 · 多角度

| 项 | 内容 |
|---|---|
| 目的 | 让买家确认形态 —— 降低"到手不符"退货 |
| 构图 | 侧面 / 背面 / 45°，与首图**同光影同背景** |
| 骨架 | `[PRODUCT], {angle} view, same studio setup as packshot` |
| 差异 | 三平台一致，白底 |

> ⚠️ 一致性关键：**光照方向、色温、背景色必须与首图完全相同**，否则像拼凑的。

---

## 图位 3 · 材质 / 细节特写

| 项 | 内容 |
|---|---|
| 目的 | 证明品质感 —— 支撑价格 |
| 构图 | 微距，对焦在 {材质关键点}（接口 / 织纹 / 涂层） |
| 骨架 | `extreme close-up macro of [PRODUCT] {detail_point}, shallow depth of field` |
| 差异 | 三平台一致；Shopee 可叠一个卖点词 |

---

## 图位 4 · 场景 / 生活图

| 项 | 内容 |
|---|---|
| 目的 | 帮买家想象拥有后的样子 |
| 构图 | 商品在真实使用环境，占比 55–70%，环境为次要 |
| 骨架 | `[PRODUCT] placed on {scene}, contextual photography, natural lighting` |
| **ML** | ✅ **Fashion/Home/Sports 类目这张可以直接当首图**（新规允许实景） |
| Shopee | ✅ 辅图位 |

> 场景要**可信**：透视、比例、接触阴影、反射都要对 —— 沙发不能飘在房间里。

---

## 图位 5 · 尺寸对照 ⭐ 差评预防位

| 项 | 内容 |
|---|---|
| 目的 | 防尺寸误解 —— 尺寸类差评的特效药 |
| 构图 | 商品 + 参照物（手 / 硬币 / A4 纸）或白底标注尺寸线 |
| 骨架 | `[PRODUCT] with size annotation, {reference_object} for scale, clean background` |
| 文字 | ✅ 标数字（`19cm` / `20000mAh`），**用 cm 不用 inch**（巴西公制） |
| 差异 | Shopee ✅ / ML ✅（辅图允许标注） |

---

## 图位 6 · 卖点信息图

| 项 | 内容 |
|---|---|
| 目的 | 把 03 Agent 的 `secondary_points[]` 变成视觉 |
| 构图 | 商品一侧 + 卖点图标列表（最多 3 条） |
| 骨架 | `infographic style, [PRODUCT] on one side, {n} benefit callouts with icons on the other` |
| 文字 | ✅ 每条卖点 ≤7 词 PT-BR（例：`Carrega 3 aparelhos ao mesmo tempo`） |
| 差异 | Shopee ✅ / ML ✅（辅图） |

---

## 图位 7 · 变体 / SKU 换色

| 项 | 内容 |
|---|---|
| 目的 | 一图展示全部变体，引导进变体链接 |
| 构图 | 主变体大图 + 变体色块行 |
| 骨架 | `[PRODUCT] in {color_1} as main, smaller thumbnails showing {color_2}, {color_3}` |
| 注意 | **换色只换颜色，形状/Logo/接口位置一个都不能动**（身份锁定的 `must_not_change`） |
| ML | 多色用 variation 功能分开建链接，图上不写"有其他颜色" |

---

## 图位 8 · 包装清单 ⭐ 差评预防位

| 项 | 内容 |
|---|---|
| 目的 | 防"以为含数据线"类误解（07 模块案例：误解型差评占比 38.5%） |
| 构图 | 平铺图：盒内所有物品摆开，含什么拍什么 |
| 骨架 | `flat lay of package contents: [PRODUCT], {included_items}, on neutral background` |
| 文字 | ✅ **必须标 `Não incluso`**（不含项）—— 这一条直接砍掉配件类差评 |
| 差异 | Shopee ✅ / ML ✅ |

---

## 图位 9 · 信任状

| 项 | 内容 |
|---|---|
| 目的 | 打消最后顾虑（质保 / 认证 / 开箱） |
| 构图 | 质保标签 / ANATEL 认证 / 开箱过程 |
| 骨架 | `[PRODUCT] with warranty badge "{text}", trust signal composition` |
| 文字 | ✅ `1 ano de garantia` / `ANATEL homologado` |
| 注意 | 认证标识必须**真实持有**，不得伪造（合规红线） |

---

## 一致性规则（Campaign Style Lock 必填字段）

整套图出图前，先填这张表，**每一条 prompt 都原样携带**：

```yaml
campaign_style_lock:
  light_direction: "top-left"        # 全套统一
  color_temperature: "5200K neutral"
  background_family: "white studio"  # 或 "warm lifestyle"
  saturation: "accurate, no oversaturation"
  camera_height: "eye-level"
  must_not_change:
    - "screen digits"
    - "logo position"
    - "port count"
```

**一个字都不能变** —— 买家滑动 9 张图时，风格跳来跳去像盗图。
