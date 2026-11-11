---
title: Data Foundationカバレッジマトリックス
description: Data Foundationが接続する各システムが、Common Finance Modelのどのデータセットを直接供給し、どのデータセットをファイルとして追加する必要があるかを示します。
sidebar:
  label: Data Foundationカバレッジ
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundationは、接続したすべてのERPシステムとインスタンスを直接読み取り、1つのCommon Finance Modelにまとめます。システムが保持していないものはファイルで補えるため、以下のどのデータセットもファイルとして供給することもできます。

## 凡例

| 記号 | 意味 |
| --- | --- |
| **完全** | Data Foundationが、システムからデータセットを直接読み取ります。 |
| **完全¹** | システムがデータを保持している場合に直接読み取ります。データのないシステム、またはデータにアクセスできない接続でも、ロードは停止しません。 |
| **ファイル** | システムはこのデータセットを供給しません。ファイルとして追加してください。 |

## SAP、Oracle、Dynamics 365

| データセット | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| エンティティ | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 会計カレンダー | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 勘定科目表 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 部門 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| プロフィットセンター | 完全¹ | 完全¹ | ファイル | ファイル | ファイル | ファイル |
| 製品 | 完全 | 完全 | 完全 | 完全¹ | 完全¹ | 完全 |
| 顧客 | 完全 | 完全 | 完全 | 完全¹ | 完全¹ | 完全 |
| 総勘定元帳 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 試算表 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 売上明細 | 完全¹ | 完全¹ | 完全¹ | 完全¹ | 完全¹ | 完全¹ |
| パイプライン | ファイル | ファイル | ファイル | ファイル | ファイル | ファイル |
| 在庫残高 | 完全¹ | 完全¹ | 完全¹ | ファイル | ファイル | 完全¹ |
| 予算 | 完全¹ | 完全¹ | 完全¹ | ファイル | ファイル | 完全¹ |
| 配賦ドライバー | 完全¹ | 完全¹ | ファイル | ファイル | ファイル | ファイル |
| 為替レート | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| セグメント値 | ファイル | ファイル | ファイル | ファイル | ファイル | ファイル |
| 評価別CO-PA | ファイル | ファイル | ファイル | ファイル | ファイル | ファイル |

## 中堅企業向けおよびクラウド財務システム

| データセット | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| エンティティ | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 会計カレンダー | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 勘定科目表 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 部門 | 完全 | 完全 | 完全¹ | 完全 | 完全 | 完全 |
| プロフィットセンター | ファイル | ファイル | ファイル | ファイル | ファイル | ファイル |
| 製品 | 完全 | 完全 | 完全¹ | 完全 | 完全¹ | 完全 |
| 顧客 | 完全 | 完全 | 完全¹ | 完全 | 完全¹ | 完全 |
| 総勘定元帳 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 試算表 | 完全 | 完全 | 完全 | 完全 | 完全 | 完全 |
| 売上明細 | 完全¹ | 完全¹ | 完全¹ | 完全¹ | 完全¹ | 完全 |
| パイプライン | ファイル | ファイル | ファイル | ファイル | ファイル | ファイル |
| 在庫残高 | ファイル | ファイル | 完全¹ | ファイル | ファイル | 完全¹ |
| 予算 | 完全¹ | 完全¹ | 完全¹ | 完全¹ | ファイル | 完全¹ |
| 配賦ドライバー | 完全¹ | 完全¹ | ファイル | ファイル | 完全¹ | 完全 |
| 為替レート | 完全 | 完全 | 完全¹ | ファイル | 完全 | 完全¹ |
| セグメント値 | ファイル | ファイル | ファイル | ファイル | 完全¹ | 完全 |
| 評価別CO-PA | ファイル | ファイル | ファイル | ファイル | ファイル | ファイル |

## CRM、連結、プランニングのソース

| データセット | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| エンティティ | ファイル | ファイル | ファイル |
| 会計カレンダー | ファイル | ファイル | ファイル |
| 勘定科目表 | ファイル | ファイル | ファイル |
| 部門 | ファイル | ファイル | ファイル |
| プロフィットセンター | ファイル | ファイル | ファイル |
| 製品 | 完全¹ | ファイル | ファイル |
| 顧客 | 完全¹ | ファイル | ファイル |
| 総勘定元帳 | ファイル | ファイル | ファイル |
| 試算表 | ファイル | ファイル | ファイル |
| 売上明細 | ファイル | ファイル | ファイル |
| パイプライン | 完全¹ | ファイル | ファイル |
| 在庫残高 | ファイル | ファイル | ファイル |
| 予算 | ファイル | 完全 | 完全 |
| 配賦ドライバー | ファイル | ファイル | ファイル |
| 為替レート | ファイル | ファイル | ファイル |
| セグメント値 | ファイル | ファイル | ファイル |
| 評価別CO-PA | ファイル | ファイル | ファイル |

## システム別の注記

- **Salesforce** はCRMソースです。顧客、製品、売上パイプラインを供給しますが、元帳は供給しません。
- **OneStream** は結果のソースです。予算データセットのみを供給し、連結結果を取り込むことで、Data Foundationがグループ損益計算書をそれと照合できるようにします。
- **Anaplan** はプランのソースです。予算データセットのみを、Budget、Forecast、またはConsolidatedのプランから供給します。
- **SAP S/4HANAとSAP ECC** は、同じマスターデータを読み取ります。ECCは、元帳を財務会計および管理会計の明細から、合計を総勘定元帳の合計テーブルから読み取ります。プロフィットセンターは、システムが保持している場合に読み取られます。売上明細は請求伝票であり、CO-PAではありません。
- **評価別CO-PA** は、どのシステムからも直接読み取られません。ファイルとして追加してください。
- **Workday** には、仕訳や残高を直接提供するサービスがありません。Data Foundationは、作成するレポートを提供し、それを読み取ります。セグメント値（ワークタグ）、顧客、製品、売上明細、人数ドライバーは、オプションのレポートから取得されます。予算はファイルのままです。
- **Xero** は為替レートを供給しません。エンティティが複数の通貨を使用する場合は、ファイルとして追加してください。
- **QuickBooks Online** は、会社ファイルが保持している場合に、部門、顧客、製品、為替レート、予算、在庫、売上明細を読み取ります。
- **NetSuite** は、カスタムセグメントをセグメント値として読み取ります。為替レートと在庫は、アカウントが提供している場合に、予算は、アカウントがNetSuite Budgetsを使用しており、ロールがそれを読み取れる場合に読み取られます。

## 関連情報

- [Data Foundation](/ja/guides/projects/data-foundation/)
- [Data Foundationを始める](/ja/guides/projects/data-foundation-getting-started/)
- [ERP外のデータのファイルを追加する](/ja/guides/projects/data-foundation/#erp-外のデータをファイルで追加する)
- 接続のアクセスガイド：
  - [NetSuite](/ja/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/ja/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/ja/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/ja/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/ja/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/ja/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/ja/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/ja/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/ja/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/ja/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/ja/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/ja/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/ja/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/ja/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/ja/guides/connections/anaplan/#data-foundation-のソースとしての-anaplan)
