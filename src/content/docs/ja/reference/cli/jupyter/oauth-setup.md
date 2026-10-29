---
title: OAuthトークン
description: PlaidCloud APIアクセス用のOAuthトークンを設定し、Jupyterノートブック、CLIツール、カスタムアプリケーションの接続を認証します。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloudは標準的なJSON-RPCリクエストを使用しており、そのリクエストを実行できるあらゆるアプリケーションから利用できます。リクエストはOAuthトークンによって保護されます。


## OAuthトークンの取得

OAuthトークンは、PlaidCloud アプリで生成します。自分に割り当てられている現在のOAuthトークンの一覧を表示したり、新しいトークンを生成したりするには、`Analyze > Tools > Registered Systems` に移動します。

移動したら、既存のトークンを確認することも、新しいトークンを作成することもできます。

## OAuth PlaidCloud設定ファイルのダウンロード
「Register a New System」を選択します。

フォームに入力し、一覧で見つけられるように、入力した名前を控えておきます。

作成したら、歯車アイコンをクリックして、登録済みシステムのレコードを開きます。設定ファイルのテキストが表示されます。

注：上部のドロップダウンから、この接続で使用するプロジェクトを必ず選択してください。選択したプロジェクトの一意の識別子が設定に追加されます。

このテキストを、お使いのシステム上の plaid.conf ファイルにコピーします。このファイルは .plaid ディレクトリに配置します。

## 設定ファイルをローカルに作成する
ノートブックのディレクトリ、またはコマンドラインで操作する予定の場所より1つ上の階層にディレクトリを作成します。ディレクトリの名前は `.plaid` にします。

`.plaid` ディレクトリの中に `plaid.conf` というファイルを作成し、上でコピーした内容を貼り付けます。ファイルを保存すると、PlaidCloudユーティリティとrpcメソッドを使って接続できるようになります。


## 高度な使い方

`.plaid` フォルダーは、使用する場所の近くに置くと便利ですが、実際には上位のディレクトリツリーのどこにでも配置できます。初期化処理は、`.plaid` ディレクトリが見つかるまでディレクトリツリーをさかのぼります。

複数の処理がアクセスを必要とし、下位階層の同じディレクトリ構造に共存させられない場合は、`.plaid` ディレクトリをより上位に配置すると便利なことがあります。


## パスの指定（オプション）
ローカルのJupyterノートブックをインストールして使用している場合、またはコマンドラインから操作している場合は、ヘルパーツールを使って、データ、Excelファイル、その他のデータをエクスポートしたり、ローカルのデータをデータフレームに読み込んだりできます。そのためには、paths.yaml ファイルが必要です。

`plaid.conf` ファイルに加えて、`paths.yaml` ファイルを作成します。`paths.yaml` は、`.plaid` ディレクトリ内の `plaid.conf` ファイルと同じ階層に置きます。次のパス情報を記述します。

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
