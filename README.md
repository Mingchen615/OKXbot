# Alpha Trading Bot OKX

基于模块化架构的OKX加密货币交易机器人，支持AI驱动的自动化交易策略。

## 特性

### 🚀 核心架构
- **模块化架构** - 清晰的子包结构，易于维护和扩展
- **异步处理** - 所有网络请求异步执行，提升性能
- **插件化设计** - 策略、AI提供商可插拔扩展
- **配置灵活** - 丰富的配置选项，支持多种交易场景

### 🤖 AI信号增强
- **多AI提供商支持** - Kimi、DeepSeek、Qwen、OpenAI、Gemini、MiniMax、MiMo
- **AI信号融合** - 共识/多数表决/置信度优先/加权平均策略
- **智能缓存** - AI信号缓存15分钟，避免重复调用
- **回退机制** - AI服务失败时自动切换备用提供商
- **置信度评估** - 基于历史表现的AI可靠性评分
- **趋势分析集成** - 多时间框架趋势分析，避免逆势信号
  - 基于10/20/50周期计算趋势方向和强度
  - 趋势强度>0.6时强制顺势交易，避免下跌趋势中持续BUY
- **BUY信号专项优化器** - 基于2025-12-25交易损失分析
  - **多因子风险检测**：价格位置(>85%)、RSI(>65)、ATR(<0.2%)、趋势强度
  - **累积风险控制**：3个及以上风险因素强制转HOLD
  - **信号增强机制**：低位+超卖+强趋势+成交量放大增强BUY信号
  - **提供商特定优化**：针对qwen、deepseek等不同提供商的历史表现优化
  - **详细日志追踪**：完整记录优化决策过程，便于分析和调试

### 📊 智能交易策略
- **三级别投资策略** - 保守型(30%-70%)、中等型(25%-75%)、激进型(15%-85%)
- **多时间框架分析** - 15分钟、1小时、4小时周期
- **横盘检测保护** - 多维度识别横盘，自动暂停交易
- **动态参数调整** - 基于市场条件自动优化策略参数
- **信号优先级排序** - 多信号冲突时的智能排序

### 🛡️ 完善风控体系
- **三级风险控制** - 当日亏损、连续亏损、仓位风险
- **智能止盈止损系统** - 支持普通模式和智能模式
  - **普通模式**：固定百分比，设置后不变
  - **智能模式**：动态调整，支持固定和多级两种子模式
- **追踪止损** - 基于入场价的动态止损，价格反向波动时锁定利润（只升不降逻辑）
- **多级止盈** - 支持2-3级止盈，不同投资类型差异化配置
- **暴跌保护** - 多时间框架暴跌检测(1.5%-3.5%阈值)
- **仓位精确控制** - 基于余额的动态仓位计算，保留5%缓冲
- **紧急停止** - 一键清仓，取消所有订单

### 💡 高级交易功能
- **智能订单执行** - 市价/限价单，支持部分成交处理
- **动态余额使用** - 自动计算最优交易量，使用全部可用余额
- **做空控制** - 可禁用做空功能，只做多交易
- **加仓管理** - 支持金字塔式加仓策略
- **反向开仓** - 信号方向改变时自动反向开仓

### 📈 实时监控分析
- **AlphaPulse实时监控** - 全新的独立实时监控系统
  - **监控为主模式**: buy/sell 信号触发主流程，hold/None 持续监控
  - **独立运行模式**: 仅运行实时监控，跳过主交易循环
  - **后备机制**: 监控异常时主流程按周期执行
  - **60秒间隔**: 持续监控市场，实时捕捉交易机会
- **仓位实时监控** - 未实现盈亏、爆仓价格监控
- **订单状态跟踪** - 活动订单实时状态更新
- **性能指标统计** - 胜率、盈亏比、最大回撤等
- **日志系统** - 按日期自动切分的智能日志管理
- **7日价格区间显示** - 在ATR数据下方显示7日价格区间（注：当前版本此功能已添加但日志显示有延迟）
- **Web监控仪表板** - 实时监控界面（端口8501）
  - 实时行情监控（BTC价格、RSI、趋势）
  - 持仓状态与盈亏
  - AI信号分布统计
  - 交易历史记录
  - 配置一览

