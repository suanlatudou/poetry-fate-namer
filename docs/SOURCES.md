# 起名典籍来源规划

## 已有基础（来自 gushi_namer）

| 典籍 | 文件 | 说明 |
|------|------|------|
| 诗经 | shijing.json | 传统「女诗经」 |
| 楚辞 | chuci.json | 传统「男楚辞」 |
| 唐诗 | tangshi.json | 精选 |
| 宋词 | songci.json | 精选 |
| 乐府 | yuefu.json |  |
| 古诗三百首 | gushi.json |  |
| 辞赋 | cifu.json |  |

数据位置：https://github.com/suanlatudou/gushi_namer/tree/master/public/json

---

## 第一批扩展（本次加入规划）

### 1. 论语

- **为什么加**：传统「文论语」，名字文雅、寓意正。
- **推荐数据源**：
  - chinese-poetry 官方：https://github.com/chinese-poetry/chinese-poetry/tree/master/论语
  - 直接 JSON：https://github.com/chinese-poetry/chinese-poetry/blob/master/论语/lunyu.json
  - 也可通过 npm 包 `chinese-poetry` 获取
- **数据结构特点**：按「篇」组织，每篇有多个段落（paragraphs）。
- **起名时注意**：需要把段落再拆成短句，过滤说教感过重或负面的句子。

### 2. 周易（易经）

- **为什么加**：传统「武周易」，卦辞、爻辞里有大量适合起名的吉祥短句（元亨利贞、自强不息、厚德载物等）。
- **推荐数据源**：
  - freizl/yijing（简繁都有）：https://github.com/freizl/yijing
    - 简体 64 卦：https://freizl.github.io/yijing/zh-CN/64gua.json
  - john-walks-slow/open-iching
  - hanzhaodeng/chinese-ancient-text 里有 周易.json
- **数据结构特点**：64 卦 + 卦辞 + 六爻爻辞。
- **起名时注意**：优先用卦辞、大象传、吉祥爻辞；避开明显「凶」「勿用」类句子。

### 3. 道德经（老子）

- **为什么加**：意境高、名字有高级感（若水、知止、守拙、玄德等）。
- **推荐数据源**：
  - hanzhaodeng/chinese-ancient-text：https://github.com/hanzhaodeng/chinese-ancient-text （有 老子.json）
  - 通行本（王弼本）全文在 GitHub 上有多份 Markdown/文本，需自己整理成统一 JSON
  - 也可参考 fundgao/DAO_DE_JING 等仓库的整理版
- **数据结构建议**：按 81 章拆分，每章一条记录。
- **起名时注意**：道德经句子偏哲学，需要严格清洗，只保留意象优美、正面的短句。

---

## 统一数据格式（建议与 gushi_namer 对齐）

为了方便后面生成逻辑复用，建议统一成：

```json
{
  "author": "孔子 或 佚名 或 老子",
  "dynasty": "春秋 / 战国",
  "content": "完整段落或章节原文",
  "book": "论语 / 周易 / 道德经",
  "title": "学而篇 / 乾卦 / 第一章"
}
```

生成名字时继续沿用 gushi_namer 的流程：
1. 选一条记录
2. 拆成句子
3. 清洗标点和不好的字
4. 从句子里取两个字组成名字
5. 保留完整出处

---

## 第二批（后续再考虑）

- 孟子
- 庄子
- 古文观止（精选）
- 大学 / 中庸
- 世说新语

---

## 当前状态

- [x] 确定第一批三本典籍
- [x] 找到可靠开源数据源
- [ ] 下载并转换成统一 JSON 格式
- [ ] 写入 data/ 目录
- [ ] 接入生成逻辑
