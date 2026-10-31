# ドキュメント作成ワークフロー（kiro-all-docs）

本サイト「猫でもわかるKiro 入門 ― IDE・CLI・Web・Mobile・Crew まとめ」は、Kiro 全体を Kiro を知らない人に案内する **非公式** の日本語サイトです。機能の網羅は姉妹サイト（IDE・CLI・Web・Crew）に任せ、本サイトは **紹介・案内** に役割を絞ります。

## 1. 一次情報

| 対象 | 一次情報 |
|---|---|
| Kiro 全般 | kiro.dev のブログ・docs（`.md` companion と HTML）・changelog・`llms.txt`・sitemap |
| Kiro Crew | `kirodotdev/KiroCrew` リポジトリ・Releases・公式 docs |
| 旧 Amazon Q Developer CLI | `aws/amazon-q-developer-cli` リポジトリの README・Releases |
| 筆者の意見・体験 | 筆者の Qiita 記事（原文引用） |

GitHub Issues・他者ブログ・姉妹サイト（自サイト）は根拠にしません。姉妹サイトは「くわしくは」の行き先としてのみリンクします。

## 2. 執筆原則

1. 一次情報のみを根拠にする。推測で書かない。
2. 公式に確認できないことは「未確認」と書く。
3. 取得日を公開文書に書かない。「〜時点」は公式の表示日を使う。
4. Kiro IDE / CLI / Web / Mobile / Crew を混同しない。同名機能は仕様差を注記し、詳細は姉妹サイトへ送る。
5. 公式間の食い違いは新しい方を正とし、食い違いの存在も書く。
6. 事実と筆者の意見を書式で分ける。意見は `02_why-kiro-cli/` と `README.md` の 🐾 ブロック 1 個に集約する。Qiita 記事の引用は原文どおり。
7. 公式の画像・図は再配布しない。図は Mermaid で自作する。スクリーンショット・録画は使わない。
8. 公式の英文は自分の言葉で要旨を書く。原文引用は 1 箇所 30 語以内。全訳・長い抜き書き・原文の構成をなぞった翻訳はしない（AWS Site Terms はサイト内容の派生的利用を許諾していない）。
9. 「Kiro」「AWS」はプレーンテキストで、真実の事実を述べる文脈のみで使う（AWS Trademark Guidelines §13）。非公式であることを README と免責に明記する。
10. 筆者の所属企業名と、所属を推測させる記述は書かない。

## 3. 表記

- 日付は ISO `YYYY-MM-DD`。
- 禁止表現: 「おそらく」「たぶん」「一般的に」「通常」「最低〜以上」など推測・曖昧表現。
- kiro.dev の changelog / docs の URL は末尾スラッシュ必須（無しは 301）。
- 製品名は `Kiro IDE` / `Kiro CLI` / `Kiro Web` / `Kiro Mobile` / `Kiro Crew`。

## 4. 検証

```bash
make check-kiro-all-ignore   # 公開範囲（最初に実行）
make check-kiro-all-all      # links / notation（＋追加予定: sources / quotes / first-person）
make check-kiro-all-urls-important   # 外部 URL（手動・push 時 CI）
```

検証スクリプトを作成・改修したら、意図的に文書を壊して検出されることを確認します（ネガティブテスト）。

## 5. ローカル管理領域（GitHub 非公開）

`work_plans/`・`06_embedded-docs/`（kiro.dev の複製。再配布しない）・`work_records/`。`make check-kiro-all-ignore` で除外を確認します。
