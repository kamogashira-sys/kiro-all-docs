# なぜ筆者は Kiro CLI が好きなのか

> **本ページは筆者の意見です。** 事実の記述には公式の出典を付けていますが、「好き」「推し」の部分は筆者個人の選好であり、他のツールとの優劣を述べるものではありません。筆者は Claude Code と OpenAI Codex も使っています。本文中の「聞き取り」は、本サイトを作るときに筆者が自分の体験を 10 の質問に答えて整理した問答（2026-11-01）を指します。

## 出会い ― 2025 年 6 月、日本語の指示だけでゲームができた

筆者が初めて Amazon Q Developer CLI（Kiro CLI の前身）を使ったのは、2025-06-09 の JAWS-UG 横浜支部のイベントでした。Builder ID を作り、Q CLI を入れ、チャットを開くという 3 ステップの準備のあと、日本語の指示を 3 回出しただけで国旗当てクイズ（HTML・CSS・JavaScript）ができあがりました。そのときの気持ちは、Qiita 記事「『Amazon Q CLI でゲームを作ろう』をやってみた」（2025-06-16）に書いています。

> 🐾 **筆者のひとこと**: 「これが日本語の指示だけで作れる時代になったのかとかなりショックを受けました。生成AI恐るべし。」（Qiita 記事「『Amazon Q CLI でゲームを作ろう』をやってみた」の原文 <https://qiita.com/kamogashira/items/59c3e641d984920c22a3>）

「一番うれしかった体験は」という問いに、筆者はこの最初の衝撃を挙げました。以来、Q CLI 時代を含めて使い続けています（2026-04-23 の記事では「約10か月」と書いています。<https://qiita.com/kamogashira/items/0e9c9e4e60b032ad9621>）。

## 好きなところ 1 ― 「厳選して足す」姿勢

「選ぶ決め手を 1 つに絞ると」という問いへの答えは、機能の選び方でした。

> 🐾 **筆者のひとこと**: 「世の中Claude Codeが大流行りですが、私はKiro CLI推しです。いい意味でAWSが他のAI Agentから厳選した機能を実装して頂けているので基本的に困ることはあまりありません。」（Qiita 記事「猫でもわかるKiro CLI(CDKコーディング編)」の原文 <https://qiita.com/kamogashira/items/0e9c9e4e60b032ad9621>）

筆者の感覚では、Claude Code の機能追加の速さと量は、使い手として追い続けるのがつらい（これは筆者個人の体力の話で、製品の評価ではありません）。Kiro CLI は追いつける量で、筆者の仕事に必要なものは揃っている、というのが選ぶ決め手です。

## 好きなところ 2 ― マニュアル車の手触り

「これから Kiro を使う人に CLI から入ることを勧めるなら」という問いへの答えが、本サイトの README の 🐾 ブロックにも載せた一言です。

> 🐾 **筆者のひとこと**: かゆいところに手が届く。`/compact` などを自分で使えるのは、車でいうとマニュアル車。IDE 版はオートマ車で確かに楽だが、細かなところまで自分で操作する手触りは薄い、というのが私の感想です。

事実として裏付けられる部分を挙げます。公式ドキュメント「Compaction」（<https://kiro.dev/docs/compaction/>）の対応表では、会話を手動で圧縮する `/compact` は **CLI では使え、IDE には無い** と示されています。端末なら、文脈をいつ畳むかを自分で決められます。

## 好きなところ 3 ― 端末から出ずに済み、端末の外からも呼べる

- **端末から離れない。** Kiro CLI の公開ブログ（2025-11-17、<https://kiro.dev/blog/introducing-kiro-cli/>）が描いた「深夜 2 時にサーバーに SSH している最中、IDE に戻らずに AI の助けを得る」場面は、筆者の使い方そのものです。
- **custom agents。** 用途ごとにツール・権限・文脈を決めたエージェントを `.kiro/agents/` に置いて切り替える。筆者は姉妹サイト 4 本の調査・下書き・GitHub への登録に Kiro CLI を使っています。
- **headless。** `KIRO_API_KEY` を置けばブラウザなしで動き、CI に載せられる（2026-04-13、<https://kiro.dev/blog/cli-2-0/>）。
- **ACP で他のエディタからも。** 2026-02-05 の ACP 対応（<https://kiro.dev/blog/kiro-adopts-acp/>）以降、JetBrains IDE や Zed から同じ Kiro を呼べます。

## 好きなところ 4 ― モデルを選べて、請求は AWS にまとまる

筆者が「一番好きな機能・使い方」として最初に挙げたのは、機能そのものではなく運用面でした。

