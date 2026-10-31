# Kiro CLI の道 ― Amazon Q Developer CLI から V3 へ

Kiro CLI は、2025-11-17 に Amazon Q Developer CLI の技術を引き継いで生まれ、約 1 年で「別の見た目の CLI」から「Kiro IDE・Kiro Web と同じエージェント本体を端末で動かすクライアント」へ変わりました。本ページは、その節目を公式ブログ・公式 changelog・公式リポジトリの告知に基づいて追います。

```mermaid
timeline
  title Kiro CLI の節目（公式の公開日）
  2025-11-17 : Amazon Q Developer CLI が v1.19.7 で積極開発を終了
             : Kiro CLI 公開（Kiro GA と同日）
  2026-02-05 : ACP 対応（JetBrains・Zed・Emacs・Neovim などから Kiro を使える）
  2026-03-23 : 新 TUI を実験提供（kiro-cli --tui）
  2026-04-13 : CLI 2.0（headless・Windows ネイティブ・TUI が既定）
  2026-06-17 : 2.8.0 で V3 を早期提供（kiro-cli --v3）
  2026-10-09 : V3 を既定にするロールアウトを告知（10-12 開始）
  2026-10 末 : CLI 3.0 を予告（本ページ執筆時点で公式 changelog に未掲載）
```

（図は公式の公開日をもとに本サイトが作成）

## 前史 ― Amazon Q Developer CLI の終わりと Kiro CLI の始まり

Kiro CLI の前身は Amazon Q Developer CLI（Q CLI）です。公式リポジトリ `aws/amazon-q-developer-cli` の README は、このプロジェクトが積極的な保守を終え、重要なセキュリティ修正のみを受けること、そして Kiro CLI がクローズドソース製品として提供されることを告知しています（原文: 「no longer being actively maintained and will only receive critical security fixes」<https://github.com/aws/amazon-q-developer-cli>）。最終リリース v1.19.7 の公開日は 2025-11-17 です（GitHub Releases）。

同じ 2025-11-17、Kiro は一般提供（GA）になり、Kiro CLI が公開されました。公式ブログ「Bring Kiro agents to your terminal with Kiro CLI」（<https://kiro.dev/blog/introducing-kiro-cli/>）は、Kiro CLI が Q Developer CLI のエージェント機能（agent mode・MCP・steering・custom agents）を引き継ぎ、ソーシャルログイン・Haiku 4.5・Auto エージェントを足したものだと説明しています。この時点ですでに、`.kiro` フォルダの設定（steering・MCP）が IDE と CLI で共用できることが売りでした。GA 発表（<https://kiro.dev/blog/general-availability/>）では、property-based testing・checkpointing・multi-root workspace と並ぶ 4 本柱の 1 つとして CLI が紹介されています。

## 2026 年前半 ― 端末の外へ、そして新しい顔

- **ACP 対応（2026-02-05）**: 公式ブログ「Specialized IDEs deserve AI too: Kiro adopts ACP」（<https://kiro.dev/blog/kiro-adopts-acp/>）。Kiro CLI が Agent Client Protocol に対応し、JetBrains IDE・Zed・Emacs・Neovim・Eclipse などの ACP 対応エディタから Kiro のエージェントを使えるようになりました。記事では JetBrains DataGrip から Kiro を使う例が示されています。ACP はのちに Kiro 自身のクライアントとハーネスの境界にも採用されます（[ハーネス統一の話](02_one-agent.md)）。
- **新しい TUI（2026-03-23）**: 公式ブログ「A new look for the Kiro CLI」（<https://kiro.dev/blog/new-look-for-cli/>）。1 行ずつ出力する従来の方式では、サブエージェントや複数エージェントの時代に限界があるとして、`kiro-cli --tui` で新しい端末 UI を実験提供。常時使える入力欄、`/` コマンドと `@` コンテキストのドロップダウン、ツール実行状況のライブ表示が特徴です。記事は「We love the terminal.」の一文で始まります。
- **CLI 2.0（2026-04-13）**: 公式ブログ「Kiro CLI 2.0」（<https://kiro.dev/blog/cli-2-0/>）。(1) **headless mode**: API キーを環境変数 `KIRO_API_KEY` に置けばブラウザなしで動き、CI/CD パイプラインに組み込める（解説記事 <https://kiro.dev/blog/introducing-headless-mode/>）(2) **Windows ネイティブ対応**（WSL 不要）(3) **TUI が既定**（`kiro-cli --classic` で従来表示に戻せる）。

## 導入事例 ― 公式ブログが紹介した 2 件

- **EC2 チーム「Root cause in 33 seconds」（2026-04-16）**: 社内ビルドの性能劣化を Kiro CLI が 33 秒で調査・原因特定・修正し、381 パッケージ・月 55 万回のビルドで月あたり約 4 年分の計算時間を削減したと報告しています。コード生成ではなく、見慣れないコードベースを横断する根本原因分析に「より汎用的なエージェント」を選んだ、という理由が書かれています（<https://kiro.dev/blog/root-cause-in-33s/>）。
- **Planview「SOC 2 compliance」（2026-04-10）**: SOC 2 の監査サイクルあたり 40 時間以上を、Kiro CLI で証跡収集を自動化して削減した事例です（Planview は 3,000 社超に提供するポートフォリオ管理ベンダー）（<https://kiro.dev/blog/automating-soc-2-compliance/>）。

## 2026 年 6 月 ― V3 早期提供: 同じハーネスが端末に来た

