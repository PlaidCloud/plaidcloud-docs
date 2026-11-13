---
title: PlaidCloud GitからのPanelアプリのデプロイ
description: HoloViz PanelアプリをPlaidCloudで提供するまでの一連の流れです。コードをPlaidCloud Gitリポジトリに置き、認証情報不要の管理対象接続で接続し、公開します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

ここでは、手元のマシンにあるPanelアプリのコードから、公開URLまでの一連の流れを、ワークスペースに組み込まれた管理対象のGitサービスである **[PlaidCloud Git](/ja/guides/git/)** をソースとして説明します。PlaidCloud Gitは管理対象のため、アプリのデプロイに使用する接続には、**サーバーのURL、ユーザー名、トークンが不要**です。PlaidCloudが代わりに認証します。

手順は5つあります。

1. 最小限のPanelアプリを作成します。
2. PlaidCloud Gitリポジトリに配置します。
3. 管理対象のPlaidCloud Git接続を作成します。
4. リポジトリを指すサーバーアプリを公開します。
5. 提供されているアプリを開きます。起動しない場合は、ビルドログを確認します。

各手順には、その内容を詳しく説明したガイドへのリンクがあります。このページは、それらを1つの流れにまとめたものです。

## 始める前に

- ワークスペースから**Git**を開き、PlaidCloud Gitにアクセスできることを確認します。デフォルトでは、ワークスペースの組織に **`apps`** リポジトリ（と **`udfs`** リポジトリ）が含まれています。Panelアプリの置き場所として最適です。
- 手元のマシンからコードをプッシュする場合は、ローカルに`git`をインストールしておきます（Gitのウェブ UIでファイルを追加することもできます）。

## 1. 最小限のPanelアプリを作成する

アプリには、**エントリポイント**（Panelアプリを構築し、`.servable()`でマークするPythonファイル）が必要です。追加のパッケージが必要な場合は、**`requirements.txt`** を、リポジトリのルート、またはエントリポイントの隣に配置します。

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

これで完全なアプリです。PlaidCloudが提供するのは`.servable()`の呼び出しです。`panel`、`bokeh`、PlaidCloudのクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされているため、`requirements.txt`には*追加の*パッケージのみを記載します。より充実した例、依存関係、ライト/ダークのテーマ設定については、[Panelアプリの作成](/ja/guides/panel-apps/creating/)を参照してください。

## 2. アプリをPlaidCloud Gitリポジトリに配置する