### 🌐 网络与代理
- **代理支持** - HTTP/HTTPS代理配置，适应网络环境
- **自动重试** - 指数退避重试机制，网络异常自动恢复

### 🧪 技术特性
- **完整技术指标库** - RSI、MACD、ADX、布林带、ATR等
- **趋势分析系统** - 多时间框架趋势分析，智能识别市场方向
  - 基于价格变化率和均线位置的综合评分系统
  - 支持微涨微跌检测（0-1%价格变化）
  - 趋势强度量化（0.0-0.9）避免过度放大
- **币种特异性参数** - BTC、ETH、SHIB等不同阈值设置
- **精度智能处理** - OKX交易所0.01张精度要求适配
- **错误恢复机制** - 自动重试、降级策略、异常处理
- **价格位置因子缩放** - 基于24小时和7日价格区间的智能信号调整
  - 极低位（<15%）：信号增强30%，风险要求降低20%
  - 高位（65-75%）：信号减弱15%，风险要求提高20%
  - 极高位（>85%）：信号减弱50%，风险要求提高100%
- **低价格位置策略** - 专门捕捉35%以下价格位置的交易机会
  - 三档分级：极低位、低位、偏低，差异化策略处理
  - 增强买入信号，提高信心度最高50%，放宽买入条件
- **API稳定性增强** - 指数退避重试机制，避免信号丢失
- **动态置信度阈值** - 基于价格位置自动调整AI信号阈值
- **智能随机偏移** - 防止任务执行时间在过去的时间算法
- **多时间框架价格分析** - 24小时(70%) + 7日(30%)综合价格位置计算
- **自适应止损系统** - 基于趋势方向的动态止损百分比调整
- **动态价格位置阈值** - 基于趋势强度自动调整价格位置阈值
  - 强势趋势：极高位放宽至98%，高位至85%
  - 弱趋势：保持严格（极高位90%，高位75%）
- **突破确认机制** - 价格突破历史高点时的特殊处理
  - 0.2%突破确认 + 量能/趋势确认 = 降低价格位置权重
- **分层信号系统** - 4级买入信号（积极/强势/适度/保守）
  - 不同等级对应不同的价格位置上限和置信度要求
- **时间衰减因子** - 信号权重随时间指数衰减（4小时半衰期）
- **自学习参数优化** - 基于历史交易数据自动优化参数
  - 持续学习，自动调整最优阈值和权重
  - 生成优化报告，追踪参数表现

## 快速开始

### 安装

```bash
# 克隆项目
git clone https://github.com/Mingchen615/OKXbot.git
cd OKXbot

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 安装依赖
pip install -e .
```

### 配置

1. 复制环境变量文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的API密钥：
```
OKX_API_KEY=your_api_key
OKX_SECRET=your_secret
OKX_PASSWORD=your_password
```

### 使用

#### 命令行方式

```bash
# 启动测试模式机器人
python main.py

# 启动带Web界面的机器人
python main.py --web

# 启动自适应模式（含ML学习）
python main.py --mode adaptive --web

# 启动真实交易（谨慎使用！）
python main.py --real-trading --mode standard

# 指定Web端口
python main.py --web --port 8080
```

## 项目结构

