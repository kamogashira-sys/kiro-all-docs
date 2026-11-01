#!/usr/bin/env python3
"""check-structure.py - kiro-all-docs ページ骨格チェック（更新手順書 §7）

使用方法:
    ./scripts/kiro-all-docs/check-structure.py

規則（.github/UPDATE_GUIDE.md §7.1・§7.3・§7.4）:
  解説ページ（kiro-all-docs/NN_*/NN_*.md）
    (1) H1 がちょうど 1 つ
    (2) `**出典**` で始まる行が、最初の H2 より前にある
    (3) 最初の H2 が `## 📑 このページの内容`
    (4) 最後の H2 が `## 次に読む`
    (5) H2 に番号を付けない（`## 1. 〜` を禁止）
    (6) `## 出典` 節を置かない（出典は冒頭のブロックに一本化）
    (7) 目次の項目が本文 H2（📑 と 次に読む を除く）と 1 対 1 で対応し、順序も一致する
  すべての Markdown（kiro-all-docs/**/*.md）
    (8) `<!-- sources: n/a -->` を見出し行に書かない（見出しの次の行に置く）
  セクション README（kiro-all-docs/NN_*/README.md）
    (9) H1 が `# NN_name - 日本語` の形
    (10) `## 📂 このセクションのファイル` と `## 関連セクション` がある
  リポジトリ README.md
    (11) 「全 N ページ＋M セクション目次」の N・M が実ファイル数と一致する
"""
import glob
import os
import re
import sys

DOC_ROOT = "kiro-all-docs"
LOCAL_ONLY = ("06_embedded-docs", "work_plans", "work_records", "05_meta")
NA = "<!-- sources: n/a -->"
TOC_H2 = "📑 このページの内容"
NEXT_H2 = "次に読む"
TOC_ITEM_RE = re.compile(r"^\d+\.\s+\[(.+?)\]\(#[^)]*\)\s*$")
PAGE_COUNT_RE = re.compile(r"全 (\d+) ページ＋(\d+) セクション目次")


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def is_local_only(path):
    norm = path.replace(os.sep, "/")
    return any(f"/{lo}/" in norm or norm.startswith(f"{lo}/") for lo in LOCAL_ONLY)


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


def headings(lines):
    """フェンス外の (行番号, レベル, テキスト) を返す。"""
    out, fence = [], False
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence:
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", l)
        if m:
            out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def check_page(path, errors):
    lines = read_lines(path)
    hs = headings(lines)
    h1 = [h for h in hs if h[1] == 1]
    h2 = [h for h in hs if h[1] == 2]
    if len(h1) != 1:
        errors.append(f"{path}: (1) H1 が {len(h1)} 個（1 個にしてください）")
    if not h2:
        errors.append(f"{path}: (3) H2 がありません")
        return
    first_h2_line = h2[0][0]
    if not any(l.startswith("**出典**") for l in lines[:first_h2_line - 1]):
        errors.append(f"{path}: (2) 最初の H2 より前に `**出典**` で始まる行がありません")
    if h2[0][2] != TOC_H2:
        errors.append(f"{path}:{h2[0][0]} (3) 最初の H2 が `## {TOC_H2}` ではありません: 「{h2[0][2]}」")
    if h2[-1][2] != NEXT_H2:
        errors.append(f"{path}:{h2[-1][0]} (4) 最後の H2 が `## {NEXT_H2}` ではありません: 「{h2[-1][2]}」")
    for n, _, t in h2:
        if re.match(r"^\d+\.\s", t):
            errors.append(f"{path}:{n} (5) H2 に番号が付いています: 「{t}」")
        if t == "出典":
            errors.append(f"{path}:{n} (6) `## 出典` 節があります（出典は冒頭のブロックに書きます）")
    # (7) 目次と本文 H2 の対応
    if h2[0][2] == TOC_H2:
        end = h2[1][0] if len(h2) > 1 else len(lines) + 1
        toc = [TOC_ITEM_RE.match(l).group(1) for l in lines[h2[0][0]:end - 1] if TOC_ITEM_RE.match(l)]
        body = [t for _, _, t in h2[1:] if t != NEXT_H2]
        if toc != body:
            errors.append(f"{path}: (7) 目次の項目と本文 H2 が一致しません\n"
                          f"      目次: {toc}\n      本文: {body}")


def check_na_placement(path, errors):
    for i, l in enumerate(read_lines(path), 1):
        if l.startswith("#") and NA in l:
            errors.append(f"{path}:{i} (8) `{NA}` が見出し行にあります（見出しの次の行に置いてください）")


def check_section_readme(path, errors):
    lines = read_lines(path)
    hs = headings(lines)
    sec = os.path.basename(os.path.dirname(path))
    h1 = [h for h in hs if h[1] == 1]
    if len(h1) != 1 or not h1[0][2].startswith(f"{sec} - "):
        errors.append(f"{path}: (9) H1 が `# {sec} - 日本語` の形ではありません")
    h2t = [t for _, lv, t in hs if lv == 2]
    for need in ("📂 このセクションのファイル", "関連セクション"):
        if need not in h2t:
            errors.append(f"{path}: (10) `## {need}` がありません")


def check_page_count(pages, sections, errors):
    txt = "\n".join(read_lines("README.md"))
    m = PAGE_COUNT_RE.search(txt)
    if not m:
        errors.append("README.md: (11) 「全 N ページ＋M セクション目次」の行が見つかりません")
        return
    n, m_ = int(m.group(1)), int(m.group(2))
    if (n, m_) != (len(pages), len(sections)):
        errors.append(f"README.md: (11) 「全 {n} ページ＋{m_} セクション目次」が実数（{len(pages)} ページ・{len(sections)} セクション）と一致しません")


def main():
    os.chdir(repo_root())
    print("=== kiro-all-docs ページ骨格チェック（更新手順書 §7） ===")
    print("")
    pages = sorted(p for p in glob.glob(f"{DOC_ROOT}/[0-9][0-9]_*/[0-9][0-9]_*.md") if not is_local_only(p))
    sections = sorted(p for p in glob.glob(f"{DOC_ROOT}/[0-9][0-9]_*/README.md") if not is_local_only(p))
    all_md = sorted(p for p in glob.glob(f"{DOC_ROOT}/**/*.md", recursive=True) if not is_local_only(p))
    errors = []
    for p in pages:
        check_page(p, errors)
    for p in all_md:
        check_na_placement(p, errors)
    for p in sections:
        check_section_readme(p, errors)
    check_page_count(pages, sections, errors)
    print(f"解説ページ: {len(pages)} 件 / セクション README: {len(sections)} 件 / Markdown 全体: {len(all_md)} 件")
    print("")
    if errors:
        print(f"❌ 骨格の違反: {len(errors)} 件")
        for e in errors:
            print(f"   - {e}")
        print("")
        print("❌ 骨格チェックに失敗しました（.github/UPDATE_GUIDE.md §7 の書式に合わせてください）")
        return 1
    print("✅ すべてのページが更新手順書 §7 の骨格に従っています")
    return 0


if __name__ == "__main__":
    sys.exit(main())
