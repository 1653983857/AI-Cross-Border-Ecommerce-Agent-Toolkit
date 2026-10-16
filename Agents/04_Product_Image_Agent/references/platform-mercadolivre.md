# Mercado Livre · 商品图规则卡（2026 新规版）

> 来源：ML 官方卖家中心（cbt.mercadolibre.com/pictures 与 global-selling 学习中心）。
> **⚠️ 规则已变**：不再要求所有类目纯白底。发布前按类目到卖家中心复核。

---

## 一、🔴 最重要的变化：背景按类目区分

官方原话：**"You can now choose between white, solid or real-life backgrounds for your
listings — depending on the category."**

| 类目 | 背景要求 |
|---|---|
| **Technology / Beauty / Health / Supermarket** | **仍要求白底**（纯白最安全） |
| **Fashion / Home / Sports / Toys / Auto / Tools / Entertainment** | **允许实景/情境背景**（商品在真实使用环境中） |

**通用底线（所有类目都适用）**：

> **背景必须干净** —— 不管白底还是实景，"Avoid messy or busy backgrounds"，
> 商品必须是照片的绝对主角。

---

## 二、硬性规格

| 项 | 要求 |
|---|---|
| 最小尺寸 | 500×500（细长商品如笔，短边 ≥250） |
| **推荐尺寸** | **1200×1200**（支持缩放） |
| 最大尺寸 | 1920×1920 |
| 比例 | **1:1 正方形**（"width and height must be the same"） |
| 格式 | JPG / PNG，**RGB 色彩空间**（不要 CMYK） |
| 文件大小 | ≤ 10 MB |
| 张数 | 无硬上限，建议 6–8 张 |

---

## 三、占比 —— 三个平台里要求最高 ⚠️

官方原话：**"the product takes up 95% of the entire image"**（商品占画面 95%，避免留白）。

| 项 | 数值 |
|---|---|
| 官方口径 | ~95% |
| 实战甜区 | **80–92%**（95% 几乎贴边，留 8% 余量更安全） |

> 对比：Amazon ≥85%、Shopee ≥60%。**ML 的占比要求最严。**

---

## 四、首图（封面）禁项 —— 比背景更容易踩坑

以下内容**任何情况下都不得出现**（官方逐条列出）：

| 禁项 | 说明 |
|---|---|
| ❌ 平台属性词 | `Mais vendido`(Bestseller)、`Full`、`MercadoLíder`、`Oferta relâmpago` |
| ❌ 水印 | 半透明 logo/文字/签名 |
| ❌ 边框 | 任何装饰边框 |
| ❌ 非产品自身的 Logo | 卖家店铺 logo、供应商 logo |
| ❌ 促销横幅 | 大促角标、倒计时 |
| ❌ 多品拼图 | "different colors and models" 这类说明 |
| ❌ 二维码 / 联系方式 / 社媒链接 | — |
| ❌ 非产品文字 | 与产品无关的任何文字 |

**只有从第二张图起**，才可以：多角度、使用场景、包装展示。

---

## 五、文字规则小结（对照 Shopee）

| 位置 | Shopee BR | Mercado Livre |
|---|---|---|
| 首图 | ✅ 推荐叠字（≤画面 20%） | ❌ 禁无关文字 |
| 辅图 | ✅ 推荐 | ✅ 卖点标注可用（非平台属性词） |

**结论：Shopee 和 ML 的一套图不可复用，首图必须分开做。**

---

## 六、像素校验参数（对应 scripts/check_main_image.py）

```bash
python scripts/check_main_image.py 图.png --platform mercadolivre
```

| 检查 | 阈值 | 依据 |
|---|---|---|
| 最小尺寸 | ≥ 500px，**<1200 警告** | 官方最低 / 推荐值 |
| 正方形 | 宽高比 1:1（±1%） | "width and height must be the same" |
| 主体占比 | ≥ 80%，**推荐 85–95%** | 官方 ~95% 口径 |
| 背景均匀度 | 边缘带主色占比 ≥ 90%（**信息项**） | 实景背景允许非均匀，仅提示"可能杂乱" |
| 文件大小 | ≤ 10 MB | 官方上限 |

> 与 Amazon 的差异：ML **不强制**背景近白 —— 校验脚本对 ML 只测「背景是否均匀干净」，
> 不测「是否纯白」。若你的类目属于 Technology/Beauty/Health/Supermarket，请按
> `--platform amazon` 的白底标准再过一遍。