```
alpha_trading_bot/
├── __init__.py                    # 简化API导出
├── core/                          # 核心基础模块
│   ├── __init__.py               # 核心模块初始化
│   ├── base.py                   # 基础数据结构和组件（147行）
│   ├── bot.py                    # 交易机器人主类（729行，核心机器人逻辑）
│   ├── exceptions.py             # 自定义异常（34行）
│   ├── health_check.py           # 健康检查模块（245行）
│   └── monitor.py                # 系统监控器（311行）
├── config/                        # 配置管理
│   ├── __init__.py               # 配置模块初始化（32行）
│   ├── manager.py                # 配置管理器（285行，配置加载与验证）
│   └── models.py                 # 配置数据模型（112行，所有配置定义）
├── exchange/                      # 交易所交互
│   ├── __init__.py               # 交易所模块初始化
│   ├── engine.py                 # 交易引擎（503行，核心交易逻辑）
│   ├── client.py                 # 交易所客户端（621行，OKX API封装）
│   ├── models.py                 # 订单、仓位等模型（174行，数据模型定义）
│   ├── trade_executor.py         # 交易执行器（旧版，兼容支持）
│   └── trading/                  # 交易管理子模块
│       ├── __init__.py           # 交易子模块初始化
│       ├── order_manager.py      # 订单管理器（380行，订单全生命周期管理）
│       ├── position_manager.py   # 仓位管理器（192行，仓位监控与操作）
│       ├── risk_manager.py       # 风险管理器（444行，三级风控体系）
│       └── trade_executor.py     # 新版交易执行器（825行，追踪止损实现）
├── strategies/                    # 交易策略
│   ├── __init__.py               # 策略模块初始化
│   ├── manager.py                # 策略管理器（1044行，核心策略逻辑）
│   ├── consolidation.py          # 横盘检测策略（472行，多维度横盘识别）
│   └── low_price_strategy.py     # 低价格位置策略（192行，35%以下专项策略）
├── ai/                            # AI信号生成
│   ├── __init__.py               # AI模块初始化（39行）
│   ├── cache/                    # AI缓存模块
│   │   └── __init__.py           # 缓存模块初始化（0行，占位模块）
│   ├── providers/                # AI提供商实现
│   │   ├── __init__.py           # 提供商模块初始化（16行）
│   │   ├── base.py               # 基础提供商类（76行，提供商基类）
│   │   ├── deepseek.py           # DeepSeek提供商（105行）
│   │   ├── kimi.py               # Kimi提供商（105行）
│   │   ├── openai.py             # OpenAI提供商（105行）
│   │   └── qwen.py               # Qwen提供商（105行）
│   ├── client.py                 # AI客户端（611行，AI服务封装+API重试机制）
│   ├── fusion.py                 # AI融合决策（408行，多AI信号融合）
│   ├── manager.py                # AI管理器（760行，AI服务管理+价格位置缩放）
│   ├── model_selector.py         # AI模型选择器（223行，模型选择逻辑）
│   ├── signals.py                # AI信号生成器（455行，信号转换处理）
│   ├── price_position_scaler.py  # 价格位置缩放器（价格位置因子调整）
│   ├── signal_optimizer.py       # 信号优化器（通用信号优化）
│   ├── buy_signal_optimizer.py   # BUY信号专项优化器（多因子风险检测）
│   ├── dynamic_cache.py          # 动态缓存管理器（AI缓存优化）
│   ├── cache_monitor.py          # 缓存性能监控器（命中率统计）
│   ├── dynamic_signal_tier.py    # 动态分层信号系统（4级买入信号）
│   ├── self_learning_optimizer.py # 自学习参数优化器（自动优化参数）
│   └── fusion/                   # AI融合策略模块
│       ├── __init__.py           # 融合策略初始化
│       └── strategies.py         # 融合策略实现（共识/加权/多数表决）
├── utils/                         # 工具模块
│   ├── __init__.py               # 工具模块初始化（16行）
│   ├── cache.py                  # 缓存管理（125行，内存缓存实现）
│   ├── crash_detector.py         # 暴跌检测器（323行，多时间框架检测）
│   ├── data_validation.py        # 数据验证模块（0行，占位模块）
│   ├── error_recovery.py         # 错误恢复模块（0行，占位模块）
│   ├── logging.py                # 日志工具（274行，日志配置与工具）
│   ├── monitoring.py             # 系统监控模块（0行，占位模块）
│   ├── smart_logger.py           # 智能日志管理器（146行，按日期切分日志）
│   ├── system_utils.py           # 系统工具模块（0行，占位模块）
│   ├── technical.py              # 技术指标库（511行，全套技术指标+趋势分析）
│   └── time_helper.py            # 时间助手模块（0行，占位模块）
├── data/                          # 数据管理
│   ├── __init__.py               # 数据模块初始化（20行）
│   ├── database.py               # 数据库管理（505行，数据存储与查询）
│   ├── manager.py                # 数据管理器（452行，数据业务逻辑）
│   └── models.py                 # 数据模型（248行，数据结构定义）
├── api/                           # 对外API
│   ├── __init__.py               # API模块初始化（26行）
│   ├── bot_api.py                # 机器人管理API（181行，RESTful API）
│   └── client.py                 # API客户端（121行，API调用封装）
└── cli/                           # 命令行接口
    ├── __init__.py               # CLI模块初始化（6行）
    └── main.py                   # CLI主程序（144行，命令行入口）
```

