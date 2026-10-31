# コミット前チェックリスト（kiro-all-docs）

## 公開範囲（最初に）

- [ ] `make check-kiro-all-ignore` が exit 0（`work_plans/`・`06_embedded-docs/`・`work_records/` が追跡されていない。ローカル絶対パスが公開ファイルに無い）

## 内容

- [ ] 事実の記述に一次情報（kiro.dev・`kirodotdev/KiroCrew`・`aws/amazon-q-developer-cli`）の出典がある
- [ ] 公式に確認できないことは「未確認」と書いた
- [ ] 要旨は自分の言葉。英文引用は 1 箇所 30 語以内。全訳・長い抜き書きをしていない
- [ ] 筆者の意見は `02_why-kiro-cli/` または `README.md` の 🐾 ブロック 1 個だけにある
- [ ] Qiita 記事の引用は原文どおり（言い換えは「（記事 N の趣旨）」と明示）
- [ ] Kiro IDE / CLI / Web / Mobile / Crew を混同していない
- [ ] 公式の画像・ロゴ・スクリーンショットを使っていない（図は Mermaid）
- [ ] 筆者の所属企業名・所属を推測させる記述が無い
- [ ] CLI 3.0 の記述は、公式 changelog（`https://kiro.dev/changelog/cli/`）の実測と一致している

## 表記

- [ ] 日付は ISO `YYYY-MM-DD`。取得日を本文に書いていない
- [ ] 禁止表現（おそらく・たぶん・一般的に・通常・最低〜以上）が無い
- [ ] kiro.dev の URL は末尾スラッシュ付き

## 機械検証

- [ ] `make check-kiro-all-all` が exit 0
- [ ] 新規ページを README・目次に追加した（存在しないページへのリンクを置いていない）
- [ ] 検証スクリプトを変更した場合、ネガティブテストを行った
