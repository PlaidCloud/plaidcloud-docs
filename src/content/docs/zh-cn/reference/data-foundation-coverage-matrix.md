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
| **完整¹** | 系统持有该数据时直接读取。系统没有该数据不会中断加载。连接无权访问该数据时，只会使该数据集为空或只有该数据集失败，其余部分照常加载。 |
| **文件** | 系统不提供该数据集。请以文件方式添加。 |

## SAP、Oracle 和 Dynamics 365

| 数据集 | SAP S/4HANA | SAP ECC | SAP S/4HANA Cloud | Oracle E-Business Suite | Oracle Fusion | Dynamics 365 Finance and Operations |
| --- | --- | --- | --- | --- | --- | --- |
| 实体 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 财务日历 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 会计科目表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 部门 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 利润中心 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 文件 | 完整¹ |
| 地点 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 项目 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 销售代表 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 产品 | 完整 | 完整 | 完整 | 完整¹ | 完整¹ | 完整 |
| 客户 | 完整 | 完整 | 完整 | 完整¹ | 完整¹ | 完整 |
| 供应商 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 总账 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 试算平衡表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 月末余额 | 文件 | 完整¹ | 文件 | 完整¹ | 完整¹ | 文件 |
| 银行余额 | 文件 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ |
| 销售明细行 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 销售管道 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 供应商发票明细行 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 采购订单 | 完整¹ | 完整¹ | 文件 | 完整¹ | 完整¹ | 文件 |
| 未清项 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 付款 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 库存余额 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 标准成本 | 完整¹ | 完整¹ | 文件 | 完整¹ | 完整¹ | 文件 |
| 固定资产 | 完整¹ | 完整¹ | 文件 | 完整¹ | 完整¹ | 文件 |
| 资产变动 | 完整¹ | 完整¹ | 文件 | 完整¹ | 完整¹ | 文件 |
| 预算 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 分摊动因 | 完整¹ | 完整¹ | 文件 | 文件 | 文件 | 文件 |
| 汇率 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 分部值 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 按估值的 CO-PA | 完整¹ | 完整¹ | 文件 | 文件 | 文件 | 文件 |

## 中端市场和云财务系统

| 数据集 | Business Central | Sage 100 | Sage Intacct | QuickBooks Online | Xero | Workday | NetSuite |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 实体 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 财务日历 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 会计科目表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 部门 | 完整 | 完整¹ | 完整 | 文件 | 完整¹ | 完整 | 完整 |
| 利润中心 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 文件 | 完整¹ |
| 地点 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 文件 | 完整¹ |
| 项目 | 文件 | 文件 | 完整¹ | 文件 | 文件 | 文件 | 文件 |
| 销售代表 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 完整¹ |
| 产品 | 完整 | 文件 | 完整 | 完整¹ | 完整¹ | 完整¹ | 完整 |
| 客户 | 完整 | 文件 | 完整 | 完整¹ | 完整¹ | 完整¹ | 完整 |
| 供应商 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 总账 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 试算平衡表 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 | 完整 |
| 月末余额 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 文件 |
| 银行余额 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 销售明细行 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整 |
| 销售管道 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 供应商发票明细行 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 未清项 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 付款 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 采购订单 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 库存余额 | 完整¹ | 文件 | 文件 | 完整¹ | 文件 | 文件 | 完整¹ |
| 标准成本 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 固定资产 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 资产变动 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |
| 预算 | 完整¹ | 文件 | 完整¹ | 完整¹ | 完整¹ | 完整¹ | 完整¹ |
| 分摊动因 | 完整¹ | 文件 | 完整¹ | 文件 | 文件 | 完整¹ | 完整 |
| 汇率 | 完整 | 文件 | 完整 | 完整¹ | 文件 | 完整 | 完整¹ |
| 分部值 | 文件 | 文件 | 文件 | 文件 | 文件 | 完整¹ | 完整¹ |
| 按估值的 CO-PA | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 | 文件 |

## CRM、合并和计划来源

