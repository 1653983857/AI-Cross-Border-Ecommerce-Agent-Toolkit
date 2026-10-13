# Examples · 真实案例库

这里的案例**跨模块串联**，一个产品从头跑到尾，展示 03 → 04 → 05 的完整链路。

单模块的聚焦案例在各 Agent 目录下的 `examples/`，本目录只放**端到端**案例。

---

## 案例索引

| # | 产品 | 市场 | 覆盖模块 | 重点演示 |
|---|---|---|---|---|
| **01** | [Patinete Elétrico 500W](./01_Patinete_Eletrico_500W/)（电动滑板车） | Shopee BR + Mercado Livre | 03 → 04 → 05 | **全链路串联** · 跨平台标题压缩（120→60 字符）· 跨模块参数一致性 |
| **02** | [Bolsa Térmica](./02_Thermal_Bag/)（保温包） | Shopee BR | 03（iterate） | **iterate 模式**：广告跑不动时的回改闭环 |
| **03** | [Closed Loop](./03_Closed_Loop/)（闭环案例） | Shopee BR | 03 → 06 → 03 → 04 → 07 → 复测 | **诊断 → 回流 → 复测** 完整闭环 · 反直觉的坑 · 复测指标选择 |

---

## 前置链路（位于各模块的 examples/ 下）

01 → 02 → 03 的完整前置链路，分散在三个模块里、互相衔接：

| 环节 | 位置 | 产出 |
|---|---|---|
| **01 市场分析** | [`01/examples/patinete_eletrico_market.md`](../Agents/01_Market_Research_Agent/examples/patinete_eletrico_market.md) | 价格带 R$ 1.989–2.966 · 机会配置 200kg · 成本可行价 R$ 1.989,36 |
| **02 产品策略** | [`02/examples/patinete_eletrico_strategy.md`](../Agents/02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md) | 主卖点「500W + 200kg」· SKU 四档 · 主推价 R$ 2.199 · 盈亏线 ROAS 2,41 |
| **03–05 素材** | [`01_Patinete_Eletrico_500W/`](./01_Patinete_Eletrico_500W/) | 标题（Shopee 89 字符 / ML 54 字符）· 9 图 · 30s 视频 |

**这条链路特别值得看的地方**：两个"独立推导指向同一结果"的验证点 ——

1. 波谷检测出的价格带下界 **R$ 1.989,13** 与定价公式反算的成本可行价 **R$ 1.989,36** 相差 **R$ 0,23**
2. 主推款毛利余量 **R$ 98,95** 与拟发券面额 **R$ 100** 相差 **R$ 1,05**

> 一条是纯数学（销量曲线），一条是纯财务（成本结构）。**它们吻合，说明这套方法论内部是自洽的。**

---

## Toolkit 规划的五款案例产品覆盖情况

`AI_Cross_Border_Ecommerce_Agent_Toolkit_制作说明` 指定的五款案例产品：

| 产品 | 落在哪 | 模块 |
|---|---|---|
| **Electric Scooter** | [`01_Patinete_Eletrico_500W/`](./01_Patinete_Eletrico_500W/) + [`01/examples`](../Agents/01_Market_Research_Agent/examples/patinete_eletrico_market.md) + [`02/examples`](../Agents/02_Product_Strategy_Agent/examples/patinete_eletrico_strategy.md) + [`07/examples`](../Agents/07_Review_Analysis_Agent/examples/electric_scooter_reviews.md) | **01 + 02 + 03 + 04 + 05 + 07 全链路** |
| **Power Bank** | [`03/examples`](../Agents/03_Listing_Creative_Agent/examples/powerbank_20000mah.md) + [`06/examples`](../Agents/06_Advertising_Optimization_Agent/examples/powerbank_20000mah_ads.md) | 03 · 06 广告诊断 |
| **Pet Carrier** | [`04/examples`](../Agents/04_Product_Image_Agent/examples/pet_carrier.md) | 04 |
| **Air Fryer** | [`05/examples`](../Agents/05_Product_Video_Agent/examples/air_fryer.md) | 05 |
| **Thermal Bag** | [`02_Thermal_Bag/`](./02_Thermal_Bag/) | 03 iterate · 06 预演 |

✅ 五款全部覆盖，其中 **Electric Scooter 走完了全部 7 个模块**（01→02→03→04→05→上架→07）。

---

## 案例结构（对照制作说明的要求）

制作说明规定案例结构为：**产品背景 → 市场分析 → AI 处理流程 → 生成结果 → 优化建议**。

本仓库的案例在此基础上增加两项：

| 区块 | 来源 | 为什么要加 |
|---|---|---|
| 产品背景 | 制作说明 | — |
| 市场分析 | 制作说明 | — |
| AI 处理流程 | 制作说明 | — |
| 生成结果 | 制作说明 | — |
| **交付给下游模块的字段** | 本仓库新增 | 让案例能**真的被复现**，而不只是被阅读 |
| **这个案例证明了什么** | 本仓库新增 | 把案例的结论显式化，方便横向对比不同案例 |

---

## 提交新案例

欢迎提交！要求：

1. **必须脱敏**：无真实店铺名、账号、买家信息、未授权品牌词
2. **参数必须真实**：示例参数要能举证，不要编
3. **必须含"交付给下游模块的字段"区块**（见 [`Templates/product_brief_template.md`](../Templates/product_brief_template.md)）
4. **必须过一遍** [`docs/04_Result_Checklist.md`](../docs/04_Result_Checklist.md)
5. 如涉及图片/视频案例，**不得包含伪造的认证标志、评价截图、销量角标**

格式参考现有案例。详见 [`CONTRIBUTING.md`](../CONTRIBUTING.md)。

---

**返回**：[项目首页](../README.md) · [架构拆解](../docs/00_Architecture_SOP_to_Agent.md)
