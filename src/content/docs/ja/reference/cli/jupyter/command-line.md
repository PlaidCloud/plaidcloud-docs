---
title: コマンドライン
description: PlaidCloudのコマンドラインインターフェイスを使って、タスクの自動化、スクリプトの実行、ターミナルからのPlaidCloudリソースの操作を行います。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloudは標準的なJSON-RPCリクエストを使用しており、そのリクエストを実行できるあらゆるアプリケーションから利用できます。


接続とAPIの実行を簡単にするために、Pythonパッケージが用意されています。


## 必要なインストール

ターミナルで次のコマンドを実行します。

```bash
pip install plaidcloud-rpc
```


## SimpleRPCオブジェクトを使ってリクエストを送信する

`plaidcloud-rpc` パッケージを使ってリクエストを送信するには、`SimpleRPC` オブジェクトを使用します。

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

`SimpleRPC` オブジェクトを作成したら、PlaidCloudにRPCリクエストを送信できます。次の例では、テーブルのメタデータをリクエストします。

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## 利用できるAPIは何ですか

PlaidCloudのほぼすべての側面を制御する多数のAPIを利用できます。インタラクティブなAPIリファレンスは、各PlaidCloudワークスペース内でテナントごとに提供されています。ワークスペースを開き、APIドキュメントのメニューに移動すると、利用可能なエンドポイントの一覧を確認できます。


## OAuthトークンの取得

OAuthトークンの取得方法と、自動認証のためのシステム設定については、[OAuthの設定](/ja/reference/cli/jupyter/oauth-setup/)をご覧ください。
