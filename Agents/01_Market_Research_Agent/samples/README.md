# samples · 样本数据

> ⚠️ **全部为合成数据**，用于验证脚本环境与演示格式清洗能力，**不代表任何真实市场**。
> 由 [`scripts/make_sample.py`](../scripts/make_sample.py) 生成（`random.seed(20261013)`，可复现）。

---

## 文件

| 文件 | 说明 |
|---|---|
| `sample_patinete_eletrico.csv` | 原始导出表（50 行），**刻意混入了各种脏数据格式** |
| `sample_patinete_eletrico.normalized.json` | `shaduola_parser.py` 的输出 |
| `sample_patinete_eletrico.metrics.md` | `market_metrics.py` 的报告（给人看） |
| `sample_patinete_eletrico.metrics.json` | 同上（给机器看） |

---

## 为什么样本要"脏"

真实的类目导出表不会干干净净。这个样本刻意混入了以下格式，用来验证清洗逻辑：

| 脏数据形式 | 出现位置 | 期望处理 |
|---|---|---|
| `R$ 2.199,90` | 价格 | 欧式千分位+小数 → `2199.9` |
| `R$ 2,199.90` | 价格 | 美式格式 → `2199.9` |
| `1.234` | 销量 | 点作千分位 → `1234` |
| `4个月` / `2025-06-15` / `420天` / `420` | 上架时间 | 统一为天数 |
| 空字符串 | 月销售额（25% 的行） | 用 `价格 × 月销量` 补算 |

跑完后 `meta.row_count_kept` 应该等于 `row_count_raw`（50 = 50），说明没有行被误丢。

---

## 复现方式

```bash
cd ../scripts
python make_sample.py                    # 重新生成 CSV（结果与仓库内一致）
python shaduola_parser.py ../samples/sample_patinete_eletrico.csv
python market_metrics.py ../samples/sample_patinete_eletrico.normalized.json \
    --bins 10 --config-fields "功率,承重"
```

---

## 跑通后你应该看到的关键结果

| 指标 | 值 | 说明 |
|---|---|---|
| 样本商品数 | 50 | — |
| 品牌数 | 6 | 只有 6 个 → **触发 CR10 无意义提示**，应改用 CR3 |
| 品牌 CR3 | 74.1% | 集中度偏高（合成数据里头部品牌商品数多） |
| 卖家数 | 34 | CR10 = 71.5% |
| 价格范围 | R$ 1,500.59 – 3,129.06 | 箱宽 R$ 162.85 |
| **检测到的波谷** | **2 个**（R$ 1,989.13 / R$ 2,966.21） | 落在箱 3 与箱 9 |
| **建议价格带** | **3 个** | 对应 SOP 1.4 的"从波谷到波谷划分" |
| 配置维度 | 功率 3 个取值 / 承重 3 个取值 | 500W 与 150kg 为主流（各 30 件，60%） |

> **如果波谷数不是 2 个**，说明你的 Python 环境或参数与本文档不一致——检查是否用了 `--bins 10`、`--valley-min-drop 0.15`。

---

**返回**：[scripts 说明](../scripts/README.md) · [01 模块说明](../README.md)