## 项目规模

- **总代码行数**: 约15,200行Python代码
- **核心模块**:
  - 交易执行: 825行（新版追踪止损实现）
  - 策略管理: 1,236行（核心策略逻辑 + 低价格位置策略）
  - AI系统: 2,900+行（多AI集成与融合 + 价格位置缩放 + BUY信号优化器）
  - 风险管理: 444行（三级风控体系）
- **模块数量**: 8大模块，67+子模块
- **功能覆盖**: 从信号生成到交易执行完整链路 + 价格位置智能分析 + 自学习优化
- **代码质量**: 模块化设计，高内聚低耦合
- **新增特性**: 7日价格分析、价格位置因子缩放、低价格位置策略、API重试机制、动态分层信号、自学习优化

## 配置说明

### 📊 基础交易配置
- `TEST_MODE`: 测试模式（默认：true）
- `MAX_POSITION_SIZE`: 最大仓位大小（默认0.01张）
- `MIN_TRADE_AMOUNT`: 最小交易量（默认0.01张，符合OKX要求）
- `LEVERAGE`: 杠杆倍数（默认10倍）
- `CYCLE_MINUTES`: 交易周期（默认15分钟）
- `RANDOM_OFFSET_ENABLED`: 是否启用随机时间偏移（默认true，用于规避风控检测）
- `RANDOM_OFFSET_RANGE`: 随机偏移范围（默认180秒=±3分钟）
- `MARGIN_MODE`: 保证金模式（cross全仓/isolated逐仓）
- `POSITION_MODE`: 持仓模式（one_way单向/hedge双向）
- `ALLOW_SHORT_SELLING`: 是否允许做空（默认false，只做多）
- `REAL_TRADING_CONFIRMED`: 实盘确认开关（默认false，实盘必须为true）
- `RUNTIME_ENVIRONMENT`: 运行环境（dev/test/staging/prod，实盘仅允许 prod/production）

### 🎯 策略配置
- `INVESTMENT_TYPE`: 投资策略（conservative稳健型/moderate中等型/aggressive激进型）
- `PROFIT_LOCK_ENABLED`: 利润锁定功能（默认开启）
- `SELL_SIGNAL_ENABLED`: 卖出信号开关（默认开启）
- `BUY_SIGNAL_ENABLED`: 买入信号开关（默认开启）
- `CONSOLIDATION_PROTECTION_ENABLED`: 横盘保护（默认开启）
- `SMART_TP_SL_ENABLED`: 智能止盈止损（默认开启）
- `LIMIT_ORDER_ENABLED`: 限价单功能（默认开启）
- `PRICE_CRASH_PROTECTION_ENABLED`: 暴跌保护（默认开启）
- ~~`TAKE_PROFIT_PERCENT`: 止盈百分比（默认6%）~~ *(已废弃，使用新的止盈止损配置)*
- ~~`STOP_LOSS_PERCENT`: 止损百分比（默认2%）~~ *(已废弃，使用新的止盈止损配置)*

