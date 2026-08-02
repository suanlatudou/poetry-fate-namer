# poetry-fate-namer

**古诗文 + 八字五行 智能起名工具**

整合 [babyname/fate](https://github.com/babyname/fate) 与 [holynova/gushi_namer](https://github.com/holynova/gushi_namer) 的优点，打造既有诗意出处、又合八字五行的起名系统。

---

## 项目目标

| 来源项目 | 优势 | 本项目如何吸收 |
|---------|------|----------------|
| **babyname/fate** | 完整的八字推算、三才五格、五行喜用神、多维评分、高性能后端 | 作为核心计算引擎 |
| **holynova/gushi_namer** | 从《诗经》《楚辞》、唐诗、宋词精选字，保留原诗句出处，UI 精美 | 作为诗意取名与出处展示模块 |

最终效果：生成的名字既**有经典出处**，又**合生辰八字**。

---

## 当前状态

- [x] 创建仓库
- [x] Fork 原项目作为参考（见下方）
- [ ] 确定技术架构
- [ ] 整合诗词数据与出处展示
- [ ] 接入八字评分逻辑
- [ ] 前端界面开发
- [ ] 可运行的 MVP

### 参考仓库（已 Fork 到本账号）

- fate: https://github.com/suanlatudou/fate
- gushi_namer: https://github.com/suanlatudou/gushi_namer

---

## 规划中的架构（待讨论）

### 方案 A：以 fate 为主体（推荐）
- 保留 Go 后端计算引擎（八字、五格、评分）
- 增强其 PoetryMode，引入 gushi_namer 精选诗库
- 前端用 React，借鉴 gushi_namer 的出处卡片展示

### 方案 B：独立新项目
- 后端用 Python/Go 重新组合逻辑
- 前端重新做

目前更倾向 **方案 A**，改动成本更低，能快速出效果。

---

## 开发计划（粗略）

1. **第一阶段**：理清两个原项目的数据结构与接口
2. **第二阶段**：把 gushi_namer 的诗句出处能力接到 fate 的生成流程
3. **第三阶段**：优化前端展示（名字 + 原诗 + 八字评分）
4. **第四阶段**：本地可运行 + 简单部署

---

## 免责声明

本项目仅供学习与参考，起名结果不构成任何命理保证。最终取名请结合个人喜好与专业意见。

---

## 致谢

- [babyname/fate](https://github.com/babyname/fate) — 现代科学取名引擎
- [holynova/gushi_namer](https://github.com/holynova/gushi_namer) — 古诗文起名
- chinese-poetry 等开源诗词数据

---

**仓库地址**：https://github.com/suanlatudou/poetry-fate-namer
