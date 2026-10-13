# 输入模板 · 图片生成简报

> **前置要求**：本模块**依赖 03 Listing Creative Agent 的输出**。
> 没跑过 03 就去跑 04，Agent 会直接报错——这是设计如此，不是 bug。

---

## 0. 任务配置

```yaml
platform*: shopee              # shopee | mercadolivre | amazon | tiktokshop | shopify
target_market*: 巴西
mode*: standard                # standard | variant | iterate
prompt_language: en            # en（通用模型）| zh（即梦/通义万相等中文模型）
has_product_photo*: true       # 是否有实拍图作为参考
```

---

## 1. 上游字段（从 03 的输出粘贴）

> ⚠️ **这五个字段为阻塞项，缺失则 Agent 拒绝执行。**

```yaml
# ── 关键：从 03 输出的「交付给下游模块的字段」区块直接粘贴 ──

core_selling_point*: ""        # 例："20000mAh com saída de 45W — recarga completa em cerca de 40 minutos"

secondary_points*: []          # 例：
  # - "Display digital de bateria"
  # - "3 saídas (2× USB-A + 1× USB-C)"

spec_table*: {}                # 直接贴 03 的 spec_table

forbidden_words*: []           # 例：["iPhone", "100% Original", "À Prova de Água"]

usage_scope_confirmed*: []     # 例：
  # - "Viagem e deslocamentos diários"
  # - "Trabalho remoto / home office"
```

---

## 2. 产品与视觉信息

```yaml
product_name*: ""              # 例："Carregador Portátil"
category*: ""                  # 例："电池 / 充电类"
visual_tone_hint: ""           # 从 03 继承，例："Tecnológico e limpo — fundo claro, tons de cinza e azul"
```

### 外观描述（帮助出图更准确）

```yaml
appearance:
  color: ""                    # 例："Preto fosco com detalhes em cinza"
  material: ""                 # 例："ABS + PC com acabamento antichamas"
  shape: ""                    # 例："Retangular com cantos arredondados"
  key_features: []             # 例：["Display LED frontal", "3 portas na face superior"]
```

---

## 3. 认证声明 ★ 合规关键

```yaml
certifications: []             # ⚠️ 只填【实际持有】的认证，无则留空 []
                               # 例：["ANATEL"]  ← 只有真的拿到才填
                               # 留空 = Agent 不会生成任何认证图
```

> **这一栏留空没有任何问题，填错才是问题。** 虚构认证标志属平台高危违规。

---

## 4. 包装与保修（用于图 8 / 图 9）

```yaml
package_content*: []           # 从 03 继承，完整列出
  # - "1× Carregador Portátil 20000mAh 45W"
  # - "1× Cabo USB-C 30 cm"
  # - "（Não incluso: adaptador de tomada）"   ← 明确"不含什么"

warranty*: ""                  # 例："6 meses contra defeito de fabricação"
warranty_scope: ""             # 例："Não cobre danos por mau uso ou queda"
support_channel: ""            # 例："Atendimento pelo chat do Shopee"
```

---

## 5. 视觉参考（可选）

```yaml
reference:
  competitor_image_notes: ""   # 竞品图片的观察（不要直接搬用素材！）
  style_reference: ""          # 例："类似 Anker 官网的极简产品摄影风格"
  avoid: []                    # 例：["花哨背景", "卡通元素", "过多英文标语"]
```

> ⚠️ **不要粘贴竞品图片链接作为图生图输入**——涉及版权，且可能被判定为盗图。

---

## 6. mode 专属字段

### mode = variant

```yaml
variant_directions: []
  # 例：["主图卖点为功率", "主图卖点为容量"]
  # 留空则由 Agent 自动分配两种差异化方向
```

### mode = iterate（对应 SOP 3.6 广告没点击 → 换主图）

```yaml
existing_main_image_desc: ""   # 现有主图的画面描述
symptom: ""                    # 例："有曝光没点击，CTR 1.2%（低于 3–5% 基准）"
change_scope: "main_image_only"  # 只改主图，其余 8 张不动
```

---

## 填写自检

- [ ] 五个阻塞字段（`core_selling_point` / `secondary_points` / `spec_table` / `forbidden_words` / `usage_scope_confirmed`）已从 03 粘贴
- [ ] `certifications` 留空或只填实际持有的
- [ ] `package_content` 包含"不含什么"
- [ ] 没有粘贴竞品图片作为图生图素材
- [ ] 我理解：**图 8（包装清单）必须实拍**，AI 生成会引发配件缺失差评
- [ ] 我理解：**图内文字由设计工具后期叠字**，不靠图像模型渲染