ワークスペースの既存の **`apps`** リポジトリを使用するか、[新しいリポジトリを作成](/ja/guides/git/repositories/#リポジトリを作成する)します。次に、コードをそこに配置します。[Panel Studio](/ja/guides/panel-apps/studio/#アプリの保存場所)で構築したアプリは、すでに`apps`内のフォルダーになっているため、自分のアプリの隣にあります。

PlaidCloudを通じてサインインするため、Gitアカウントには別のパスワードがありません。**write:repository**権限を持つ[パーソナルアクセストークンを生成](/ja/guides/git/repositories/#個人用アクセストークンを生成する)し（**アバター → Settings → Applications**）、Gitからプロンプトが表示されたときに、パスワードとして使用します。`apps`へのプッシュには**Contributor**アクセスが必要です。**Git**タブで**閲覧者**と表示されている場合は、ワークスペース管理者に**Git Contributors**への追加を依頼してください。**Git**タブで、リポジトリのクローンアドレスの横にあるコピーボタンを使用し、次を実行します。

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

リポジトリのパス`<org>/apps`（`<org>`はワークスペースの組織名）を控えておいてください。次の手順で、そのパスを入力します。クローン、コミット、プッシュの詳細は、[リポジトリ](/ja/guides/git/repositories/)にあります。

> **ここでのトークンは、*ご自身*がコードをプッシュするためだけのものです**。次に作成する接続は管理対象で、トークンは不要です。この2つを混同しないでください。

## 3. 管理対象のPlaidCloud Git接続を作成する

**接続**は、Panelのデプロイメントに、コードの場所を伝えます。PlaidCloud Gitの接続は*管理対象*です。PlaidCloudがホストと認証情報を提供するため、入力するのはリポジトリのターゲットのみです。

1. **Tools > Connections**を開き、**新規接続**をクリックして、**PlaidCloud Git**を選択します。
2. 接続に**アカウント名**を付けます（たとえば、`Apps Repo`）。
3. **Repository Path**を`<org>/apps`（手順2で控えたパス）に、**デフォルトブランチ**を`main`に設定します。アプリがサブディレクトリにある場合を除き、**開始パス**は空白のままにします。
4. **作成**をクリックします。

サーバーURL、ユーザー、パスワード、SSL/SSHのフィールドはありません。PlaidCloud Gitは管理対象のため、ホストと認証はプラットフォームが処理します。接続の**使用方法**と**セキュリティモデル**（ワークスペース内で誰が使用できるか）を含む、フォーム全体については、[PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/)を参照してください。

> **古いワークスペースのビルドの場合は、** サーバーURLや認証情報のフィールドがまだ表示される場合は、空白のままにしてください。どちらの場合も、プラットフォームが代わりに認証します。

## 4. サーバーアプリを公開する

次に、サーバーのデプロイメントを、その接続に向けます。

1. **アプリ**を開き、**New app** > **Server based**を選択します。
2. **ディレクトリ設定**で、**アプリ名**と**URLスラッグ**を設定します。スラッグはアプリのURLと内部名になるため、小文字、数字、ハイフンのみで、文字で始まり、40文字以内にします（たとえば、`hello-panel`）。
3. **Git接続と公開ウォッチャー**で：
   - **Git接続** — 手順3で作成したPlaidCloud Git接続です。
   - **ブランチ** — `main`です。このブランチにプッシュすると、アプリが自動的に再ビルドされ、再デプロイされます。
   - **エントリポイント** — `app.py`です。
4. **ランタイム**で、**CPU**、**メモリ**、**デザイン**（PlaidCloudのモダンな外観には**FAST**）、**Idle**ウィンドウを選択します。サインインなしでアプリにアクセスできるようにする場合のみ、**パブリックアクセスを許可**をチェックします。
5. **公開**をクリックします。

このダイアログのすべてのフィールドについては、[Panelアプリの作成](/ja/guides/panel-apps/creating/#アプリを公開する)で説明しています。

## 5. アプリを開く。起動しない場合はログを確認する

公開すると、アプリは**ビルド**されます。PlaidCloudがブランチをクローンし、`requirements.txt`（リポジトリのルートのものと、あればアプリのフォルダーのもの）をインストールして、コンテナーイメージをビルドします。**ステータス**は**マイPanelアプリ**リストに表示され、自動的に更新されます。

- ステータスが**準備完了**になったら、`https://<your-tenant-host>/serve/<slug>/`でアプリを開きます。アイドル状態の後の最初のリクエストでは、起動に（約15秒）かかります。
- ビルドが失敗した場合は、アプリを開いて**ビルド**ログを確認します。不足している依存関係やインポートエラーが、そこに表示されます。各ステータスの意味、ログの読み方、再ビルドの実行方法については、[Panelアプリの使い方](/ja/guides/panel-apps/using/)を参照してください。

以降は、**接続のブランチにプッシュするたびに、アプリが自動的に再ビルドされ、再デプロイされます**。`app.py`を編集して`git push`すれば、変更が反映されます。（ただし、アプリが**ロック**されている場合は除きます。[アプリのロック](/ja/guides/panel-apps/using/#アプリのロック)を参照してください。その場合、ロックを解除するまで、プッシュはスキップされます。）

## 次のステップ

- [Panelアプリの作成](/ja/guides/panel-apps/creating/) — より充実した例、依存関係、ライト/ダークのテーマ設定
- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) — 接続フォーム全体、使用方法、セキュリティモデル
- [データとサインイン中のユーザーの読み取り](/ja/guides/panel-apps/accessing-data/) — アプリを閲覧しているユーザーとして、PlaidCloudのデータをクエリします
- [リポジトリ](/ja/guides/git/repositories/) — PlaidCloud Gitでのブランチ、トークン、共同作業
