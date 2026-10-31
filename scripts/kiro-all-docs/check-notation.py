#!/usr/bin/env python3
"""check-notation.py - kiro-all-docs 表記規約チェック

使用方法:
    ./scripts/kiro-all-docs/check-notation.py

本サイト（Kiro 全体の紹介・案内）の表記規約:
    (b) **製品名の揺れ**
        `Kiro IDE` / `Kiro CLI` / `Kiro Web` / `Kiro Mobile` / `Kiro Crew` の
        大文字小文字の崩れ（`kiro Web`・`Kiro cli` 等）を検出する。
        ⚠️ `kiro-cli`（コマンド名）・`kiro.dev`（ドメイン）・`q-cli-docs`（リポジトリ名）は対象外。
    (c) **非 ISO 日付**
        本文の日付は `YYYY-MM-DD`。英語表記（`Jul 1, 2026`）は
        **公式表記の引用・出典表示・表記形式の説明**でのみ許容する。
    (e) **取得日の本文混入**
        「いつ取得したか」は作業記録に書く。本文の時点表示は公式の表示日を使う。
    (f) **裸 URL 直後の全角文字による autolink 事故**
    (g) **禁止表現（推測・曖昧表現）**
        「おそらく」「たぶん」「一般的に」「通常」「最低〜以上」など。
        ⚠️ `.github/` の規約文書は禁止表現の一覧そのものを載せるため対象外。
    (i) **所属企業名の非掲載**（聞き取り 0-6 の公開制限）
        筆者の所属を示す語句（「勤務先」「弊社」「自社」「職場」「所属企業」「当社」）を
        公開文書で使わない。製品説明の「自社の〜」等の一般用法も含めて検出し、
        人が目視で判断する（警告ではなくエラー。許容する場合は言い換える）。

姉妹サイト（kiro-web-docs）の check-notation.py から流用し、Web 固有の規則
（(a) 他製品コマンドの混入・(d) 版番号の創作・(h) 出典日の書式）を外した。
本サイトは全サーフェスを案内し、版番号（CLI 2.0・IDE 1.4.26 等）を本文で使うため。

⚠️ 設計方針:
    URL の書式は check-links.py、出典の有無は check-sources.py、英文引用の長さは
    check-quotes.py、一人称は check-first-person.py が持つ。本スクリプトは**表記**だけを見る。
"""
import glob
import os
import re
import sys

DOC_ROOT = "kiro-all-docs"
LOCAL_ONLY = ("06_embedded-docs", "work_plans", "work_records")

# 規約そのものを記述しているファイル（禁止表現の一覧等を含む）。(e)(g)(i) の対象外。
POLICY_DOCS = (".github/WORKFLOW.md", ".github/COMMIT_CHECKLIST.md",
               ".github/pull_request_template.md")

# ------------------------------------------------------------
# (b) 製品名の揺れ
# ------------------------------------------------------------
# 正: Kiro IDE / Kiro CLI / Kiro Web / Kiro Mobile / Kiro Crew
PRODUCT_NAME_RE = re.compile(
    r"\b(?!Kiro (?:IDE|CLI|Web|Mobile|Crew)\b)"
    r"[Kk][Ii][Rr][Oo]\s+(?:[Ii][Dd][Ee]|[Cc][Ll][Ii]|[Ww][Ee][Bb]|[Mm][Oo][Bb][Ii][Ll][Ee]|[Cc][Rr][Ee][Ww])\b")

# ------------------------------------------------------------
# (c) 非 ISO 日付
# ------------------------------------------------------------
MONTHS = (r"(?:January|February|March|April|May|June|July|August|September|"
          r"October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)")
EN_DATE_RE = re.compile(rf"\b{MONTHS}\.?\s+\d{{1,2}},\s*\d{{4}}")
DATE_OK_RE = re.compile(r"Page updated|Last Updated|出典|公式|引用|原文|形式|表記|>")

# ------------------------------------------------------------
# (e) 取得日の混入
# ------------------------------------------------------------
FETCH_DATE_RE = re.compile(r"取得日\s*[:：]|取得日は\s*\d{4}|\d{4}-\d{2}-\d{2}\s*(?:に)?取得")

# ------------------------------------------------------------
# (f) autolink 事故
# ------------------------------------------------------------
# ⚠ 直前が日本語（Python の \w に含まれる）でも検出できるよう、\b ではなく
#    「英数字・括弧・< が直前に無い」ことで URL の先頭を判定する。
BARE_URL_FULLWIDTH_RE = re.compile(
    r"(?<![A-Za-z0-9<(\[/])https?://[^\s<>()\[\]`]+[０-９Ａ-Ｚａ-ｚぁ-んァ-ヶ一-龠、。（）「」]")

