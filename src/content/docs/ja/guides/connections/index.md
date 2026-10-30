---
title: 接続
description: PlaidCloud の接続を設定して管理します。接続は、ワークフローが外部のデータベース、クラウドストレージ、ERP、REST API に到達できるようにする、保存済みの構成です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**接続**とは、PlaidCloud が外部システム（データベース、クラウドストレージアカウント、ERP、REST API）に到達できるようにする、保存済みの構成です。そのシステムからの読み取りまたはそのシステムへの書き込みが必要なワークフローのステップは接続を参照するため、資格情報とエンドポイントの詳細は 1 か所で管理されます。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="多くのワークフローのステップが 1 つの保存済み接続を参照します。接続は資格情報とエンドポイントを 1 か所に保持し、外部システム（データベース、クラウドストレージ、ERP、REST API）に到達します。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">ワークフローのステップ</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">インポートステップ</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">エクスポートステップ</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">ルックアップステップ</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">接続</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">資格情報 + エンドポイント（1 回のみ）</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">外部システム</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">DB · ストレージ · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">接続は 1 回設定するだけです。外部システムの読み取りや書き込みを行うすべてのステップがその接続を指すため、資格情報とエンドポイントの詳細がステップごとに重複することはありません。</figcaption>
</figure>

## ガイド

- [接続の作成と管理](/ja/guides/connections/create-connection/) — 接続の作成、編集、テスト、アクセス制御を行い、環境ごとに構成します。
- [自分のウェアハウスを使用する](/ja/guides/connections/external-lakehouse/) — 自分の Snowflake または Databricks ウェアハウスを自分で接続し、自分の ID でサインインして、複数のウェアハウスを管理し、各実行のコストを確認します。
- [PlaidCloud Git 接続](/ja/guides/connections/plaidcloud-git/) — サーバー URL や資格情報なしで、ワークスペース専用のマネージド Git サーバーに接続し、そこから Panel アプリのビルドを自動化します。
- [接続のクローン](/ja/guides/connections/clone-connection/) — 既存の接続を複製して、新しい環境やテナントで使用します。
- [Data Foundation: Common Finance Model](/ja/guides/projects/data-foundation/) — Common Finance Model は、複数の ERP システムとインスタンスの ERP データを、1 つの勘定科目表、1 組のエンティティ、1 つの報告通貨を持つ単一のモデルにまとめます。レポート、メトリック、AI アシスタントはすべてこのモデルを読み取ります。
- [Singer ソース](/ja/guides/connections/singer-sources/) — Singer タップで Stripe、GitHub、Slack、BigQuery などのソースに接続し、そのデータをプロジェクトのテーブルにインポートします。
- [NetSuite に接続する](/ja/guides/connections/netsuite/) — NetSuite 接続を設定し、SuiteQL で財務データと業務データを取得します。
- [Data Foundation 向けの NetSuite アクセス](/ja/guides/connections/netsuite-access-for-data-foundation/) — Data Foundation が NetSuite を直接読み取れるように NetSuite 管理者が行う設定と、返送する内容を説明します。
- [NetSuite の財務データをインポートする](/ja/guides/connections/import-netsuite-financials/) — SuiteQL を書かずに、定型の NetSuite インポートステップで残高、GL 明細、マスターデータを取得します。
- [NetSuite の仕訳エントリを転記する](/ja/guides/connections/post-netsuite-journal-entries/) — ヘッダーテーブルと明細テーブルをマッピングし、プレビューして、仕訳エントリを NetSuite に転記します。
- [Acumatica に接続する](/ja/guides/connections/acumatica/) — Acumatica 接続を設定し、エンティティをインポートして、仕訳トランザクション、請求書、仕入請求書、支払を転記します。
- [Business Central に接続する](/ja/guides/connections/business-central/) — Azure AD で Business Central 接続を設定し、OData エンティティをインポートして、総勘定元帳の仕訳明細を転記します。
- [Dynamics 365 Finance & Operations に接続する](/ja/guides/connections/dynamics-365-fo/) — Azure AD で D365 F&O 接続を設定し、OData/DMF エンティティをインポートして、仕訳エントリを転記します。
- [Oracle Fusion に接続する](/ja/guides/connections/oracle-fusion/) — Oracle Fusion 接続を設定し、GL 残高と仕訳バッチをインポートして、FBDI で仕訳を転記します。
- [Workday Financials に接続する](/ja/guides/connections/workday-financials/) — 統合システムユーザーで Workday Financials 接続を設定し、RaaS レポートをインポートして、仕訳エントリを転記します。
- [SAP S/4HANA Cloud に接続する](/ja/guides/connections/s4hana-cloud/) — OAuth2 で S/4HANA Cloud への直接接続を設定し、試算表と仕訳エントリ明細をインポートして、SOAP で仕訳エントリを転記します。
- [SAP ECC / S/4HANA からのアドホック抽出](/ja/guides/connections/sap-adhoc-extract/) — テーブル、トランザクションコード、保存済みの SAP クエリで SAP を検索し、抽出をプレビューして計画し、PlaidLink エージェント経由でテーブルに取り込みます。
- [Sage Intacct に接続する](/ja/guides/connections/sage-intacct/) — Sage Intacct 接続を設定し、財務データと会計データを取得します。
- [Xero に接続する](/ja/guides/connections/xero/) — ワンクリックで Xero の組織を認可し、Accounting API のエンティティをインポートして、手動仕訳、請求書、仕入請求書、支払、クレジットノートを転記します。
- [Salesforce に接続する](/ja/guides/connections/salesforce/) — Salesforce の External Client App と実行ユーザーを設定し、CRM オブジェクトをプロジェクトのテーブルに抽出します。
- [HFM / FCCS からの抽出（アドホック）](/ja/guides/connections/hfm-fccs/) — Oracle FCCS に接続し、POV ピッカーでデータスライスをセルフサービスで取得します。HFM チームへの依頼は不要です。
- [TM1 に接続する](/ja/guides/connections/tm1/) — IBM TM1 / Planning Analytics サーバーに接続し、ビューまたは MDX でキューブデータを期間別に読み取ります。
- [Anaplan に接続する](/ja/guides/connections/anaplan/) — Anaplan に接続し、保存済みビューの読み取り、既存のエクスポートアクションの実行、PlaidCloud ディメンションへのリストのロードを行います。読み取り専用です。
- [QuickBooks に接続する](/ja/guides/connections/quickbooks/) — QuickBooks Online の前提条件と現在の制限事項を説明します。
- [転記レジスターを確認する](/ja/guides/connections/posting-register/) — 財務・会計部門が、閲覧可能なすべてのプロジェクトと接続にわたる ERP の転記を確認する、テナントレベルのコンソールです。

## 関連情報

- [コネクタリファレンス](/ja/reference/connectors/) — サポートされているシステムの完全なカタログと、それぞれに必要なフィールドです。