### 🛡️ 风险控制配置
- `MAX_DAILY_LOSS`: 最大日亏损（默认100 USDT）
- `MAX_POSITION_RISK`: 最大仓位风险比例（默认5%）
- **止盈止损配置**:
  - `TAKE_PROFIT_ENABLED`: 止盈总开关（默认开启）
  - `STOP_LOSS_ENABLED`: 止损总开关（默认开启）
  - `TAKE_PROFIT_MODE`: 止盈模式（normal普通/smart智能）
  - `STOP_LOSS_MODE`: 止损模式（normal普通/smart智能）
- **普通模式配置**（固定百分比，设置后不变）:
  - `{INVESTMENT_TYPE}_NORMAL_TP_PERCENT`: 止盈百分比（如CONSERVATIVE_NORMAL_TP_PERCENT=6）
  - `{INVESTMENT_TYPE}_NORMAL_SL_PERCENT`: 止损百分比（如CONSERVATIVE_NORMAL_SL_PERCENT=2）
- **智能模式-固定模式配置**（动态调整）:
  - `{INVESTMENT_TYPE}_SMART_FIXED_TP_PERCENT`: 智能固定止盈百分比
  - `{INVESTMENT_TYPE}_SMART_FIXED_SL_PERCENT`: 智能固定止损百分比
- **智能模式-多级模式配置**（多个止盈订单，动态调整）:
  - `{INVESTMENT_TYPE}_SMART_MULTI_TP_LEVELS`: 多级止盈级别（如2,5,8）
  - `{INVESTMENT_TYPE}_SMART_MULTI_TP_RATIOS`: 各级平仓比例（如0.6,0.3,0.1）
- `TRAILING_STOP_ENABLED`: 追踪止损开关（默认开启）
- `TRAILING_DISTANCE`: 追踪距离（默认1.5%）
- `TRAILING_STOP_LOSS_ENABLED`: 追踪止损功能（默认开启）
- `TRAILING_STOP_LOSS_MODE`: 追踪模式（entry_based基于入场价）
- `MAX_CONSECUTIVE_LOSSES`: 最大连续亏损次数（默认3次）

### 🤖 AI配置
- `AI_MODE`: AI决策模式（single单AI/fusion融合）
- `AI_DEFAULT_PROVIDER`: 默认AI提供商（kimi/deepseek/qwen/openai/gemini/minimax/mimo）
- `AI_MIN_CONFIDENCE`: 最小置信度阈值（默认30%）
- `AI_FUSION_PROVIDERS`: AI融合提供商列表（支持 deepseek/kimi/openai/qwen/gemini/minimax/mimo）
- `AI_FUSION_WEIGHTS`: AI融合权重（建议按 provider 列表配置并保证归一化，如 `deepseek:0.4,kimi:0.3,mimo:0.3`）
- `AI_FUSION_STRATEGY`: AI融合策略（consensus/weighted/majority/confidence）
- `AI_FUSION_THRESHOLD`: AI融合阈值（默认60%）
- `AI_CACHE_DURATION`: AI信号缓存时间（默认900秒）
- `AI_TIMEOUT`: AI请求超时时间（默认30秒）
- `AI_MAX_RETRIES`: AI最大重试次数（默认2次）
- `USE_MULTI_AI_FUSION`: 是否使用多AI融合（默认开启）
- `FALLBACK_ENABLED`: 回退机制开关（默认开启）
- `ENABLE_SIGNAL_OPTIMIZATION`: 信号优化开关（默认开启）
- `ENABLE_BUY_OPTIMIZER`: BUY信号优化器开关（默认开启）
- `BUY_MAX_PRICE_POSITION`: BUY信号最大价格位置（默认85%）
- `BUY_COOLDOWN_MINUTES`: BUY信号冷却时间（默认30分钟）
- `ENABLE_DYNAMIC_MODEL_SELECTION`: 动态模型选择开关（默认开启）
- `ENABLE_DYNAMIC_CACHE`: 动态缓存开关（默认开启）
- `PRICE_POSITION_SCALING_ENABLED`: 价格位置因子缩放开关（默认开启）
- `LOW_PRICE_STRATEGY_ENABLED`: 低价格位置策略开关（默认开启）
- `LOW_PRICE_THRESHOLD`: 低价格位置阈值（默认35%）
- `EXTREME_LOW_THRESHOLD`: 极低位阈值（默认15%）
- `BUY_MAX_RSI`: BUY信号最大RSI值（默认65）
- `BUY_MIN_ATR`: BUY信号最小ATR百分比（默认0.15%）

