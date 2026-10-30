---
title: Oracle Fusionコネクタ
description: PlaidCloudでOAuth2資格情報を使ってOracle Fusion Cloud接続を設定し、ODataとBIP経由でGL残高と仕訳バッチをインポートし、FBDI経由で仕訳を転記します。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## APIのドキュメント

このコネクタが使用するエンドポイントとバルク抽出/ロードの経路については、Oracle Fusion Cloudの[REST API（OData）](https://docs.oracle.com/en/cloud/saas/financials/)と、[BI Publisher（BIP）およびFile-Based Data Import（FBDI）](https://docs.oracle.com/en/cloud/saas/applications-common/)のリファレンスに記載されています。

## 認証の仕組み

接続は、専用のAPIユーザーに対して、OAuth2クライアント資格情報（またはFusion Cloudのセキュリティ設定が連携ユーザー向けに発行するベーシック認証のAPI資格情報）で認証します。APIユーザーのロールによって、読み取れる総勘定元帳のエンティティと、転記できるFBDI/GLインターフェースの機能の両方が決まります。

## 構成

| フィールド | タイプ | 説明 |
|---|---|---|
| 名前 | テキスト | この接続の表示名。 |
| インスタンスURL | テキスト | Fusion CloudのインスタンスURL（例：`https://yourorg.fa.us2.oraclecloud.com`）。 |
| クライアントID | テキスト | APIユーザーのOAuth2クライアントID（ベーシック認証の場合はユーザー名）。 |
| クライアントシークレット | テキスト | APIユーザーのOAuth2クライアントシークレット（ベーシック認証の場合はパスワード）。暗号化して保存されます。 |

## インポートできるエンティティ

2つのインポートステップは取得するデータ量に応じて使い分けます。どちらも`gl_balances`と`journal_batches`に対して使用します。

- **Import Fusion Entity** — ODataとBIPを直接呼び出します。定期的な、範囲が限られた取得に使用します。
- **Import Fusion Bulk Extract** — 非同期のFBDI/BIPエクスポートジョブです。大量のデータの抽出に使用します。

どちらも、日付、会計期間、数値の残高/金額フィールドに対する範囲フィルター（`ge`/`le`）と、元帳や通貨などの離散フィールドに対する等価フィルターに対応しています。フィールドの詳細については、[Import Fusion Entity](/ja/reference/workflow-steps/oracle-fusion/import-fusion-entity/)と[Import Fusion Bulk Extract](/ja/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)を参照してください。

## 仕訳エントリの転記

**Oracle Fusion: Post Journal Entry**ステップは、PlaidCloudの共有ERP書き込みパイプラインを通じて、総勘定元帳の仕訳バッチを転記します。バッチをFBDIファイルとしてOracleのGL_INTERFACEステージングテーブルに書き込み、Journal Import Launcher ESSジョブを送信して完了状態になるまでポーリングし、バッチを転記済みと報告する前に確認します。訂正は、元のエントリを編集するのではなく、借方と貸方を入れ替えた新しい取消エントリを転記します。フィールドの詳細については[Oracle Fusion: Post Journal Entry](/ja/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)を、転記の手順全体については[Oracle Fusionに接続する](/ja/guides/connections/oracle-fusion/)を参照してください。

## 既知の制限事項

| 制限事項 | 意味 |
|---|---|
| ESSジョブの遅延 | Journal Import Launcherは同期呼び出しではなくスケジュールされたジョブとして実行されるため、転記の実行にはAPIへの直接書き込みよりもかなり長い時間がかかります。 |
| バルク抽出の遅延 | `import_fusion_bulk_extract`はFBDI/BIPエクスポートジョブの完了を待ちます。`import_fusion_entity`の直接の経路では扱えない大量の取得にのみ使用してください。 |
## 関連項目

- [Oracle Fusionに接続する（ガイド）](/ja/guides/connections/oracle-fusion/) — 接続の作成、テスト、エンティティのインポート、仕訳の転記までの手順。
- [Import Fusion Entity](/ja/reference/workflow-steps/oracle-fusion/import-fusion-entity/)
- [Import Fusion Bulk Extract](/ja/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)
- [Oracle Fusion: Post Journal Entry](/ja/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)
- [ERP転記履歴の確認](/ja/guides/connections/erp-post-history/)