| 数据集 | Salesforce | OneStream | Anaplan |
| --- | --- | --- | --- |
| 实体 | 文件 | 文件 | 文件 |
| 财务日历 | 完整¹ | 文件 | 文件 |
| 会计科目表 | 文件 | 文件 | 文件 |
| 部门 | 文件 | 文件 | 文件 |
| 利润中心 | 文件 | 文件 | 文件 |
| 项目 | 完整¹ | 文件 | 文件 |
| 销售代表 | 完整¹ | 文件 | 文件 |
| 产品 | 完整¹ | 文件 | 文件 |
| 客户 | 完整¹ | 文件 | 文件 |
| 总账 | 文件 | 文件 | 文件 |
| 试算平衡表 | 文件 | 文件 | 文件 |
| 销售明细行 | 文件 | 文件 | 文件 |
| 销售管道 | 完整¹ | 文件 | 文件 |
| 销售订单 | 完整¹ | 文件 | 文件 |
| 库存余额 | 文件 | 文件 | 文件 |
| 预算 | 文件 | 完整 | 完整 |
| 分摊动因 | 文件 | 完整¹ | 完整¹ |
| 汇率 | 文件 | 文件 | 文件 |
| 分部值 | 文件 | 文件 | 文件 |
| 按估值的 CO-PA | 文件 | 文件 | 文件 |

## 各系统说明

- **销售订单、合同、递延收入和库存变动**不会从任何系统读取，Salesforce 订单除外。请以文件方式添加。
- **Salesforce** 是 CRM 来源。它提供客户、产品、销售管道、销售代表（用户）、作为项目的营销活动、其财务月份和订单，从不提供总账。订单需要在 Salesforce 中启用 Orders。当 Salesforce 拒绝读取订单时，只有订单月份失败，并保留上次加载的内容。
- **OneStream** 是结果来源。它提供预算数据集，用于导入您的合并结果，以便 Data Foundation 将集团损益表与之核对，并将 Budget 或 Forecast 方案作为计划提供。可选的第二个适配器会将计划人数和数量作为分摊动因提供。
- **Anaplan** 是计划来源。它提供预算数据集（来自 Budget、Forecast 或 Consolidated 计划），并通过可选的第二个导出提供分摊动因。
- **SAP S/4HANA 和 SAP ECC** 读取相同的主数据、供应商、供应商发票、采购订单、未清项、付款、固定资产登记簿和标准成本。ECC 从财务会计和管理会计行项目读取其账务，从总账汇总表读取其合计和月末余额。系统持有利润中心和工厂（地点）时会读取。销售明细行是开票凭证。按估值的 CO-PA 从您指定的经营范围行项目表读取；未指定时，请以文件方式添加。
- **Oracle E-Business Suite** 从您分别为地点和利润中心指定的会计科目表段读取它们。
- **Oracle Fusion** 从各自的 BI Publisher 报表读取每个可选数据集。未部署客户、产品、地点或供应商报表时，该数据集为空并显示警告；其他任何报表的数据集会失败，并保留上次加载的内容；其余所有内容照常加载。
- **Workday** 没有直接的日记账或余额服务。Data Foundation 会提供需要您构建的报表并读取它们。分部值（worktags）、客户、产品、供应商、销售明细行、子分类账、银行余额、预算和动因来自可选报表，月末余额来自期初余额报表中的期末余额。
- **Sage 100** 通过 PlaidLink 代理读取，每个连接对应一个公司。它的账簿使用单一货币，因此不提供汇率，Data Foundation 也不读取其产品、客户或销售明细行。当科目掩码包含部门段时，部门会从该账户的部门段中读取。
- **Xero** 不提供汇率。如果您的实体使用多种货币，请以文件方式添加。部门、地点和利润中心是名称恰好为 Department、Site 和 Profit centre 的跟踪类别中的选项。Xero 允许两个跟踪类别，因此一个组织最多拥有这三者中的两个。
- **QuickBooks Online** 没有部门：其位置被读取为地点，其类别被读取为利润中心。公司持有客户、产品、供应商、汇率、预算、库存、销售和采购时会读取它们；只有当公司跟踪现有数量时才会读取库存。
- **NetSuite** 将自定义分部读取为分部值，将类别读取为利润中心，将位置读取为地点。账户提供汇率和库存时会读取它们；账户使用 NetSuite Budgets 且角色可以读取时会读取预算。

