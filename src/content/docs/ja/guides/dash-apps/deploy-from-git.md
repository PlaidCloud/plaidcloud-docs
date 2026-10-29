---
title: PlaidCloud GitからDashアプリをデプロイする
description: PlaidCloud で Plotly Dash アプリを提供するまでの一連の手順です。コードを PlaidCloud Git リポジトリに置き、認証情報不要のマネージド接続で連携し、ライブで公開します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

ここでは、手元のマシンにある Dash アプリのコードからライブ URL までの全手順を、ワークスペースに組み込まれたマネージド Git サービスである **[PlaidCloud Git](/ja/guides/git/)** をソースとして説明します。PlaidCloud Git はマネージドサービスのため、アプリのデプロイに使う接続には**サーバー URL、ユーザー名、トークンは不要**です。認証は PlaidCloud が代行します。

手順は次の5つです。

1. 最小限の Dash アプリを書く。
2. PlaidCloud Git リポジトリに置く。
3. マネージドの PlaidCloud Git 接続を作成する。
4. リポジトリを指す Dash アプリを公開する。
5. 提供されたアプリを開く。起動しない場合はビルドログを確認する。

この手順は[PlaidCloud GitからPanelアプリをデプロイする](/ja/guides/panel-apps/deploy-from-git/)とほぼ同じです。どちらも Git からビルドされ、同じ方法で提供されるサーバーサイドの Python アプリです。違いは、アプリのコード自体と、公開ダイアログの1つのフィールドだけです。

## 始める前に

- ワークスペースから **Git** を開き、PlaidCloud Git にアクセスできることを確認します。デフォルトでは、ワークスペースの組織に **`apps`** リポジトリが含まれています。Dashアプリにもそのまま使えます。
- 手元のマシンからコードをプッシュする場合は、`git` をローカルにインストールしておきます（Git の Web UI でファイルを追加することもできます）。

## 1. 最小限のDashアプリを書く

アプリには**エントリポイント**が必要です。これは、Dash アプリを構築して Flask サーバーを公開する Python ファイルです。必要に応じて、追加パッケージ用の **`requirements.txt`** を、リポジトリのルートまたはエントリポイントと同じ場所に置きます。

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

`app.py` を作成します。

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