### Gemini 配置示例

```bash
# 单AI使用 Gemini
AI_MODE=single
AI_DEFAULT_PROVIDER=gemini
GEMINI_API_KEY=your_gemini_api_key

# 多AI融合包含 Gemini
AI_MODE=fusion
AI_FUSION_PROVIDERS=deepseek,kimi,gemini
AI_FUSION_WEIGHTS=deepseek:0.4,kimi:0.3,gemini:0.3
AI_FUSION_STRATEGY=weighted
```

> 说明：系统同时支持 `GEMINI_API_KEY` 与 `GOOGLE_API_KEY`，若二者同时存在，优先使用 `GOOGLE_API_KEY`。

### Gemini 灰度发布与回滚（shadow/小流量/全量）

#### 分阶段发布策略

1. **Shadow 阶段（仅观测）**
   - `AI_MODE=fusion`
   - `AI_FUSION_PROVIDERS=deepseek,kimi,gemini`
   - `AI_FUSION_WEIGHTS=deepseek:0.45,kimi:0.45,gemini:0.10`
   - 观测项：Gemini 成功率、429/5xx 比例、fallback 触发率。

2. **小流量阶段（10%~30%）**
   - 按 0.10 → 0.20 → 0.30 逐步提高 Gemini 权重，每个阶段至少观测 24h。
   - 推荐门槛：请求成功率 >= 99%，429/5xx <= 1%。

3. **全量阶段（目标权重）**
   - 达到目标权重后连续观察 72h，保留配置级快速回滚路径。

#### 配置级回滚演练

- 回滚开关：`AI_DEFAULT_PROVIDER`、`AI_FUSION_PROVIDERS`、`AI_MODE`

```bash
# 紧急回滚到单AI稳定路径
AI_MODE=single
AI_DEFAULT_PROVIDER=deepseek

# 融合模式回滚（移除 Gemini）
AI_MODE=fusion
AI_FUSION_PROVIDERS=deepseek,kimi
AI_FUSION_WEIGHTS=deepseek:0.5,kimi:0.5
```

#### 上线检查清单（验收报告）

- 功能：single/fusion 均可识别 `gemini`，策略切换无签名兼容错误
- 性能：Gemini 超时/重试行为符合预期，交易周期无明显恶化
- 稳定性：fallback 可用，主链路失败时可降级到稳定 provider 或 HOLD
- 安全：密钥扫描门禁启用，SBOM 与签名验证步骤执行，可追溯回滚

### 密钥轮换与泄漏处置

- 轮换流程文档：`markdown/SECURITY_KEY_ROTATION_RUNBOOK.md`
- 关键要求：
  - 发现泄漏后立即吊销旧 key 并切换新 key
  - 必要时通过 `AI_MODE` / `AI_DEFAULT_PROVIDER` / `AI_FUSION_PROVIDERS` 快速回滚
  - 轮换记录必须包含时间线与影响范围

### 🌐 网络与代理配置
- `HTTP_PROXY`: HTTP代理地址（如 http://127.0.0.1:7890）
- `HTTPS_PROXY`: HTTPS代理地址（如 http://127.0.0.1:7890）
- `TIMEOUT`: 网络超时时间（默认30秒）
- `MAX_RETRIES`: 最大重试次数（默认3次）
- `RETRY_DELAY`: 重试延迟（默认1秒）

### 🖥️ Web界面配置
- `WEB_INTERFACE_ENABLED`: Web界面开关（默认关闭）
- `WEB_PORT`: Web服务端口（默认8501）

### 💰 止盈止损配置示例

