# 整合来源与纠偏

五个完整上游项目以 Git submodule 固定提交加入仓库 external/investment/；`.gitmodules` 和 sources.lock.json 可追溯。安装包只内置选定文本参考快照，使用 library.py 按需查询；不是把所有上游技能分别注册。附属文件不在快照时必须从锁定提交获取。上游 API 密钥、订阅、真实账户与平台能力不因收录源码而自动具备。

| 来源 | 内部作用 | 整合方式与修正 |
|---|---|---|
| taxueseek/taxue-invest | 国内基金研究、选基、资产配置、数据源路线 | 保留原文作参考；不继承通用基金规模阈值、固定仓位与回撤保证、A/C简单口号；实际金额由独立引擎算 |
| yennanliu/InvestSkill | ETF尽调、组合检查、压力测试、论点跟踪、事实核验 | 不把买卖评分当胜率；不使用模型训练记忆产生实时风险数值；VaR不是最大损失或压力损失的保证下界 |
| tradermonty/claude-trading-skills | 风险预算、仓位、纪律、日志、复盘、回测检查 | 股票止损与Kelly不直接用于场外基金；历史胜率未经校准不能作为仓位依据 |
| anthropics/financial-services | 研究来源、估值敏感性、投资论点、客户配置流程 | 作为资料，未部署Claude代理、不配置其连接器或商业数据账号；个股DCF不直接套基金 |
| PyPortfolio/PyPortfolioOpt | 同币种风险估计与HRP对照 | 真实运行风险模型与HRP；最终成本/约束/金额由CVXPY统一求解并独立复核 |

本技能原创指令与计算代码采用仓库MIT许可；第三方原文保留各自许可。`THIRD_PARTY_NOTICES.md` 和离线压缩包中的原LICENSE必须一起分发。taxue-invest采用Prosperity Public License 3.0.0，包含非商业/商业试用限制，不被本仓库MIT许可证覆盖；正式商业使用必须按原许可处理或单独取得授权，不能把它宣传为无限制开源。

这些来源提供方法与软件；无一因收录就成为已验证投资优势。来源固定时间为2026-10-29，实时产品政策、行情与费率必须每次另行核验。
