---
title: PlaidCloud GitからPanelアプリをデプロイする
description: HoloViz PanelアプリをPlaidCloudで配信するまでの一連の手順です。コードをPlaidCloud Gitリポジトリに置き、認証情報不要のマネージド接続で接続して、公開します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

このページでは、お使いのマシン上のPanelアプリのコードからライブURLまでの全手順を、ワークスペースに組み込まれたマネージドGitサービスである **[PlaidCloud Git](/ja/guides/git/)** をソースとして説明します。PlaidCloud Gitはマネージドサービスのため、アプリのデプロイ元となる接続には **サーバーURL、ユーザー名、トークンは不要** です。PlaidCloudがお客様に代わって認証します。

手順は次の5つです。

1. 最小限のPanelアプリを作成する。
2. PlaidCloud Gitリポジトリに置く。
3. マネージドのPlaidCloud Git接続を作成する。
4. リポジトリを指すサーバーアプリを公開する。
5. 配信されたアプリを開く。起動しない場合はビルドログを確認する。

各手順は、それぞれの詳細ガイドにリンクしています。このページは、それらを1つの流れにまとめたものです。

## 始める前に

- ワークスペースから **Git** を開き、PlaidCloud Gitにアクセスできることを確認します。デフォルトでは、ワークスペースの組織に **`apps`** リポジトリ（および **`udfs`** リポジトリ）が含まれています。apps はPanelアプリに最適な置き場所です。
- お使いのマシンからコードをプッシュする場合は、`git` をローカルにインストールしておきます（GitのWeb UIでファイルを追加することもできます）。

## 1. 最小限のPanelアプリを作成する

アプリには **エントリポイント** が必要です。これはPanelアプリを構築して `.servable()` を付けるPythonファイルです。必要に応じて、追加パッケージ用の **`requirements.txt`** をリポジトリのルート、またはエントリポイントと同じ場所に置きます。

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

これで完全なアプリです。PlaidCloudが配信するのは `.servable()` を呼び出したものです。`panel`、`bokeh`、およびPlaidCloudクライアントライブラリ（`plaidcloud-rpc`、`plaidcloud-utilities`）はプリインストールされているため、`requirements.txt` には *追加の* パッケージだけを記載します。より充実した例、依存関係、ライト／ダークテーマについては、[Panelアプリを作成する](/ja/guides/panel-apps/creating/) を参照してください。

## 2. アプリをPlaidCloud Gitリポジトリに置く

