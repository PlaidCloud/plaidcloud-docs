---
title: Data Foundation 覆盖矩阵
description: Data Foundation 所连接的每个系统直接提供哪些 Common Finance Model 数据集，以及哪些需要以文件方式添加。
sidebar:
  label: Data Foundation 覆盖范围
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/data-foundation-coverage-matrix.md
---

Data Foundation 会直接读取您连接的每个 ERP 系统和实例，汇入同一个 Common Finance Model。系统中没有的内容可以用文件补充，因此下面的每个数据集也都可以作为文件提供。

## 图例

| 标记 | 含义 |
| --- | --- |
| **完整** | Data Foundation 直接从系统读取该数据集。 |
| **完整¹** | 系统持有该数据时直接读取。系统没有该数据，或连接无权访问该数据，不会中断加载。 |
| **文件** | 系统不提供该数据集。请以文件方式添加。 |

## SAP、Oracle 和 Dynamics 365

| 数据集 | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| 实体 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 财务日历 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 会计科目表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 部门 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 利润中心 | 完整¹ | 完整¹ | 文件 | 文件 | 文件 | 文件 |
| 产品 | 完整 | 完整 | 完整 | 完整¹ | 完整¹ | 完整 |
| 客户 | 完整 | 完整 | 完整 | 完整¹ | 完整¹ | 完整 |
| 总账 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 试算平衡表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 销售明细行 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 销售管道 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 库存余额 | 完整¹ | 完整¹ | 完整¹ | 文件 | 文件 | 完整¹ |
| 预算 | 完整¹ | 完整¹ | 完整¹ | 文件 | 文件 | 完整¹ |
| 分摊动因 | 完整¹ | 完整¹ | 文件 | 文件 | 文件 | 文件 |
| 汇率 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 分部值 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 按估值的 CO-PA | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |

## 中端市场和云财务系统

| 数据集 | Business Central | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- |
| 实体 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 财务日历 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 会计科目表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 部门 | 完整 | 完整 | 完整¹ | 完整 | 完整 | 完整 |
| 利润中心 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 产品 | 完整 | 完整 | 完整¹ | 完整 | 完整¹ | 完整 |
| 客户 | 完整 | 完整 | 完整¹ | 完整 | 完整¹ | 完整 |
| 总账 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 试算平衡表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 销售明细行 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整 |
| 销售管道 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 库存余额 | 文件 | 文件 | 完整¹ | 文件 | 文件 | 完整¹ |
| 预算 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 文件 | 完整¹ |
| 分摊动因 | 完整¹ | 完整¹ | 文件 | 文件 | 完整¹ | 完整 |
| 汇率 | 完整 | 完整 | 完整¹ | 文件 | 完整 | 完整¹ |
| 分部值 | 文件 | 文件 | 文件 | 文件 | 完整¹ | 完整 |
| 按估值的 CO-PA | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |

## CRM、合并和计划来源

| 数据集 | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| 实体 | 文件 | 文件 | 文件 |
| 财务日历 | 文件 | 文件 | 文件 |
| 会计科目表 | 文件 | 文件 | 文件 |
| 部门 | 文件 | 文件 | 文件 |
| 利润中心 | 文件 | 文件 | 文件 |
| 产品 | 完整¹ | 文件 | 文件 |
| 客户 | 完整¹ | 文件 | 文件 |
| 总账 | 文件 | 文件 | 文件 |
| 试算平衡表 | 文件 | 文件 | 文件 |
| 销售明细行 | 文件 | 文件 | 文件 |
| 销售管道 | 完整¹ | 文件 | 文件 |
| 库存余额 | 文件 | 文件 | 文件 |
| 预算 | 文件 | 完整 | 完整 |
| 分摊动因 | 文件 | 文件 | 文件 |
| 汇率 | 文件 | 文件 | 文件 |
| 分部值 | 文件 | 文件 | 文件 |
| 按估值的 CO-PA | 文件 | 文件 | 文件 |

## 各系统说明

- **Salesforce** 是 CRM 来源。它提供客户、产品和销售管道，从不提供总账。
- **OneStream** 是结果来源。它只提供预算数据集，用于导入您的合并结果，以便 Data Foundation 将集团损益表与之核对。
- **Anaplan** 是计划来源。它只提供预算数据集，来自 Budget、Forecast 或 Consolidated 计划。
- **SAP S/4HANA 和 SAP ECC** 读取相同的主数据。ECC 从财务会计和管理会计行项目读取其账务，从总账汇总表读取其合计。系统持有利润中心时会读取。销售明细行是开票凭证，而不是 CO-PA。
- **按估值的 CO-PA** 不会直接从任何系统读取。请以文件方式添加。
- **Workday** 没有直接的日记账或余额服务。Data Foundation 会提供需要您构建的报表并读取它们。分部值（worktags）、客户、产品、销售明细行和人数动因来自可选报表。预算仍使用文件。
- **Xero** 不提供汇率。如果您的实体使用多种货币，请以文件方式添加。
- **QuickBooks Online** 在公司文件中持有部门、客户、产品、汇率、预算、库存和销售明细行时会读取它们。
- **NetSuite** 将自定义分部读取为分部值。账户提供汇率和库存时会读取它们；账户使用 NetSuite Budgets 且角色可以读取时会读取预算。

## 相关内容

- [Data Foundation](/zh-cn/guides/projects/data-foundation/)
- [Data Foundation 入门](/zh-cn/guides/projects/data-foundation-getting-started/)
- [添加 ERP 之外的数据文件](/zh-cn/guides/projects/data-foundation/#添加文件以补充-erp-之外的数据)
- 连接访问指南：
  - [NetSuite](/zh-cn/guides/connections/netsuite-access-for-data-foundation/)
  - [Salesforce](/zh-cn/guides/connections/salesforce-access-for-data-foundation/)
  - [SAP S/4HANA](/zh-cn/guides/connections/sap-s4hana-access-for-data-foundation/)
  - [SAP ECC](/zh-cn/guides/connections/sap-ecc-access-for-data-foundation/)
  - [SAP S/4HANA Cloud](/zh-cn/guides/connections/s4hana-cloud-access-for-data-foundation/)
  - [Oracle E-Business Suite](/zh-cn/guides/connections/oracle-ebs-access-for-data-foundation/)
  - [Oracle Fusion](/zh-cn/guides/connections/oracle-fusion-access-for-data-foundation/)
  - [Dynamics 365 Finance and Operations](/zh-cn/guides/connections/dynamics-365-fo-access-for-data-foundation/)
  - [Business Central](/zh-cn/guides/connections/business-central-access-for-data-foundation/)
  - [Sage Intacct](/zh-cn/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/zh-cn/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/zh-cn/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/zh-cn/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/zh-cn/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/zh-cn/guides/connections/anaplan/#将-anaplan-作为-data-foundation-源)
