#!/usr/bin/env python3
"""下载并转换第一批扩展典籍为统一格式（Termux / 手机可用）"""
import json
import urllib.request
from urllib.parse import quote

def fetch(url):
    # 对 URL 里的中文路径做编码，避免 ascii 报错
    from urllib.parse import urlsplit, urlunsplit
    parts = urlsplit(url)
    encoded_path = "/".join(quote(seg) if seg else "" for seg in parts.path.split("/"))
    safe_url = urlunsplit((parts.scheme, parts.netloc, encoded_path, parts.query, parts.fragment))
    req = urllib.request.Request(safe_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))

print("开始下载…（手机网络可能稍慢）")

# ---------- 论语 ----------
print("下载 论语…")
lunyu_raw = fetch("https://raw.githubusercontent.com/chinese-poetry/chinese-poetry/master/论语/lunyu.json")
lunyu = []
for item in lunyu_raw:
    chapter = item.get("chapter", "")
    for p in item.get("paragraphs", []):
        if p and p.strip():
            lunyu.append({
                "author": "孔子及其弟子",
                "dynasty": "春秋",
                "content": p.strip(),
                "book": "论语",
                "title": chapter,
            })
print(f"论语: {len(lunyu)} 条")

# ---------- 周易 ----------
print("下载 周易…")
zhouyi_raw = fetch("https://freizl.github.io/yijing/zh-CN/64gua.json")
zhouyi = []
for gua in zhouyi_raw:
    name = gua.get("name", "")
    if gua.get("gua_ci"):
        zhouyi.append({"author": "佚名", "dynasty": "周", "content": gua["gua_ci"], "book": "周易", "title": f"{name}卦·卦辞"})
    if gua.get("da_xiang"):
        zhouyi.append({"author": "佚名", "dynasty": "周", "content": gua["da_xiang"], "book": "周易", "title": f"{name}卦·大象"})
    for yao in gua.get("yao_ci", []):
        if yao:
            zhouyi.append({"author": "佚名", "dynasty": "周", "content": yao, "book": "周易", "title": f"{name}卦·爻辞"})
print(f"周易: {len(zhouyi)} 条")

# ---------- 道德经 ----------
print("下载 道德经…")
ddj_raw = fetch("https://raw.githubusercontent.com/hanzhaodeng/chinese-ancient-text/master/老子.json")
ddj = []
for art in ddj_raw.get("articles", []):
    content_list = art.get("content", [])
    content = "".join(content_list) if isinstance(content_list, list) else str(content_list)
    content = content.strip()
    if content:
        ddj.append({
            "author": "老子",
            "dynasty": "春秋",
            "content": content,
            "book": "道德经",
            "title": art.get("title", ""),
        })
print(f"道德经: {len(ddj)} 条")

# 写出
for name, data in [("lunyu", lunyu), ("zhouyi", zhouyi), ("daodejing", ddj)]:
    path = f"{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"已写出 {path}")

print("完成！")
