---
title: Apache Doris
description: PlaidCloudでApache Dorisデータベース接続を設定し、大規模なデータセットに対してリアルタイムの分析クエリを実行します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/doris.md
---

**Apache Doris**は、StarRocksの派生元となった高性能なMPP分析データベースです。このコネクターを使用すると、PlaidCloudのワークフローからDorisのデプロイメントにクエリを実行できます。接続にはMySQLワイヤープロトコルと、標準的なユーザー名とパスワードによる認証を使用します。

## 上流のドキュメント
[Apache Dorisのドキュメント](https://doris.apache.org/docs/4.x/gettingStarted/what-is-apache-doris)。

[Apache Dorisプロジェクトのホームページ](https://doris.apache.org/)。

## セットアップ

このコネクターはベンダー固有の認証フローを使用し、ワークスペースの**接続**画面から直接設定します。表示される設定項目は、テナント管理者が連携用に用意した認証情報によって異なります。

最新のセットアップの詳細については、上流の[dorisのドキュメント](https://doris.apache.org/docs/)を参照してください。

テナントでのこのコネクターの設定についてサポートが必要な場合は、アカウントチームにお問い合わせください。コネクター固有の認証情報、環境URL、必要な事前プロビジョニングは、通常、PlaidCloudサポートとの調整が必要です。
