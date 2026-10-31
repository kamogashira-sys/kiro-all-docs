# はじめ方 ― Kiro CLI を 3 ステップで、ほかの入口は公式へ

Kiro には IDE・CLI・Web・Mobile・Crew の 5 つの入口があります（[選び方](../01_story/02_one-agent.md)）。本ページでは **Kiro CLI** を最初の 1 プロンプトまで 3 ステップで案内し（CLI を取り上げる理由は [なぜ筆者は Kiro CLI が好きなのか](../02_why-kiro-cli/01_why-i-love-kiro-cli.md)）、ほかの入口は公式の導線を示します。手順はすべて公式ドキュメントのものです。

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

Linux で glibc が 2.34 より古い場合や、rpm・deb・AppImage で入れたい場合の代替手順も同じ公式ページにあります。入ったかどうかは次で確かめられます。

```bash
kiro-cli --version
```

筆者の環境（2.37.0・2026-10-30）では `kiro-cli 2.37.0` と表示されました。

### ステップ 2: サインイン

```bash
kiro-cli login
```

公式の手順は 3 つです。(1) 端末で `kiro-cli` または `kiro-cli login` を実行すると、Enter を押してブラウザでサインインを完了するよう促される (2) ブラウザでプロバイダを選んで認証する (3) 認証後、端末に戻るようブラウザに表示され、サインイン済みになる。

サインインの方法は、公式ページの分類では **GitHub・Google・AWS Builder ID**（個人向け）と **Your organization**（AWS IAM Identity Center、または Okta・Microsoft Entra ID などの外部 IdP）です。ブラウザの無いリモートマシンでは `kiro-cli login --use-device-flow` のデバイスフロー、CI では API キー（環境変数 `KIRO_API_KEY`）が使えます。どの方法で入っているかは `kiro-cli whoami` で確認できます。

### ステップ 3: 最初の 1 プロンプト

プロジェクトのディレクトリに入って、チャットを開きます。

```bash
cd my-project
kiro-cli chat
```

筆者の環境（2.37.0・2026-10-30）で `kiro-cli --help` を実行すると、主なサブコマンドは次のように表示されます。

```text
Popular Subcommands              Usage: kiro-cli [subcommand]
╭────────────────────────────────────────────────────╮
│ chat         Chat with Kiro CLI                    │
│ agent        Manage AI agents                      │
│ doctor       Debug installation issues             │
│ settings     Customize appearance & behavior       │
│ quit         Quit the app                          │
╰────────────────────────────────────────────────────╯
```

最初の 1 プロンプトは、日本語で用件を書くだけです。筆者が初めて使った 2025-06-09 の指示は「ゲームをhtml,css,javascriptで作って。国旗当てのクイズです。…」でした（<https://qiita.com/kamogashira/items/59c3e641d984920c22a3>）。小さく始めるなら、次のような 1 行で十分です。

```text
このリポジトリの構成を調べて、README に書くべき「はじめ方」を提案して
```

チャットの中では `/` でコマンド一覧、`@` でファイルなどの文脈を追加できます（公式ブログ「A new look for the Kiro CLI」<https://kiro.dev/blog/new-look-for-cli/>）。V3 の機能（Specs の `/spec new`、`/tangent`、クラウドセッション `kiro-cli --cloud` など）は [Kiro CLI の道](../01_story/03_cli-journey.md) と公式の V3 ページ（<https://kiro.dev/docs/cli/v3/>）を参照してください。

## ほかの入口

| 入口 | 公式の導線 | くわしくは（姉妹サイト） |
|---|---|---|
| **Kiro IDE** | <https://kiro.dev/downloads/> からインストーラを入手（macOS・Windows・Linux）。VS Code の設定と拡張機能を取り込める | [猫でもわかるKiro IDE アップデート情報](https://github.com/kamogashira-sys/kiro-ide-docs) |
| **Kiro Web** | <https://app.kiro.dev> にサインイン。有料プラン（Pro 以上）が必要で、GitHub または GitLab を接続する | [猫でもわかるKiro Web アップデート情報](https://github.com/kamogashira-sys/kiro-web-docs) |
| **Kiro Mobile（iOS）** | 公式ドキュメント <https://kiro.dev/docs/mobile/>。Web と同じアカウントでクラウドセッションを扱う | 本シリーズに Mobile 専用サイトはありません |
| **Kiro Crew（OSS）** | リポジトリ <https://github.com/kirodotdev/KiroCrew> と公式ドキュメント <https://kiro.dev/docs/crew/> | [猫でもわかるKiro Crewアップデート情報](https://github.com/kamogashira-sys/kiro-crew-docs) |
| **ACP 対応エディタ** | Kiro CLI を ACP サーバーとして JetBrains IDE・Zed などから使う（<https://kiro.dev/docs/cli/acp/>） | CLI 版サイトを参照 |

組織で IAM Identity Center を使っている場合、Kiro Web とクラウドセッションは管理者が有効化する必要があります（公式「Authentication」の注記）。

## 出典

| 出典 | 更新日 |
|---|---|
| [Installation](https://kiro.dev/docs/getting-started/installation/) | 2026-10-21 |
| [Authentication](https://kiro.dev/docs/getting-started/authentication/) | 2026-10-29 |
| [CLI](https://kiro.dev/docs/cli/) | 2026-08-04 |
| [A new look for the Kiro CLI](https://kiro.dev/blog/new-look-for-cli/) | 2026-03-23 |

## 次に読む <!-- sources: n/a -->

- [1 つのエージェント、5 つの入口](../01_story/02_one-agent.md)
- [なぜ筆者は Kiro CLI が好きなのか](../02_why-kiro-cli/01_why-i-love-kiro-cli.md)
