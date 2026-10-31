#!/usr/bin/env python3
"""check-sources.py - kiro-all-docs 出典有無チェック（節単位）

使用方法:
    ./scripts/kiro-all-docs/check-sources.py

規則（作業計画 §9-1 `sources`）:
    `kiro-all-docs/00_start/`・`01_story/`・`03_reference/` の各 `##` 節（H2 以下の本文。
    H3 以下は親の H2 節に含める）に、次のいずれかへのリンクが 1 つ以上あること。
        - https://kiro.dev/
        - https://github.com/kirodotdev/
        - https://github.com/aws/amazon-q-developer-cli
        - https://github.com/kamogashira-sys/   （姉妹サイト）
        - https://qiita.com/kamogashira/        （筆者の記事）
    除外:
        - 🐾 ブロック（`> 🐾` で始まる引用）だけで構成される節
        - 本文が無い節（見出しだけ・次の見出しまで空行のみ）
        - `<!-- sources: n/a -->` を見出し行または本文に含む節（出典を要しない節。目次・ナビゲーション等）。
          **除外した節は実行時に全件表示する**（暗黙に見逃さない）。
    H1 直下（最初の `##` より前）の導入文は、ページ全体のどこかに出典があれば良いとし、
    単独では検査しない。

⚠️ 「事実を述べる段落」を自動判別することはできない（レビュー F12）。本スクリプトは
   節単位の機械可能な近似であり、出典の妥当性は人の目視（§9-2）が担う。
"""
import glob
import os
import re
import sys

TARGET_DIRS = ("kiro-all-docs/00_start", "kiro-all-docs/01_story", "kiro-all-docs/03_reference")
SOURCE_RE = re.compile(
    r"https://(?:kiro\.dev/|github\.com/kirodotdev/|github\.com/aws/amazon-q-developer-cli"
    r"|github\.com/kamogashira-sys/|qiita\.com/kamogashira/)")
H2_RE = re.compile(r"^## ")
H1_RE = re.compile(r"^# ")
NA_MARK = "<!-- sources: n/a -->"


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def sections(lines):
    """(見出し行番号, 見出しテキスト, 本文行リスト) を H2 単位で返す。"""
    out = []
    cur = None
    in_fence = False
    for i, line in enumerate(lines, 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
        if not in_fence and H2_RE.match(line):
            if cur:
                out.append(cur)
            cur = (i, line.strip()[3:], [])
            continue
        if cur:
            cur[2].append(line)
    if cur:
        out.append(cur)
    return out


def body_kind(body):
    """'empty' / 'paw_only' / 'text'"""
    nonempty = [l for l in body if l.strip()]
    if not nonempty:
        return "empty"
    if all(l.lstrip().startswith(">") for l in nonempty) and any("🐾" in l for l in nonempty):
        return "paw_only"
    return "text"


def main():
    os.chdir(repo_root())
    print("=== kiro-all-docs 出典有無チェック（H2 節単位） ===")
    print("")
    files = []
    for d in TARGET_DIRS:
        files += sorted(glob.glob(f"{d}/**/*.md", recursive=True))
    files = [f for f in files if os.path.isfile(f)]

    errors, skipped, checked = [], [], 0
    for f in files:
        lines = open(f, encoding="utf-8").read().splitlines()
        for lineno, title, body in sections(lines):
            text = "\n".join(body)
            if NA_MARK in text or NA_MARK in title:
                skipped.append((f, lineno, title, "n/a 指定"))
                continue
            kind = body_kind(body)
            if kind == "empty":
                skipped.append((f, lineno, title, "本文なし"))
                continue
            if kind == "paw_only":
                skipped.append((f, lineno, title, "🐾 ブロックのみ"))
                continue
            checked += 1
            if not SOURCE_RE.search(text):
                errors.append((f, lineno, title))

    print(f"検査ファイル: {len(files)} 件 / 検査した節: {checked} 件")
    print(f"除外した節: {len(skipped)} 件")
    for f, n, t, why in skipped:
        print(f"   {f}:{n} 「{t}」 … {why}")
    print("")
    if errors:
        print(f"❌ 出典リンクの無い節: {len(errors)} 件")
        for f, n, t in errors:
            print(f"   - {f}:{n} 「{t}」")
        print("")
        print("❌ 出典チェックに失敗しました（公式・姉妹サイト・Qiita へのリンクを節内に置くか、"
              "出典を要しない節なら <!-- sources: n/a --> を明示してください）")
        return 1
    print("✅ 検査したすべての節に出典リンクがあります")
    return 0


if __name__ == "__main__":
    sys.exit(main())
