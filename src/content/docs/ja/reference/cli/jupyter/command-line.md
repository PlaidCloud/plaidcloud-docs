---
title: コマンドライン
description: PlaidCloudのコマンドラインインターフェイスを使って、タスクの自動化、スクリプトの実行、ターミナルからのPlaidCloudリソースの操作を行います。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud には、HTTP リクエストを送信できるあらゆるアプリケーションから利用できる REST API があります。さらに使いやすくするため、Python パッケージ `plaidcloud-rpc` が接続とリクエストの詳細を処理します。

:::caution[JSON-RPC は非推奨]
JSON-RPC は非推奨であり、今後のリリースで削除されます。呼び出しを REST API に送信する `plaidcloud-rpc` 1.25.0 以降を使用し、新しい連携は REST API を使って作成してください。[JSON-RPC は非推奨](#json-rpc-は非推奨)を参照してください。
:::


## 必要なインストール

ターミナルで次のコマンドを実行します。

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## SimpleRPC オブジェクトを使ったリクエスト

`plaidcloud-rpc` パッケージを使ってリクエストを送信するには、`SimpleRPC` オブジェクトを使用します。

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

`SimpleRPC` オブジェクトをインスタンス化したら、PlaidCloud にリクエストを送信できます。この例では、テーブルのメタデータを要求します。

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` は、各呼び出しを同じトークンで、ワークスペースのホストの `/rest/v1/` にある REST API に送信します。REST API がまだ対応していない呼び出しや、まだ以前のリリースで稼働しているワークスペースへの呼び出しでは、代わりに JSON-RPC が使用されるため、どちらの場合も同じコードが動作します。呼び出しが失敗すると、どちらの場合も `RPCError` が発生します。


## REST API を直接呼び出す

`call_rest` は、`SimpleRPC` と同じトークン、TLS 設定、再試行で、REST API の任意のエンドポイントにリクエストを送信します。HTTP メソッド、`/rest/v1/` 以下のパスに加え、必要に応じてクエリ文字列用の `params` と JSON リクエスト本文用の `body` を指定します。

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

デコードされた JSON レスポンスを返します。レスポンスに本文がない場合は `None` を返します。成功以外のレスポンスでは、HTTP ステータスを `code` とする `RPCError` が発生します。


## JSON-RPC は非推奨

JSON-RPC は非推奨であり、今後のリリースで削除されます。1.25.0 より前のバージョンの `plaidcloud-rpc` はすべての呼び出しを JSON-RPC で送信するため、JSON-RPC が削除されると動作しなくなります。1.25.0 以降にアップグレードしてください。`SimpleRPC` のコードを変更する必要はありません。新しい連携は REST API を使って作成してください。


## 利用できるAPIは何ですか

PlaidCloudのほぼすべての側面を制御する多数のAPIを利用できます。インタラクティブなAPIリファレンスは、各PlaidCloudワークスペース内でテナントごとに提供されています。ワークスペースを開き、APIドキュメントのメニューに移動すると、利用可能なエンドポイントの一覧を確認できます。


## OAuthトークンの取得

OAuthトークンの取得方法と、自動認証のためのシステム設定については、[OAuthの設定](/ja/reference/cli/jupyter/oauth-setup/)をご覧ください。
