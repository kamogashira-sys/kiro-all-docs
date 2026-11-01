# どのアプリを選ぶか ― 「どれか」ではなく「この仕事にはどれか」

Kiro は IDE・CLI・Web・Mobile・Crew の 5 つの入口を持ちます。公式ブログ「Which Kiro app should I pick?」（2026-08-12、Massimo Re Ferre、<https://kiro.dev/blog/which-kiro-app-should-i-pick/>）は、この問いに「それは状況による」と答えたうえで、**問いの立て方自体を変える** ことを勧めています。「どれを選ぶか（which one）」ではなく「この仕事にはどれか（which one for this）」。本ページはその記事の要旨と、各入口の公式ドキュメントの冒頭をまとめたものです。

**出典**（公開日・更新日は公式ページの表示日）:

| 出典 | 公開・更新日 |
|---|---|
| [Which Kiro app should I pick?](https://kiro.dev/blog/which-kiro-app-should-i-pick/) | 2026-08-12 |
| [How Kiro works（「What each surface adds」）](https://kiro.dev/docs/how-kiro-works/) | 2026-10-23 |
| [IDE（公式ドキュメント）](https://kiro.dev/docs/ide/) | 2026-08-04 |
| [CLI（公式ドキュメント）](https://kiro.dev/docs/cli/) | 2026-08-04 |
| [Kiro Web（公式ドキュメント）](https://kiro.dev/docs/web/) | 2026-10-23 |
| [Mobile（公式ドキュメント）](https://kiro.dev/docs/mobile/) | 2026-08-04 |
| [Crew Quick start（公式ドキュメント）](https://kiro.dev/docs/crew/) | 2026-10-20 |
| [Agentic engineering in the cloud](https://kiro.dev/blog/agentic-engineering-in-the-cloud/) | 2026-09-03 |

---

## 📑 このページの内容
<!-- sources: n/a -->

1. [なぜ選択を間違えようがないのか](#なぜ選択を間違えようがないのか)
2. [公式が挙げる 2 つの原則](#公式が挙げる-2-つの原則)
3. [入口ごとの説明](#入口ごとの説明)
4. [早見表](#早見表)

## なぜ選択を間違えようがないのか

記事（<https://kiro.dev/blog/which-kiro-app-should-i-pick/>）の前提は [ハーネス統一](../01_story/02_one-agent.md) です。Kiro のエージェント本体（ハーネス）は 1 つで、IDE・CLI・Web はそれを使うための「アプリ」にすぎない。ハーネスが「何ができるか」を決め、アプリが「どう体験するか」を決める。両者は意図的に切り離されています。

記事はその帰結を 3 つ挙げています。

1. ハーネスに足した機能は、すべての入口に同時に現れる
2. どの入口を使っても振る舞いが一貫する
3. セッションをラップトップで始め、クラウドで走らせ続け、スマートフォンから確かめられる。ずっと同じエージェントだから

設定（skills・steering・custom agents・調整した好み）もアプリの中ではなくハーネスの周りに置くので、入口を変えても環境を作り直さなくてよい、と記事は述べています（公開時点では特定のアプリの組み合わせで成り立ち、すべての組み合わせに広げるのが方向性、との注記あり）。

記事の言い方では、入口を選ぶことは「壁に囲まれた庭」を選ぶことではなく「玄関」を選ぶことです。どの入口も他を置き換えるためには作られておらず、重なりがあるのは欠陥ではなく、1 つの土台の上に複数の体験層があることの自然な形だ、と説明しています。

## 公式が挙げる 2 つの原則

記事の「The principles behind these decisions」（<https://kiro.dev/blog/which-kiro-app-should-i-pick/>）の要旨です。

| 原則 | 内容 |
|---|---|
| **ソフトウェア配送のライフサイクルに仕える** | 作る対象は「ソフトウェアを出荷する人」のためのアプリ。開発者がまず、その周りの PM・アーキテクト・QA・UX・運用も含む。試す問いは「この人は開発者か」ではなく「これはソフトウェアを出荷する行為に仕えるか」。万人向けの汎用 AI アシスタントは作らない |
| **builder のいる場所で出会い、前へ進む手助けをする** | ファイルと関数の中で生きる「code-first」の人と、エージェントを指揮してコードは副産物と見る「agent-first」の人がいる。業界の大半はまだ前者で、後者は小さいが業界の向かう先。agent-first の世界に向けて作りつつ、両者の間に簡単な「乗り口」を置く |

## 入口ごとの説明

記事の「The apps, one by one」と、各入口の公式ドキュメント冒頭（`.md` companion）に基づきます。

### Kiro IDE ― ホームベース

- 記事: 「Kiro」と聞いて多くの人が思い浮かべるもの。Code OSS ベースのエディタで、GA。企業チームの主流の開発者にとっての「ホームベース」。**Agent Focus Mode**（実験機能）で、Code Focus（慣れたコード中心の編集）と Agent Focus（複数セッションの並行指揮・ワークフローの観察）をエディタの中で切り替えられる。これが「agent-first の世界を、知っている環境の安全圏から覗く乗り口」
- 公式ドキュメント（<https://kiro.dev/docs/ide/>、2026-08-04 更新）: VS Code を基盤にした desktop の開発環境。IDE 固有の機能として Editor・Specs・Chat を挙げ、Steering・Hooks・MCP・Custom Agents・Skills・Powers は「CLI・Web と共有するコアのエージェントエンジン」の機能として並べている
- 姉妹サイト: [猫でもわかるKiro IDE アップデート情報](https://github.com/kamogashira-sys/kiro-ide-docs)

### Kiro CLI ― 端末とパイプライン

- 記事: GA。まったく違う 2 つの聴衆が同じインターフェースを求めている。(1) **端末を好む開発者**。シェルに住み、フラグとパイプで考え、グラフィカルな画面を摩擦と感じる人たち。4〜6 セッションを並行させ、コードを覗くことはあっても全行はレビューせず、テストに（大きく）頼る。(2) **自動化**。人がまったく介在せず、シェルスクリプトに包まれ、GitHub や GitLab の CI/CD パイプラインの 1 ステップとして動く。「UI のない Kiro」。これはエンジンと体験が切り離されているからこそ可能
- 記事が「予想外に学んだこと」: 全員が「より豊かなアプリに卒業」したいわけではない。フル TUI を出した後、一部の利用者には TUI でも多すぎて、**lite mode を足さざるを得なかった**。「more surface doesn't always mean more useful」
- 公式ドキュメント（<https://kiro.dev/docs/cli/>、2026-08-04 更新）: CLI 固有の機能として Interactive Chat・Terminal UI・Headless Mode・Voice Mode・ACP・Auto Complete・Code Intelligence を挙げている
- 姉妹サイト: [猫でもわかるKiro CLI アップデート情報](https://github.com/kamogashira-sys/q-cli-docs)。本サイトの [Kiro CLI の道](../01_story/03_cli-journey.md) も

### Kiro Web ― クラウドファーストの入口

- 記事（公開時点）: プレビュー。協業し、仕事を起こし、背景で動くエージェントを見守る場所。そして次第に **クラウドセッションのコントロールプレーン** になっている。IDE や CLI からもクラウドのエージェントを起こせるようになった今、問いは「どう始めるか」から「走っているものをどこで見て操るか」に移り、Web がその一か所になりつつある。想定する聴衆は frontier developer、チーム、PM やリードなど「エディタの中に一日いなくてもソフトウェアの出荷に参加したい人」。ハーネス統一の配当が最初に見える場所でもある。Specs は IDE 専用だったが、spec の流れがハーネスに移ると、作り直しなしで Web に現れた
- 公式ドキュメント（<https://kiro.dev/docs/web/>、2026-10-23 更新）: ブラウザで動く開発エージェント（<https://app.kiro.dev>）。Pro・Pro+・Pro Max・Power プランで利用でき、既定モード・Spec mode・autonomous mode の 3 つの働き方がある。どの流れでも結果は既定ブランチに届く前に人が確認し、Kiro が自動でマージすることはない。提供は `us-east-1` のみ
- その後の状態: 2026-09-03 の公式ブログで Kiro Web とクラウドセッションは **GA** になりました（<https://kiro.dev/blog/agentic-engineering-in-the-cloud/>）
- 姉妹サイト: [猫でもわかるKiro Web アップデート情報](https://github.com/kamogashira-sys/kiro-web-docs)

### Kiro Mobile ― 移動中の Kiro

- 記事（公開時点）: プレビュー。「議論の余地はなく、必須の要件」。クラウドでエージェントを実行する開発ツールにはスマートフォンの入口が要る。得意なのは遠隔の仕事。背景エージェントの監視、結果の確認、操作の承認、長時間タスクの後押し。ローカルのラップトップのセッションにスマートフォンから届くのは難しく、まだ開いている課題
- 公式ドキュメント（<https://kiro.dev/docs/mobile/>、2026-08-04 更新）: iOS 向けに Apple TestFlight で早期アクセス提供。詳細なドキュメントは「coming soon」。セッションと設定は Kiro Web と同期し、Web・IDE・CLI で始めたクラウドセッションをスマートフォンから操作する
- 本シリーズに Mobile 専用の姉妹サイトはありません

### Kiro Crew ― 外側のハーネス

- 記事: 常駐の memory、スケジュール実行、非同期の背景エージェントを束ね、「エージェントを動かす」を越えて「エージェントの一団を、スケジュールで、寝ている間も動かす」ための入口。最初の **オープンソース** のアプリで、GA 製品と同じ品質・サポートの基準を課す。「運転する」のではなく「委ねる」場所。聴衆は、1 体を操縦するより一団を問題に向けたい power user と frontier developer。社内では MeshClaw という名前で数か月使われ、6 か月弱で 39,000 人超の Amazon の builder が使い、nearly 500 人が貢献した
- 記事の「正直な補足」: Crew を「アプリ」と呼ぶのは控えめすぎる。Kiro のエンジンの周りに作られたシステム拡張で、自前の Web・Slack・デスクトップアプリを持つ。常時稼働・複数エージェント統率・memory の多くは共有ハーネスではなく Crew 自身にあり、意図的に原則から外れて出荷した。整合させる計画はある
- 公式ドキュメント（<https://kiro.dev/docs/crew/>、2026-10-20 更新）: 自分のハードウェアでローカルまたはリモートに動く、オープンソースの personal AI agent。persistent・self-learning・self-evolving。デスクトップアプリ・Web ダッシュボード・CLI、さらに Slack・Discord・Telegram・Teams・Webex・WeCom・WeChat (Weixin) から使える
- 姉妹サイト: [猫でもわかるKiro Crewアップデート情報](https://github.com/kamogashira-sys/kiro-crew-docs)。本サイトの [Kiro Crew の起源](../01_story/04_crew-origin.md) も

## 早見表

記事の「cheat sheet」（<https://kiro.dev/blog/which-kiro-app-should-i-pick/>）を本サイトが訳したものです。成熟度は **記事公開時点（2026-08-12）** の表記で、Web はその後 GA になっています（上記）。

| やりたいこと | 入口 | 成熟度（2026-08-12 時点） |
|---|---|---|
| エディタの中で AI を織り込んでコードを書く。気になったら Agent Focus Mode で agent-first を覗く | **IDE** | GA |
| 端末で作業する。または人を介さず動かす（スクリプト・CI/CD・パイプライン） | **CLI** | GA |
| 腰を据えてエージェントと働く。どこで起こしたクラウドセッションも一か所で開始・確認・操作する | **Web** | Preview（2026-09-03 に GA） |
| 移動中の短い操作。スマートフォンからセッションを起こす・承認する・確かめる・後押しする | **Mobile** | Preview |
| もっとも自律的な仕事を委ねる。memory・スケジュール・非同期エージェント。離れている間も動き続ける一団 | **Crew** | Open source |

記事の結びは、どの答えも「仕事」であって「アイデンティティ」ではない、という点です。机では IDE、パイプラインでは CLI、電車では Mobile、常時稼働には Crew。同じエンジンの上で全部を同時に使ってよい。「どのアプリを、永遠に」ではなく「この仕事、この瞬間、この気分にはどのアプリか」。

## 次に読む
<!-- sources: n/a -->

- [はじめ方 ― Kiro CLI を 3 ステップで、ほかの入口は公式へ](03_get-started.md)
- [Kiro とは](01_what-is-kiro.md)
- [1 つのエージェント、5 つの入口](../01_story/02_one-agent.md)
