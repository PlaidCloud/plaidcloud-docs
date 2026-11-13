---
title: PlaidCloud Git から Panelアプリをデプロイする
description: HoloViz Panelアプリを PlaidCloud で提供するための一連の手順です。コードを PlaidCloud Git リポジトリに置き、認証情報不要の管理対象接続で接続し、本番に公開します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

これは、お使いのマシン上のPanelアプリのコードから、公開 URL までの一連の手順です。ソースには、ワークスペースに組み込まれた管理対象の Git サービスである **[PlaidCloud Git](/ja/guides/git/)** を使用します。PlaidCloud Git は管理対象のため、アプリのデプロイ元となる接続に**サーバー URL、ユーザー名、トークンは不要**です。PlaidCloud があなたに代わって認証を行います。

手順は 5 つあります。

1. 最小限のPanelアプリを作成します。
2. それを PlaidCloud Git リポジトリに置きます。
3. 管理対象の PlaidCloud Git 接続を作成します。
4. リポジトリを指すサーバーアプリを公開します。
5. 提供されたアプリを開きます。起動しない場合はビルドログを確認します。

各手順には、それぞれの詳しいガイドへのリンクがあります。このページは、それらを 1 つの流れにまとめたものです。

## 始める前に

- ワークスペースから **Git** を開き、PlaidCloud Git にアクセスできることを確認します。デフォルトでは、ワークスペースの組織に **`apps`** リポジトリ（と **`udfs`** リポジトリ）があり、Panelアプリの置き場所として最適です。
- お使いのマシンからコードをプッシュする場合は、ローカルに `git` をインストールしておきます（Git の Web UI でファイルを追加することもできます）。

## 1. 最小限のPanelアプリを作成する

アプリには**エントリポイント**が必要です。これは、Panelアプリを構築して `.servable()` を付ける Python ファイルです。必要に応じて、追加パッケージ用の **`requirements.txt`** を、リポジトリのルート、またはエントリポイントの隣に置きます。

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

これで完全なアプリです。PlaidCloud が提供するのは、`.servable()` を呼び出したものです。`panel`、`bokeh`、PlaidCloud クライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はあらかじめインストールされているため、`requirements.txt` には*追加の*パッケージだけを記載します。より充実した例、依存関係、ライトテーマとダークテーマについては、[Panelアプリを作成する](/ja/guides/panel-apps/creating/)を参照してください。

## 2. アプリを PlaidCloud Git リポジトリに置く

