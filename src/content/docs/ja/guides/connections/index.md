---
title: 接続
description: PlaidCloud の接続（ワークフローが外部のデータベース、クラウドストレージ、ERP、REST API にアクセスするための保存済み設定）をセットアップして管理します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**接続**とは、PlaidCloud が外部システム（データベース、クラウドストレージアカウント、ERP、REST API）にアクセスするための保存済みの設定です。そのシステムとの間で読み取りや書き込みを行うワークフローステップは接続を参照するため、認証情報とエンドポイントの詳細は 1 か所で管理できます。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="多数のワークフローステップが 1 つの保存済み接続を参照します。接続は認証情報とエンドポイントを 1 か所で保持し、外部システム（データベース、クラウドストレージ、ERP、REST API）に接続します。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">ワークフローステップ</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">インポートステップ</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">エクスポートステップ</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">ルックアップステップ</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">接続</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">認証情報 + エンドポイント（1 回のみ）</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">外部システム</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · ストレージ · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">接続は 1 回設定するだけで、外部システムを読み書きするすべてのステップがその接続を参照します。そのため、認証情報やエンドポイントの詳細をステップごとに重複して設定する必要はありません。</figcaption>
</figure>

## ガイド

- [接続の作成と管理](/ja/guides/connections/create-connection/) — 接続の作成、編集、テスト、アクセス制御を行い、環境ごとに設定します。
- [独自のウェアハウスを使用する](/ja/guides/connections/external-lakehouse/) — 独自の Snowflake または Databricks ウェアハウスを自分で接続し、自分の ID でサインインして、複数のウェアハウスを管理し、実行ごとのコストを確認します。
- [PlaidCloud Git 接続](/ja/guides/connections/plaidcloud-git/) — サーバー URL や認証情報なしで、ワークスペース専用のマネージド Git サーバーに接続し、そこから Panel アプリのビルドを自動化します。
- [接続のクローン](/ja/guides/connections/clone-connection/) — 既存の接続を複製して、新しい環境やテナント用に使用します。
- [Data Foundation: Common Finance Model](/ja/guides/projects/data-foundation/) — Common Finance Model は、複数の ERP システムとインスタンスの ERP データを、1 つの勘定科目表、1 組のエンティティ、1 つの報告通貨を持つ単一のモデルに集約し、レポート、メトリック、AI アシスタントのすべてがそれを読み取ります。
- システムごとの Data Foundation アクセス（PlaidCloud に読み取りアクセスを付与する管理者向けに、1 システム 1 ページで、返送する情報も説明）: [NetSuite](/ja/guides/connections/netsuite-access-for-data-foundation/)、[SAP S/4HANA](/ja/guides/connections/sap-s4hana-access-for-data-foundation/)、[SAP ECC](/ja/guides/connections/sap-ecc-access-for-data-foundation/)、[SAP S/4HANA Cloud](/ja/guides/connections/s4hana-cloud-access-for-data-foundation/)、[Oracle E-Business Suite](/ja/guides/connections/oracle-ebs-access-for-data-foundation/)、[Oracle Fusion](/ja/guides/connections/oracle-fusion-access-for-data-foundation/)、[Dynamics 365 Finance and Operations](/ja/guides/connections/dynamics-365-fo-access-for-data-foundation/)、[Business Central](/ja/guides/connections/business-central-access-for-data-foundation/)、[Sage Intacct](/ja/guides/connections/sage-intacct-access-for-data-foundation/)、[QuickBooks](/ja/guides/connections/quickbooks-access-for-data-foundation/)、[Xero](/ja/guides/connections/xero-access-for-data-foundation/)、[Workday](/ja/guides/connections/workday-access-for-data-foundation/)、[Salesforce](/ja/guides/connections/salesforce-access-for-data-foundation/)。各システムが提供するデータセットについては、[Data Foundation カバレッジマトリックス](/ja/reference/data-foundation-coverage-matrix/)を参照してください。
- [Singer ソース](/ja/guides/connections/singer-sources/) — Singer タップを使用して Stripe、GitHub、Slack、BigQuery などのソースに接続し、そのデータをプロジェクトのテーブルにインポートします。
- [NetSuite に接続する](/ja/guides/connections/netsuite/) — NetSuite 接続をセットアップし、SuiteQL で財務データと業務データを取得します。
- [NetSuite の財務データをインポートする](/ja/guides/connections/import-netsuite-financials/) — 定型の NetSuite インポートステップで、SuiteQL を書かずに残高、GL 明細、マスターデータを取得します。
- [NetSuite の仕訳を転記する](/ja/guides/connections/post-netsuite-journal-entries/) — ヘッダーテーブルと明細テーブルをマッピングし、プレビューして、仕訳を NetSuite に転記します。
- [Acumatica に接続する](/ja/guides/connections/acumatica/) — Acumatica 接続をセットアップし、エンティティをインポートして、仕訳トランザクション、請求書、買掛金請求書、支払を転記します。
- [Business Central に接続する](/ja/guides/connections/business-central/) — Azure AD を使用して Business Central 接続をセットアップし、OData エンティティをインポートして、総勘定仕訳帳の明細を転記します。
- [Dynamics 365 Finance & Operations に接続する](/ja/guides/connections/dynamics-365-fo/) — Azure AD を使用して D365 F&O 接続をセットアップし、OData/DMF エンティティをインポートして、仕訳を転記します。
- [Oracle Fusion に接続する](/ja/guides/connections/oracle-fusion/) — Oracle Fusion 接続をセットアップし、GL 残高と仕訳バッチをインポートして、FBDI で仕訳を転記します。
- [Workday Financials に接続する](/ja/guides/connections/workday-financials/) — 統合システムユーザーを使用して Workday Financials 接続をセットアップし、RaaS レポートをインポートして、仕訳を転記します。
- [SAP S/4HANA Cloud に接続する](/ja/guides/connections/s4hana-cloud/) — OAuth2 を使用して S/4HANA Cloud への直接接続をセットアップし、試算表と仕訳明細をインポートして、SOAP で仕訳を転記します。
- [SAP ECC / S/4HANA からのアドホック抽出](/ja/guides/connections/sap-adhoc-extract/) — テーブル、トランザクションコード、保存済みの SAP クエリで SAP を検索し、抽出をプレビューして計画し、PlaidLink エージェント経由でテーブルに取り込みます。
- [Sage Intacct に接続する](/ja/guides/connections/sage-intacct/) — Sage Intacct 接続をセットアップし、財務データと会計データを取得します。
- [Xero に接続する](/ja/guides/connections/xero/) — Xero の組織をワンクリックで承認し、Accounting API のエンティティをインポートして、手動仕訳、請求書、買掛金請求書、支払、クレジットノートを転記します。
- [Salesforce に接続する](/ja/guides/connections/salesforce/) — Salesforce の External Client App と実行ユーザーをセットアップし、CRM オブジェクトをプロジェクトのテーブルに抽出します。
- [HFM / FCCS からの抽出（アドホック）](/ja/guides/connections/hfm-fccs/) — Oracle FCCS に接続し、HFM チームへの依頼なしに、ポイントオブビューのピッカーでデータスライスをセルフサービスで取得します。
- [TM1 に接続する](/ja/guides/connections/tm1/) — IBM TM1 / Planning Analytics サーバーに接続し、ビューまたは MDX でキューブデータを期間ごとにスライスして読み取ります。
- [Anaplan に接続する](/ja/guides/connections/anaplan/) — Anaplan に接続し、保存済みビューの読み取り、既存のエクスポートアクションの実行、リストの PlaidCloud ディメンションへの読み込みを行います。読み取り専用です。
- [Data Foundation 向け OneStream](/ja/guides/connections/onestream-for-data-foundation/) — Data Foundation がデータアダプター経由で連結結果を読み取れるように、OneStream 管理者が設定する内容。
- [QuickBooks に接続する](/ja/guides/connections/quickbooks/) — QuickBooks Online の前提条件と現在の制限事項。
- [転記レジスターを確認する](/ja/guides/connections/posting-register/) — 財務・会計担当者が、閲覧できるすべてのプロジェクトと接続にわたる ERP の転記を確認するための、テナントレベルのコンソール。

## 関連項目

- [コネクターリファレンス](/ja/reference/connectors/) — サポートされるシステムの全カタログと、各システムに必要なフィールド。
