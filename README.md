# poetry-fate-namer

**古诗文 + 八字五行 智能起名工具**

整合 [babyname/fate](https://github.com/babyname/fate) 与 [holynova/gushi_namer](https://github.com/holynova/gushi_namer) 的优点。

---

## 当前进度（2026-08-03）

| 事项 | 状态 |
|------|------|
| 创建本仓库 | ✅ |
| Fork fate / gushi_namer 到本账号 | ✅ |
| 分析两边代码与数据结构 | ✅ |
| 写出详细集成方案 | ✅ `docs/INTEGRATION.md` |
| 在 fate 上开开发分支 | ✅ `feature/poetry-source` |
| 实现带完整出处的名字生成 | 进行中 |
| 前端展示原诗句 + 评分 | 待做 |
| 本地可运行 MVP | 待做 |

---

## 仓库地址

- **本项目**：https://github.com/suanlatudou/poetry-fate-namer
- **fate fork**：https://github.com/suanlatudou/fate （分支 `feature/poetry-source`）
- **gushi_namer fork**：https://github.com/suanlatudou/gushi_namer

---

## 核心思路（方案 A）

**PoetryFirst + fate 评分**

1. 先用 gushi_namer 的方式，从精选诗库生成「有完整出处」的候选名字
2. 再把这些名字丢进 fate 的评分系统（八字、五格、音韵等）
3. 前端展示时同时显示：原诗句 + 出处 + 分数

详见：[docs/INTEGRATION.md](docs/INTEGRATION.md)

---

## 文档

- [集成方案](docs/INTEGRATION.md)
- [架构规划](docs/ARCHITECTURE.md)
- [路线图](docs/ROADMAP.md)
- [参考取名逻辑](docs/REFERENCE_NAMER.ts)

---

## 致谢

- [babyname/fate](https://github.com/babyname/fate)
- [holynova/gushi_namer](https://github.com/holynova/gushi_namer)
