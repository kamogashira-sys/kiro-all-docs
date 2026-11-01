# 公式ブログ索引

**収録範囲: 公式ブログ 2025-07-14〜2026-10-30 公開分（113 本）**

kiro.dev の公式ブログ（<https://kiro.dev/blog/>）の全記事を、公開日・タイトル・本サイトの分類タグ・必読度・内容説明（1〜2 行）で一覧にしたものです。詳細は各記事の公式ページで読んでください。節目の記事を時系列で追うなら [Kiro の年表](../01_story/01_timeline.md) が向いています。

- 日付は各記事ページの表示日です（ISO 形式 `YYYY-MM-DD`）。新しい記事が上です。
- タイトルは公式の原文です。
- **分類タグ・必読度・内容説明は本サイトが付けたもの**で、公式のものではありません。分類は 1 記事に 1 つだけです。
- 内容説明は本サイトが記事本文を読んで自分の言葉で書いた要旨です。原文の翻訳ではありません。数値は記事の記載どおりです。
- このページは `scripts/kiro-all-docs/gen-blog-index.py` が `blog-index.tsv` から生成しています。手で編集しないでください。

## 分類タグ <!-- sources: n/a -->

| タグ | 意味 | 本数 |
|---|---|---|
| 製品発表 | 新しい製品・機能・サーフェスの公開告知 | 36 |
| モデル | 利用できる AI モデルの追加・変更 | 16 |
| 料金 | 料金プラン・クレジット・無料枠・学生／スタートアップ向けプログラム | 17 |
| 事例 | 顧客・社内チーム・コミュニティの利用事例 | 11 |
| 技術解説 | 仕組み・設計判断・使い方の解説 | 25 |
| コミュニティ | ハッカソン・コミュニティハブ・周年など | 8 |

## 必読度 <!-- sources: n/a -->

| 必読度 | 意味 | 本数 |
|---|---|---|
| ★★★ | Kiro を理解するために必読。製品・入口の誕生、ハーネス統一の設計判断、安全の仕組み、Kiro CLI の節目 | 23 |
| ★★ | Kiro を使う人は読んでおきたい。主要機能の考え方、代表的な事例、料金の節目 | 36 |
| ★ | 参考。個別のモデル追加、個別の料金・プログラム、コミュニティの告知 | 54 |

★★★ だけを先に読みたい人は、この表を「必読」列で絞ってください。★★★ の大半は [Kiro の年表](../01_story/01_timeline.md) の 30 本にも入っています（年表に入れていない ★★★ は Kiro Crew の software factory 2 本）。

## 一覧

