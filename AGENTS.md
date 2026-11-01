# kiro-all-docs 作業規約（エージェント向け）

## 適用範囲

本ファイルは、リポジトリ `kamogashira-sys/kiro-all-docs`（「猫でもわかるKiro 入門 ― IDE・CLI・Web・Mobile・Crew まとめ」。Kiro 全体の非公式日本語案内サイト）での作業にだけ適用します。成果物は公開されます。

## 品質優先

- 一次情報（kiro.dev のブログ・docs・changelog、`kirodotdev/KiroCrew`、`aws/amazon-q-developer-cli` の告知）で確認できたことだけを書く。確認できないことは「未確認」と書く
- 速さより正確さを優先し、検証工程を省略しない
- 推測表現（おそらく・たぶん・一般的に・通常・最低〜以上）を使わない
- 取得日・実機の版番号・コマンド出力を解説ページ（`00_start/`・`01_story/`・`03_reference/`）に書かない
- 筆者の意見は `kiro-all-docs/02_why-kiro-cli/` と `README.md` の 🐾 ブロック 1 個にだけ書く
- 公式間の食い違いは更新日の新しい方を正とし、食い違いの存在も本文に書く

## 更新手順

更新は次の手順書に従います。

#[[file:.github/UPDATE_GUIDE.md]]

- ページの書式は手順書 §7（出典は冒頭・目次あり・H2 に番号なし・末尾は「次に読む」）
- 作業は feature branch で行い、PR を作る。`main` への直接 push はしない
- 禁止事項は手順書 §11

## コミット前の順序

1. 対象ファイルを名前で指定して `git add`（`git add .` は使わない）
2. `make check-kiro-all-ignore`（exit 0）
3. `make check-kiro-all-all`（exit 0。first-person の警告は全件を目視で判断する）
4. 外部 URL を追加・変更した場合は `make check-kiro-all-urls-important`（exit 0）
5. コミット（`docs: <要旨>`／`chore: <要旨>`）
6. 作業記録をリポジトリ外のローカル管理領域 `work_records/YYYYMMDD/` に追記（JST。日時は `date` コマンドで取得）
