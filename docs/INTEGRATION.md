# 集成方案：把 gushi_namer 的诗意出处接到 fate

## 目标（MVP）

生成名字时同时输出：

1. 名字本身
2. **完整原诗句**（不是只有「有诗词」标记）
3. 标题、作者、典籍、朝代
4. 八字 / 五格 / 综合评分（复用 fate）

---

## 两边现状对比

### gushi_namer（优势在「出处」）

核心文件：`src/utils/namer.ts`

生成结果结构：

```ts
interface GeneratedName {
  name: string;        // 两个字的名
  sentence: string;    // 原句
  content: string;     // 整首
  title: string;       // 篇名
  author: string;
  book: string;        // 诗经 / 楚辞 / 唐诗...
  dynasty: string;
}
```

取名逻辑简述：
1. 加载某本典籍的 JSON（`public/json/shijing.json` 等）
2. 随机选一首 → 拆成句子 → 清洗标点和不好的字
3. 从句子里随机取两个字组成名字
4. **完整保留出处信息**

数据位置（你账号下的 fork）：
- https://github.com/suanlatudou/gushi_namer/tree/master/public/json

### fate（优势在「命理评分」）

- 已有 `PoetrySearchTab.tsx`（只是搜索，不是起名核心流程）
- 生成结果里有 `HasPoetry` 标记
- 评分管线完整（八字、五格、音韵、文化等）
- 诗词数据主要来自 chinese-poetry，出处展示不如 gushi_namer 精致

关键前端文件：
- `web/src/components/naming/PoetrySearchTab.tsx`
- `web/src/components/naming/NameCard.tsx`
- `web/src/components/naming/NameDetailModal.tsx`

---

## 推荐落地路径（方案 A 细化）

### 阶段 1：数据层（先做）

把 gushi_namer 的 7 本精选诗库当作「优质诗意来源」：

- shijing.json（诗经）
- chuci.json（楚辞）
- tangshi.json（唐诗）
- songci.json（宋词）
- yuefu.json（乐府）
- gushi.json（古诗三百首）
- cifu.json（辞赋）

放在 fate 的 `data/` 或 `resources/poetry/` 下，或做成可配置数据源。

### 阶段 2：生成逻辑改造

在 fate 的命名 pipeline 里增加一种模式：

**PoetryFirst 模式**

1. 先按 gushi_namer 的方式从精选诗库生成一批候选名字（带完整出处）
2. 再把这些候选名字丢进 fate 现有的评分器（五行、五格、音韵…）
3. 按综合分排序输出

这样改动最小，又能立刻拥有「漂亮出处 + 命理分数」。

### 阶段 3：前端展示

改造 `NameCard` / `NameDetailModal`：

- 有出处时，直接显示：
  - 原句（高亮名字用字）
  - 篇名 · 作者 · 典籍
- 参考 gushi_namer 的 `NameCard.tsx` 样式

---

## 最小可运行 MVP 定义

满足以下条件就算第一版成功：

1. 输入姓氏 + 出生时间
2. 能生成一批名字
3. 每个名字下面能看到**完整原诗句 + 出处**
4. 同时有基础评分（至少五格或综合分）
5. 本地能跑起来

---

## 下一步具体动作

1. 在 fate fork 上新建分支 `feature/poetry-source`
2. 引入 gushi_namer 诗库数据
3. 实现 PoetryFirst 生成路径（可先用简化版，甚至先在前端/脚本层验证）
4. 改前端卡片展示出处
5. 跑通后再考虑更深度的后端融合

---

## 参考代码位置（你账号下）

| 内容 | 地址 |
|------|------|
| gushi_namer 取名逻辑 | https://github.com/suanlatudou/gushi_namer/blob/master/src/utils/namer.ts |
| 诗库 JSON | https://github.com/suanlatudou/gushi_namer/tree/master/public/json |
| fate 诗词搜索页 | https://github.com/suanlatudou/fate/blob/main/web/src/components/naming/PoetrySearchTab.tsx |
| fate 名字卡片 | https://github.com/suanlatudou/fate/blob/main/web/src/components/naming/NameCard.tsx |
