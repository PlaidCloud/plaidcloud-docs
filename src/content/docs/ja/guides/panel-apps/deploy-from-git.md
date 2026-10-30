---
title: PlaidCloud GitからPanelアプリをデプロイする
description: PlaidCloudでHoloViz Panelアプリを配信するまでの一連の流れです。コードをPlaidCloud Gitリポジトリに置き、認証情報が不要なマネージド接続で接続して、公開します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

ここでは、ご自分のマシン上のPanelアプリのコードから、公開されたURLまでの全体の流れを、ワークスペースに組み込まれたマネージドのGitサービスである **[PlaidCloud Git](/ja/guides/git/)** をソースとして説明します。PlaidCloud Gitはマネージドなので、アプリのデプロイ元となる接続には、**サーバーのURL、ユーザー名、トークンは不要**です。PlaidCloudがユーザーに代わって認証します。

手順は5つです。

1. 最小限のPanelアプリを書きます。
2. PlaidCloud Gitリポジトリに置きます。
3. マネージドのPlaidCloud Git接続を作成します。
4. リポジトリを指すサーバーアプリを公開します。
5. 配信されたアプリを開きます。起動しない場合はビルドログを確認します。

各ステップには、その部分に関する詳細なガイドへのリンクがあります。このページは、それらを1つの流れにまとめたものです。

## 始める前に

- ワークスペースから**Git**を開き、PlaidCloud Gitにアクセスできることを確認します。デフォルトでは、ワークスペースの組織には **`apps`** リポジトリ（と **`udfs`** リポジトリ）があり、Panelアプリの置き場所として最適です。
- マシンからコードをプッシュする場合は、ローカルに`git`をインストールしてください（GitのWeb UIでファイルを追加することもできます）。

## 1. 最小限のPanelアプリを書く

アプリには、Panelアプリを構築して`.servable()`としてマークするPythonファイルである**エントリポイント**が必要です。必要に応じて、追加のパッケージ用の **`requirements.txt`** も、リポジトリのルートまたはエントリポイントの隣に置きます。

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

`app.py`を作成します。

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

これで完全なアプリです。PlaidCloudが配信するのは`.servable()`の呼び出しです。`panel`、`bokeh`、PlaidCloudのクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされているため、`requirements.txt`には*追加の*パッケージだけを記載します。より充実した例、依存関係、ライトとダークのテーマ設定については、[Panelアプリの作成](/ja/guides/panel-apps/creating/)を参照してください。

## 2. アプリをPlaidCloud Gitリポジトリに置く