| 公開日 | タイトル | 分類 | 必読 | 内容 |
|---|---|---|---|---|
| 2026-10-30 | [Spec it safe: shift left and harden your specs with security requirements](https://kiro.dev/blog/spec-it-safe/) | 技術解説 | ★★ | 機能要件だけの spec に、CWE の弱点分類に対応するセキュリティ要件を実装前に足す Power の紹介。「シフトレフト」を spec の層で行う。 |
| 2026-10-28 | [Kiro for Students expands to 41 more universities](https://kiro.dev/blog/41-more-universities/) | 料金 | ★ | 学生プログラムを 41 大学に追加拡大。サインインの流れも簡略化。 |
| 2026-10-27 | [Kiro’s new free trial gives you 500 extra credits](https://kiro.dev/blog/kiros-new-free-trial-gives-you-500-extra-credits/) | 料金 | ★ | 11 月 1 日からの無料トライアル変更。初回の Pro 移行で当月残りが無料、12 か月有効の 500 クレジット、料金とクレジットの日割り。 |
| 2026-10-26 | [Claude Haiku 5.5 is now available in Kiro](https://kiro.dev/blog/haiku-5-5/) | モデル | ★ | Claude Haiku 5.5 を IDE・CLI・Web・Crew で提供開始。大量・高速の作業（要約、分類、小さな編集）向け。Claude 5.5 の 3 モデルが揃った。 |
| 2026-10-26 | [Keeping a software factory stable at 1,000 PRs a week](https://kiro.dev/blog/software-factory-stability/) | 事例 | ★★★ | 週 1,000 PR を壊さずに続ける品質の仕組み。信頼の根拠を人のレビューからテストと検査に移す 5 段階、PR Readiness の単一判定、blocking の定義。 |
| 2026-10-20 | [How Kiro fixes itself, and how we keep the fixes honest](https://kiro.dev/blog/how-kiro-fixes-itself/) | 技術解説 | ★★ | Kiro 自身の実行記録からプロンプトやツール説明の欠陥を見つけ、厳しい検査を通った修正だけを採用する kiro-trace。初週に 8 本の PR。 |
| 2026-10-20 | [Introducing memory in Kiro IDE and CLI](https://kiro.dev/blog/memory-in-ide-cli/) | 製品発表 | ★★★ | memory を IDE・CLI に追加。作業中に現れた修正・好み・デバッグの知見を保存して次のセッションに持ち越す。steering との役割の違い。 |
| 2026-10-15 | [Kimi K3 model is now available in Kiro](https://kiro.dev/blog/kimi-k3/) | モデル | ★ | Moonshot AI の Kimi K3（2.8 兆パラメータ・100 万トークン文脈のオープンウェイトモデル）を Kiro に追加。 |
| 2026-10-14 | [Local sandboxing in Kiro: keep agent commands within boundaries](https://kiro.dev/blog/local-sandboxing/) | 製品発表 | ★★★ | IDE・CLI のローカルサンドボックスが GA。エージェントが実行するコマンドの到達範囲を OS の仕組みで制限し、ツール拒否をシェル経由で迂回される穴を塞ぐ。 |
| 2026-10-13 | [Introducing improved enterprise sign-in controls](https://kiro.dev/blog/sign-in-controls/) | 製品発表 | ★ | 企業の管理者が、管理デバイスで使えるサインイン方法（Identity Center のみ、など）を制限できる機能。 |
| 2026-10-09 | [Kiro CLI V3 is rolling out as the default experience](https://kiro.dev/blog/cli-3/) | 製品発表 | ★★★ | Kiro CLI V3（統一ハーネス）を既定にするロールアウトの告知。10 月 12 日から起動時プロンプト、CLI 3.0 を 10 月末までに予定。移行手順と、廃止される autocomplete・desktop app・Classic。 |
| 2026-10-02 | [Claude Sonnet 5.5 is now available in Kiro](https://kiro.dev/blog/sonnet-5-5/) | モデル | ★ | Claude Sonnet 5.5 を IDE・CLI・Crew・Web で提供開始。Sonnet 5 より 3 割以上速く、Opus 5.5 の横で動く低コストのサブエージェントに向く。 |
| 2026-09-30 | [Introducing Kiro workflows](https://kiro.dev/blog/introducing-workflows/) | 製品発表 | ★★★ | Kiro workflows の発表。複数のエージェントが段階・ループ・並列で働く手順を実行基盤が進める。各ステップは新しい文脈で動き、Kiro 自身の開発に使った。 |
| 2026-09-28 | [Claude Opus 5.5 is now available in Kiro](https://kiro.dev/blog/opus-5-5/) | モデル | ★ | Claude Opus 5.5 を IDE・CLI・Crew・Web で提供開始。Fable 5.1 相当の性能を Opus 5 より 40% 低い費用で、ツール呼び出しも約 4 割減。 |
| 2026-09-18 | [How we built a software factory with Kiro Crew to merge 1,000 PRs in a week](https://kiro.dev/blog/software-factory-1000-prs/) | 事例 | ★★★ | Kiro Crew を作る 3 人が 1 週間で 1,000 PR をマージ。1 セッション手動から Crew Mode までの 5 段階、統制の 4 つの問題、読者への助言。 |
| 2026-09-16 | [Claude Fable 5.1 is now available in Kiro](https://kiro.dev/blog/fable-5-1/) | モデル | ★ | Claude Fable 5.1 を企業顧客向けに提供開始。長時間・大量文脈のセッションで症状ではなく根本原因に向かうと公式が述べる。 |
| 2026-09-14 | [GPT‑5.6 models now support 1 million token context windows in Kiro](https://kiro.dev/blog/gpt-5-6-1m-context/) | モデル | ★ | GPT-5.6 の 3 モデルが 100 万トークンのコンテキストに対応。リポジトリ全体を一度に読むコードレビューや移行が可能に。 |
| 2026-09-14 | [Tackling technical debt at scale with autonomous mode in Kiro Web](https://kiro.dev/blog/tackling-technical-debt-at-scale-with-autonomous-mode/) | 事例 | ★★ | OSS の形式検証ツールの技術的負債を、Kiro Web の autonomous mode で issue から PR まで通して処理した 2 つの事例と設定方法。 |
| 2026-09-08 | [Kiro adds ISO/IEC 27001:2022 coverage](https://kiro.dev/blog/iso-27001/) | 製品発表 | ★ | Kiro が AWS の ISO/IEC 27001:2022 認証の範囲に含まれた。調達・セキュリティ・ベンダーリスクの評価に使える独立した証拠。 |
| 2026-09-08 | [A free year of Kiro, now for students around the world](https://kiro.dev/blog/students-2026/) | 料金 | ★ | 学生プログラムを 16 か国 121 大学に拡大。1 年間無料・月 1,000 クレジット・プレミアムモデルや Kiro Web も含む。 |
| 2026-09-03 | [Agentic engineering in the cloud](https://kiro.dev/blog/agentic-engineering-in-the-cloud/) | 製品発表 | ★★★ | Kiro Web とクラウドセッションが GA。ローカルの設定をクラウドセッションにも効かせる cloud configuration を同時提供。プレビュー以降の使われ方の例。 |
| 2026-08-26 | [Are AI coding agents actually getting better?](https://kiro.dev/blog/diagnostics-over-time/) | 技術解説 | ★ | IDE の diagnostics ツールが捉えたエラーの推移から、コーディングエージェントが実際に良くなっているかを測る分析。 |
| 2026-08-21 | [Continuous Prompt Evaluation: How We Use LLM Judges and Live Signals to Improve Kiro Agent Quality](https://kiro.dev/blog/continuous-prompt-evaluation/) | 技術解説 | ★ | LLM を審査員にした評価と実運用の信号で、システムプロンプトの劣化や副作用を継続的に見つけて直す社内の仕組み。 |
| 2026-08-21 | [How We Learned to Trust an AI Agent to Triage Production Incidents](https://kiro.dev/blog/trust-agent-triage/) | 事例 | ★★ | 日曜 2 時 33 分の本番アラームに対し、エージェントが 13 分半で根拠付きの診断をチケットに書いた事例。人は判断だけを担う。 |
| 2026-08-18 | [Close the laptop, keep the agent: building with cloud sessions](https://kiro.dev/blog/cloud-sessions/) | 製品発表 | ★★★ | クラウドセッションのプレビュー。エージェントがクラウドのサンドボックスで動き、CLI（--cloud）・IDE・Web のどこからでも続けられる。Payments API 追加の実例を CLI から通して見せる。 |
| 2026-08-12 | [Which Kiro app should I pick?](https://kiro.dev/blog/which-kiro-app-should-i-pick/) | 技術解説 | ★★★ | IDE・CLI・Web・Mobile・Crew の選び方。「どれか」ではなく「この仕事にはどれか」。1 つのハーネスの上の複数の玄関、Crew が原則から外れて出荷された正直な補足。 |
| 2026-08-07 | [Kiro powers now support Agent Plugins](https://kiro.dev/blog/powers-supports-plugins/) | 製品発表 | ★ | Powers が Agent Plugins 形式を読み込めるように。同じ知識とツールをクライアントごとに別々に包装し直す負担を減らす。 |
| 2026-08-04 | [Introducing Kiro Crew](https://kiro.dev/blog/introducing-kiro-crew/) | 製品発表 | ★★★ | Kiro Crew の OSS 公開。社内の side project MeshClaw として生まれ 6 か月弱で 39,000 人超が使った経緯、初日からのセキュリティ、memory・スケジュール・Apps、ガバナンス。 |
| 2026-08-03 | [One agent, every surface: how we built the Kiro agent harness](https://kiro.dev/blog/one-agent/) | 技術解説 | ★★★ | 本サイトの中核。IDE（TypeScript）・CLI（Rust）・Web（Python）で別々だったハーネスを 1 つに統一した経緯、独立プロセスと ACP を選んだ理由、Cedar による権限、Kiro 自身で作った話。 |
| 2026-07-31 | [GPT‑5.6 update: lower credit multipliers for Terra and Luna](https://kiro.dev/blog/gpt-5-6-pricing/) | 料金 | ★ | OpenAI の値下げを受け、GPT-5.6 Terra・Luna のクレジット倍率を引き下げ。 |
| 2026-07-24 | [Claude Opus 5 is now available in Kiro](https://kiro.dev/blog/opus-5/) | モデル | ★ | Claude Opus 5 を IDE・CLI・Web で提供開始。長時間の作業と並列エージェントの調整に強く、費用と遅延の制御も細かくなったと公式が述べる。 |
| 2026-07-20 | [How Kiro and Snyk create multi-layered security guardrails](https://kiro.dev/blog/kiro-and-snyk-guardrails/) | 技術解説 | ★ | Snyk Studio を MCP で Kiro につなぎ、生成されたコードの脆弱性を多層で検査する構成の解説。 |
| 2026-07-16 | [Celebrating the builders: how founders are shipping faster with Kiro](https://kiro.dev/blog/one-year-startups/) | 事例 | ★ | 1 周年に合わせたスタートアップ事例集。クレジットプログラム 3 段階と、創業者がどう Kiro で出荷を速めたか。 |
| 2026-07-16 | [One year of Kiro: how students are building the future, right now](https://kiro.dev/blog/one-year-students/) | 事例 | ★ | 1 周年に合わせた学生の事例集。アクセシビリティアプリから電子工作のプロトタイピングツールまで。 |
| 2026-07-14 | [GPT‑5.6 is now available in Kiro](https://kiro.dev/blog/gpt-5-6/) | モデル | ★★ | OpenAI のモデルが初めて Kiro に。GPT-5.6 の Sol・Terra・Luna の 3 段階を IDE・CLI・Web で提供。1 周年に合わせた発表。 |
| 2026-07-14 | [One year of Kiro: a look back, and a look ahead](https://kiro.dev/blog/one-year/) | コミュニティ | ★★★ | 1 周年の回顧。「developers deserve better than vibe coding」という出発点、最初の 5 日で 10 万人超、10 月までに倍増。これまでとこれから。 |
| 2026-07-13 | [Welcome to birthday week](https://kiro.dev/blog/birthday-2026/) | コミュニティ | ★ | 1 周年の週（7 月 13〜17 日）の告知。追加クレジットの機会と、#1YearOfKiro でのコミュニティの事例共有。 |
| 2026-07-02 | [Set a cap on overage spend, or pre-pay for it](https://kiro.dev/blog/cap-prepay-overage/) | 料金 | ★ | 超過利用に上限を設ける（Identity Center 利用組織は Service Quotas から）か、前払いで買う選択肢。請求の予測可能性を高める。 |
| 2026-07-01 | [Sonnet 5 is now available in Kiro](https://kiro.dev/blog/sonnet-5/) | モデル | ★ | Claude Sonnet 5 を IDE・CLI・Web で提供開始。Opus 4.8 に近い性能を Sonnet の価格で、という位置づけ。 |
| 2026-06-26 | [One Task, Two Providers: Coordinating Changes Across GitLab and GitHub in one session](https://kiro.dev/blog/coordinating-changes-across-gitlab-and-github-in-one-session/) | 技術解説 | ★ | Kiro Web で GitHub と GitLab のリポジトリを同じセッションに入れ、1 つの変更を MR と PR として両方に出す手順。 |
| 2026-06-25 | [From OpenAPI/Swagger specifications to test suite in seconds with Kiro](https://kiro.dev/blog/from-openapi-swagger-to-test-suite-in-seconds-with-kiro/) | 技術解説 | ★ | OpenAPI/Swagger 仕様からテストスイートを生成する例。仕様とテストが別々に保守されて乖離する問題への対処。 |
| 2026-06-25 | [Introducing Agent Focus](https://kiro.dev/blog/introducing-agent-focus/) | 製品発表 | ★★ | IDE に Agent Focus（実験機能）を追加。コード中心ではなく、エージェントとの対話と複数セッションの指揮を中心に置く表示。 |
| 2026-06-18 | [Introducing automations in Kiro on the web](https://kiro.dev/blog/introducing-automations/) | 製品発表 | ★★ | Kiro Web に automations（スケジュール実行）を追加。依存関係の更新やドキュメントの追従など繰り返しの保守を自律セッションで回し PR を開く。 |
| 2026-06-17 | [Introducing Kiro for iOS](https://kiro.dev/blog/introducing-kiro-for-ios/) | 製品発表 | ★★★ | iOS アプリの公開。クラウドセッションの開始・監視・差分確認・承認をスマートフォンから。chat・spec・autonomy の 3 モード。 |
| 2026-06-15 | [Introducing the Kiro merch store](https://kiro.dev/blog/kiro-merch-store/) | コミュニティ | ★ | 公式グッズストア shop.kiro.dev の開設。アパレルや Kiro の ghost をあしらった小物。 |
| 2026-06-11 | [Introducing Kiro Pro Max ($100/mo): more credits, less guesswork](https://kiro.dev/blog/kiro-pro-max/) | 料金 | ★ | 月 100 ドルの Pro Max tier を新設。Pro+（40 ドル）と Power（200 ドル）の間を埋め、月 5,000 クレジット。 |
| 2026-06-11 | [New in Kiro Web: Build with Spec, GitLab, and more](https://kiro.dev/blog/kiro-web-specs-gitlab/) | 製品発表 | ★★ | Kiro Web に Specs（ブラウザで要件・設計・タスクを確認して実装）と GitLab 対応を追加。1 セッションで複数リポジトリを横断。 |
| 2026-05-29 | [Opus 4.8 is now available in Kiro](https://kiro.dev/blog/opus-4-8/) | モデル | ★ | Claude Opus 4.8 を IDE・CLI・Web で提供開始。自己検証とツール呼び出しの効率が上がり、任せられる範囲が広がったと公式が述べる。 |
| 2026-05-21 | [Test Driven Development (TDD) with Kiro: this is how it should feel](https://kiro.dev/blog/how-tdd-should-feel/) | 技術解説 | ★ | red-green-refactor の規律を守りにくかった TDD を、Kiro に任せると負担なく回せるという筆者の経験と手順。 |
| 2026-05-18 | [Introducing Kiro Web](https://kiro.dev/blog/introducing-kiro-web/) | 製品発表 | ★★★ | Kiro Web をプレビュー公開（有料プラン向け）。「自律性は別製品ではなく Kiro の中核に属する」として、re:Invent の構想を Web から実装。 |
| 2026-05-12 | [Requirements analysis: catching requirement bugs before they become code](https://kiro.dev/blog/deep-spec-analysis/) | 製品発表 | ★★ | 要件文の粒度の誤り・曖昧さ・欠落を実装前に見つける要件分析。バグの多くは要件文の一文の解釈違いに遡る、という出発点。 |
| 2026-05-12 | [Specs just got faster (and smarter)](https://kiro.dev/blog/faster-smarter-specs/) | 製品発表 | ★★ | spec のタスク一覧から依存関係のグラフを作り、独立したタスクを並列実行する「Run all Tasks」の改良。承認フローの簡略化も。 |
| 2026-05-08 | [More room to explore: $20 paid tier sign-up bonus](https://kiro.dev/blog/new-paid-tier-bonus/) | 料金 | ★ | 有料プランに初めて上げたときのボーナスを 20 ドル（1,000 クレジット）に倍増。Free tier は変更なし。 |
| 2026-05-07 | [Introducing Kiro Ambassadors](https://kiro.dev/blog/introducing-kiro-ambassadors/) | コミュニティ | ★ | もっとも活発な開発者と関係を公式化する Kiro Ambassadors プログラム。無料サブスクリプションや先行アクセスと、フィードバック・発信の約束。 |
| 2026-04-23 | [Build with Kiro: Introducing the community hub and Kiro Labs](https://kiro.dev/blog/introducing-community-and-labs/) | コミュニティ | ★ | コミュニティハブと、Amazon 社員が Kiro で・Kiro のために作った OSS を集める GitHub 組織 Kiro Labs の開設。 |
| 2026-04-17 | [Opus 4.7 is now available in Kiro](https://kiro.dev/blog/opus-4-7/) | モデル | ★ | Claude Opus 4.7 を IDE・CLI で提供開始。複数ファイル・複数ツールにまたがる長い実装で、指示からの逸脱が少ないと公式が述べる。 |
| 2026-04-16 | [Root cause in 33 seconds: How Kiro CLI saved 4 years of build time](https://kiro.dev/blog/root-cause-in-33s/) | 事例 | ★★ | EC2 チームが Kiro CLI で社内ビルドの性能劣化を 33 秒で原因特定・修正。381 パッケージ・月 55 万回のビルドで月約 4 年分の計算時間を削減。 |
| 2026-04-13 | [Kiro CLI 2.0: a new look and feel, headless CI/CD pipelines, and Windows support](https://kiro.dev/blog/cli-2-0/) | 製品発表 | ★★★ | Kiro CLI 2.0。headless mode（CI/CD から実行）、Windows ネイティブ対応、TUI を既定に。端末に住む開発者の要望に応えた版。 |
| 2026-04-13 | [Run Kiro CLI programmatically: introducing headless mode](https://kiro.dev/blog/introducing-headless-mode/) | 製品発表 | ★★ | API キーを環境変数に置けばブラウザなしで動く headless mode の解説。GitHub Actions で push ごとに動く自動コードレビューを作る例。 |
| 2026-04-10 | [Planview saves 40+ hours per audit cycle by automating SOC 2 compliance with Kiro CLI](https://kiro.dev/blog/automating-soc-2-compliance/) | 事例 | ★★ | Planview が Kiro CLI で SOC 2 の証跡収集を自動化し、監査サイクルあたり 40 時間以上を削減した事例。20 超のクラウドサービスからの手作業を置き換えた。 |
| 2026-04-07 | [We’re bringing back the Kiro startup credits program](https://kiro.dev/blog/bringing-back-startup-credits/) | 料金 | ★ | スタートアップ向けクレジットプログラムの再開。シード〜シリーズ A の企業に最長 1 年分の Pro+ を、チーム規模で 3 段階。 |
| 2026-04-02 | [MiniMax M2.5 and GLM-5 are now in Kiro](https://kiro.dev/blog/minimax-m25-and-glm-5/) | モデル | ★ | オープンウェイトの MiniMax M2.5（0.25x）と GLM-5（0.5x）を IDE・CLI に追加。クレジット倍率と向く作業の説明。 |
| 2026-03-26 | [Bringing agentic AI to silicon development](https://kiro.dev/blog/bringing-agentic-ai-to-silicon-development/) | 事例 | ★ | Annapurna Labs が半導体設計に Kiro を適用した事例。閉じた EDA ツールチェーンなど、ハードウェア開発特有の制約への対処。 |
| 2026-03-24 | [From copilots to coworkers at AAAI: the gap between agentic research and production](https://kiro.dev/blog/from-copilots-to-coworkers/) | 技術解説 | ★ | AAAI 2026 のパネル（Microsoft・Mistral・NUS・LinkedIn・AWS）の記録。コーディングエージェントを本番に出すと何が壊れ、何を作り直すか。 |
| 2026-03-23 | [A new look for the Kiro CLI](https://kiro.dev/blog/new-look-for-cli/) | 製品発表 | ★★★ | kiro-cli --tui で新しい端末 UI を実験提供。「We love the terminal.」で始まり、従来表示と並行提供して準備が整ったら既定にすると述べる。 |
| 2026-03-18 | [Introducing the Kiro Students tier](https://kiro.dev/blog/introducing-kiro-students-tier/) | 料金 | ★ | 学生向け tier の開始。対象大学の学生は 1 年間無料、月 1,000 クレジット、クレジットカード不要。 |
| 2026-03-12 | [Enterprise governance: control your MCP servers and models](https://kiro.dev/blog/enterprise-governance-mcp-and-models/) | 製品発表 | ★★ | 企業の管理者が MCP サーバー接続と使えるモデルを一元管理する機能。コンプライアンス要件の厳しい組織の導入前提に応える。 |
| 2026-02-27 | [Surgical precision with AST-based code editing in Kiro](https://kiro.dev/blog/surgical-precision-with-ast/) | 技術解説 | ★★ | AST（抽象構文木）ベースのコード探索・編集エンジン。行範囲の推測や文字列一致ではなく構造を狙い、ベンチマークでトークンを 2 割削減。 |
| 2026-02-23 | [The hidden inefficiencies in AI coding (and how we find them)](https://kiro.dev/blog/hidden-inefficiencies-ai-coding/) | 技術解説 | ★★ | テストは通ったが 17 ターンかかった、のような「成功の中の無駄」を見つけるため、エージェントの行動全体を分析する社内システム CORAL。 |
| 2026-02-19 | [The bug fix paradox: why AI agents keep breaking working code](https://kiro.dev/blog/bug-fix-paradox/) | 技術解説 | ★★ | エージェントがバグ修正のつもりで防御コードや無関係な変更を増やしてしまう問題と、変更の境界を明示する「property-aware code evolution」。 |
| 2026-02-18 | [Kiro loves regulated workloads](https://kiro.dev/blog/introducing-govcloud/) | 製品発表 | ★★ | AWS GovCloud (US) リージョンで Kiro を提供。公共部門など、公開インターネットに出られない規制環境の開発者向け。 |
| 2026-02-18 | [New spec types: fix bugs and build on top of existing apps](https://kiro.dev/blog/specs-bugfix-and-design-first/) | 製品発表 | ★★ | 要件先行だけだった Specs に、設計先行（既存アプリに乗せる）とバグ修正（変えるものと変えないものを明示）の型を追加。 |
| 2026-02-17 | [Claude Sonnet 4.6 is now available in Kiro](https://kiro.dev/blog/sonnet-4-6/) | モデル | ★ | Claude Sonnet 4.6 を IDE・CLI で提供開始。Opus 4.6 に近い性能をより少ないトークンで。 |
| 2026-02-13 | [Enterprise identity and usage metrics](https://kiro.dev/blog/enterprise-identity-and-usage-metrics/) | 製品発表 | ★★ | Okta・Microsoft Entra ID など外部 ID プロバイダー対応と、ユーザー単位の利用メトリクス。企業導入の事例（Rackspace など）にも触れる。 |
| 2026-02-10 | [Open weight models are here: more choice, more speed, less cost](https://kiro.dev/blog/open-weight-models/) | モデル | ★★ | IDE・CLI にオープンウェイトモデルを追加。速さと費用を優先するタスクと強い推論が要るタスクでモデルを選び分ける考え方。 |
| 2026-02-05 | [Kiro 0.9: Custom subagents in the IDE, new enterprise controls, and granular code review](https://kiro.dev/blog/custom-subagents-skills-and-enterprise-controls/) | 製品発表 | ★★ | IDE 0.9。用途別に道具と文脈を絞る custom subagents、skills 対応、企業向け統制、より細かなコードレビュー。 |
| 2026-02-05 | [Specialized IDEs deserve AI too: Kiro adopts ACP](https://kiro.dev/blog/kiro-adopts-acp/) | 製品発表 | ★★★ | Kiro CLI が Agent Client Protocol に対応。Eclipse・Emacs・JetBrains・Neovim・Zed などから Kiro のエージェントを使える。LSP になぞらえた ACP の説明。 |
| 2026-02-05 | [Opus 4.6 is now available in Kiro](https://kiro.dev/blog/opus-4-6/) | モデル | ★ | Claude Opus 4.6 を IDE・CLI で提供開始。大規模な既存プロジェクトに対する精密な spec 作成に向くと公式が位置づける。 |
| 2026-02-05 | [Refactoring made right: how program analysis makes AI agents safe and reliable](https://kiro.dev/blog/refactoring-made-right/) | 技術解説 | ★★ | 関数名の変更やファイル移動をテキスト置換ではなくコードの構造の問題として扱い、プログラム解析で安全に行う仕組み。 |
| 2026-01-16 | [Run all tasks: the feature we refused to ship (until now)](https://kiro.dev/blog/run-all-tasks/) | 製品発表 | ★★ | 公開当初あえて付けなかった「全タスク実行」ボタンを 6 か月後に追加した経緯。可視性と制御を重んじた判断と、それを変えた理由。 |
| 2026-01-14 | [Empowering Kiro with IDE diagnostics](https://kiro.dev/blog/empowering-kiro-with-ide-diagnostics/) | 技術解説 | ★★ | エディタが常時出している型エラーや未解決 import の診断をエージェントに渡し、ビルドを回さずに品質へ収束させる仕組み。 |
| 2025-12-18 | [Property-Based Testing Caught a Security Bug I Never Would Have Found](https://kiro.dev/blog/property-based-testing-fixed-security-bug/) | 事例 | ★★ | チャットアプリのストレージを spec から実装したところ、property-based test の 75 回目で JavaScript のプロトタイプの扱いに起因するバグを検出した事例。 |
| 2025-12-17 | [Multi-root workspaces in Kiro: work across projects, not just inside one](https://kiro.dev/blog/multi-root-workspaces/) | 製品発表 | ★ | 複数のフォルダ（アプリと共有ライブラリ、複数のマイクロサービスなど）を 1 つの IDE ウィンドウで扱う multi-root workspace。 |
| 2025-12-03 | [Introducing Kiro powers](https://kiro.dev/blog/introducing-powers/) | 製品発表 | ★★★ | フレームワークの知識と MCP サーバーを束ね、必要なときだけ読み込む Powers。MCP サーバーを多数つなぐとツール定義でコンテキストが埋まる問題への対処。 |
| 2025-12-02 | [Introducing Kiro autonomous agent](https://kiro.dev/blog/introducing-kiro-autonomous-agent/) | 製品発表 | ★★★ | re:Invent で発表した、人が付き添わず文脈を保ちながら自律的に働く「frontier agent」の構想。のちに Kiro Web の autonomous mode になった（追記）。 |
| 2025-11-24 | [Introducing Opus 4.5 in Kiro](https://kiro.dev/blog/introducing-opus-45/) | モデル | ★ | Claude Opus 4.5 を Kiro で提供開始。複雑なコードベースを横断する長時間タスクと spec-driven development に向く。 |
| 2025-11-17 | [Kiro is generally available: Build with your team in the IDE and terminal](https://kiro.dev/blog/general-availability/) | 製品発表 | ★★★ | 一般提供（GA）。property-based testing・checkpointing・multi-root workspace・Kiro CLI・チームプランを同時に発表。spec-driven development を最初に持ち込んだと公式が述べる。 |
| 2025-11-17 | [Never lose your way: Introducing checkpointing in Kiro](https://kiro.dev/blog/introducing-checkpointing/) | 製品発表 | ★★ | エージェントの変更をファイルと会話の文脈ごと巻き戻せる checkpointing。失敗を恐れず大きなリファクタリングを任せられるようにする。 |
| 2025-11-17 | [Bring Kiro agents to your terminal with Kiro CLI](https://kiro.dev/blog/introducing-kiro-cli/) | 製品発表 | ★★★ | Kiro CLI の誕生。Q Developer CLI のエージェント技術（agent mode・MCP・steering・custom agents）を引き継ぎ、ソーシャルログインと Auto を追加。.kiro 設定を IDE と共用。 |
| 2025-11-17 | [Introducing the Kiro startup credits program](https://kiro.dev/blog/one-year-free-for-startups-2025/) | 料金 | ★ | スタートアップ向けクレジットプログラムの開始。応募多数で受付終了（記事冒頭の追記）。 |
| 2025-11-17 | [Does your code match your spec?](https://kiro.dev/blog/property-based-testing/) | 技術解説 | ★★★ | 仕様から性質（property）を取り出し、多数のランダム入力で検証する property-based testing を Specs に組み込んだ理由。単体テストが仕様を写しているかという問題への答え。 |
| 2025-11-11 | [Making your Kiro credits go further](https://kiro.dev/blog/making-credits-go-further/) | 料金 | ★ | Auto エージェントの効率改善。従来 1 クレジットだった典型的なリクエストが 0.79 クレジットになり、同じクレジットで約 2 割多く使える。 |
| 2025-11-04 | [Stop repeating yourself: why global steering is the AI context layer you’ve been missing](https://kiro.dev/blog/stop-repeating-yourself/) | 技術解説 | ★★ | プロジェクトごとに同じ好みや規約を説明し直す無駄を示し、全ワークスペースに効く global steering を「AI の文脈レイヤー」として紹介。 |
| 2025-10-31 | [Introducing remote MCP servers](https://kiro.dev/blog/introducing-remote-mcp/) | 製品発表 | ★★ | ローカル実行だけだった MCP サーバーに加え、リモート MCP サーバー接続とワンクリックインストールに対応。 |
| 2025-10-31 | [This is Kiroween](https://kiro.dev/blog/kiroween-2025/) | コミュニティ | ★ | ハロウィンをテーマにした初のハッカソン「Kiroween」。賞金総額 10 万ドル・66 名が受賞、参加者には Pro+ 相当の利用枠を提供。 |
| 2025-10-23 | [Teaching Kiro new tricks with agent steering and MCP](https://kiro.dev/blog/teaching-kiro-new-tricks-with-agent-steering-and-mcp/) | 技術解説 | ★★ | 社内独自のライブラリや DSL を Kiro に理解させる方法。架空のライブラリ MathJSON を例に、steering と MCP の使い分けを示す。 |
| 2025-10-21 | [Multimodal development with Kiro: from design to done](https://kiro.dev/blog/multimodal-development-with-kiro-from-design-to-done/) | 技術解説 | ★ | ERD や UML の図を Kiro のマルチモーダルチャットに読ませ、スキーマやサービス境界に落とす例。金融取引システムの構築で試した話。 |
| 2025-10-16 | [The wait(list) is over, get started with Kiro today](https://kiro.dev/blog/waitlist-is-over/) | 製品発表 | ★★ | 公開 90 日で待機リストを廃止。新規ユーザーに期間限定で 500 ボーナスクレジット。当時の料金の要点も再説明。 |
| 2025-10-09 | [How I stopped worrying about ReadMe files](https://kiro.dev/blog/how-i-stopped-worrying-about-readme-files/) | 技術解説 | ★ | ファイル保存をきっかけに README や API ドキュメントを自動更新する agent hooks の使い方。ドキュメントが古くなる問題への対処。 |
| 2025-09-15 | [Announcing new pricing plans and Auto, our new agent](https://kiro.dev/blog/new-pricing-plans-and-auto/) | 料金 | ★★ | vibe と spec で分かれていた上限を 1 つのクレジットプールに統合した新料金と、タスクごとに最適なモデルを選ぶ Auto エージェントの発表。 |
| 2025-08-28 | [Use Kiro for free until September 15](https://kiro.dev/blog/free-until-september-15/) | 料金 | ★ | 料金更新に伴い、無料利用期間を 9 月 15 日まで延長。9 月分の返金と、期間中の追加リクエストの無償提供。 |
| 2025-08-22 | [Important Kiro pricing updates](https://kiro.dev/blog/important-pricing-updates/) | 料金 | ★ | 一部のタスクが複数リクエストを誤って消費していた計測バグの修正と、利用上限のリセットの告知。 |
| 2025-08-15 | [Kiro pricing plans are now live](https://kiro.dev/blog/pricing-plans-are-live/) | 料金 | ★ | 料金プランの提供開始。Google・GitHub・Builder ID のアカウントを Free tier に移行し、全ユーザーに 14 日間のウェルカムボーナス。 |
| 2025-08-13 | [Unlock your development productivity with Kiro and Model Context Protocol (MCP)](https://kiro.dev/blog/unlock-your-development-productivity-with-kiro-and-mcp/) | 技術解説 | ★★ | 社内ナレッジベースや独自 API など、組み込みツールでは届かない範囲を MCP で Kiro につなぐ考え方と設定例。 |
| 2025-08-07 | [Understanding Kiro's pricing: specs, vibes, and usage tracking](https://kiro.dev/blog/understanding-kiro-pricing-specs-vibes-usage-tracking/) | 料金 | ★ | 当時の「spec request」と「vibe request」の違い、利用量の見方など、最初の料金モデルに寄せられた質問への回答。 |
| 2025-08-01 | [Kiro pricing update + waitlist invites coming soon](https://kiro.dev/blog/pricing-waitlist-updates/) | 料金 | ★ | 待機リストからの招待開始と、料金プラン導入の予告。新規ユーザーの 2 週間トライアル特典（追記あり）。 |
| 2025-07-24 | [This is fine... (really)](https://kiro.dev/blog/this-is-fine-really/) | コミュニティ | ★ | プレビュー公開 1 週間で 10 万人超が利用し、想定を超える需要で容量上限に達したことの報告と、待機リストへの対応。 |
| 2025-07-16 | [Automate your development workflow with Kiro’s AI agent hooks](https://kiro.dev/blog/automate-your-development-workflow-with-agent-hooks/) | 技術解説 | ★★ | テストの更新、ドキュメントの同期、コーディング規約の適用を、コーディング中のイベントに反応して自動で行う agent hooks の紹介。 |
| 2025-07-16 | [How Kiro helped me code a game](https://kiro.dev/blog/how-kiro-helped-me-code-a-game/) | 事例 | ★ | 6 か月かけて Kiro で作った OSS のクラフトゲーム「Spirit of Kiro」。LLM が組み合わせを即興で決める設計と、作者が学んだ AI との作り方。 |
| 2025-07-15 | [From chat to specs: a deep dive into AI-assisted development with Kiro](https://kiro.dev/blog/from-chat-to-specs-deep-dive/) | 技術解説 | ★★ | 「actually, I meant...」を繰り返すチャット型開発の非効率を示し、要件→設計→タスクの spec-driven development がなぜ有効かを解説。 |
| 2025-07-15 | [Kiro and the future of AI spec-driven software development](https://kiro.dev/blog/kiro-and-the-future-of-software-development/) | 技術解説 | ★★ | 1950〜60 年代の高級言語の革命と比較し、「どうやるか」ではなく「何をするか」を書く宣言的な開発として Specs を位置づけるエッセイ。 |
| 2025-07-14 | [Announcing the Code with Kiro Hackathon](https://kiro.dev/blog/code-with-kiro-hackathon/) | コミュニティ | ★ | プレビュー公開と同日に発表された最初のハッカソン。Kiro で動くアプリを作るのが条件で、賞金総額 10 万ドル、4 つの部門。 |
| 2025-07-14 | [Introducing Kiro](https://kiro.dev/blog/introducing-kiro/) | 製品発表 | ★★★ | Kiro の誕生記事。プロンプトだけで作ったものを本番に持っていく難しさに対し、Specs と Hooks を中核にした AI IDE として発表。待機リスト制のプレビュー。 |

## 索引の更新方法 <!-- sources: n/a -->

1. `make check-kiro-all-blog-sync` で公式 sitemap と `blog-index.tsv` の差分を確認する（手動のみ。CI では実行しない）
2. 差分の記事ページを開き、表示日・`<title>` を `blog-index.tsv` に追記し、本文を読んで分類タグ・必読度・内容説明（1〜2 行、自分の言葉で）を付ける
3. `./scripts/kiro-all-docs/gen-blog-index.py` で本ページを再生成する
4. リポジトリ README の収録範囲行を本ページの 1 行目と同じ値に更新する（`make check-kiro-all-blog-index-count` が一致を検査する）

## 次に読む <!-- sources: n/a -->

- [Kiro の年表 ― 節目の記事だけを選んで](../01_story/01_timeline.md)
- [情報源の使い分け](03_sources.md)
- [目次](../README.md)
