# 用語集 ― 本サイトで使う言葉

本サイトと公式ドキュメントに繰り返し出る言葉を、公式ドキュメント各ページの説明文（`llms.txt` の 1 行説明と各ページの冒頭）を本サイトの言葉で要約して並べたものです。英語の用語は公式の表記のまま使っています。詳しい仕様は各出典ページで確認してください。

## 全体の構造

| 用語 | 意味 | 出典 |
|---|---|---|
| **agent harness（エージェントハーネス）** | エージェントの本体。会話の進行、ツールの実行、文脈の管理、権限の評価、モデルとの通信を担う。Kiro ではこれが 1 つに統一されており、独立したプロセスとして動く | [How Kiro works](https://kiro.dev/docs/how-kiro-works/) |
| **unified agent harness（統一エージェントハーネス）** | IDE・CLI・Web・Mobile が共通に使う 1 つのハーネス。2026-08-03 の公式ブログで、3 つあったハーネスを統一した経緯が公表された | [One agent, every surface](https://kiro.dev/blog/one-agent/) |
| **surface（サーフェス、入口）** | ハーネスを使うための窓口。IDE・CLI・Web・Mobile の 4 つに Kiro Crew と ACP 対応エディタを加えた呼び方を本サイトでは「5 つの入口」としている | [How Kiro works](https://kiro.dev/docs/how-kiro-works/) |
| **V2 / V3** | Kiro CLI のハーネスの世代。V2 = 従来の CLI 固有のハーネス、V3 = 統一ハーネス。CLI の版番号（2.x・3.0）とは別の言葉 | [What's new in CLI V3](https://kiro.dev/docs/cli/v3/) |
| **ACP（Agent Client Protocol）** | エディタやアプリとエージェントをつなぐオープンなプロトコル。Kiro 自身の入口も、JetBrains・Zed などの対応エディタも、同じ ACP でハーネスに接続する。MCP とは役割が異なる（MCP はエージェントと外部ツールをつなぐ） | [ACP](https://kiro.dev/docs/acp/) |
| **cloud session（クラウドセッション）** | 自分のマシンではなく管理されたクラウドのサンドボックスで動くセッション。アカウントに属するので、ある入口で始めて別の入口から続けられる | [Cloud sessions](https://kiro.dev/docs/cloud-sessions/) |
| **cloud sandbox（クラウドサンドボックス）** | Web・Mobile・クラウドセッションのエージェントが動く隔離環境。接続したリポジトリを clone して作業し、結果を PR / MR で返す | [How Kiro works](https://kiro.dev/docs/how-kiro-works/) |
| **cloud configuration** | ローカルの `~/.kiro/` の設定をアカウントに同期し、クラウドセッションでも効かせる仕組み | [Cloud configuration](https://kiro.dev/docs/web/cloud-configuration/) |

## 設定と文脈

| 用語 | 意味 | 出典 |
|---|---|---|
| **Specs（スペック）** | 機能追加やバグ修正を、要件・設計・タスクの 3 つの文書に構造化してから実装する進め方。要件先行・設計先行・バグ修正・Quick Spec などの型がある | [Specs](https://kiro.dev/docs/specs/) |
| **Steering（ステアリング）** | プロジェクトの規約・アーキテクチャ・標準を書いた Markdown。毎回説明しなくても Kiro が従う。`.kiro/steering/`（プロジェクト）と `~/.kiro/steering/`（個人）に置く | [Steering](https://kiro.dev/docs/steering/) |
| **Hooks（フック）** | ファイル変更・ツール実行・タスク完了などのイベントで、シェルコマンドやエージェントへの指示を自動実行する仕組み。Prompt Submit・Pre Tool Use・Post Tool Use・Agent Stop などの型がある。IDE 版と CLI 版で仕様が異なる点は姉妹サイトを参照 | [Hooks](https://kiro.dev/docs/hooks/) |
| **global hooks** | `~/.kiro/hooks/` に置き、すべてのワークスペースで発火する hooks。ハーネス統一の成果として、クライアントの変更なしに全入口に展開された例 | [How Kiro works](https://kiro.dev/docs/how-kiro-works/) |
| **MCP（Model Context Protocol）** | 外部サーバーに接続してツール・プロンプト・リソースをエージェントに足す規格。例: AWS ドキュメント MCP サーバー | [MCP](https://kiro.dev/docs/mcp/) |
| **Powers（パワー）** | 特定の技術の知識・ワークフロー・MCP サーバーを束ね、関係するキーワードが出たときだけ読み込むパッケージ。MCP サーバーを多数つなぐとコンテキストが埋まる問題への対処として 2025-12-03 に発表 | [Powers](https://kiro.dev/docs/powers/) |
| **Agent Skills（スキル）** | 指示・スクリプト・テンプレートを束ねた持ち運べる指示パッケージ。オープン標準に従い、他の対応ツールと相互に使える | [Agent Skills](https://kiro.dev/docs/skills/) |
| **custom agents（カスタムエージェント）** | 使えるツール・権限・含める文脈を設定ファイルで定めた専用のエージェント。`~/.kiro/agents/`（個人）または `.kiro/agents/`（プロジェクト）に置く | [Custom agents](https://kiro.dev/docs/custom-agents/) |
| **sub-agents（サブエージェント）** | 主エージェントが、並列化・専用ツール・文脈の分離が有効なときに起こす子のエージェント。隔離された文脈で動き、結果を親に返す | [Invoking as sub-agents](https://kiro.dev/docs/custom-agents/subagents/) |
| **workflows（ワークフロー）** | 複数のエージェントが段階・ループ・並列で働く再利用可能な手順。各ステップは新しい文脈のセッションで動き、Kiro の実行基盤が計画どおりに進める | [Workflows](https://kiro.dev/docs/workflows/) |
| **memory（メモリ）** | 作業中に現れた修正・好み・デバッグの知見・やらないと決めた方法を保存し、次のセッションに持ち越す仕組み。利用者単位でローカルに保存され、同じマシンの IDE と CLI で共有される | [Memory](https://kiro.dev/docs/memory/) |
| **compaction（圧縮）** | 会話がモデルの上限に近づいたとき、古い履歴を自動で要約してセッションを続ける仕組み。目標・決定・進捗は残す | [Compaction](https://kiro.dev/docs/compaction/) |
| **checkpoints / rewind** | checkpoints はエージェントの変更を巻き戻してファイルを戻す。rewind は会話を前のターンから枝分かれさせる | [Checkpoints and rewind](https://kiro.dev/docs/checkpoints/) |
| **AGENTS.md** | リポジトリや、そのサブディレクトリに置く指示ファイル。V3 ではサブディレクトリごとの `AGENTS.md` が読まれる | [Kiro CLI V3 is rolling out as the default experience](https://kiro.dev/blog/cli-3/) |
| **Configuration scopes（設定スコープ）** | 設定の置き場所と優先順位。Project（`.kiro/`）・User（`~/.kiro/`）・Cloud・Workspace trust の 4 つ | [Configuration scopes](https://kiro.dev/docs/configuration/) |

## 安全と権限

| 用語 | 意味 | 出典 |
|---|---|---|
| **permissions（権限）/ capability** | エージェントが何をしてよいかを、capability（ファイル読み取り・書き込み・シェル・Web など）ごとにパターンと効果で宣言する仕組み。効果は deny > ask > allow の順に強い | [Permissions](https://kiro.dev/docs/permissions/) |
| **`permissions.yaml`** | 権限ルールを書くファイル。CLI 向けに書いた同じファイルを IDE も読む | [How Kiro works](https://kiro.dev/docs/how-kiro-works/) |
| **Workspace trust** | プロジェクトごとの権限ルールを `~/.kiro/workspace-roots/<hash>/` に置き、clone したリポジトリが自分自身に信頼を与えられないようにする仕組み | [How Kiro works](https://kiro.dev/docs/how-kiro-works/) |
| **Kiroignore** | gitignore 形式のパターンで、Kiro が触れないファイルを指定する | [Kiroignore](https://kiro.dev/docs/kiroignore/) |
| **local command sandbox（ローカルサンドボックス）** | ローカルで動くシェルコマンドと子プロセスの到達範囲とネットワークを OS の仕組みで制限する。既定はオフ | [Local command sandbox](https://kiro.dev/docs/sandbox/) |
| **Cedar** | 統一ハーネスの capability ベースの権限モデルを裏打ちしているポリシー言語。公式ブログ「One agent, every surface」は「formally verified policy language」と説明している | [One agent, every surface](https://kiro.dev/blog/one-agent/) |

## モデルと実行

| 用語 | 意味 | 出典 |
|---|---|---|
| **Auto** | タスクごとに最適なモデルを Kiro が自動で選ぶ仕組み。2025-09-15 に新料金と同時に発表 | [Models](https://kiro.dev/docs/models/)・[Announcing new pricing plans and Auto](https://kiro.dev/blog/new-pricing-plans-and-auto/) |
| **reasoning effort（推論の深さ）** | モデルがどれだけ推論に時間をかけるかを調整する設定。速さ・深さ・費用のバランスを取る | [Reasoning effort](https://kiro.dev/docs/models/effort/) |
| **Built-in tools（組み込みツール）** | ハーネスが備えるファイル操作・シェル・Web アクセス・コードインテリジェンスなどのツール。custom agents で絞れる | [Built-in tools](https://kiro.dev/docs/tools/) |
| **headless mode** | Kiro CLI を人が対話しない形で動かすモード。API キーで認証し、CI/CD パイプラインに組み込める | [CLI](https://kiro.dev/docs/cli/) |
| **TUI（Terminal User Interface）** | Kiro CLI の、画面全体を使う対話表示。2.0 で既定になった | [Kiro CLI 2.0](https://kiro.dev/blog/cli-2-0/) |
| **Agent Focus（Mode）** | Kiro IDE で、複数のエージェントセッションを並べて指揮する表示。コード中心の表示と切り替えられる | [Introducing Agent Focus](https://kiro.dev/blog/introducing-agent-focus/) |
| **autonomous mode（自律モード）** | Kiro Web で、計画から実装・PR 作成までの結果を丸ごと委ねる働き方 | [Kiro Web](https://kiro.dev/docs/web/) |
| **Automations（自動化）** | Kiro Web で、繰り返しの作業をスケジュールで自律セッションとして実行し PR を開く機能 | [Introducing automations](https://kiro.dev/blog/introducing-automations/) |
| **Crew Mode** | Kiro Crew で、個々のセッションの外にいてセッションの作成・監視・判定・次の決定を行うエージェント | [How we built a software factory](https://kiro.dev/blog/software-factory-1000-prs/) |

## 日本語の言い換えについて <!-- sources: n/a -->

本サイトは英語の用語を公式の表記のまま使い、初出で括弧内に日本語の説明を添えています。「ハーネス」「入口（サーフェス）」のように日本語を使っている箇所もありますが、公式の訳語ではなく本サイトの言い換えです。

## 次に読む <!-- sources: n/a -->

- [Kiro とは](../00_start/01_what-is-kiro.md)
- [情報源の使い分け](03_sources.md)
- [目次](../README.md)
