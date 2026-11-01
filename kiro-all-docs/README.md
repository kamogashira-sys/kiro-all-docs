# 猫でもわかるKiro 入門 ― 目次

入口は [リポジトリの README](../README.md) にあります。本ページはサイト本体の目次です。

## はじめての人向け（`00_start/`）

| ページ | 内容 |
|---|---|
| [Kiro とは ― 1 つのエージェント、どこでも同じ](00_start/01_what-is-kiro.md) | 公式「How Kiro works」に基づく全体像。1 ターンの 6 段階、ハーネスが持つ機能の 1 行説明、設定の 4 つのスコープ、どこで動くか、入口が足すもの |
| [どのアプリを選ぶか ― 「どれか」ではなく「この仕事にはどれか」](00_start/02_which-app.md) | 公式「Which Kiro app should I pick?」の要旨。2 つの原則、入口ごとの説明と公式ドキュメントの冒頭、早見表 |
| [はじめ方 ― Kiro CLI を 3 ステップで、ほかの入口は公式へ](00_start/03_get-started.md) | インストール → サインイン → 最初の 1 プロンプト（公式手順）。IDE・Web・Mobile・Crew・ACP エディタの導線 |

## 開発経緯・秘話（`01_story/`）

| ページ | 内容 |
|---|---|
| [Kiro の年表 ― 節目の記事だけを選んで](01_story/01_timeline.md) | 公式ブログ 113 本から節目の 30 本を選び、各 1〜2 行の要旨。2025-07-14 の誕生から 2026-10 の memory まで |
| [1 つのエージェント、5 つの入口 ― Kiro がハーネスを統一した話](01_story/02_one-agent.md) | 設定が自分に付いて回る理由。3 つのハーネスが 1 つになった経緯と成果、Crew の例外、技術的な判断 |
| [Kiro CLI の道 ― Amazon Q Developer CLI から V3 へ](01_story/03_cli-journey.md) | 2025-11-17 の誕生から ACP・新 TUI・2.0・V3 早期提供・既定化まで。CLI 3.0 の現在の状態 |
| [Kiro Crew の起源 ― MeshClaw から software factory へ](01_story/04_crew-origin.md) | 社内 side project から OSS 公開へ。原則から外れて出荷した理由、3 人で週 1,000 PR、品質を保つ仕組み |

## 筆者の推し（`02_why-kiro-cli/`）

| ページ | 内容 |
|---|---|
| [なぜ筆者は Kiro CLI が好きなのか](02_why-kiro-cli/01_why-i-love-kiro-cli.md) | 筆者の意見ページ。出会い、選ぶ理由、マニュアル車の手触り、V3 で変わったこと |
| [筆者の記事 ― Qiita に書いた Kiro の話](02_why-kiro-cli/02_my-articles.md) | 本サイトが紹介する 3 本の公開日・登壇・要旨、「猫でもわかる Q CLI・Kiro CLI」シリーズ 6 本、出会いの記事 |

## リファレンス（`03_reference/`）

| ページ | 内容 |
|---|---|
| [公式ブログ索引](03_reference/01_blog-index.md) | kiro.dev 公式ブログ全記事の公開日・タイトル・分類タグ（機械生成。要約なし） |
| [用語集](03_reference/02_glossary.md) | agent harness・surface・ACP・Specs・Steering・Hooks・MCP・Powers・Skills・permissions など、本サイトと公式ドキュメントに繰り返し出る言葉 |
| [情報源の使い分け](03_reference/03_sources.md) | 本サイトが何を根拠に書いているか。優先順位、ブログに `.md` 版が無いこと、日付の読み方、公式間の食い違いの扱い、検証方法 |

## 読む順番の例

| あなたは | 順番 |
|---|---|
| Kiro を初めて知った | [Kiro とは](00_start/01_what-is-kiro.md) → [どのアプリを選ぶか](00_start/02_which-app.md) → [はじめ方](00_start/03_get-started.md) |
| 「なぜ今 Kiro か」を知りたい | [1 つのエージェント、5 つの入口](01_story/02_one-agent.md) → [Kiro の年表](01_story/01_timeline.md) → [Kiro CLI の道](01_story/03_cli-journey.md) |
| 言葉が分からなくて止まった | [用語集](03_reference/02_glossary.md) |
| 公式の記事を自分で追いたい | [公式ブログ索引](03_reference/01_blog-index.md) → [情報源の使い分け](03_reference/03_sources.md) |
