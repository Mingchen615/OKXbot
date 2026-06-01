# Alpha Trading Bot OKX

基于 AI 驱动的 OKX 加密货币自动交易机器人，支持多 AI 融合、智能止盈止损、Web 监控仪表板。

## 功能特性

### AI 信号系统
- **7 大 AI 提供商**: DeepSeek, Kimi, OpenAI, Qwen, Gemini, MiniMax, MiMo
- **多 AI 融合**: 加权平均 / 共识 / 多数表决 / 置信度优先
- **信号优化管道**: 自适应买入条件、高位过滤、持续下跌检测、市场结构分析
- **智能缓存**: 15 分钟信号缓存，避免重复调用

### 交易策略
- **三级别投资**: 保守型 / 稳健型 / 激进型
- **智能止盈止损**: 普通模式 + 智能模式（多级止盈）
- **追踪止损**: 基于入场价的动态止损，只升不降
- **自适应止损**: 上升趋势 2%，下降趋势 4%

### 风控体系
- **三级风控**: 日亏损限制、连续亏损限制、仓位风险控制
- **暴跌保护**: 多时间框架暴跌检测
- **熔断机制**: 自动暂停交易

### Web 监控仪表板
- 实时行情监控 (BTC 价格、RSI、趋势)
- 持仓状态与盈亏
- AI 信号分布统计
- 交易历史记录
- 配置一览

## 快速开始

### 安装

```bash
git clone https://github.com/Mingchen615/OKXbot.git
cd OKXbot

python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

pip install -e .
```

### 配置

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```bash
# 交易所配置
OKX_API_KEY=your_api_key
OKX_SECRET=your_secret
OKX_PASSWORD=your_password

# AI 配置
AI_MODE=single
AI_DEFAULT_PROVIDER=mimo
MIMO_API_KEY=your_mimo_api_key

# 代理配置 (可选)
HTTP_PROXY=http://127.0.0.1:7890
HTTPS_PROXY=http://127.0.0.1:7890

# 止盈止损
TAKE_PROFIT_ENABLED=true
STOP_LOSS_ENABLED=true
TAKE_PROFIT_MODE=smart
STOP_LOSS_MODE=smart
INVESTMENT_TYPE=conservative

# Web 界面
WEB_INTERFACE_ENABLED=true
WEB_PORT=8501
```

### 启动

```bash
# 标准模式 + Web 界面
python main.py --web

# 自适应模式 (含 ML 学习)
python main.py --mode adaptive --web

# 指定端口
python main.py --web --port 8080
```

打开浏览器访问: **http://localhost:8501**

## 项目结构

```
alpha_trading_bot/
├── core/               # 核心交易逻辑
│   ├── bot.py          # 标准模式交易机器人
│   ├── adaptive_bot.py # 自适应模式交易机器人
│   ├── position_manager.py    # 仓位管理
│   ├── stop_loss_manager.py   # 止损管理
│   └── decision_engine.py     # 决策引擎
├── ai/                 # AI 信号系统
│   ├── client.py       # AI 客户端
│   ├── providers.py    # 提供商配置
│   ├── integrator.py   # 信号优化管道
│   ├── fusion/         # 多 AI 融合策略
│   ├── adaptive/       # 自适应策略
│   └── ml/             # 机器学习组件
├── exchange/           # 交易所交互
│   ├── client.py       # OKX 客户端
│   ├── market_data.py  # 行情数据
│   └── order_service.py # 订单服务
├── config/             # 配置管理
│   └── models.py       # 配置数据模型
├── utils/              # 工具模块
│   └── technical/      # 技术指标 (RSI, MACD, ATR...)
├── web/                # Web 仪表板
│   ├── server.py       # aiohttp 服务器
│   └── templates/      # HTML 模板
└── main.py             # 统一入口
```

## 配置说明

### 投资类型

| 类型 | R/R 阈值 | 止盈 | 止损 | 适用场景 |
|------|----------|------|------|----------|
| conservative | 0.8 | 6% | 2% | 风险厌恶 |
| moderate | 1.0 | 8% | 3% | 平衡型 |
| aggressive | 0.6 | 12% | 5% | 风险偏好 |

### AI 提供商

| 提供商 | 环境变量 | 备注 |
|--------|----------|------|
| DeepSeek | `DEEPSEEK_API_KEY` | 推理模型 |
| Kimi | `KIMI_API_KEY` | 晚间较慢 |
| OpenAI | `OPENAI_API_KEY` | GPT-4o |
| Qwen | `QWEN_API_KEY` | 阿里云 |
| Gemini | `GEMINI_API_KEY` | Google |
| MiniMax | `MINIMAX_API_KEY` | 推理模型 |
| MiMo | `MIMO_API_KEY` | 小米 MiMo |

### 智能止盈止损

```bash
# 多级止盈配置
CONSERVATIVE_SMART_MULTI_TP_LEVELS=2,3.5,5
CONSERVATIVE_SMART_MULTI_TP_RATIOS=0.5,0.3,0.2
```

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest

# 代码格式化
black alpha_trading_bot/
```

## 许可证

MIT License

---

**风险提示**: 加密货币交易存在高风险，可能导致资金损失。首次使用请在测试模式下运行。
