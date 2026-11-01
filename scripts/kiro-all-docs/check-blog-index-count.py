#!/usr/bin/env python3
"""check-blog-index-count.py - ブログ索引の件数と README の収録範囲行の整合チェック

使用方法:
    ./scripts/kiro-all-docs/check-blog-index-count.py

規則（作業計画 §9-1 `blog-index-count`）:
    kiro-all-docs/03_reference/01_blog-index.md が存在する場合のみ検査する。
    1. 索引の一覧表の行数（記事数）= 索引冒頭の収録範囲行の N
    2. 索引冒頭の収録範囲行（期間・N）= README.md（リポジトリ直下）の収録範囲行
    3. 索引が scripts/kiro-all-docs/blog-index.tsv から再生成した内容と一致する（gen-blog-index.py --check）
終了コード: 0 = 合格、1 = 不合格
"""
import os
import re
import subprocess
import sys

RANGE_RE = re.compile(r"収録範囲: 公式ブログ (\d{4}-\d{2}-\d{2})〜(\d{4}-\d{2}-\d{2}) 公開分（(\d+) 本）")
ROW_RE = re.compile(r"^\| \d{4}-\d{2}-\d{2} \| \[.+\]\(https://kiro\.dev/blog/[^)]+/\) \| [^|]+ \|$")


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def main():
    root = repo_root()
    index = os.path.join(root, "kiro-all-docs", "03_reference", "01_blog-index.md")
    readme = os.path.join(root, "README.md")
    if not os.path.exists(index):
        print("SKIP: 01_blog-index.md が無いため検査しない")
        return 0
    text = open(index, encoding="utf-8").read()
    m = RANGE_RE.search(text)
    if not m:
        print("NG: 索引に収録範囲行が無い")
        return 1
    first, last, n = m.group(1), m.group(2), int(m.group(3))
    rows = [l for l in text.splitlines() if ROW_RE.match(l)]
    ok = True
    if len(rows) != n:
        print(f"NG: 索引の記事行 {len(rows)} 件 != 収録範囲行の {n} 本")
        ok = False
    else:
        print(f"OK: 索引の記事行 {len(rows)} 件 = 収録範囲行の {n} 本")
    rtext = open(readme, encoding="utf-8").read()
    rm = RANGE_RE.search(rtext)
    if not rm:
        print("NG: README.md に収録範囲行が無い")
        ok = False
    elif rm.groups() != m.groups():
        print(f"NG: README の収録範囲 {rm.groups()} != 索引の {m.groups()}")
        ok = False
    else:
        print(f"OK: README の収録範囲行が索引と一致（{first}〜{last}・{n} 本）")
    r = subprocess.run([sys.executable, os.path.join(root, "scripts", "kiro-all-docs", "gen-blog-index.py"), "--check"],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