ワークスペースにある既存の **`apps`** リポジトリを使用するか、[新しく作成](/ja/guides/git/repositories/#リポジトリの作成)します。次に、コードをその中に入れます。

PlaidCloud経由でサインインするため、Gitアカウントには別のパスワードがありません。リポジトリの**読み取り**と**書き込み**のスコープを持つ[パーソナルアクセストークンを生成](/ja/guides/git/repositories/#個人用アクセストークンの生成)し（**アバター → Settings → Applications**）、Gitがパスワードを求めたときにそれを使用します。リポジトリの**コード**ボタンから**HTTPS**のクローンURLをコピーし、次のように実行します。

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

リポジトリのパス（`<org>/apps`）を控えておいてください。`<org>`はワークスペースの組織名です。このパスは次のステップで入力します。クローン、コミット、プッシュの詳細は、[リポジトリ](/ja/guides/git/repositories/)にあります。

> **ここでのトークンは、*ご自身が*コードをプッシュするためだけのものです。** 次に作成する接続はマネージドでトークンは不要なので、両者を混同しないでください。

## 3. マネージドのPlaidCloud Git接続を作成する

**接続**は、Panelのデプロイにコードの場所を伝えます。PlaidCloud Gitでは、接続は*マネージド*で、ホストと認証情報はPlaidCloudが提供するため、入力するのはリポジトリの対象だけです。

1. **Tools > Connections**を開き、**新規接続**をクリックして、**PlaidCloud Git**を選択します。
2. 接続に**アカウント名**を付けます（例：`Apps Repo`）。
3. **Repository Path**を、ステップ2で控えたパスの`<org>/apps`に設定し、**デフォルトブランチ**を`main`に設定します。アプリがサブディレクトリにある場合を除き、**開始パス**は空白のままにします。
4. **作成**をクリックします。

サーバーURL、ユーザー、パスワード、SSL/SSHのフィールドはありません。PlaidCloud Gitはマネージドなので、ホストと認証はプラットフォームが処理します。接続の**使用方法**と**セキュリティモデル**（ワークスペース内で誰が使用できるか）を含むフォームの詳細については、[PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/)を参照してください。

> **古いワークスペースのビルドをお使いの場合は、** フォームにサーバーURLや認証情報のフィールドが表示されていても、空白のままにしてください。どちらの場合も、プラットフォームがユーザーに代わって認証します。

## 4. サーバーアプリを公開する

次に、サーバーのデプロイをその接続に向けます。

1. **マイPanelアプリ**を開き、**新しいサーバーアプリ**をクリックします。
2. **ディレクトリ設定**で、**アプリ名**と**URLスラッグ**を設定します。スラッグはアプリのURLと内部名になるため、小文字、数字、ハイフンを使い、先頭は文字、40文字以内にします（例：`hello-panel`）。
3. **Git接続と公開ウォッチャー**で、次の項目を設定します。
   - **Git接続** — ステップ3で作成したPlaidCloud Git接続です。
   - **ブランチ** — `main`です。このブランチにプッシュすると、アプリが自動的に再ビルドされ、再デプロイされます。
   - **エントリポイント** — `app.py`です。
4. **ランタイム**で、**CPU**、**メモリ**、**デザイン**（PlaidCloudの最新の外観には**FAST**）、**アイドル**の時間枠を選択します。サインインなしでアプリにアクセスできるようにする場合にのみ、**パブリックアクセスを許可**をオンにします。
5. **公開**をクリックします。

このダイアログのすべてのフィールドについては、[Panelアプリの作成](/ja/guides/panel-apps/creating/#アプリを公開する)で説明しています。

## 5. アプリを開く。起動しない場合はログを確認する

公開すると、アプリの**ビルド**が行われます。PlaidCloudはブランチをクローンし、`requirements.txt`（リポジトリのルートのものと、アプリのフォルダーのもの。存在する場合）をインストールして、コンテナーイメージをビルドします。**ステータス**は**マイPanelアプリ**の一覧に表示され、自動的に更新されます。

- ステータスが**準備完了**になったら、`https://<your-tenant-host>/serve/<slug>/`でアプリを開きます。アイドル状態の後の最初のリクエストでは、起動に約15秒かかります。
- ビルドが失敗した場合は、アプリを開いて**ビルド**ログを確認します。依存関係の不足やインポートエラーは、ここに表示されます。各ステータスの意味、ログの読み方、再ビルドの実行方法については、[Panelアプリの使用](/ja/guides/panel-apps/using/)を参照してください。

以降は、**接続のブランチにプッシュするたびに、アプリが自動的に再ビルドされ、再デプロイされます**。`app.py`を編集して`git push`すれば、変更が反映されます。（ただし、アプリが**ロック**されている場合は除きます。[アプリのロック](/ja/guides/panel-apps/using/#アプリのロック)を参照してください。その場合、ロックを解除するまでプッシュはスキップされます。）

## 次のステップ

- [Panelアプリの作成](/ja/guides/panel-apps/creating/) — より充実した例、依存関係、ライトとダークのテーマ設定
- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) — 接続フォームの詳細、使用方法、セキュリティモデル
- [データとサインイン中のユーザーの読み取り](/ja/guides/panel-apps/accessing-data/) — アプリを閲覧しているユーザーとしてPlaidCloudのデータをクエリします
- [リポジトリ](/ja/guides/git/repositories/) — PlaidCloud Gitでのブランチ、トークン、共同作業
