---
title: PlaidCloud GitからPanelアプリをデプロイする
description: HoloViz PanelアプリをPlaidCloudで配信するまでの一連の手順です。コードをPlaidCloud Gitリポジトリに置き、認証情報不要のマネージド接続で接続し、公開します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

このガイドでは、お使いのマシン上にあるPanelアプリのコードから、公開URLで動作するまでの全手順を説明します。ソースには、ワークスペースに組み込まれたマネージドGitサービスである **[PlaidCloud Git](/ja/guides/git/)** を使用します。PlaidCloud Gitはマネージドサービスのため、アプリのデプロイ元となる接続には **サーバーURL、ユーザー名、トークンは不要** です。PlaidCloudがお客様に代わって認証を行います。

手順は次の5つです。

1. 最小限のPanelアプリを作成します。
2. PlaidCloud Gitリポジトリに配置します。
3. マネージドのPlaidCloud Git接続を作成します。
4. リポジトリを指すサーバーアプリを公開します。
5. 配信されたアプリを開きます。起動しない場合はビルドログを確認します。

各手順には、その内容を詳しく説明したガイドへのリンクがあります。このページは、それらを1つの流れにまとめたものです。

## 始める前に

- ワークスペースから **Git** を開き、PlaidCloud Gitにアクセスできることを確認します。デフォルトでは、ワークスペースの組織に **`apps`** リポジトリ（および **`udfs`** リポジトリ）が含まれています。apps はPanelアプリの置き場所として最適です。
- マシンからコードをプッシュする場合は、`git` をローカルにインストールしておきます（Git Webインターフェースでファイルを追加することもできます）。

## 1. 最小限のPanelアプリを作成する

アプリには **エントリポイント** が必要です。これはPanelアプリをビルドし、`.servable()` を指定するPythonファイルです。追加パッケージが必要な場合は、リポジトリのルート、またはエントリポイントと同じ場所に **`requirements.txt`** を置きます（省略可能）。

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

`app.py` を作成します。

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

これで完全なアプリです。PlaidCloudが配信するのは `.servable()` の呼び出しです。`panel`、`bokeh`、およびPlaidCloudクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされているため、`requirements.txt` には *追加の* パッケージだけを記載してください。より詳しい例、依存関係、ライト/ダークテーマについては、[Panelアプリを作成する](/ja/guides/panel-apps/creating/)を参照してください。

## 2. アプリをPlaidCloud Gitリポジトリに配置する

