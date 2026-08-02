# 开发路线图

## 阶段 0：准备（已完成）

- [x] 创建本仓库 poetry-fate-namer
- [x] Fork babyname/fate → suanlatudou/fate
- [x] Fork holynova/gushi_namer → suanlatudou/gushi_namer
- [x] 写清架构与集成方案

## 阶段 1：调研与方案（已完成）

- [x] 分析 gushi_namer 取名逻辑与数据结构
- [x] 分析 fate 现有 Poetry 相关代码
- [x] 确定「PoetryFirst + fate 评分」的集成路径
- [x] 写出 docs/INTEGRATION.md
- [x] 探索其他古籍来源，确定第一批扩展：论语、周易、道德经

## 阶段 2：MVP 实现（进行中）

- [x] 在 fate fork 创建分支 feature/poetry-source
- [x] 整理第一批新典籍数据（论语 512 / 周易 514 / 道德经 81）
- [x] 编写转换脚本 data/convert_classics.py（一键生成完整 JSON）
- [ ] 把完整 JSON 提交进仓库（运行 convert_classics.py 即可）
- [ ] 引入 gushi_namer 精选诗库 + 第一批新典籍
- [ ] 实现带完整出处的候选名生成
- [ ] 把候选名接入 fate 评分
- [ ] 前端 NameCard / 详情页展示原诗句 + 出处
- [ ] 本地跑通「输入姓氏+生日 → 得到有出处+有评分的名字」

## 阶段 3：体验优化

- [ ] 支持按典籍筛选
- [ ] 出处高亮名字用字
- [ ] 收藏与分享卡片
- [ ] 过滤明显不好的字

## 阶段 4：完善

- [ ] 更完整的喜用神匹配
- [ ] 性能与批量生成优化
- [ ] 文档与使用说明

---

**当前优先级**：运行 `data/convert_classics.py` 生成完整 JSON 后，开始写生成逻辑。
