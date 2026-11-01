# はじめ方 ― Kiro CLI を 3 ステップで、ほかの入口は公式へ

Kiro には IDE・CLI・Web・Mobile・Crew の 5 つの入口があります（それぞれの向き不向きは [README の「5 つの入口」](../../README.md#-5-つの入口) と公式ブログ <https://kiro.dev/blog/which-kiro-app-should-i-pick/>）。本ページでは **Kiro CLI** を最初の 1 プロンプトまで 3 ステップで案内し（CLI を取り上げる理由は [なぜ筆者は Kiro CLI が好きなのか](../02_why-kiro-cli/01_why-i-love-kiro-cli.md)）、ほかの入口は公式の導線を示します。手順はすべて公式ドキュメントのものです。

**出典**（公開日・更新日は公式ページの表示日）:

| 出典 | 更新日 |
|---|---|
| [Installation](https://kiro.dev/docs/getting-started/installation/) | 2026-10-21 |
| [Authentication](https://kiro.dev/docs/getting-started/authentication/) | 2026-10-29 |
| [CLI](https://kiro.dev/docs/cli/) | 2026-08-04 |
| [A new look for the Kiro CLI](https://kiro.dev/blog/new-look-for-cli/) | 2026-03-23 |

---

## 📑 このページの内容
<!-- sources: n/a -->

1. [Kiro CLI を 3 ステップで](#kiro-cli-を-3-ステップで)
2. [ほかの入口](#ほかの入口)

## Kiro CLI を 3 ステップで

公式ドキュメント「Installation」（更新 2026-10-21、<https://kiro.dev/docs/getting-started/installation/>）と「Authentication」（更新 2026-10-29、<https://kiro.dev/docs/getting-started/authentication/>）に基づきます。

### ステップ 1: インストール

OS に合わせて 1 行です。

```bash
# macOS（Homebrew）
brew install kiro-cli

# macOS / Linux（インストールスクリプト）
curl -fsSL https://cli.kiro.dev/install | bash
```

```powershell
# Windows 11（PowerShell または Windows Terminal。コマンドプロンプトは対象外）
irm 'https://cli.kiro.dev/install.ps1' | iex
```

Linux で glibc が 2.34 より古い場合や、rpm・deb・AppImage で入れたい場合の代替手順も同じ公式ページにあります。Kiro CLI は背景で自動更新され、新しい版が出ると静かにダウンロードしてアプリ終了時に入れ替わります（公式「Installation」の Upgrading の節）。

### ステップ 2: サインイン

```bash
kiro-cli login
```

公式の手順は 3 つです。(1) 端末で `kiro-cli` または `kiro-cli login` を実行すると、Enter を押してブラウザでサインインを完了するよう促される (2) ブラウザでプロバイダを選んで認証する (3) 認証後、端末に戻るようブラウザに表示され、サインイン済みになる。

サインインの方法は、公式ページの分類では **GitHub・Google・AWS Builder ID**（個人向け。Builder ID は AWS アカウント不要の無料の個人 ID）と **Your organization**（組織の ID 基盤でサインインする方法。AWS IAM Identity Center、または Okta・Microsoft Entra ID などの外部 IdP）です。新規ユーザーは無料の Kiro Free から始まります（<https://kiro.dev/docs/billing/>）。ブラウザの無いリモートマシンでは `kiro-cli login --use-device-flow`（別の端末のブラウザでコードを入力する方式）、CI では API キー（環境変数 `KIRO_API_KEY`）が使えます。どの方法で入っているかは `kiro-cli whoami` で確認できます。

### ステップ 3: 最初の 1 プロンプト

プロジェクトのディレクトリに入って、チャットを開きます。

```bash
cd my-project
kiro-cli chat
```

公式ドキュメントの「Start building」はこの `cd` と `kiro-cli chat` の 2 行だけで、ほかの準備は要りません。

最初の 1 プロンプトは、日本語で用件を書くだけです。「日本語の指示だけでゲームができた」という体験は [なぜ筆者は Kiro CLI が好きなのか](../02_why-kiro-cli/01_why-i-love-kiro-cli.md) に書きました。小さく始めるなら、次のような 1 行で十分です。

```text
このリポジトリの構成を調べて、README に書くべき「はじめ方」を提案して
```

送ると何が起きるか。公式ドキュメント「How Kiro works」（<https://kiro.dev/docs/how-kiro-works/>）の説明では、エージェントはまず文脈（あなたの指示・steering・添付）を組み立ててモデルに渡し、モデルが返したツール呼び出し（ファイルを読む・検索する・コマンドを実行する）を 1 つずつ権限ルールで確認してから実行し、結果をモデルに戻して、終わるまで繰り返します。ファイルの変更やコマンド実行のように許可が決まっていない操作は、実行前に端末で「許可する／しない／今後も許可」を聞かれます。読むだけの指示なら、提案文が返ってきて終わりです。

チャットの中では `/` でコマンド一覧、`@` でファイルなどの文脈を追加できます（公式ブログ「A new look for the Kiro CLI」<https://kiro.dev/blog/new-look-for-cli/>）。

### いま入れると V2 か V3 か

2.x 系をインストールした直後の既定は V2（従来のハーネス）です。2026-10-09 の公式ブログは、2026-10-12 から起動時に V3（Kiro IDE・Kiro Web と同じ統一ハーネス）への切り替えを促すプロンプトを段階的に表示し、CLI 3.0 の公開で V3 が既定になると説明しています（<https://kiro.dev/blog/cli-3/>）。待たずに試すなら `kiro-cli --v3` で V3 のセッションを開けます。V3 だけにある機能（Specs の `/spec new`、`/tangent`、クラウドセッション `kiro-cli --cloud` など）と移行の注意点は [Kiro CLI の道](../01_story/03_cli-journey.md) と公式の V3 ページ（<https://kiro.dev/docs/cli/v3/>）を参照してください。

## ほかの入口

| 入口 | 公式の導線 | くわしくは（姉妹サイト） |
|---|---|---|
| **Kiro IDE** | <https://kiro.dev/downloads/> からインストーラを入手（macOS・Windows・Linux）。VS Code の設定と拡張機能を取り込める（公式「Installation」の Import settings） | [猫でもわかるKiro IDE アップデート情報](https://github.com/kamogashira-sys/kiro-ide-docs) |
| **Kiro Web** | <https://app.kiro.dev> にサインイン。有料プラン（Pro 以上）が必要で、GitHub または GitLab を接続する（公式「Authentication」の Web の節） | [猫でもわかるKiro Web アップデート情報](https://github.com/kamogashira-sys/kiro-web-docs) |
| **Kiro Mobile（iOS）** | 公式ドキュメント <https://kiro.dev/docs/mobile/>。Web と同じアカウントでクラウドセッションを扱う | 本シリーズに Mobile 専用サイトはありません |
| **Kiro Crew（OSS）** | リポジトリ <https://github.com/kirodotdev/KiroCrew> と公式ドキュメント <https://kiro.dev/docs/crew/> | [猫でもわかるKiro Crewアップデート情報](https://github.com/kamogashira-sys/kiro-crew-docs) |
| （注記）**ACP 対応エディタ** | 入口ではなく経路です。Kiro CLI を ACP サーバーとして JetBrains IDE・Zed などから使う（<https://kiro.dev/docs/cli/acp/>） | CLI 版サイトを参照 |

組織で IAM Identity Center を使っている場合、Kiro Web とクラウドセッションは管理者が有効化する必要があります（公式「Authentication」の注記）。

## 次に読む
<!-- sources: n/a -->

- [1 つのエージェント、5 つの入口](../01_story/02_one-agent.md)
- [なぜ筆者は Kiro CLI が好きなのか](../02_why-kiro-cli/01_why-i-love-kiro-cli.md)