## 月末余额

Data Foundation 读取每个系统自身在每个月末报告的期末余额（请参阅[这些数字可信吗？](/zh-cn/guides/projects/data-foundation-proof/)），来源如下：

| 系统 | 月末余额的读取来源 |
| --- | --- |
| SAP ECC | 总账汇总表（`FAGLFLEXT`，传统总账为 `GLT0`） |
| Oracle E-Business Suite | `GL_BALANCES`，必须包含每个期间 |
| Oracle Fusion | PlaidCloudBalances 报表，涵盖每个期间 |
| Business Central | 每个月末的试算平衡表 |
| Sage Intacct | 科目余额（每个月的期末余额） |
| QuickBooks Online | 每个月末的 Trial Balance 报表 |
| Xero | 每个月末的 Trial Balance 报表 |
| Workday | Beginning Balances 报表的期末余额 |

SAP S/4HANA、SAP S/4HANA Cloud、Dynamics 365 Finance and Operations、NetSuite 和 Sage 100 不报告 Data Foundation 可读取的单独余额。它们照常加载和工作。当 Business Central 拒绝提供某个月末的试算平衡表时，该月的余额会失败，并保留上次加载的内容。

## 日记账明细

除金额外，每个总账明细行还会携带日记账的类型、单据日期、录入人及录入时间、审批人、所冲销的日记账及其税额（系统持有这些数据时）。财务日历会携带每个期间的状态。

| 系统 | 日记账类型 | 单据日期 | 录入人及时间 | 审批人 | 冲销 | 税 | 期间状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SAP S/4HANA | 是 | 是 | 是 | 否 | 否 | 代码 | 是 |
| SAP ECC | 是 | 是 | 是 | 否 | 是 | 代码和金额 | 是 |
| SAP S/4HANA Cloud | 是 | 是 | 是 | 否 | 是 | 否 | 否 |
| Oracle E-Business Suite | 是 | 是 | 是 | 是 | 是 | 否 | 是 |
| Oracle Fusion | 是 | 是 | 是 | 是 | 是 | 否 | 是 |
| Dynamics 365 Finance and Operations | 是 | 是 | 是 | 否 | 否 | 否 | 是 |
| Business Central | 是 | 是 | 是 | 否 | 是 | 否 | 是 |
| Sage 100 | 否 | 否 | 否 | 否 | 否 | 否 | 期间结束后即结账 |
| Sage Intacct | 是 | 是 | 是 | 是 | 是 | 否 | 是 |
| QuickBooks Online | 是 | 是 | 是 | 否 | 否 | 否 | 关账日期 |
| Xero | 是 | 是 | 仅时间 | 否 | 否 | 否 | 锁定日期 |
| Workday | 是 | 是 | 是 | 是 | 是 | 代码和金额 | 是 |
| NetSuite | 是 | 是 | 是 | 否 | 否 | 否 | 是 |

SAP S/4HANA Cloud 从 Journal Entry 服务读取日记账的录入人及其冲销对象，Sage Intacct 从日记账批次读取这些信息，Oracle E-Business Suite 从 `GL_JE_BATCHES` 读取审批人。无法读取这些信息的连接会使这些列为空。

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
  - [Sage 100](/zh-cn/guides/connections/sage-100/)
  - [Sage Intacct](/zh-cn/guides/connections/sage-intacct-access-for-data-foundation/)
  - [QuickBooks Online](/zh-cn/guides/connections/quickbooks-access-for-data-foundation/)
  - [Xero](/zh-cn/guides/connections/xero-access-for-data-foundation/)
  - [Workday](/zh-cn/guides/connections/workday-access-for-data-foundation/)
  - [OneStream](/zh-cn/guides/connections/onestream-for-data-foundation/)
  - [Anaplan](/zh-cn/guides/connections/anaplan/#将-anaplan-作为-data-foundation-源)
