#!/usr/bin/env python3
"""check-quotes.py - kiro-all-docs 英文引用の長さチェック

使用方法:
    ./scripts/kiro-all-docs/check-quotes.py

規則（作業計画 §6-2 原則 9・§9-1 `quotes`）:
    公式の英文を引用するときは 1 箇所 30 語以内。対象は 「…」『…』"…" “…” で囲まれた、
    英数字が主体（ASCII 文字が 70% 以上）の文字列。
    フェンスコードブロック・インラインコードは対象外（コマンド例・設定例は引用ではない）。
    ⚠️ 日本語の引用（Qiita 記事の原文など）は語数で測れないため対象外。

根拠: AWS Site Terms はサイト内容の派生的利用を許諾していない（権利確認 0-2）。
"""
import glob
import os
import re
import sys

DOC_ROOT = "kiro-all-docs"
LOCAL_ONLY = ("06_embedded-docs", "work_plans", "work_records", "05_meta")
MAX_WORDS = 30
QUOTE_RE = re.compile(r"[「『\"“]([^」』\"”]{20,})[」』\"”]")


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def is_local_only(path):
    norm = path.replace(os.sep, "/")
    return any(f"/{lo}/" in norm or norm.startswith(f"{lo}/") for lo in LOCAL_ONLY)


def target_files():
    files = sorted(glob.glob(f"{DOC_ROOT}/**/*.md", recursive=True))
    files = [f for f in files if not is_local_only(f)]
    files += ["README.md"]
    return [f for f in files if os.path.isfile(f)]


def strip_code(txt):
    out, in_fence = [], False
    for line in txt.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        out.append(re.sub(r"`[^`\n]*`", "", line))
    return "".join(out)


def is_english(s):
    letters = [c for c in s if not c.isspace()]
    if not letters:
        return False
    ascii_n = sum(1 for c in letters if ord(c) < 128)
    return ascii_n / len(letters) >= 0.7


def main():
    os.chdir(repo_root())
    print("=== kiro-all-docs 英文引用の長さチェック ===")
    print("")
    errors, quotes = [], 0
    for f in target_files():
        txt = strip_code(open(f, encoding="utf-8").read())
        for i, line in enumerate(txt.splitlines(), 1):
            for m in QUOTE_RE.finditer(line):
                q = m.group(1)
                if not is_english(q):
                    continue
                quotes += 1
                words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-./]*", q))
                if words > MAX_WORDS:
                    errors.append((f, i, words, q[:60]))
    print(f"検査ファイル: {len(target_files())} 件 / 英文引用: {quotes} 箇所")
    print("")
    if errors:
        print(f"❌ {MAX_WORDS} 語を超える英文引用: {len(errors)} 件")
        for f, i, w, q in errors:
            print(f"   - {f}:{i} {w} 語: {q!r}…")
        print("")
        print("❌ 英文引用チェックに失敗しました（要旨を自分の言葉で書き、引用は短くしてください）")
        return 1
    print(f"✅ すべての英文引用が {MAX_WORDS} 語以内です")
    return 0


if __name__ == "__main__":
    sys.exit(main())
