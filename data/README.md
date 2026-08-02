# 扩展典籍数据（第一批）

统一格式，可直接用于起名生成。

## 文件说明

| 文件 | 典籍 | 条数 | 来源 |
|------|------|------|------|
| lunyu.json | 论语 | 512 | chinese-poetry |
| zhouyi.json | 周易 | 514 | freizl/yijing |
| daodejing.json | 道德经 | 81 | hanzhaodeng/chinese-ancient-text |

## 数据格式

```json
{
  "author": "作者",
  "dynasty": "朝代",
  "content": "原文",
  "book": "典籍名",
  "title": "章节/篇名"
}
```

## 使用注意

- 周易爻辞中含有「凶」「勿用」「有悔」等，生成名字时应做过滤
- 道德经偏哲学，建议只取意象优美的短句
- 生成逻辑可复用 gushi_namer 的 namer.ts 流程
