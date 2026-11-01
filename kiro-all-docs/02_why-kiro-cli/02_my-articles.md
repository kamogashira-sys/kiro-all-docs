# 筆者の記事 ― Qiita に書いた Kiro の話

> **本ページは筆者の記事の案内です。** 各記事の内容は筆者個人の体験と意見であり、公式の情報ではありません。要旨は記事本文の見出しと冒頭の記述に基づいています。

筆者は 2025 年 6 月に Amazon Q Developer CLI（Kiro CLI の前身）を使い始めてから、JAWS-UG（AWS のユーザーコミュニティ）での登壇内容を Qiita 記事に再構成してきました。本サイトの入口で紹介している 3 本と、その土台になった「猫でもわかる Q CLI・Kiro CLI」シリーズ 6 本を、公開日の新しい順に並べます。

## 本サイトが紹介する 3 本

### 猫でもわかるKiro Web ― 端末を閉じても働き続けるKiroの正体

- **公開日**: 2026-09-28 　**URL**: <https://qiita.com/kamogashira/items/b1dd5f5dec37ca75206e>
- **登壇**: JAWS-UG 栃木 オフライン #10（2026-09-26）の 10 分登壇の再構成
- **要旨**:
  1. Kiro は形態ごとに別々だったエージェント本体を「統一エージェントハーネス」へ一本化しつつあり、Kiro Web は公開当初からこの新系列で提供されている
  2. Kiro Web は AWS クラウド上の隔離されたサンドボックスで動く Kiro で、端末を閉じても働き続ける
  3. Automation（スケジュール実行）と Kiro Mobile を組み合わせると、物理マシンなしで「勝手に働き続ける Kiro」が作れる。Kiro Crew を入れる前に Kiro Web で足りないか考える価値がある
- **読む前の注意**: 記事中のサンドボックスのスペックは筆者が Kiro Web 上で Kiro 自身に調べさせた実機調査の値で、公式には公表されていません。記事自身がそう明記しています

### Kiro５兄弟のいまどきのセキュリティ基礎知識 ― Kiro CLIとDraw.io MCPで信頼境界を描くまで

- **公開日**: 2026-08-29（最終更新 2026-10-23） 　**URL**: <https://qiita.com/kamogashira/items/519a52614ba113bfe9cb>
- **登壇**: Security-JAWS 第42回（2026-08-26）の再構成
- **要旨**:
  1. Kiro 5 兄弟（IDE・CLI・Web・Mobile・Crew）を「2＋2＋1」で理解する。IDE と CLI は統一ハーネスへの統合が進行中で、権限設定の共通軸が `permissions.yaml`。一番重要なのは「どのエンジンで動いているか」
  2. Web と Mobile は同じクラウドセッションを見る 2 つの窓。「サンドボックスだから安全」ではない
  3. Kiro Crew は同じ「サンドボックス」という言葉でも別物。論理構成図・物理構成図・シーケンス図を Kiro CLI と Draw.io MCP で描き、誰を信頼しどこで判定するかを確かめる
- **読む前の注意**: 本文は 2026-08-26 時点の内容で、その後の更新箇所には日付が付いています。Kiro Crew の図は 2026-10-22 に v0.9.0 と照合した版に差し替えられています（記事の修正履歴）

### 猫でもわかるKiro CLI(CDKコーディング編)

- **公開日**: 2026-04-23 　**URL**: <https://qiita.com/kamogashira/items/0e9c9e4e60b032ad9621>
- **登壇**: JAWS-UG CDK支部 #25（2026-04-15）の再構成
- **要旨**:
  1. 約 10 か月、Q CLI の頃から使い続けてたどり着いた、Kiro CLI での AWS CDK（AWS のインフラをコードで定義するツール）コーディングの考え方
  2. 「AI になるべくコードを書かせない（CDK 限定）」。高品質なサンプルコード（aws-cdk-examples）をベースに、Kiro CLI にその内容を詳細に理解させてから改造する
  3. 「作業計画書が命」。緻密な作業計画書を作ってから修正に入る
- 本サイトの [なぜ筆者は Kiro CLI が好きなのか](01_why-i-love-kiro-cli.md) で引用している「世の中Claude Codeが大流行りですが、私はKiro CLI推しです」はこの記事の原文です

## 「猫でもわかる Q CLI・Kiro CLI」シリーズ（6 本）

上の CDK コーディング編は、このシリーズの第 6 弾です。シリーズ一覧は同記事の「猫でもわかるQ CLI・Kiro CLIシリーズ一覧」の表に基づき、公開日・タグは Qiita の記事メタデータです。Q CLI 時代の 3 本は、Kiro CLI の前身を知るうえでの参考として挙げます（Q CLI の仕様は現在の Kiro CLI と異なります）。

| # | 公開日 | 記事 | 対象 |
|---|---|---|---|
| 1 | 2025-08-05 | [猫でもわかるQ Developer CLI(CDK開発編)+ちょっとだけKiro](https://qiita.com/kamogashira/items/672fbc6cbc48c28364ff) | Amazon Q Developer CLI |
| 2 | 2025-11-03 | [「猫でもわかるAmazon Q Developer CLI 解体新書」爆誕！](https://qiita.com/kamogashira/items/ec2ed9b39052d55d4f13) | Amazon Q Developer CLI |
| 3 | 2025-11-16 | [猫でもわかるAmazon Q Developer CLI(できる子編)](https://qiita.com/kamogashira/items/95cc366b4a1815bc4c50) | Amazon Q Developer CLI |
| 4 | 2026-02-15 | [猫でもわかるKiro CLI(セキュリティ編)](https://qiita.com/kamogashira/items/52bbf8f66a8ce0cb9166) | Kiro CLI |
| 5 | 2026-03-15 | [猫でもわかるKiro CLI(仕様駆動開発への道編)](https://qiita.com/kamogashira/items/4f6dac31ab4919278412) | Kiro CLI |
| 6 | 2026-04-23 | [猫でもわかるKiro CLI(CDKコーディング編)](https://qiita.com/kamogashira/items/0e9c9e4e60b032ad9621) | Kiro CLI |

## 出会いの記事

| 公開日 | 記事 | 内容 |
|---|---|---|
| 2025-06-16 | [「Amazon Q CLI でゲームを作ろう」をやってみた](https://qiita.com/kamogashira/items/59c3e641d984920c22a3) | 2025-06-09 の JAWS-UG 横浜支部のイベントで、日本語の指示だけで国旗当てクイズができた体験。筆者が CLI 型エージェントを使い始めたきっかけ（[なぜ筆者は Kiro CLI が好きなのか](01_why-i-love-kiro-cli.md) の「出会い」） |

## 姉妹サイトとの関係

Qiita 記事は登壇の再構成で、「その時点のスナップショット」と記事自身が注記しています。版ごとの更新を追い続けているのは姉妹サイト 4 本（[Kiro IDE](https://github.com/kamogashira-sys/kiro-ide-docs)・[Kiro CLI](https://github.com/kamogashira-sys/q-cli-docs)・[Kiro Web](https://github.com/kamogashira-sys/kiro-web-docs)・[Kiro Crew](https://github.com/kamogashira-sys/kiro-crew-docs)）で、最新の仕様はそちらと公式ドキュメントで確認してください。

## 次に読む <!-- sources: n/a -->

- [なぜ筆者は Kiro CLI が好きなのか](01_why-i-love-kiro-cli.md)
- [Kiro CLI の道](../01_story/03_cli-journey.md)
- [目次](../README.md)
