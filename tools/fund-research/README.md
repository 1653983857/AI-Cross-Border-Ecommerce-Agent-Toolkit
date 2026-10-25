# 基金研究工具（美股为主，兼顾 A 股）

独立安装 FinanceToolkit 2.2.3 与 AKShare 1.19.3，不修改电商模块的依赖。
这里保存安装配置和轻量查询入口，不复制上游整个仓库，也不提交虚拟环境。

## 安装

需要 Python 3.12，建议在仓库根目录运行：

```bash
python tools/fund-research/bootstrap.py
```

脚本在本目录创建 `.venv`，安装两个上游软件包并检查导入。
以下命令在 `tools/fund-research` 目录执行；Windows 将 `.venv/bin/python` 换成 `.venv\Scripts\python.exe`。

```bash
.venv/bin/python fund_cli.py doctor
.venv/bin/python fund_cli.py us-history VOO --start 2024-01-01 --end 2025-01-01
.venv/bin/python fund_cli.py cn-history 000001
```

代码仅为接口示例，不代表推荐购买。美股命令默认明确使用 Yahoo Finance，不需要 FMP Key。
国内命令返回场外开放式基金单位净值；ETF 场内行情应使用 AKShare 对应 ETF 接口，不能混用代码。
输出为 CSV，附带数据源、获取时间、列名和包版本的 metadata.json。

## 扩展使用 FinanceToolkit

安装后可直接在该虚拟环境使用 Toolkit 的风险、绩效、ETF 资料等功能。
FMP 数据权限取决于订阅；此配置不购买套餐、不创建账户、不连接券商、不执行交易。
需要 FMP 时，将密钥放在操作系统环境变量 `FMP_API_KEY`，再使用：

```bash
.venv/bin/python fund_cli.py us-history VOO --start 2024-01-01 --end 2025-01-01 --source FinancialModelingPrep
```

脚本不会自动加载 `.env`，不要把密钥写入代码、命令参数或提交到 GitHub。
MCP 是可选的独立接入方式，本次不修改任何客户端的 MCP 配置。

## 研究口径与限制

- 第一版实现依赖安装、环境诊断和两市场历史数据导出，不声称已实现全市场自动选基或持仓穿透。
- 比较基金时先统一资产类别、日期区间、基准和币种；美国上市 ETF 与国内美股 QDII 分开评估。
- 单位净值不等于分红再投资总回报；国内单位净值不能直接与美股复权价格做收益排名。
- 风险、费率、流动性、跟踪偏离、集中度及 QDII 溢价需要分别核查，历史排名不用于承诺收益。
- 网络访问、接口变化、限流和 FMP 权限可能导致请求失败。无数据时应报错，不补造数据。
- 顶层版本固定；全部依赖的实测版本另见 `requirements-lock.txt`（以验证环境为准）。

## 上游与授权

- FinanceToolkit（MIT）：https://github.com/JerBouma/FinanceToolkit
- ETF 文档：https://www.jeroenbouma.com/projects/financetoolkit/docs/etf-information
- AKShare（MIT）：https://github.com/akfamily/akshare
- 国内基金接口：https://github.com/akfamily/akshare/blob/main/docs/data/fund/fund_public.md

上游包安装时包含其许可证。软件开源不等于数据可以无限抓取或任意再分发；数据服务条款仍适用。
