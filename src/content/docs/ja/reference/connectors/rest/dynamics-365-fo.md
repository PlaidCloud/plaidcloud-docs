---
title: Dynamics 365 Finance & Operations RESTコネクター
description: PlaidCloudでDynamics 365 Finance & Operations接続を設定し、OData/DMFエンティティをインポートして、仕訳を非同期で転記します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## APIドキュメント

D365 F&Oの[OData v4エンドポイント](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata)と[Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export)に、このコネクターが使用するエンドポイントと一括抽出パスが記載されています。

## 認証の仕組み

この接続は、Entra ID（Azure AD）の**クライアント資格情報**を使用してアプリケーションとして認証します。アプリ登録のクライアントIDとシークレットを、環境のリソースにスコープされたアクセストークンに交換します。対話型のサインインはありません。

## 設定

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| 環境URL | テキスト | D365 F&Oの環境URL（例：`https://yourorg.operations.dynamics.com`）。 |
| クライアントID | テキスト | Entraアプリ登録のアプリケーション（クライアント）ID。 |
| クライアントシークレット | テキスト | アプリ登録のクライアントシークレット。暗号化して保存されます。 |
| テナントID | テキスト | Azure ADのテナントID。 |
| リソース/スコープ | テキスト | 要求するOAuth2スコープ。通常は環境URLに`/.default`を付けたものです。 |

## インポートできるエンティティ

**Import D365 F&O Entity**ステップは、`main_accounts`、`currencies`、`customers`、`vendors`、`released_products`、`ledger_journal_headers`の6つのエンティティに対応しています。各取得は、`odata`同期モード（通常の取得向けの直接呼び出し）または`dmf`一括モード（大規模な抽出向けの、非同期のData Management Frameworkエクスポートジョブ）のいずれかで実行され、日付、勘定科目、ディメンションの範囲を含む、エンティティごとのサーバー側フィルターを使用できます。フィールドの詳細は[Import D365 F&O Entity](/ja/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)ステップを参照してください。

## 仕訳の転記

**D365 F&O: Post Journal Entry**ステップは、PlaidCloudの共通ERP書き込みパイプラインを通じて総勘定元帳の仕訳を転記します。D365 F&Oの非同期カスタムサービスの仕訳転記アクションに送信し、最終状態になるまでポーリングし、確認してから仕訳を転記済みとして報告します。訂正では、元の仕訳を編集するのではなく、借方と貸方を入れ替えた新しい取消仕訳を転記します。フィールドのリファレンスは[D365 F&O: Post Journal Entry](/ja/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)ステップを、転記の手順全体は[Dynamics 365 Finance & Operationsへの接続](/ja/guides/connections/dynamics-365-fo/)を参照してください。

## 既知の制限事項

| 制限事項 | 意味 |
|---|---|
| DMF同期モードには抽出の待ち時間がある | `dmf`による取得は非同期のエクスポートジョブを待つため、同じサイズの`odata`による取得よりもかなり遅くなります。 |
| ディメンションのフィルタリングは構造に依存する | 勘定科目構造に含まれない財務ディメンションは、サーバー側でフィルターできません。取得後にワークフロー内で絞り込んでください。 |
## 関連項目

- [Dynamics 365 Finance & Operationsへの接続（ガイド）](/ja/guides/connections/dynamics-365-fo/) — 接続の作成、テスト、エンティティのインポート、仕訳の転記までの手順。
- [Import D365 F&O Entity](/ja/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/ja/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
