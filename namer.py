#!/usr/bin/env python3
"""
从典籍生成带完整出处的名字（参考 gushi_namer 的 namer.ts）

用法：
  python namer.py                  # 从全部典籍各生成几个
  python namer.py --book 论语      # 指定典籍
  python namer.py --count 10       # 生成数量
  python namer.py --surname 李     # 带姓氏输出
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# 不适合入名的字（来自 gushi_namer，并补充说教虚词）
BAD_CHARS = set(
    "胸鬼懒禽鸟鸡我邪罪凶丑仇鼠蟋蟀淫秽妹狐鸡鸭蝇悔鱼肉苦犬吠窥血丧饥女搔"
    "父母昏狗蟊疾病痛死潦哀痒害蛇牲妇狸鹅穴畜烂兽靡爪氓劫鬣螽毛婚姻匪婆羞辱"
    "子曰曰矣乎也者焉哉兮夫"
)

BOOK_FILES = {
    "论语": "lunyu.json",
    "周易": "zhouyi.json",
    "道德经": "daodejing.json",
}


def load_book(name: str) -> list[dict]:
    filename = BOOK_FILES.get(name)
    if not filename:
        raise SystemExit(f"未知典籍: {name}，可选: {', '.join(BOOK_FILES)}")
    path = DATA_DIR / filename
    if not path.exists():
        raise SystemExit(
            f"找不到数据文件: {path}\n请先运行: python data/convert_classics.py"
        )
    return json.loads(path.read_text(encoding="utf-8"))


def format_str(s: str) -> str:
    s = re.sub(r"[\s\u3000]+", "", s)
    s = s.replace("<br>", "").replace("<p>", "").replace("</p>", "")
    s = re.sub(r"\([^)]*\)", "", s)
    return s


def split_sentence(content: str) -> list[str]:
    if not content:
        return []
    s = format_str(content)
    s = re.sub(r"[！。？；]", lambda m: m.group(0) + "|", s)
    s = s.rstrip("|")
    return [x for x in s.split("|") if len(x) >= 2]


def clean_punctuation(s: str) -> str:
    return re.sub(
        r"[<>《》！*\(\^\)\$%~!@#…&%￥—\+=、。，？；‘’“”：·`「」【】]",
        "",
        s,
    )


def clean_bad_char(s: str) -> str:
    return "".join(c for c in s if c not in BAD_CHARS)


def get_two_char(chars: list[str]) -> str | None:
    if len(chars) < 2:
        return None
    i = random.randrange(len(chars))
    j = random.randrange(len(chars))
    for _ in range(100):
        if i != j:
            break
        j = random.randrange(len(chars))
    if i > j:
        i, j = j, i
    return chars[i] + chars[j]


def gen_one(book_data: list[dict], max_retry: int = 80) -> dict | None:
    for _ in range(max_retry):
        passage = random.choice(book_data)
        content = passage.get("content") or ""
        sentences = split_sentence(content)
        if not sentences:
            continue
        sentence = random.choice(sentences)
        cleaned = clean_bad_char(clean_punctuation(sentence))
        if len(cleaned) < 2:
            continue
        name = get_two_char(list(cleaned))
        if not name or len(name) != 2:
            continue
        if name[0] == name[1]:
            continue
        return {
            "name": name,
            "sentence": sentence.strip(),
            "content": content,
            "title": passage.get("title", ""),
            "author": passage.get("author", ""),
            "book": passage.get("book", ""),
            "dynasty": passage.get("dynasty", ""),
        }
    return None


def gen_batch(book_data: list[dict], count: int) -> list[dict]:
    seen: set[str] = set()
    results: list[dict] = []
    attempts = 0
    while len(results) < count and attempts < count * 20:
        attempts += 1
        item = gen_one(book_data)
        if not item:
            continue
        if item["name"] in seen:
            continue
        seen.add(item["name"])
        results.append(item)
    return results


def print_result(item: dict, surname: str = "") -> None:
    full = f"{surname}{item['name']}" if surname else item["name"]
    print(f"【{full}】")
    print(f"  原句：{item['sentence']}")
    print(
        f"  出处：《{item['title']}》 · {item['author']} · "
        f"{item['book']}（{item['dynasty']}）"
    )
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="典籍取名生成器")
    parser.add_argument(
        "--book", default="", help="指定典籍：论语 / 周易 / 道德经（默认全部）"
    )
    parser.add_argument("--count", type=int, default=5, help="每个典籍生成数量")
    parser.add_argument("--surname", default="", help="姓氏，如：李")
    parser.add_argument("--seed", type=int, default=None, help="随机种子（可复现）")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    books = [args.book] if args.book else list(BOOK_FILES.keys())

    for book_name in books:
        data = load_book(book_name)
        print(f"======== {book_name}（共 {len(data)} 条）========")
        results = gen_batch(data, args.count)
        if not results:
            print("  （未能生成有效名字，请换典籍或增加重试）")
            continue
        for item in results:
            print_result(item, args.surname)


if __name__ == "__main__":
    main()