#### 基础配置
```bash
# 启用止盈止损
TAKE_PROFIT_ENABLED=true
STOP_LOSS_ENABLED=true

# 选择模式（normal普通/smart智能）
TAKE_PROFIT_MODE=smart
STOP_LOSS_MODE=smart
```

#### 普通模式（固定值）
```bash
# 保守型配置（适合风险厌恶者）
CONSERVATIVE_NORMAL_TP_PERCENT=6    # 6%止盈
CONSERVATIVE_NORMAL_SL_PERCENT=2    # 2%止损
# 支持小数，如1.5%止损：CONSERVATIVE_NORMAL_SL_PERCENT=1.5

# 中等型配置（平衡型投资者）
MODERATE_NORMAL_TP_PERCENT=8        # 8%止盈
MODERATE_NORMAL_SL_PERCENT=3        # 3%止损
# 支持小数，如2.75%止损：MODERATE_NORMAL_SL_PERCENT=2.75

# 激进型配置（风险偏好者）
AGGRESSIVE_NORMAL_TP_PERCENT=12     # 12%止盈
AGGRESSIVE_NORMAL_SL_PERCENT=5      # 5%止损
# 支持小数，如4.5%止损：AGGRESSIVE_NORMAL_SL_PERCENT=4.5
```

#### 智能模式-固定模式（动态调整）
```bash
# 智能固定模式配置
CONSERVATIVE_SMART_FIXED_TP_PERCENT=6   # 6%止盈，动态调整
CONSERVATIVE_SMART_FIXED_SL_PERCENT=2   # 2%止损，追踪止损
```

#### 智能模式-多级模式（分批止盈）
```bash
# 多级止盈配置（保守型：快速锁定利润）
CONSERVATIVE_SMART_MULTI_TP_LEVELS=2,5,8        # 2%、5%、8%三级别
CONSERVATIVE_SMART_MULTI_TP_RATIOS=0.6,0.3,0.1  # 60%、30%、10%分批平仓
# 支持小数级别，如1.5%、3.75%、7.25%：CONSERVATIVE_SMART_MULTI_TP_LEVELS=1.5,3.75,7.25

# 多级止盈配置（激进型：追求更高收益）
AGGRESSIVE_SMART_MULTI_TP_LEVELS=5,10,15        # 5%、10%、15%三级别
AGGRESSIVE_SMART_MULTI_TP_RATIOS=0.2,0.3,0.5    # 20%、30%、50%分批平仓
# 支持小数级别，如4.5%、9.25%、14.75%：AGGRESSIVE_SMART_MULTI_TP_LEVELS=4.5,9.25,14.75
```

#### 投资类型选择
```bash
# 设置投资类型（自动选择对应配置）
INVESTMENT_TYPE=conservative    # 稳健型
# INVESTMENT_TYPE=moderate      # 中等型
# INVESTMENT_TYPE=aggressive    # 激进型
```

### 🔧 系统配置
- `MAX_HISTORY_LENGTH`: 最大历史记录长度（默认100条）
- `LOG_LEVEL`: 日志级别（INFO/DEBUG/WARNING/ERROR）
- `MONITORING_ENABLED`: 监控功能开关（默认开启）
- `WEB_INTERFACE_ENABLED`: Web界面开关（默认关闭）
- `WEB_PORT`: Web服务端口（默认8501）
- `ALPHA_PULSE_ONLY_MODE`: AlphaPulse独立运行模式（默认false）
- `ALPHA_PULSE_PRIMARY_MODE`: AlphaPulse监控为主模式（默认true）

### 🎯 AlphaPulse实时监控配置
AlphaPulse是全新的实时监控系统，支持"监控为主"和"独立运行"两种模式。

#### 基础配置
```bash
# 启用AlphaPulse
ALPHA_PULSE_ENABLED=true

# 监控为主模式（默认true）
# true: buy/sell信号触发主流程，hold/None持续监控
# false: 主流程按15分钟周期运行
ALPHA_PULSE_PRIMARY_MODE=true

# 独立运行模式（默认false）
# true: 仅运行实时监控，不执行主交易循环
ALPHA_PULSE_ONLY_MODE=false
```

