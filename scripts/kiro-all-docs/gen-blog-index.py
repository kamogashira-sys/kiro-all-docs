#!/usr/bin/env python3
"""gen-blog-index.py - 公式ブログ索引（kiro-all-docs/03_reference/01_blog-index.md）を機械生成する

使用方法:
    ./scripts/kiro-all-docs/gen-blog-index.py            # 生成して書き込む
    ./scripts/kiro-all-docs/gen-blog-index.py --check    # 生成結果と現状ファイルの差分を確認（書き込まない）

入力: scripts/kiro-all-docs/blog-index.tsv（ヘッダ行 + date / slug / title / tag）
    - date  : 公式記事ページの表示日（ISO）
    - slug  : https://kiro.dev/blog/<slug>/ の <slug>
    - title : 公式記事の <title>（原文のまま）
    - tag   : 本サイトの分類（製品発表／モデル／料金／事例／技術解説／コミュニティ のいずれか 1 つ）

規則（作業計画 §5-5 `01_blog-index.md`・F1）:
    - 日付・タイトル・分類タグのみ。1 行要約は付けない
    - 新しい記事が上（日付降順。同日は slug 昇順）
    - 冒頭に「収録範囲: 公式ブログ 2025-07-14〜YYYY-MM-DD 公開分（N 本）」の 1 行を置く
      （README の収録範囲行と件数が一致することを check-blog-index-count.py が検査する）
"""
import csv
import os
import sys
from collections import Counter

TAGS = ("製品発表", "モデル", "料金", "事例", "技術解説", "コミュニティ")
TAG_DESC = {
    "製品発表": "新しい製品・機能・サーフェスの公開告知",
    "モデル": "利用できる AI モデルの追加・変更",
    "料金": "料金プラン・クレジット・無料枠・学生／スタートアップ向けプログラム",
    "事例": "顧客・社内チーム・コミュニティの利用事例",
    "技術解説": "仕組み・設計判断・使い方の解説",
    "コミュニティ": "ハッカソン・コミュニティハブ・周年など",
}


def repo_root():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def load_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter="\t")
        rows = list(reader)
    for r in rows:
        if r["tag"] not in TAGS:
            sys.exit(f"ERROR: 未定義の分類タグ: {r['slug']} -> {r['tag']}")
        if len(r["date"]) != 10 or r["date"][4] != "-" or r["date"][7] != "-":
            sys.exit(f"ERROR: 日付が ISO 形式でない: {r['slug']} -> {r['date']}")
    slugs = [r["slug"] for r in rows]
    dup = [s for s, c in Counter(slugs).items() if c > 1]
    if dup:
        sys.exit(f"ERROR: slug が重複: {dup}")
    return rows


def render(rows):
    rows = sorted(rows, key=lambda r: (r["date"], r["slug"]), reverse=True)
    # 同日は slug 昇順にしたいので日付ごとに並べ直す
    by_date = {}
    for r in rows:
        by_date.setdefault(r["date"], []).append(r)
    ordered = []
    for d in sorted(by_date, reverse=True):
        ordered.extend(sorted(by_date[d], key=lambda r: r["slug"]))

    first = min(r["date"] for r in rows)
    last = max(r["date"] for r in rows)
    n = len(rows)
    counts = Counter(r["tag"] for r in rows)

    out = []
    out.append("# 公式ブログ索引")
    out.append("")
    out.append(f"**収録範囲: 公式ブログ {first}〜{last} 公開分（{n} 本）**")
    out.append("")
    out.append("kiro.dev の公式ブログ（<https://kiro.dev/blog/>）の全記事を、公開日・タイトル・本サイトの分類タグだけで一覧にしたものです。"
               "要約は付けていません。各記事の内容は公式ページで読んでください。節目の記事の要旨は [Kiro の年表](../01_story/01_timeline.md) にあります。")
    out.append("")
    out.append("- 日付は各記事ページの表示日です（ISO 形式 `YYYY-MM-DD`）。新しい記事が上です。")
    out.append("- タイトルは公式の原文です。")
    out.append("- **分類タグは本サイトが付けたもの**で、公式の分類ではありません。1 記事に 1 つだけ付けています。")
    out.append("- このページは `scripts/kiro-all-docs/gen-blog-index.py` が `blog-index.tsv` から生成しています。手で編集しないでください。")
    out.append("")
    out.append("## 分類タグ <!-- sources: n/a -->")
    out.append("")
    out.append("| タグ | 意味 | 本数 |")
    out.append("|---|---|---|")
    for t in TAGS:
        out.append(f"| {t} | {TAG_DESC[t]} | {counts.get(t, 0)} |")
    out.append("")
    out.append("## 一覧")
    out.append("")
    out.append("| 公開日 | タイトル | 分類 |")
    out.append("|---|---|---|")
    for r in ordered:
        title = r["title"].replace("|", "\\|")
        out.append(f"| {r['date']} | [{title}](https://kiro.dev/blog/{r['slug']}/) | {r['tag']} |")
    out.append("")
    out.append("## 索引の更新方法 <!-- sources: n/a -->")
    out.append("")
    out.append("1. `make check-kiro-all-blog-sync` で公式 sitemap と `blog-index.tsv` の差分を確認する（手動のみ。CI では実行しない）")
    out.append("2. 差分の記事ページを開き、表示日・`<title>` を `blog-index.tsv` に追記し、分類タグを付ける")
    out.append("3. `./scripts/kiro-all-docs/gen-blog-index.py` で本ページを再生成する")
    out.append("4. リポジトリ README の収録範囲行を本ページの 1 行目と同じ値に更新する（`make check-kiro-all-blog-index-count` が一致を検査する）")
    out.append("")
    out.append("## 次に読む <!-- sources: n/a -->")
    out.append("")
    out.append("- [Kiro の年表 ― 節目の記事だけを選んで](../01_story/01_timeline.md)")
    out.append("- [情報源の使い分け](03_sources.md)")
    out.append("- [目次](../README.md)")
    return "\n".join(out) + "\n"


def main():
    root = repo_root()
    tsv = os.path.join(root, "scripts", "kiro-all-docs", "blog-index.tsv")
    target = os.path.join(root, "kiro-all-docs", "03_reference", "01_blog-index.md")
    rows = load_rows(tsv)
    text = render(rows)
    if "--check" in sys.argv:
        cur = open(target, encoding="utf-8").read() if os.path.exists(target) else ""
        if cur == text:
            print(f"OK: {os.path.relpath(target, root)} は TSV と一致（{len(rows)} 本）")
            return 0
        print(f"NG: {os.path.relpath(target, root)} が TSV から生成した内容と異なる。gen-blog-index.py を実行してください")
        return 1
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"生成: {os.path.relpath(target, root)}（{len(rows)} 本、{min(r['date'] for r in rows)}〜{max(r['date'] for r in rows)}）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