- **モデルを選べる。** 公式のモデル一覧（<https://kiro.dev/docs/models/available-models/>）には、Anthropic の Claude 各版、OpenAI の GPT-5.6（Sol・Terra・Luna）、GLM-5・DeepSeek 3.2・Kimi K3 といったオープンウェイト系（重みが公開されているモデル）が並びます。CLI では `/model` で切り替えられ、既定の Auto はタスクごとにモデルを自動で選びます。
- **請求が AWS にまとまる。** 組織で使う場合の話です。公式ドキュメントは、IAM Identity Center で Kiro を使う組織では、Kiro の費用が AWS コンソールの Billing and Cost Management に「Kiro」として表示されると説明しています（<https://kiro.dev/docs/enterprise/>）。AWS を使っている組織なら、エージェントの費用を別の請求先に分けずに済みます。

> 🐾 **筆者のひとこと**: Anthropic・OpenAI など多彩な LLM を 1 つの道具で使えて、AWS の請求にまとめられる。この 2 つが、仕事で使う道具として Kiro CLI を選ぶ最初の理由です。

## V3 になって ― 戸惑ったことと、よかったこと

V3（統一ハーネス）への移行で、筆者が「一番対応に時間がかかった」のは **権限（セキュリティ設定）の変化** でした。公式ブログは、V2 の「信頼するツールの一覧と個別設定」から V3 の「アクションとリソースに対するルール」へ変わり、deny が ask に、ask が allow に優先すると説明しています（<https://kiro.dev/blog/cli-3/>）。移行後に `/upgrade-agent diagnostics`（自動変換の結果と警告を表示するコマンド）で警告を確認する手順も同記事にあります。

よかったのは **hooks** です。V3 の hooks は独立した `.kiro/hooks/*.json` ファイルで、`SessionStart`・`PreToolUse`・`PostToolUse` などのトリガーを IDE・CLI・Web で共通に使えます（<https://kiro.dev/blog/one-agent/>）。

> 🐾 **筆者のひとこと**: Hooks はやっと他の AI エージェントと動作が合った、というのが正直な感想です（他製品との同等性は公式に記述が無いため、筆者の体験として書いています）。

表示モードについては、2026-04 の記事で「Classic モードで LLM の思考内容を確認するのが勉強になる」と書きましたが、今は TUI を使っています。LLM が賢くなり、筆者自身が LLM のクセを理解してきたので、以前のように思考を逐一確認する必要がなくなった、というのが理由です。CLI 3.0 で Classic が廃止されることは、筆者にとっては問題になりませんでした。

## まとめ

- 出会いは 2025-06-09。日本語だけでゲームができた衝撃が、今も一番の体験。
- 選ぶ決め手は「厳選して足す」姿勢。端末派の筆者には、`/compact` のように自分で操作できるマニュアル車の手触りが合っている。
- 道具としては、複数ベンダーのモデルを選べること、組織では AWS の請求にまとまること。
- V3 では権限の変化に時間がかかったが、hooks の統一は歓迎している。

どの入口が合うかは人と仕事によって違います。公式の選び方は「Which Kiro app should I pick?」（<https://kiro.dev/blog/which-kiro-app-should-i-pick/>）が、「どれを選ぶかではなく、この仕事にはどれか」と整理しています。

## 出典

| 出典 | 公開・更新日 |
|---|---|
| Qiita [「Amazon Q CLI でゲームを作ろう」をやってみた](https://qiita.com/kamogashira/items/59c3e641d984920c22a3) | 2025-06-16 |
| Qiita [猫でもわかるKiro CLI(CDKコーディング編)](https://qiita.com/kamogashira/items/0e9c9e4e60b032ad9621) | 2026-04-23 |
| [Bring Kiro agents to your terminal with Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/) | 2025-11-17 |
| [Specialized IDEs deserve AI too: Kiro adopts ACP](https://kiro.dev/blog/kiro-adopts-acp/) | 2026-02-05 |
| [Kiro CLI 2.0](https://kiro.dev/blog/cli-2-0/) | 2026-04-13 |
| [One agent, every surface](https://kiro.dev/blog/one-agent/) | 2026-08-03 |
| [Which Kiro app should I pick?](https://kiro.dev/blog/which-kiro-app-should-i-pick/) | 2026-08-12 |
| [Kiro CLI V3 is rolling out as the default experience](https://kiro.dev/blog/cli-3/) | 2026-10-09 |
| [Enterprise（Billing の節）](https://kiro.dev/docs/enterprise/)・[Available models](https://kiro.dev/docs/models/available-models/)・[Compaction](https://kiro.dev/docs/compaction/) | 公式ドキュメント |

## 次に読む <!-- sources: n/a -->

- [はじめ方 ― Kiro CLI を 3 ステップで](../00_start/03_get-started.md)
- [Kiro CLI の道](../01_story/03_cli-journey.md)
- [猫でもわかるKiro CLI アップデート情報](https://github.com/kamogashira-sys/q-cli-docs)（姉妹サイト。機能・設定・全版の解説）
