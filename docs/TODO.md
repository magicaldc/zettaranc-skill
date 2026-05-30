# TODO

> Zettaranc Skill 待办清单
> 更新日期：2026-05-30（意图识别编排层落地）
> 当前版本：v2.8.0
> 状态：✅ 已完成 / ⏳ 进行中 / 📋 待规划

---

## ✅ 已完成（v2.8.0 意图识别编排层）

### 意图识别系统
- [x] 意图识别规则引擎（rules/intent_rules.yaml）
- [x] 四意图路由：stock / career / life / chat
- [x] 规则匹配 15/15 测试通过
- [x] 向量知识库适配器（modules/knowledge_retriever.py）
- [x] 按意图注入分类过滤（01_战法系列 / 06_行业宏观 / 05_交易心理等）
- [x] 统一入口 IntentRouter（modules/intent_router.py）
- [x] 交互式聊天界面（modules/intent_chat.py）
- [x] 技术设计文档 v2（docs/intent-router-design.md）

### LLM 生成层
- [x] MiniMax LLM 提供商（modules/llm_providers.py）
- [x] LLM_API_KEY 可选配置（未配置时跳过生成）
- [x] 通用 LLM 环境变量（LLM_API_KEY / LLM_BASE_URL / LLM_MODEL）

### 配置优化
- [x] Tushare 配置条件化（仅 DATA_MODE=jnb 时强制检查）
- [x] 知识库默认关闭（KB_ENABLED=false）
- [x] 配置指南文档（docs/CONFIG_GUIDE.md）
- [x] .env.example 完整示例

### 角色框架
- [x] Z哥职业决策框架（rules/career_prompt.md）
- [x] Z哥人生决策框架（rules/life_prompt.md）
- [x] 跨领域通用心法迁移（选择大于努力 / 周期思维 / 安全边际）

---

## ✅ 已完成（v2.7.0 数据层充实）

### 数据层充实
- [x] 真实财务数据入库（2,733 条，53 只股票）
- [x] 多接口组合：fina_indicator + income + balancesheet + daily_basic
- [x] PE/PB/PS 覆盖率 >88%
- [x] 资金流向全量入库（207,361 条，60 天）
- [x] 指标缓存打通（6,360 条）
- [x] Tushare 官方指标（12,554 条）

### Bug 修复
- [x] strategies.py DB 路径不一致（导致战法识别报错）
- [x] 财务数据表结构不匹配（字段名映射修复）

### 测试体系
- [x] SAT/UAT 两阶段真实数据测试
- [x] run_sat_uat.py 可复用测试脚本
- [x] 264 测试通过

### 文档
- [x] docs/USER_GUIDE.md（3 万字，20 章）
- [x] CHANGELOG.md 全面更新
- [x] AGENTS.md 全面更新（v2.8.0/新模块/文件树对齐）

---

## ✅ 已完成（v2.4.0 - v2.6.0）

### 基础指标（60+）
- [x] KDJ / MACD / BBI / RSI / WR / 布林带 / DMI
- [x] 双线战法 / 单针下 20 / 砖形图
- [x] 量比 / 资金流向 / 筹码分布

### 买入战法（10+）
- [x] B1 / B2 / B3 / SB1 / 超级 B1
- [x] 长安战法 / 平行重炮 / 坑里起好货 / 对称 VA
- [x] 四分之三阴量 / 娜娜图形 / 异动地量

### 卖出/逃顶（6 种）
- [x] S1 / S2 / S3 逃顶体系
- [x] 滴滴战法 / MACD 金叉空·死叉多 / 祖冲之法
- [x] 主力出货五式 / 灾后重建 / 跃跃欲试 / 关键 K 识别

### P2 核心模块
- [x] 三波理论（建仓波/拉升波/冲刺波）
- [x] 麒麟会四阶段（吸筹/拉升/派发/回落）

### 分析工具
- [x] 持股诊断（防卖飞评分 + 出货信号扫描）
- [x] 选股评分（趋势/量价/风险三维度）
- [x] 自选股观察池（增删改查 + 批量扫描）
- [x] 策略组合回测（多策略融合 + 资金曲线）

### CLI 工具
- [x] analyze / screen / watchlist / diagnose / backtest
- [x] pyproject.toml 打包 + zt 命令

---

## 📋 待实现（量化指标缺口清单）

### P3 — 中价值 / 概念性

- [ ] **蜈蚣图识别**
  - 来源：`knowledge/trading-core.md` 3.0b
  - 定义：堆量不涨 + 长上下影十字星交替 + 无呼吸节奏
  - 价值：直接排除垃圾票
  - 难点：「呼吸节奏」量化定义较模糊
  - 文件建议：`modules/screener.py`（作为过滤条件）

- [ ] **牛绳理论量化**
  - 来源：`knowledge/trend-lines.md`
  - 定义：白线在黄线上 = 主力牵牛，跌破 = 牛绳断
  - 现状：双线战法已有基础，但「牛绳」概念未单独封装
  - 难度：低（在现有双线基础上加一层抽象）
  - 文件建议：`modules/indicators/price_patterns.py`

- [ ] **量比战法引擎**
  - 来源：`knowledge/trading-core.md` 3.6
  - 定义：集合竞价量比计算 + 攻击日/出货日判定
  - 价值：开盘精细择时
  - 难点：需要分钟级/竞价数据，Tushare 免费版可能不支持
  - 文件建议：新增 `modules/market_timing.py`

- [ ] **沙漏评分 V9**
  - 来源：TANGOO 09 / 复盘专用z 10
  - 定义：S_shape + Delta 评分引擎，通达信已有指标
  - 价值：Z 哥说的「完美图形」量化标准
  - 难点：需要了解通达信沙漏指标的具体算法
  - 文件建议：新增 `modules/sandglass.py`

---

## ⏳ 进行中

（暂无）

---

## 版本路线图

| 版本 | 主题 | 状态 |
|------|------|------|
| **v2.4.0** | CLI 工具 + 回测框架 + 递推修复 | ✅ 已完成 |
| **v2.5.0** | P0/P1 指标补全 + 工程化补完 | ✅ 已完成 |
| **v2.6.0** | P2 核心模块（三波理论/麒麟会） | ✅ 已完成 |
| **v2.7.0** | 数据层充实 + SAT/UAT 测试 + 使用手册 | ✅ 已完成 |
| **v2.8.0** | 意图识别编排层 + RAG + 可选 LLM | ✅ 已完成 |
| **v2.9.0** | 沙漏 V9 + 蜈蚣图 + 牛绳理论 | 📋 待定 |
| **v3.0.0** | 少妇模拟器完整版（自动化择时+选股+买入+卖出闭环） | 🎯 长期目标 |
