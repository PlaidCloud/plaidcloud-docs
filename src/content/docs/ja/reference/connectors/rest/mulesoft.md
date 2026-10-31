---
title: MuleSoft RESTコネクター
description: PlaidCloudをMuleSoft Anypointゲートウェイに接続し、API定義を添付して、ワークフローステップでそのエンドポイントを一覧表示できるようにします。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypointは、APIゲートウェイです。組織がその背後で公開しているサービスを、デプロイメントごとに固有のアドレスで前面から提供します。そのため、1つのサービス向けに作られたコネクターとは異なり、MuleSoft接続は自身のエンドポイントを把握していません。APIとその定義がどこにあるかを、ユーザーが指定します。

## APIドキュメント

この接続のAPIドキュメントは、ゲートウェイが前面で提供しているサービスを説明するドキュメントそのものです。

## 設定

MuleSoftは、[汎用REST接続](/ja/reference/connectors/rest/generic-rest/)と同じフォームを使用します。4つのタブ、フィールド、動作のすべてが同じです。ここで特に重要なのは次の2つです。

- **ホストまたはIPアドレス** — AnypointゲートウェイのアドレスMuleSoftのアドレスはデプロイメントごとに固有のため、デフォルトはありません。
- **認証タイプ** — ゲートウェイが想定する`None`、`Basic`、`API Key`、`Bearer Token`、`OAuth 2.0`のいずれか。こちらで勝手に想定されるものはありません。

## ワークフローでのエンドポイントの一覧表示

ゲートウェイには組み込みのエンドポイント一覧がないため、**API定義**でAPIのOpenAPI 3.xまたはSwagger 2.0の定義を接続に添付します。定義が公開されているアドレス、またはDocumentに保存した`.json`か`.yaml`ファイルのいずれかを指定できます。フィールドについては[API定義](/ja/reference/connectors/rest/generic-rest/#api定義)を参照してください。

この接続を使用する[RESTリクエストステップ](/ja/guides/workflows/rest-request-step/)では、**エンドポイントソース**を**接続のAPI定義から**に設定し、**カタログをロード**を選択すると、各パスを手入力する代わりに、APIのエンドポイントから選択できます。

## 関連項目

- [汎用REST接続](/ja/reference/connectors/rest/generic-rest/) — このフォームのフィールドリファレンス全体。
- [接続の作成と管理](/ja/guides/connections/create-connection/)
- [RESTリクエストワークフローステップ](/ja/guides/workflows/rest-request-step/)
