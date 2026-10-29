---
title: Oracle Essbaseコネクタ
description: PlaidCloudをOracle Essbase 21cまたはOracle Analytics Cloudにサービスアカウントで接続し、ワークフローからEssbaseキューブに対してライブMDXクエリを実行します。
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## APIのドキュメント

このコネクタは、[Oracle EssbaseのREST API](https://docs.oracle.com/en/database/other-databases/essbase/)と通信します。これは、Essbase 21cとOracle Analytics Cloud（OAC）についてOracleが文書化している`grid/mdx`、アプリケーション、データベース、アウトラインの各エンドポイントです。

## 接続先

Oracle Essbase **21c以降**、およびOracle Analytics Cloud（OAC）のEssbaseです。これらのバージョンは、文書化されたREST APIでEssbaseを公開しており、PlaidCloudはこのAPIを呼び出します。REST導入前のオンプレミス版Essbaseは**サポートされません**。従来のJava APIやグリッドクライアントを経由する方法はありません。

接続を作成すると、[Essbase: キューブのクエリ](/ja/reference/workflow-steps/essbase/essbase-query/)ステップがキューブに対してライブMDXを実行して結果グリッドをテーブルに格納し、[Essbase: ディメンションの読み取り](/ja/reference/workflow-steps/essbase/essbase-dimension-read/)ステップがディメンションのアウトラインをPlaidCloudのディメンションに読み込みます。

## 認証の仕組み

接続は、HTTP基本認証で、サービスアカウントのユーザー名とパスワードを使って認証します。そのアカウントのEssbaseでのプロビジョニングによって、参照およびクエリできるアプリケーションとキューブが決まります。そのため、クエリを実行する予定のアプリケーションにのみ、読み取りアクセスを付与してください。

## 構成

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| ベースURL | テキスト | Essbaseサーバーのオリジン（例：`https://your-host:9001`）。末尾の`/essbase/...`パスを含めず、オリジンのみを入力します。 |
| デフォルトアプリケーション | テキスト *（任意）* | Essbase: キューブのクエリステップのフォームで、このアプリケーションをあらかじめ選択します。 |
| ユーザー名 | テキスト | HTTP基本認証用のサービスアカウントのユーザー。 |
| パスワード | テキスト | サービスアカウントのパスワード。暗号化して保存されます。 |
| SSLを検証 | トグル | デフォルトでオンです。自己署名証明書など、検証できない証明書を使用しているホストの場合にのみオフにします。 |

## 接続のテスト

接続エディターで**接続をテスト**を使用します。テストが成功すると、Essbaseサーバーに到達し、サービスアカウントが参照できるアプリケーションを一覧表示して、見つかった数を報告します。これにより、クエリを作成する前に、ベースURLと資格情報の両方を確認できます。

## 関連項目

- [Essbase: キューブのクエリ](/ja/reference/workflow-steps/essbase/essbase-query/) — キューブに対してライブMDXクエリを実行し、結果をテーブルに格納します。
- [Essbase: ディメンションの読み取り](/ja/reference/workflow-steps/essbase/essbase-dimension-read/) — ディメンションのアウトラインをPlaidCloudのディメンションに読み込みます。
- [Oracle Essbaseステップ](/ja/reference/workflow-steps/essbase/)
- [Oracle Essbaseに接続する（ガイド）](/ja/guides/connections/essbase/)
- [接続の作成と管理](/ja/guides/connections/create-connection/)