#### 监控为主模式流程
```
启动 --> AlphaPulse持续监控（60秒间隔）
       ↓
       ├─ buy/sell → 触发主流程（AI分析 → 交易执行）
       ├─ hold/None → 继续监控，不触发主流程
       └─ 监控异常 → 主流程后备启动（按15分钟周期）
```

#### 监控币种配置
```bash
# 建议只监控BTC，稳定运行后再添加其他币种
ALPHA_PULSE_SYMBOLS=BTC/USDT:USDT

# 多币种配置（增加系统负载）
# ALPHA_PULSE_SYMBOLS=BTC/USDT:USDT,ETH/USDT:USDT
```

#### 信号阈值配置
```bash
# BUY/SELL信号触发阈值（0.0-1.0）
ALPHA_PULSE_BUY_THRESHOLD=0.65
ALPHA_PULSE_SELL_THRESHOLD=0.65

# AI最小置信度
ALPHA_PULSE_MIN_CONFIDENCE=0.70

# 同交易对冷却时间（分钟）
ALPHA_PULSE_COOLDOWN_MINUTES=15
```

#### 后备模式配置
```bash
# 启用后备定时任务
FALLBACK_CRON_ENABLED=true

# 监控间隔（秒）
ALPHA_PULSE_INTERVAL=60
```

#### 配置组合示例
```bash
# 场景1：监控为主（推荐）
ALPHA_PULSE_ENABLED=true
ALPHA_PULSE_PRIMARY_MODE=true
ALPHA_PULSE_ONLY_MODE=false
ALPHA_PULSE_SYMBOLS=BTC/USDT:USDT

# 场景2：仅监控，不交易
ALPHA_PULSE_ENABLED=true
ALPHA_PULSE_PRIMARY_MODE=true
ALPHA_PULSE_ONLY_MODE=true
ALPHA_PULSE_SYMBOLS=BTC/USDT:USDT

# 场景3：传统模式（主流程为主）
ALPHA_PULSE_ENABLED=true
ALPHA_PULSE_PRIMARY_MODE=false
ALPHA_PULSE_ONLY_MODE=false
```

## 开发

### 运行测试
```bash
pip install -e ".[dev]"
pytest
```

### 代码格式化
```bash
black alpha_trading_bot/
```

### 类型检查
```bash
mypy alpha_trading_bot/
```

## 注意事项

⚠️ **风险提示**：
- 加密货币交易存在高风险，可能导致资金损失
- 首次使用请务必在测试模式下运行
- 建议先进行充分的回测和模拟交易
- 合理设置风险控制参数
- 不要投入超过承受能力的资金

## 贡献

欢迎提交Issue和Pull Request！

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

## 更新日志

### v1.0.0 (2026-06-01) - 首发版本
- 🚀 **核心架构** - 模块化设计，异步处理，插件化扩展
- 🤖 **多AI支持** - DeepSeek、Kimi、OpenAI、Qwen、Gemini、MiniMax、MiMo
- 📊 **AI信号融合** - 加权平均/共识/多数表决/置信度优先
- 🎯 **智能交易策略** - 保守型/稳健型/激进型三级别投资
- 🛡️ **完善风控体系** - 三级风控、智能止盈止损、追踪止损
- 📈 **技术指标库** - RSI、MACD、ADX、布林带、ATR全套指标
- 🖥️ **Web监控仪表板** - 实时行情、持仓状态、信号分布、交易历史
- 🌐 **代理支持** - HTTP/HTTPS代理配置
- 🔄 **信号优化管道** - 自适应买入、高位过滤、市场结构分析
- 🧠 **自适应模式** - 市场状态检测、策略自动选择、ML优化
- 🛠️ **完整工具链** - Docker部署、CI/CD、代码规范

---

**免责声明**：本项目仅供学习和研究使用，不构成投资建议。使用本软件进行交易产生的任何损失，作者和贡献者不承担任何责任。请理性投资，注意风险。