ワークスペースにすでにある **`apps`** リポジトリを使うか、[新しいリポジトリを作成](/ja/guides/git/repositories/#リポジトリを作成する)します。次に、コードをそこに入れます。[Panel Studio](/ja/guides/panel-apps/studio/#アプリの保存場所) で作成したアプリはすでに `apps` 内のフォルダーになっているため、あなたのアプリの隣に表示されます。

PlaidCloud 経由でサインインするため、Git アカウントには別のパスワードがありません。**write:repository** 権限を持つ[個人用アクセストークンを生成](/ja/guides/git/repositories/#個人用アクセストークンを生成する)し（**アバター → Settings → Applications**）、Git がパスワードを求めたときにそれを使用します。`apps` にプッシュするには **Contributor** アクセスが必要です。**Git** タブで自分が**閲覧者**と表示されている場合は、ワークスペース管理者に **Git Contributors** への追加を依頼してください。**Git** タブでリポジトリのクローンアドレスの横にあるコピーボタンを使い、次を実行します。

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

リポジトリのパス `<org>/apps` を控えておきます。`<org>` は、ワークスペースの組織名です。このパスは、次の手順で入力します。クローン、コミット、プッシュの詳細な手順は、[リポジトリ](/ja/guides/git/repositories/)にあります。

> **ここでのトークンは、*あなた*がコードをプッシュするためだけのものです。** 次に作成する接続は管理対象でトークンは不要です。この 2 つを混同しないでください。

## 3. 管理対象の PlaidCloud Git 接続を作成する

**接続**は、Panelデプロイメントにコードの場所を伝えます。PlaidCloud Git の場合、接続は*管理対象*で、PlaidCloud がホストと認証情報を提供するため、入力するのはリポジトリのターゲットだけです。

1. **Tools > Connections** を開き、**新規接続**をクリックして、**PlaidCloud Git** を選択します。
2. 接続に**アカウント名**を付けます（例: `Apps Repo`）。
3. **Repository Path** に、手順 2 で控えた `<org>/apps` を、**デフォルトブランチ**に `main` を設定します。アプリがサブディレクトリにある場合を除き、**開始パス**は空のままにします。
4. **作成**をクリックします。

サーバー URL、ユーザー、パスワード、SSL/SSH のフィールドはありません。PlaidCloud Git は管理対象のため、プラットフォームがホストと認証を処理します。接続の**使用方法**と**セキュリティモデル**（ワークスペース内で誰が使用できるか）を含む、フォームの完全な説明は、[PlaidCloud Git 接続](/ja/guides/connections/plaidcloud-git/)を参照してください。

> **古いワークスペースビルドを使っていますか？** フォームに**サーバーURL**や認証情報のフィールドがまだ表示されている場合は、空のままにしてください。どちらの場合も、プラットフォームがあなたに代わって認証を行います。

## 4. サーバーアプリを公開する

次に、その接続を指すサーバーデプロイメントを設定します。

1. **マイPanelアプリ**を開き、**新しいサーバーアプリ**をクリックします。
2. **ディレクトリ設定**で、**アプリ名**と **URLスラッグ**を設定します。スラッグはアプリの URL と内部名になるため、小文字、数字、ハイフンを使い、文字で始め、40 文字以内にします（例: `hello-panel`）。
3. **Git接続と公開ウォッチャー**で、次を設定します。
   - **Git接続** — 手順 3 で作成した PlaidCloud Git 接続。
   - **ブランチ** — `main`。このブランチへのプッシュで、アプリが自動的に再ビルドされ、再デプロイされます。
   - **エントリポイント** — `app.py`。
4. **ランタイム**で、**CPU**、**メモリ**、**デザイン**（PlaidCloud の最新の外観には **FAST**）、**Idle** ウィンドウを選択します。サインインなしでアプリにアクセスできるようにする場合にのみ、**パブリックアクセスを許可**にチェックを入れます。
5. **公開**をクリックします。

このダイアログのすべてのフィールドは、[Panelアプリを作成する](/ja/guides/panel-apps/creating/#アプリを公開する)で説明されています。

## 5. アプリを開く。起動しない場合はログを確認する

公開すると、アプリが**ビルド**されます。PlaidCloud はブランチをクローンし、`requirements.txt`（リポジトリのルートとアプリフォルダーにあるもの）をインストールし、コンテナイメージをビルドします。その**ステータス**は**マイPanelアプリ**一覧に表示され、自動的に更新されます。

- ステータスが**準備完了**になったら、`https://<your-tenant-host>/serve/<slug>/` でアプリを開きます。アイドル状態の後の最初のリクエストでアプリが起動します（約 15 秒）。
- ビルドが失敗した場合は、アプリを開いて**作成**ログを確認してください。依存関係の不足やインポートエラーはここに表示されます。各ステータスの意味、ログの読み方、再ビルドの実行方法については、[Panelアプリを使用する](/ja/guides/panel-apps/using/)を参照してください。

以降は、**接続のブランチにプッシュするたびに、アプリが自動的に再ビルドされ、再デプロイされます**。`app.py` を編集して `git push` すれば、変更が本番に反映されます。（ただし、アプリが**ロック**されている場合は別です。[アプリのロック](/ja/guides/panel-apps/using/#アプリのロック)を参照してください。その場合、ロックを解除するまでプッシュはスキップされます。）

## 次のステップ

- [Panelアプリを作成する](/ja/guides/panel-apps/creating/) — より充実した例、依存関係、ライトテーマとダークテーマ
- [PlaidCloud Git 接続](/ja/guides/connections/plaidcloud-git/) — 接続フォームの全項目、使用方法、セキュリティモデル
- [データとサインイン中のユーザーを読み取る](/ja/guides/panel-apps/accessing-data/) — アプリを見ているユーザーとして PlaidCloud のデータをクエリします
- [リポジトリ](/ja/guides/git/repositories/) — PlaidCloud Git でのブランチ、トークン、共同作業
