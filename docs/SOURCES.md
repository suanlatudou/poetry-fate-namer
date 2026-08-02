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

## 第一批扩展（已整理）

| 典籍 | 条数 | 状态 | 说明 |
|------|------|------|------|
| **论语** | 512 | ✅ 转换脚本就绪 | chinese-poetry 源 |
| **周易** | 514 | ✅ 转换脚本就绪 | 卦辞 + 大象 + 爻辞 |
| **道德经** | 81 | ✅ 已入库 + 脚本 | 81 章全文 |

### 如何生成完整 JSON

```bash
cd data
python3 convert_classics.py
```

会自动下载并生成：
- `lunyu.json`
- `zhouyi.json`
- `daodejing.json`

统一格式：

```json
{
  "author": "孔子及其弟子 / 佚名 / 老子",
  "dynasty": "春秋 / 周",
  "content": "原文",
  "book": "论语 / 周易 / 道德经",
  "title": "学而篇 / 乾卦·卦辞 / 道经·第一章"
}
```

### 数据来源链接

- 论语：https://github.com/chinese-poetry/chinese-poetry/tree/master/论语
- 周易：https://freizl.github.io/yijing/zh-CN/64gua.json
- 道德经：https://github.com/hanzhaodeng/chinese-ancient-text

---

## 第二批（后续）

- 孟子
- 庄子
- 古文观止（精选）
- 大学 / 中庸
- 世说新语

---

## 当前状态

- [x] 确定第一批三本典籍
- [x] 找到可靠开源数据源
- [x] 写好转换脚本 `data/convert_classics.py`
- [x] 本地验证转换结果（论语 512 / 周易 514 / 道德经 81）
- [ ] 把完整 JSON 提交进仓库（可运行脚本生成）
- [ ] 接入生成逻辑