公式 changelog 2.8.0（2026-06-17、<https://kiro.dev/changelog/cli/2-8/>）が V3 の早期提供を告知しました。既存の 2.x と並行して動き、`kiro-cli --v3` で opt-in します。changelog は、Kiro CLI 3.0 が Kiro IDE・Kiro Web と同じ統一ハーネス上に構築されること、端末での Specs・capability ベースの権限・独立ファイル形式の hooks・タグ指定のエージェント設定が V3 で入ることを挙げています。

公式ドキュメント「What's new in CLI V3」（<https://kiro.dev/docs/cli/v3/>）は、V2 と V3 の対応表、移行手順、V3 だけにある機能（Introspect サブエージェント、`/tangent`）を載せています。

## 2026 年 10 月 ― V3 が既定に

2026-10-09 の公式ブログ「Kiro CLI V3 is rolling out as the default experience」（<https://kiro.dev/blog/cli-3/>）の要点です。

| 項目 | 内容 |
|---|---|
| ロールアウト | 2026-10-12 から、起動時に V3 への切り替えを促すプロンプトを段階的に表示。「Switch to V3 and upgrade my configs」「Remind me later」「Don't ask again」の 3 択。**Don't ask again は V2 に留まる選択ではなく**、CLI 3.0 公開時に V3 へ移る |
| CLI 3.0 | 「by the end of October」に公開予定と記事は述べている（下の「現在の状態」参照） |
| V3 で使えるもの | クラウドセッション（`kiro-cli --cloud`。ラップトップを閉じても作業が続く。us-east-1 のみ）、memory（`/memories`）、Specs（`/spec new`）、`/tangent` の復活、`/sessions` パネル、workflows（opt-in）、global hooks、サブディレクトリの `AGENTS.md` |
| 廃止 | inline shell autocomplete、CLI desktop app、Classic（非 TUI）表示。新機能は TUI に集中する |
| 移行 | custom agents は `.json.bak` にバックアップして「universal config」形式へ自動変換。変換できない hooks は警告。`/upgrade-agent`・`kiro-cli agent upgrade <dir>`（2.29 以降・`--dry-run` あり）。権限は V2 の信頼ツール一覧から V3 の「アクションとリソースへのルール」へ（deny > ask > allow）。`use_aws` ツールは廃止され、AWS CLI はシェルツール経由 |
| 戻り方 | `kiro-cli --v2`（その起動のみ）。V2 のセッションは V3 で再開できるが、逆は不可 |

「TUI を出したあと lite mode を追加せざるを得なかった」という話は、公式ブログ「Which Kiro app should I pick?」（2026-08-12、<https://kiro.dev/blog/which-kiro-app-should-i-pick/>）にあります。端末派の一部は「より少ない表示」を望んでいた、という観察です。

### 現在の状態（公式 changelog の実測）

公式 changelog（<https://kiro.dev/changelog/cli/>）の最新系列は **2.36（2.36.0・2026-10-29）** で、3.0 系列のページはまだありません。したがって本ページでは CLI 3.0 を「2026-10-09 のブログで予告されたもの」として扱い、公開が確認できた時点で更新します。2.36.0 では、V3 セッションで日常的な操作を Kiro が代わりに承認する「Approve for me」や、ACP のエンジンを選ぶ `acp.agentEngine` 設定が追加されています（<https://kiro.dev/changelog/cli/2-36/>）。

## 公式ドキュメントで確かめる

| 知りたいこと | 公式ページ |
|---|---|
| CLI 全体 | <https://kiro.dev/docs/cli/> |
| V3 の変更点と移行 | <https://kiro.dev/docs/cli/v3/> |
| 版ごとの変更 | <https://kiro.dev/changelog/cli/> |
| V2 時代から全版の日本語解説 | [猫でもわかるKiro CLI アップデート情報](https://github.com/kamogashira-sys/q-cli-docs)（姉妹サイト） |

## 出典

| 出典 | 公開・更新日 |
|---|---|
| [aws/amazon-q-developer-cli README・Releases](https://github.com/aws/amazon-q-developer-cli) | v1.19.7: 2025-11-17 |
| [Bring Kiro agents to your terminal with Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/) | 2025-11-17 |
| [Kiro is generally available](https://kiro.dev/blog/general-availability/) | 2025-11-17 |
| [Specialized IDEs deserve AI too: Kiro adopts ACP](https://kiro.dev/blog/kiro-adopts-acp/) | 2026-02-05 |
| [A new look for the Kiro CLI](https://kiro.dev/blog/new-look-for-cli/) | 2026-03-23 |
| [Planview saves 40+ hours per audit cycle](https://kiro.dev/blog/automating-soc-2-compliance/) | 2026-04-10 |
| [Kiro CLI 2.0](https://kiro.dev/blog/cli-2-0/)・[introducing headless mode](https://kiro.dev/blog/introducing-headless-mode/) | 2026-04-13 |
| [Root cause in 33 seconds](https://kiro.dev/blog/root-cause-in-33s/) | 2026-04-16 |
| [Changelog CLI 2.8: CLI v3 Early Access](https://kiro.dev/changelog/cli/2-8/) | 2026-06-17 |
| [Which Kiro app should I pick?](https://kiro.dev/blog/which-kiro-app-should-i-pick/) | 2026-08-12 |
| [Kiro CLI V3 is rolling out as the default experience](https://kiro.dev/blog/cli-3/) | 2026-10-09 |
| [Changelog CLI 2.36](https://kiro.dev/changelog/cli/2-36/) | 2026-10-29 |

## 次に読む <!-- sources: n/a -->

- [1 つのエージェント、5 つの入口](02_one-agent.md)
- [なぜ筆者は Kiro CLI が好きなのか](../02_why-kiro-cli/01_why-i-love-kiro-cli.md)
- [はじめ方](../00_start/03_get-started.md)