ワークスペースにある既存の **`apps`** リポジトリを使うか、[新しいリポジトリを作成](/ja/guides/git/repositories/#リポジトリを作成する) します。そのうえで、コードをリポジトリに入れます。

PlaidCloud経由でサインインするため、Gitアカウントには別のパスワードがありません。**write:repository** 権限を持つ [個人用アクセストークンを生成](/ja/guides/git/repositories/#個人用アクセストークンを生成する) し（**アバター → 設定 → アプリケーション**）、Gitがパスワードを求めたらそれを入力します。`apps` へのプッシュには **コントリビューター** のアクセス権が必要です。**Git** タブで **閲覧者** と表示されている場合は、ワークスペース管理者に **Git Contributors** への追加を依頼してください。**Git** タブでリポジトリのクローンアドレスの横にあるコピーボタンを使い、次を実行します。

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

リポジトリのパス `<org>/apps` を控えておいてください。`<org>` はワークスペースの組織名です。このパスは次の手順で入力します。クローン、コミット、プッシュの詳細は [リポジトリ](/ja/guides/git/repositories/) を参照してください。

> **ここでのトークンは、お客様がコードをプッシュするためだけのものです。** 次に作成する接続はマネージドでトークンは不要です。両者を混同しないでください。

## 3. マネージドのPlaidCloud Git接続を作成する

**接続** は、Panelデプロイメントがコードの置き場所を知るためのものです。PlaidCloud Gitの接続は *マネージド* で、ホストと認証情報はPlaidCloudが用意するため、入力するのはリポジトリの指定だけです。

1. **ツール > 接続** を開き、**新規接続** をクリックして **PlaidCloud Git** を選択します。
2. 接続に **アカウント名** を付けます（例: `Apps Repo`）。
3. **Repository Path** に手順2で控えたパス `<org>/apps` を、**デフォルトブランチ** に `main` を設定します。アプリがサブディレクトリにある場合を除き、**開始パス** は空欄のままにします。
4. **作成** をクリックします。

サーバーURL、ユーザー、パスワード、SSL/SSHのフィールドはありません。PlaidCloud Gitはマネージドのため、ホストと認証はプラットフォームが処理します。接続の **使用方法** と **セキュリティモデル**（ワークスペース内で誰が使用できるか）を含むフォームの詳細は、[PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) を参照してください。

> **古いワークスペースビルドをお使いですか？** フォームにサーバーURLや認証情報のフィールドが表示されていても、空欄のままにしてください。どちらの場合も、プラットフォームがお客様に代わって認証します。

## 4. サーバーアプリを公開する

次に、その接続をサーバーデプロイメントに指定します。

1. **マイPanelアプリ** を開き、**新しいサーバーアプリ** をクリックします。
2. **ディレクトリ設定** で **アプリ名** と **URLスラッグ** を設定します。スラッグはアプリのURLと内部名になるため、小文字の英字、数字、ハイフンを使い、英字で始め、40文字以内にしてください（例: `hello-panel`）。
3. **Git接続と公開ウォッチャー** で次を設定します。
   - **Git接続** — 手順3で作成したPlaidCloud Git接続。
   - **ブランチ** — `main`。このブランチへのプッシュのたびに、アプリが自動的に再ビルドされ再デプロイされます。
   - **エントリポイント** — `app.py`。
4. **ランタイム** で、**CPU**、**メモリ**、**デザイン**（PlaidCloudのモダンな外観には **FAST**）、**アイドル** の時間を選択します。サインインなしでアプリにアクセスできるようにする場合のみ、**パブリックアクセスを許可** をオンにします。
5. **公開** をクリックします。

このダイアログの各フィールドについては、[Panelアプリを作成する](/ja/guides/panel-apps/creating/#アプリを公開する) で説明しています。

## 5. アプリを開く。起動しない場合はログを確認する

公開すると、アプリの **ビルド** が始まります。PlaidCloudがブランチをクローンし、`requirements.txt`（リポジトリのルートとアプリのフォルダーにあればその両方）をインストールして、コンテナーイメージを作成します。その **ステータス** は **マイPanelアプリ** の一覧に表示され、自動的に更新されます。

- ステータスが **準備完了** になったら、`https://<your-tenant-host>/serve/<slug>/` でアプリを開きます。アイドル状態の後の最初のリクエストでアプリが起動します（約15秒）。
- ビルドが失敗した場合は、アプリを開いて **ビルド** ログを確認します。依存関係の不足やインポートエラーはそこに表示されます。各ステータスの意味、ログの読み方、再ビルドの方法は [Panelアプリを使う](/ja/guides/panel-apps/using/) を参照してください。

以降は、**接続のブランチにプッシュするたびに、アプリが自動的に再ビルドされ再デプロイされます**。`app.py` を編集して `git push` すれば、変更が反映されます。（アプリが **ロック** されている場合は、ロックを解除するまでプッシュはスキップされます。[アプリのロック](/ja/guides/panel-apps/using/#アプリをロックする) を参照してください。）

## 次のステップ

- [Panelアプリを作成する](/ja/guides/panel-apps/creating/) — より充実した例、依存関係、ライト／ダークテーマ
- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) — 接続フォームの詳細、使用方法、セキュリティモデル
- [データとサインイン中のユーザーの読み取り](/ja/guides/panel-apps/accessing-data/) — アプリを表示しているユーザーとしてPlaidCloudのデータをクエリします
- [リポジトリ](/ja/guides/git/repositories/) — PlaidCloud Gitでのブランチ、トークン、共同作業
