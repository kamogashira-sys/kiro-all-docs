#!/usr/bin/env python3
"""check-first-person.py - kiro-all-docs 一人称（筆者の意見）の所在チェック【警告のみ】

使用方法:
    ./scripts/kiro-all-docs/check-first-person.py

規則（作業計画 §4-3・§9-1 `first-person`）:
    筆者の意見は `kiro-all-docs/02_why-kiro-cli/` と、README.md の 🐾 ブロック 1 個に集約する。
    それ以外の公開文書で、🐾 ブロック（`> 🐾` で始まる引用ブロックとその継続行）の外に
    「私」「筆者は」「筆者が」「推し」が現れたら**警告**する。
    許容語（事実の記述に必要な一人称）: 「筆者の環境」「筆者の記事」「筆者のひとこと」「筆者の実機」
    「筆者の推し」、および推しページのタイトル「なぜ筆者は Kiro CLI が好きなのか」（リンク文言）
    ⚠️ 本スクリプトは終了コードを変えない（常に exit 0）。警告は人が目視で判断する（§9-2）。
    加えて README.md の 🐾 ブロック数を数え、1 個でなければ警告する（§4-3 規則 1）。
"""
import glob
import os
import re
import sys

DOC_ROOT = "kiro-all-docs"
LOCAL_ONLY = ("06_embedded-docs", "work_plans", "work_records", "05_meta")
OPINION_DIR = "kiro-all-docs/02_why-kiro-cli/"
FIRST_PERSON_RE = re.compile(r"私|筆者は|筆者が|推し")
# 推しページのタイトル「なぜ筆者は Kiro CLI が好きなのか」へのリンク文言は許容する
ALLOWED_RE = re.compile(r"筆者の環境|筆者の記事|筆者のひとこと|筆者の実機|筆者の推し|なぜ筆者は Kiro CLI が好きなのか")


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def is_local_only(path):
    norm = path.replace(os.sep, "/")
    return any(f"/{lo}/" in norm or norm.startswith(f"{lo}/") for lo in LOCAL_ONLY)


def target_files():
    files = sorted(glob.glob(f"{DOC_ROOT}/**/*.md", recursive=True))
    files = [f for f in files if not is_local_only(f) and not f.startswith(OPINION_DIR)]
    files += ["README.md"]
    return [f for f in files if os.path.isfile(f)]


def paw_flags(lines):
    """各行が 🐾 ブロック内かを返す。`> 🐾` で始まる行から、`>` が続く間を 1 ブロックとする。"""
    flags, in_paw, blocks = [], False, 0
    for line in lines:
        s = line.lstrip()
        if s.startswith(">") and "🐾" in s:
            in_paw = True
            blocks += 1
        elif not s.startswith(">"):
            in_paw = False
        flags.append(in_paw)
    return flags, blocks


def main():
    os.chdir(repo_root())
    print("=== kiro-all-docs 一人称の所在チェック（警告のみ） ===")
    print("")
    warnings = []
    readme_paws = 0
    for f in target_files():
        lines = open(f, encoding="utf-8").read().splitlines()
        flags, blocks = paw_flags(lines)
        if f == "README.md":
            readme_paws = blocks
        in_fence = False
        for i, (line, in_paw) in enumerate(zip(lines, flags), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or in_paw:
                continue
            stripped = ALLOWED_RE.sub("", re.sub(r"`[^`]*`", "", line))
            m = FIRST_PERSON_RE.search(stripped)
            if m:
                warnings.append((f, i, m.group(0), line.strip()[:70]))

    print(f"README.md の 🐾 ブロック数: {readme_paws}（規則: 1 個）")
    if readme_paws != 1:
        print("   ⚠  README.md の 🐾 ブロックは 1 個にしてください（§4-3 規則 1）")
    print("")
    if warnings:
        print(f"⚠  🐾 ブロック外の一人称・推し表現: {len(warnings)} 件（目視で判断してください）")
        for f, i, w, ctx in warnings:
            print(f"   - {f}:{i} {w!r}: {ctx}")
    else:
        print("✅ 🐾 ブロック外に一人称・推し表現はありません")
    print("")
    print("（本チェックは警告のみ。終了コードは 0）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
