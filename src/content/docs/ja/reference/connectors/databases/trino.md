---
title: Trino
description: PlaidCloudでTrinoの分散クエリエンジン接続を設定し、複数のデータソースにまたがるフェデレーテッドクエリを実行します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino**（旧PrestoSQL）は、データレイクに対してよく使われる分散SQLクエリエンジンです。このコネクタを使うと、PlaidCloudのワークフローからTrinoのデプロイメントをクエリできます。認証にはHTTP基本認証またはJWTを使用します。対象とするカタログとスキーマによって、クエリが参照する基盤のデータソースが決まります。

## 上流のドキュメント
[Trinoのドキュメント](https://trino.io/docs/current/index.html)。

## セットアップ

このコネクタはベンダー固有の認証フローを使用し、ワークスペースの**接続**画面から直接構成します。表示される構成フィールドは、テナント管理者がこの連携のために用意した資格情報によって異なります。

最新のセットアップの詳細については、上流の[Trinoのドキュメント](https://trino.io/docs/current/)を参照してください。

テナントでこのコネクタを設定する際にサポートが必要な場合は、アカウントチームにお問い合わせください。コネクタ固有の資格情報、環境のURL、必要な事前プロビジョニングは、通常、PlaidCloudサポートとの調整が必要です。
