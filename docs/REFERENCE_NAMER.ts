// 从 gushi_namer 提取的核心取名逻辑（参考用）
// 原文件：https://github.com/suanlatudou/gushi_namer/blob/master/src/utils/namer.ts
// 后续可移植到 fate 后端（Go）或在前端/脚本层先实现 MVP

export interface Book {
  content: string;
  title: string;
  author: string;
  book: string;
  dynasty: string;
}

export interface GeneratedName {
  name: string;      // 两个字
  sentence: string;  // 原句（最重要）
  content: string;
  title: string;
  author: string;
  book: string;
  dynasty: string;
}

/*
核心流程：
1. loadBook(bookName) → 加载 JSON
2. 随机选一首 passage
3. splitSentence → 按句号等拆分
4. cleanPunctuation + cleanBadChar
5. getTwoChar → 从句子中取两个字组成名字
6. 返回完整 GeneratedName（带出处）
*/
