# 情報源の使い分け ― 本サイトが何を根拠に書いているか

本サイトは紹介・案内の文書で、根拠は一次情報に限っています。本ページは、その一次情報が kiro.dev のどこにあり、どう読み分けているか、どこに落とし穴があるかをまとめたものです。姉妹サイト（[Kiro IDE](https://github.com/kamogashira-sys/kiro-ide-docs)・[Kiro CLI](https://github.com/kamogashira-sys/q-cli-docs)・[Kiro Web](https://github.com/kamogashira-sys/kiro-web-docs)・[Kiro Crew](https://github.com/kamogashira-sys/kiro-crew-docs)）の同名ページと同じ構成にしています。

**出典**: 本ページで挙げる各公式ページ（<https://kiro.dev/>・<https://github.com/kirodotdev/KiroCrew>・<https://github.com/aws/amazon-q-developer-cli>）。

---

## 📑 このページの内容
<!-- sources: n/a -->

1. [情報源の優先順位](#情報源の優先順位)
2. [落とし穴 1: ブログには `.md` 版が無い](#落とし穴-1-ブログには-md-版が無い)
3. [落とし穴 2: docs の `.md` 版は内容が欠けることがある](#落とし穴-2-docs-の-md-版は内容が欠けることがある)
4. [落とし穴 3: 日付の読み方](#落とし穴-3-日付の読み方)
5. [落とし穴 4: URL の末尾スラッシュと User-Agent](#落とし穴-4-url-の末尾スラッシュと-user-agent)
6. [落とし穴 5: 公式ページ間で記述が食い違うことがある](#落とし穴-5-公式ページ間で記述が食い違うことがある)
7. [本サイトの検証方法](#本サイトの検証方法)

## 情報源の優先順位

上位が下位を上書きします。**下位だけを根拠に書くことはしません。**

| 順位 | 情報源 | 本サイトでの用途 | 制約 |
|---|---|---|---|
| **1** | 公式ブログ（<https://kiro.dev/blog/>） | 開発経緯・設計判断・発表日。本サイトの `01_story/` の主な根拠 | **`.md` 版が無い**（下記）。本文は長く、要約は自分の言葉で最小限にする |
| **1** | 公式 changelog（IDE <https://kiro.dev/changelog/ide/>・CLI <https://kiro.dev/changelog/cli/>・Web <https://kiro.dev/changelog/web/>） | 版と公開日の正。「CLI 3.0 が公開されたか」のような事実の判定 | 系列ページが無い版は 404。版ごとの解説は姉妹サイトの役割 |
| **1** | Kiro Crew リポジトリ（<https://github.com/kirodotdev/KiroCrew>）と公式 docs（<https://kiro.dev/docs/crew/>） | Crew の仕様・版・ガバナンス | 本サイトは Crew の版ごとの追跡はしない（姉妹サイトの役割） |
| **1** | `aws/amazon-q-developer-cli` の README・Releases（<https://github.com/aws/amazon-q-developer-cli>） | 前身 Amazon Q Developer CLI の積極開発終了の告知と最終版 | Kiro CLI 自体の仕様の根拠にはしない |
| **2** | 公式ドキュメント（<https://kiro.dev/docs/>。HTML を正とし、`.md` companion を読みやすさのために使う） | 機能の定義・設定の置き場所・利用できる入口 | `.md` 版に既知の欠落がある（下記） |
| **3** | `llms.txt`（<https://kiro.dev/llms.txt>） | docs ページの全量と、各ページの 1 行説明。IDE / CLI / Web / Crew / Mobile の区分 | 字下げをページ階層の根拠にしない |
| **4** | `sitemap.xml`（<https://kiro.dev/sitemap.xml>） | ブログ記事の全量の機械検証（[公式ブログ索引](01_blog-index.md) の収録範囲の正。索引の分類・必読度・内容説明は本サイトが各記事を読んで付けたもの） | `/blog/page/N/` と feed は記事ではない |
| **5** | Atom フィード（<https://kiro.dev/changelog/feed.atom>） | 新しい更新の速報検知のみ | 直近の一定件数しか入らず、網羅性がない。日付の時刻はタイムゾーンの扱いが要るので使わない |
| **—** | 筆者の Qiita 記事（<https://qiita.com/kamogashira>） | 筆者の意見・体験の原文（`02_why-kiro-cli/` のみ） | 事実の根拠にはしない |

根拠にしないもの: GitHub Issues（<https://github.com/kirodotdev/Kiro>）、他者のブログ、姉妹サイト（自サイト）。姉妹サイトは「くわしくは」の行き先としてのみリンクします。

## 落とし穴 1: ブログには `.md` 版が無い

公式ドキュメントは URL に `.md` を付けると Markdown 版が取れます（例: <https://kiro.dev/docs/how-kiro-works.md>）。`llms.txt` 自身がこの仕組みを説明しています。**公式ブログにはこの仕組みがありません**。`https://kiro.dev/blog/<slug>.md` は 404 です。ブログ本文は Next.js の RSC（React Server Components）形式で HTML に埋め込まれており、本文だけを取り出すには変換が要ります。

本サイトは、ブログを根拠にする箇所では記事ページ（HTML）を読み、要旨を自分の言葉で書いています。原文の引用は 1 箇所 30 語以内にとどめ、記事の全訳や長い抜き書きはしていません（権利上の理由。[方針](../../README.md#-本サイトの方針)）。

## 落とし穴 2: docs の `.md` 版は内容が欠けることがある

姉妹サイトが実測して記録している既知の欠落です。本サイトでも、`.md` 版で読んだ内容は HTML で確認しています。

| 欠落 | 症状 |
|---|---|
| プレースホルダが潰れる | 波かっこや `${…}` のプレースホルダが空文字や `$` になる |
| 共有ページで複数サーフェスの内容が連結される | IDE / CLI / Web の記述が区切りなく続き、どのサーフェスの記述か判別できない |
| 移転したページの `.md` が 404 になる | 旧 URL の `.md` を取得すると空ファイルになり、「検証したつもり」になる。404 を無視しないこと |
| 折りたたまれた項目が無い | HTML でも `.md` でも、画面で折りたたまれている項目は本文に出てこないことがある |

詳細は姉妹サイトの各「情報源の使い分け」ページに実測値つきで書かれています（例: [Kiro Web 版](https://github.com/kamogashira-sys/kiro-web-docs/blob/main/kiro-web-docs/00_information/02_information-sources.md)）。

## 落とし穴 3: 日付の読み方

公式ページ（ブログ <https://kiro.dev/blog/>・changelog <https://kiro.dev/changelog/cli/>・docs <https://kiro.dev/docs/>）に出る日付の形と、本サイトでの扱いです。

| 場所 | 表記 | 本サイトの扱い |
|---|---|---|
| ブログ記事ページ | 月名フル（例: `August 3, 2026`） | 記事の公開日として、ISO 形式（`2026-08-03`）で書く |
| changelog の各エントリ | 月名フル | 版の公開日の正 |
| docs の各ページ | `Page updated:` の後に月名フル | 「更新日」として出典表に書く。ページ本文に埋め込まれた構造化データ（JSON-LD）の `dateModified` にも同じ日付が ISO 形式で入っている |
| Atom フィード | 時刻付き | 使わない（タイムゾーン変換が要るため） |

本サイトは日付をすべて ISO 形式で書き、**タイムゾーンの変換はしません**。公式ページの表示日をそのまま日付として扱います。また、**本サイトがいつ情報を取得したかは公開文書に書きません**。公式の日付と混同されるためです。

> ⚠ docs の `Page updated:` の日付は、HTML 上で React のコメントマーカーに分断されています（`Page updated:<!-- --> <!-- -->October 23, 2026` の形）。単純な文字列検索では見つからないので、機械的に取るときは `dateModified` を使うのが確実です。

## 落とし穴 4: URL の末尾スラッシュと User-Agent

kiro.dev（<https://kiro.dev/>）のページは末尾スラッシュ付きが正の URL で、無しは 301 でリダイレクトされます。機械的に取得するときは末尾スラッシュを付けてください。User-Agent を空文字で明示すると 403 になります（既定のままなら問題ありません）。

## 落とし穴 5: 公式ページ間で記述が食い違うことがある

同じ事項について、ブログと docs、あるいは docs 同士で記述が異なることがあります。本サイトは **更新日の新しい方を正とし、食い違いの存在自体も本文に書きます**。どちらを正とすべきか判断できない場合は「未確認」と書き、両方の記述を示します。

例: 公式ドキュメント「What's new in CLI V3」（<https://kiro.dev/docs/cli/v3/>、更新日 2026-10-31）は V3 を「early release」と呼び opt-in を前提に書いていますが、2026-10-09 の公式ブログは V3 を既定の体験にするロールアウトを告知しています。更新日は docs の方が新しいので、本サイトは「段階的なロールアウトの途中で、opt-in も有効」と読み、両方の記述があることを [Kiro CLI の道](../01_story/03_cli-journey.md) に注記しています。

## 本サイトの検証方法
<!-- sources: n/a -->

| 検査 | 内容 | 実行 |
|---|---|---|
| links | 内部リンクの実在、見出しアンカー（日本語含む）、kiro.dev URL の書式 | `make check-kiro-all-links`・CI |
| notation | 製品名の揺れ、非 ISO 日付、取得日の記載、禁止表現、所属を推測させる語句 | `make check-kiro-all-notation`・CI |
| sources | `00_start/`・`01_story/`・`03_reference/` の各 H2 節に出典リンクがあるか | `make check-kiro-all-sources`・CI |
| quotes | 英文引用が 1 箇所 30 語以内か | `make check-kiro-all-quotes`・CI |
| first-person | 🐾 ブロックと `02_why-kiro-cli/` の外に一人称と筆者の選好を示す語が無いか（警告） | `make check-kiro-all-first-person`・CI |
| blog-index-count | [公式ブログ索引](01_blog-index.md) の件数 = README の収録範囲行の N、索引 = TSV から再生成した内容 | `make check-kiro-all-blog-index-count`・CI |
| structure | 各ページの骨格（出典ブロックが冒頭にある、目次がある、H2 に番号が無い、末尾が「次に読む」）とセクション README・README のページ数 | `make check-kiro-all-structure`・CI |
| blog-sync | 索引の元データと `sitemap.xml` の差分 | `make check-kiro-all-blog-sync`・手動のみ |
| urls-important | 公式・姉妹サイト・Qiita の URL の到達性 | `make check-kiro-all-urls-important`・CI |
| ignore | 公開範囲（ローカル管理領域が追跡されていないこと） | `make check-kiro-all-ignore`・CI |

毎日の公式更新の監視は本サイトでは行いません（姉妹サイトの役割）。本サイトは収録範囲を明記した紹介文書です。 更新の手順と各ページの書式は [更新手順書](../../.github/UPDATE_GUIDE.md) にまとめています。

## 次に読む
<!-- sources: n/a -->

- [公式ブログ索引](01_blog-index.md)
- [用語集](02_glossary.md)
- [目次](../README.md)
