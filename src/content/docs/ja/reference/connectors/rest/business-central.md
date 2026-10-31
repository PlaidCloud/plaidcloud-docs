---
title: Business Central RESTコネクター
description: Azure ADクライアント資格情報を使用してMicrosoft Dynamics 365 Business Central接続をPlaidCloudで設定し、ODataエンティティをインポートして総勘定元帳の仕訳明細行を転記します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## APIドキュメント

Business Centralの[標準OData v2.0 API](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/)に、このコネクターが使用するエンティティと`$filter`/`$orderby`オプションが記載されています。

## 認証の仕組み

この接続は、Entra ID（Azure AD）の**クライアント資格情報（S2S）** を使用してアプリケーションとして認証します。アプリ登録のクライアントIDとシークレットを、`https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`でアクセストークンに交換し、スコープは`https://api.businesscentral.dynamics.com/.default`です。対話型のサインインはありません。アプリ登録には、Business Centralへ付与されたAPIアクセス許可（`API.ReadWrite.All`、または管理者が発行するより限定的なスコープ）が必要です。

すべてのリクエストは、1つの**環境**（たとえば`Production`やサンドボックス環境）と、その中の1つの**会社**にスコープが限定されます。どちらもリクエストごとに選択するのではなく、接続に設定します。

## 設定

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| クライアントID | テキスト | Entraアプリ登録のアプリケーション（クライアント）ID。 |
| クライアントシークレット | テキスト | アプリ登録のクライアントシークレット。暗号化して保存されます。 |
| テナントID | テキスト | Azure ADのテナントID。 |
| 環境 | テキスト | Business Centralの環境名（例：`Production`）。 |
| 会社 | テキスト | この接続が読み取りと転記の対象とするBusiness Centralの会社ID。 |

## インポートできるエンティティ

**Import Business Central Entity**ステップは、`accounts`、`generalLedgerEntries`、`customers`、`vendors`、`items`、`journals`の6つのエンティティに対応しています。各取得では、エンティティごとのサーバー側フィルターを使用できます。フィールドの詳細は[Import Business Central Entity](/ja/reference/workflow-steps/business-central/import-business-central-entity/)ステップを参照してください。

`generalLedgerEntries`は読み取り専用で、転記済みのもののみを対象とします。未転記の仕訳バッチに残っている明細行は含まれないため、試算表や総勘定元帳の明細を取得する際に使用するエンティティです。

## 総勘定元帳の仕訳明細行の転記

**Business Central Post**ステップは、**既存**の仕訳バッチ内に明細行を作成し、PlaidCloudの共通ERP書き込みパイプラインを通じてそのバッチを転記します。転記前にバッチにこのリクエストの明細行のみが含まれていることを検証し、転記は（仕訳バッチ自体ではなく）`generalLedgerEntries`に対して確認します。フィールドのリファレンスは[Business Central: Post General Journal Lines](/ja/reference/workflow-steps/business-central/business-central-post/)ステップを、転記の手順全体は[Business Centralへの接続](/ja/guides/connections/business-central/)を参照してください。

## 既知の制限事項

| 制限事項 | 意味 |
|---|---|
| 書き込みのドキュメントタイプは1つのみ | 総勘定元帳の仕訳明細行の転記のみに対応しています。下書きドキュメントのフロー（販売/購買請求書、下書き → 転記済み）には対応していません。このフローの転記アクションは、Microsoftの公開ドキュメントでは特定されていないためです。 |
| 既存のバッチへの転記のみ | このコネクターは、Business Centralで仕訳バッチを作成することはありません。先にBusiness Central側で作成してください。 |
| 同一バッチへの同時転記 | 冪等性のガードはドキュメント番号単位であり、仕訳バッチ単位ではありません。異なる2つのドキュメント番号が同じバッチへ同時に転記される場合、直列化は保証されません。 |
## 関連項目

- [Business Centralへの接続（ガイド）](/ja/guides/connections/business-central/) — 接続の作成、テスト、エンティティのインポート、仕訳の転記までの手順。
- [Import Business Central Entity](/ja/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/ja/reference/workflow-steps/business-central/business-central-post/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
