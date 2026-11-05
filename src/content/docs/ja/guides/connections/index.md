---
title: 接続
description: PlaidCloudの接続の設定と管理について説明します。接続は、ワークフローが外部のデータベース、クラウドストレージ、ERP、REST APIにアクセスするための保存済みの構成です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**接続**は、PlaidCloudが外部システム（データベース、クラウドストレージアカウント、ERP、REST API）にアクセスするための保存済みの構成です。そのシステムから読み取る、またはそのシステムへ書き込むワークフローステップは接続を参照するため、認証情報とエンドポイントの詳細が1か所にまとまります。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="多数のワークフローステップが1つの保存済み接続を参照します。接続は認証情報とエンドポイントを1か所で保持し、データベース、クラウドストレージ、ERP、REST APIなどの外部システムにアクセスします。" style="width:100%;max-width:680px;height:auto;">
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
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">認証情報とエンドポイントを1回だけ設定</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">外部システム</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · ストレージ · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">接続を1回構成すれば、外部システムを読み書きするすべてのステップがその接続を指すため、認証情報とエンドポイントの詳細をステップごとに重複して持つ必要がありません。</figcaption>
</figure>

## ガイド

- [接続の作成と管理](/ja/guides/connections/create-connection/) — 接続の作成、編集、テスト、アクセス制御を行い、環境ごとに構成します。
- [独自のウェアハウスを使用する](/ja/guides/connections/external-lakehouse/) — 独自のSnowflakeまたはDatabricksウェアハウスを自分で接続し、自分のIDでサインインして、複数のウェアハウスを管理し、実行ごとのコストを確認します。
- [PlaidCloud Git接続](/ja/guides/connections/plaidcloud-git/) — サーバーURLや認証情報なしで、ワークスペース専用のマネージドGitサーバーに接続し、そこからPanelアプリのビルドを自動化します。
- [接続の複製](/ja/guides/connections/clone-connection/) — 既存の接続を複製して、新しい環境やテナント向けに使用します。
- [Data Foundation: Common Finance Model](/ja/guides/projects/data-foundation/) — Common Finance Modelは、複数のERPシステムやインスタンスのERPデータを、1つの勘定科目表、1組のエンティティ、1つの報告通貨を持つ単一のモデルにまとめます。レポート、メトリック、AIアシスタントはすべてこのモデルを参照します。
- [Singerソース](/ja/guides/connections/singer-sources/) — Singerタップを使ってStripe、GitHub、Slack、BigQueryなどのソースに接続し、そのデータをプロジェクトのテーブルにインポートします。
- [NetSuiteに接続](/ja/guides/connections/netsuite/) — NetSuite 接続を設定し、SuiteQLで財務データと業務データを取得します。
- [Data Foundation向けのNetSuiteアクセス](/ja/guides/connections/netsuite-access-for-data-foundation/) — Data FoundationがNetSuiteを直接読み取れるようにするためにNetSuite管理者が設定する内容と、返送する情報です。
- [NetSuite財務データのインポート](/ja/guides/connections/import-netsuite-financials/) — SuiteQLを書かずに、定型のNetSuiteインポートステップで残高、GL明細、マスターデータを取得します。
- [NetSuite仕訳の転記](/ja/guides/connections/post-netsuite-journal-entries/) — ヘッダーテーブルと明細テーブルをマッピングし、プレビューして、仕訳をNetSuiteに転記します。
- [Acumaticaに接続](/ja/guides/connections/acumatica/) — Acumatica接続を設定し、エンティティをインポートして、仕訳トランザクション、請求書、買掛金、支払を転記します。
- [Business Centralに接続](/ja/guides/connections/business-central/) — Azure ADでBusiness Central接続を設定し、ODataエンティティをインポートして、総勘定元帳の仕訳明細を転記します。
- [Dynamics 365 Finance & Operationsに接続](/ja/guides/connections/dynamics-365-fo/) — Azure ADでD365 F&O接続を設定し、OData/DMFエンティティをインポートして、仕訳を転記します。
- [Oracle Fusionに接続](/ja/guides/connections/oracle-fusion/) — Oracle Fusion接続を設定し、GL残高と仕訳バッチをインポートして、FBDI経由で仕訳を転記します。
- [Workday Financialsに接続](/ja/guides/connections/workday-financials/) — 統合システムユーザーでWorkday Financials接続を設定し、RaaSレポートをインポートして、仕訳を転記します。
- [SAP S/4HANA Cloudに接続](/ja/guides/connections/s4hana-cloud/) — OAuth2でS/4HANA Cloudへの直接接続を設定し、試算表と仕訳明細をインポートして、SOAP経由で仕訳を転記します。
- [SAP ECC / S/4HANAからのアドホック抽出](/ja/guides/connections/sap-adhoc-extract/) — テーブル、トランザクションコード、または保存済みのSAP Queryを指定してSAPを検索し、抽出をプレビューして計画した上で、PlaidLinkエージェント経由でテーブルに取り込みます。
- [Sage Intacctに接続](/ja/guides/connections/sage-intacct/) — Sage Intacct接続を設定し、財務データと会計データを取得します。
- [Xeroに接続](/ja/guides/connections/xero/) — Xero組織をワンクリックで承認し、Accounting APIエンティティをインポートして、手動仕訳、請求書、買掛金、支払、クレジットノートを転記します。
- [Salesforceに接続](/ja/guides/connections/salesforce/) — SalesforceのExternal Client Appと実行ユーザーを設定し、CRMオブジェクトをプロジェクトのテーブルに抽出します。
- [HFM / FCCSからの抽出（アドホック）](/ja/guides/connections/hfm-fccs/) — Oracle FCCSに接続し、HFMチームへのチケットなしで、POV（視点）ピッカーを使ってデータのスライスをセルフサービスで取得します。
- [TM1に接続](/ja/guides/connections/tm1/) — IBM TM1 / Planning Analyticsサーバーに接続し、ビューまたはMDXでキューブデータを期間別に読み取ります。
- [Anaplanに接続](/ja/guides/connections/anaplan/) — Anaplanに接続し、保存済みビューの読み取り、既存のエクスポートアクションの実行、リストのPlaidCloudディメンションへのロードを行います。読み取り専用です。
- [Data Foundation向けOneStream](/ja/guides/connections/onestream-for-data-foundation/) — Data Foundationがデータアダプター経由で連結結果を読み取れるようにするために、OneStream管理者が設定する内容です。
- [QuickBooksに接続](/ja/guides/connections/quickbooks/) — QuickBooks Onlineの前提条件と現在の制限事項です。
- [転記レジスターの確認](/ja/guides/connections/posting-register/) — 経理・財務担当者が、閲覧可能なすべてのプロジェクトと接続にわたるERP転記を確認する、テナントレベルのコンソールです。

## 関連項目

- [コネクターリファレンス](/ja/reference/connectors/) — サポート対象システムの完全なカタログと、各システムに必要なフィールドです。