ワークスペースの既存の **`apps`** リポジトリを使用するか、[新しいリポジトリを作成](/ja/guides/git/repositories/#リポジトリを作成する)します。その後、コードをリポジトリに入れます。

PlaidCloud経由でサインインするため、Gitアカウントには別のパスワードがありません。**write:repository** 権限を持つ[パーソナルアクセストークンを生成](/ja/guides/git/repositories/#パーソナルアクセストークンを生成する)し（**自分のアバター → 設定 → アプリケーション**）、Gitがパスワードを求めたときにそのトークンを入力します。`apps` にプッシュするには **Contributor** アクセスが必要です。**Git** タブに読み取りアクセスと表示される場合は、ワークスペースの管理者に **Git Contributors** へ追加するよう依頼してください。**Git** タブでリポジトリの **Copy clone URL** を選択し、次のコマンドを実行します。

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

リポジトリのパス `<org>/apps` を控えておいてください。`<org>` はワークスペースの組織名です。このパスは次の手順で入力します。クローン、コミット、プッシュの詳細は[リポジトリ](/ja/guides/git/repositories/)を参照してください。

> **ここでのトークンは、 *お客様自身* がコードをプッシュするためだけのものです。** 次に作成する接続はマネージドでトークンは不要です。両者を混同しないようにしてください。

## 3. マネージドのPlaidCloud Git接続を作成する

**接続** は、Panelデプロイメントがコードの場所を把握するための設定です。PlaidCloud Gitの接続は *マネージド* で、ホストと認証情報はPlaidCloudが提供するため、リポジトリのターゲットだけを入力します。

1. **Tools > Connections** を開き、**新規接続** をクリックして **PlaidCloud Git** を選択します。
2. 接続に **アカウント名** を付けます（例: `Apps Repo`）。
3. **Repository Path** に、手順2で控えたパス `<org>/apps` を設定し、**デフォルトブランチ** を `main` にします。アプリがサブディレクトリにある場合を除き、**開始パス** は空欄のままにします。
4. **作成** をクリックします。

サーバーURL、ユーザー、パスワード、SSL/SSHのフィールドはありません。PlaidCloud Gitはマネージドのため、ホストと認証はプラットフォームが処理します。接続の **使用方法** と **セキュリティモデル**（ワークスペース内で誰が使用できるか）を含むフォームの詳細は、[PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/)を参照してください。

> **古いワークスペースビルドをお使いですか？** フォームにサーバーURLや認証情報のフィールドがまだ表示される場合は、空欄のままにしてください。どちらの場合も、プラットフォームがお客様に代わって認証します。

## 4. サーバーアプリを公開する

次に、サーバーデプロイメントをその接続に向けます。

1. **マイPanelアプリ** を開き、**新しいサーバーアプリ** をクリックします。
2. **ディレクトリ設定** で **アプリ名** と **URLスラッグ** を設定します。スラッグはアプリのURLと内部名になるため、英小文字、数字、ハイフンを使用し、先頭は英字、40文字以内にしてください（例: `hello-panel`）。
3. **Git接続と公開ウォッチャー** で次を設定します。
   - **Git接続** — 手順3で作成したPlaidCloud Git接続です。
   - **ブランチ** — `main`。このブランチへのプッシュのたびに、アプリが自動的に再ビルドされ再デプロイされます。
   - **エントリポイント** — `app.py`。
4. **ランタイム** で、**CPU**、**メモリ**、**デザイン**（PlaidCloudのモダンな外観には **FAST**）、**アイドル** の時間を選択します。サインインなしでアプリにアクセスできるようにする場合にのみ、**パブリックアクセスを許可** にチェックを入れます。
5. **公開** をクリックします。

このダイアログの各フィールドについては、[Panelアプリを作成する](/ja/guides/panel-apps/creating/#アプリを公開する)で説明しています。

## 5. アプリを開く、起動しない場合はログを確認する

公開後、アプリは **ビルド** されます。PlaidCloudがブランチをクローンし、`requirements.txt`（リポジトリのルートとアプリフォルダーにあればその両方）をインストールして、コンテナイメージをビルドします。その **ステータス** は **マイPanelアプリ** 一覧に表示され、自動的に更新されます。

- ステータスが **準備完了** になったら、`https://<your-tenant-host>/serve/<slug>/` でアプリを開きます。アイドル状態の後の最初のリクエストでアプリが起動します（約15秒）。
- ビルドが失敗した場合は、アプリを開いて **作成** ログを確認してください。依存関係の不足やインポートエラーはここに表示されます。各ステータスの意味、ログの読み方、再ビルドの実行方法については、[Panelアプリを使用する](/ja/guides/panel-apps/using/)を参照してください。

以降は、**接続のブランチへプッシュするたびにアプリが自動的に再ビルドされ再デプロイされます**。`app.py` を編集して `git push` すれば、変更が公開されます（ただし、アプリが **ロック** されている場合は、ロックを解除するまでプッシュはスキップされます。[アプリのロック](/ja/guides/panel-apps/using/#アプリのロック)を参照してください）。

## 次のステップ

- [Panelアプリを作成する](/ja/guides/panel-apps/creating/) — より詳しい例、依存関係、ライト/ダークテーマについて説明します
- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) — 接続フォームの詳細、使用方法、セキュリティモデルについて説明します
- [データとサインイン中のユーザーの読み取り](/ja/guides/panel-apps/accessing-data/) — アプリを閲覧しているユーザーとしてPlaidCloudのデータをクエリします
- [リポジトリ](/ja/guides/git/repositories/) — PlaidCloud Gitでのブランチ、トークン、共同作業について説明します
