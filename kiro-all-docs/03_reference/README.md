# 03_reference - リファレンス

**公式の記事を自分で追う人、言葉につまずいた人、本サイトの根拠を確かめたい人のためのセクションです。**

---

## 📂 このセクションのファイル <!-- sources: n/a -->

| ファイル | 内容 |
|---------|------|
| [01_blog-index.md](01_blog-index.md) | **公式ブログ索引**。kiro.dev 公式ブログ全記事の公開日・タイトル・分類タグ・必読度（★1〜3）・内容説明 1〜2 行。`gen-blog-index.py` で `blog-index.tsv` から生成 |
| [02_glossary.md](02_glossary.md) | **用語集**。agent harness・surface・ACP・Specs・Steering・Hooks・MCP・Powers・Skills・permissions など、本サイトと公式ドキュメントに繰り返し出る言葉 |
| [03_sources.md](03_sources.md) | **情報源の使い分け**。本サイトが何を根拠に書いているか。優先順位、ブログに `.md` 版が無いこと、日付の読み方、公式間の食い違いの扱い、検証方法 |

---

## 索引の更新

索引の元データは `scripts/kiro-all-docs/blog-index.tsv` です。公式 sitemap（<https://kiro.dev/sitemap.xml>）との差分は `make check-kiro-all-blog-sync`（手動）で確認し、追記後に `make gen-kiro-all-blog-index` で再生成します。手順は [公式ブログ索引](01_blog-index.md) の末尾にあります。

---

## 主な出典

- 公式ブログ <https://kiro.dev/blog/>・公式ドキュメント <https://kiro.dev/docs/>・`llms.txt` <https://kiro.dev/llms.txt>・sitemap <https://kiro.dev/sitemap.xml>

[サイト全体の目次](../README.md)