これで完全なアプリです。`dash`、`plotly`、`dash-mantine-components`、`dash-ag-grid`、PlaidCloud クライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされているため、`requirements.txt` には*追加の*パッケージだけを記載します。`Dash(__name__)` に `requests_pathname_prefix` や `url_base_pathname` を渡さないでください。プラットフォームが `DASH_URL_BASE_PATHNAME` を通じて URL プレフィックスを自動的に設定するため、両方を設定すると起動時に設定エラーが発生します。アプリの完全な規約とデータアクセス用ヘルパーについては、[アプリの規約](/ja/guides/dash-apps/#アプリの規約)と[Dashアプリでのデータとサインイン中ユーザーの読み取り](/ja/guides/dash-apps/accessing-data/)をご覧ください。

## 2. アプリをPlaidCloud Gitリポジトリに置く

ワークスペースの既存の **`apps`** リポジトリを使うか、[新しいリポジトリを作成](/ja/guides/git/repositories/#リポジトリの作成)します。その後、コードをリポジトリに登録します。

PlaidCloud 経由でサインインするため、Git アカウントには別途パスワードがありません。リポジトリの**読み取り**と**書き込み**のスコープを持つ[パーソナルアクセストークンを生成](/ja/guides/git/repositories/#個人用アクセストークンの生成)し（**アバター → 設定 → アプリケーション**）、Git がパスワードを求めたらそのトークンを入力します。リポジトリの **コード** ボタンから **HTTPS** のクローン URL をコピーし、次のように実行します。

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

リポジトリパス `<org>/apps` を控えておいてください。`<org>` はワークスペースの組織名です。このパスは次の手順で入力します。クローン、コミット、プッシュの詳細は[リポジトリ](/ja/guides/git/repositories/)をご覧ください。

> **ここでのトークンは、*ご自身*がコードをプッシュするためだけのものです。** 次に作成する接続はマネージドでトークンは不要です。両者を混同しないでください。

## 3. マネージドのPlaidCloud Git接続を作成する

**接続**は、Dash デプロイメントにコードの場所を伝えます。PlaidCloud Git の接続は*マネージド*です。ホストと認証情報は PlaidCloud が用意するため、入力するのはリポジトリの指定だけです。これは、サーバー型 Panel アプリが使うものと同じ種類の接続です。

1. **ツール > 接続**を開き、**新規接続**をクリックして **PlaidCloud Git** を選択します。
2. 接続に**アカウント名**を付けます（例: `Apps Repo`）。
3. **Repository Path** に、手順2で控えたパスである `<org>/apps` を設定し、**デフォルトブランチ**を `main` にします。アプリがサブディレクトリにある場合を除き、**開始パス**は空欄のままにします。
4. **作成**をクリックします。

サーバー URL、ユーザー、パスワード、SSL/SSH のフィールドはありません。PlaidCloud Git はマネージドサービスのため、ホストと認証はプラットフォームが処理します。接続の**使用方法**と**セキュリティモデル**（ワークスペース内で誰が利用できるか）を含むフォームの詳細については、[PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/)をご覧ください。

## 4. Dashアプリを公開する

次に、Dash デプロイメントをその接続に向けます。

1. **マイPanelアプリ**を開き、**新しいDashアプリ**をクリックします。
2. **ディレクトリ設定**で、**アプリ名**と**URLスラッグ**を設定します。スラッグはアプリの URL と内部名になるため、小文字、数字、ハイフンを使い、先頭は英字、40文字以内にしてください（例: `hello-dash`）。任意で**メモ**にアプリの説明を入力できます。
3. **Git接続と公開ウォッチャー**で、次を設定します。
   - **Git接続**: 手順3で作成した PlaidCloud Git 接続。
   - **ブランチ**: `main`。このブランチへのプッシュで、アプリが自動的に再ビルドされ再デプロイされます。
   - **エントリポイント**: `app.py`。
4. **ランタイム**で、**CPU**、**メモリ**、**アイドル (分)** の時間枠を選択します。サインインなしでアプリにアクセスできるようにする場合のみ、**パブリックアクセスを許可**にチェックを入れます。**デザイン**の設定はありません。これは Panel 固有のオプションです。
5. **詳細 (埋め込み配信)** は任意です。アプリを別のサイトに埋め込む場合を除き、空のままにします。
6. **公開**をクリックします。

## 5. アプリを開く（起動しない場合はログを確認する）

公開すると、アプリの**ビルド**が始まります。PlaidCloud はブランチをクローンし、`requirements.txt` をインストールして、`platform-dash-base` イメージからコンテナーイメージをビルドします。**ステータス**は**マイPanelアプリ**の一覧に表示され、自動的に更新されます。

- ステータスが**準備完了**になったら、`https://<your-tenant-host>/serve/<slug>/` でアプリを開きます。アイドル状態の後の最初のリクエストでアプリが起動し、その間は PlaidCloud の短い読み込み画面が表示されます。
- ビルドが失敗した場合は、アプリを開いて**ビルド**ログを確認します。依存関係の不足やインポートエラーはここに表示されます。各ステータスの意味、ログの読み方、再ビルドの実行方法については、[Dashアプリの使用](/ja/guides/dash-apps/using/)をご覧ください。

以降は、**接続のブランチにプッシュするたびにアプリが自動的に再ビルドされ再デプロイされます**。`app.py` を編集して `git push` すれば、変更が反映されます。（アプリが**ロック**されている場合は、ロックを解除するまでプッシュはスキップされます。詳しくは[Dashアプリの使用](/ja/guides/dash-apps/using/#アプリのロック)をご覧ください。）

## 次のステップ

- [Dashアプリでのデータとサインイン中ユーザーの読み取り](/ja/guides/dash-apps/accessing-data/): アプリを閲覧しているユーザーとして PlaidCloud のデータにクエリを実行します。
- [Dashアプリの使用](/ja/guides/dash-apps/using/): ビルドステータス、ログ、ロック、アプリの削除。
- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/): 接続フォームの詳細、使用方法、セキュリティモデル。
- [リポジトリ](/ja/guides/git/repositories/): PlaidCloud Git でのブランチ、トークン、共同作業。