# ------------------------------------------------------------
# (g) 禁止表現
# ------------------------------------------------------------
BANNED = ["おそらく", "たぶん", "多分", "一般的に", "通常", "と思われる", "と思われます",
          "かもしれない", "かもしれません", "だろう", "でしょう", "予想されます"]
BANNED_RE = [re.compile(r"最低\s*[^。]{0,12}以上")]

# ------------------------------------------------------------
# (i) 所属企業名の非掲載
# ------------------------------------------------------------
AFFILIATION_RE = re.compile(r"勤務先|弊社|自社|職場|所属企業|当社|所属先")


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def is_local_only(path):
    norm = path.replace(os.sep, "/")
    return any(f"/{lo}/" in norm or norm.startswith(f"{lo}/") for lo in LOCAL_ONLY)


def target_files():
    files = sorted(glob.glob(f"{DOC_ROOT}/**/*.md", recursive=True))
    files = [f for f in files if not is_local_only(f)]
    files += ["README.md"] + sorted(glob.glob(".github/*.md"))
    return [f for f in files if os.path.isfile(f)]


def code_line_flags(path):
    """各行がフェンスコードブロック内かどうかを返す（1-indexed）。"""
    flags = {}
    in_fence = False
    for i, line in enumerate(open(path, encoding="utf-8"), 1):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            flags[i] = True
            continue
        flags[i] = in_fence
    return flags


def strip_inline_code(line):
    return re.sub(r"`[^`]*`", "", line)


def main():
    os.chdir(repo_root())
    print("=== kiro-all-docs 表記規約チェック ===")
    print("")

    errors = []
    stats = {"files": 0, "lines": 0}

    for path in target_files():
        stats["files"] += 1
        in_code = code_line_flags(path)
        is_policy = path in POLICY_DOCS

        for i, raw in enumerate(open(path, encoding="utf-8"), 1):
            stats["lines"] += 1
            if in_code.get(i, False):
                continue
            line = strip_inline_code(raw)

            # (b) 製品名の揺れ
            for m in PRODUCT_NAME_RE.finditer(line):
                errors.append(
                    f"{path}:{i} (b) 製品名の表記が揺れています: {m.group(0)!r}"
                    "（正: Kiro IDE / Kiro CLI / Kiro Web / Kiro Mobile / Kiro Crew）"
                )

            # (c) 非 ISO 日付
            for m in EN_DATE_RE.finditer(line):
                if not DATE_OK_RE.search(line):
                    errors.append(
                        f"{path}:{i} (c) 英語表記の日付が出典・引用以外で使われています: "
                        f"{m.group(0)!r}（本文は ISO `YYYY-MM-DD`）"
                    )

            # (e) 取得日の混入
            if not is_policy and FETCH_DATE_RE.search(line):
                errors.append(
                    f"{path}:{i} (e) 取得日が本文に書かれています"
                    "（取得日は作業記録に残し、本文には公式の表示日を書きます）"
                )

            # (f) autolink 事故（インラインコード内の URL は描画されないので対象外）
            m = BARE_URL_FULLWIDTH_RE.search(line)
            if m:
                errors.append(
                    f"{path}:{i} (f) 裸の URL の直後に全角文字があります: {m.group(0)[-40:]!r}"
                    "（`<https://...>` で囲むか半角空白を入れてください）"
                )

            # (g) 禁止表現
            if not is_policy:
                for w in BANNED:
                    if w in line:
                        errors.append(
                            f"{path}:{i} (g) 推測・曖昧表現が使われています: {w!r}"
                            "（一次情報で確認して断定するか「未確認」と明示してください）"
                        )
                for pat in BANNED_RE:
                    m = pat.search(line)
                    if m:
                        errors.append(
                            f"{path}:{i} (g) 根拠のない範囲表現です: {m.group(0)!r}"
                        )

            # (i) 所属企業名の非掲載
            if not is_policy:
                m = AFFILIATION_RE.search(line)
                if m:
                    errors.append(
                        f"{path}:{i} (i) 筆者の所属を示しうる語句があります: {m.group(0)!r}"
                        "（公開制限: 所属企業名・所属を推測させる記述は書かない。言い換えてください）"
                    )

    print(f"検査ファイル: {stats['files']} 件 / {stats['lines']} 行")
    print("")

    if errors:
        print(f"❌ エラー {len(errors)} 件:")
        for e in errors:
            print(f"   - {e}")
        print("")
        print("❌ 表記規約チェックに失敗しました")
        return 1

    print("✅ 表記規約に違反はありません")
    return 0


if __name__ == "__main__":
    sys.exit(main())
