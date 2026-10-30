---
title: 连接
description: 设置和管理 PlaidCloud 连接——使工作流能够访问外部数据库、云存储、ERP 和 REST API 的已保存配置。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/connections/index.md
---

**连接**是使 PlaidCloud 能够访问外部系统（数据库、云存储账户、ERP 或 REST API）的已保存配置。需要从该系统读取或向其写入的工作流步骤会引用该连接，因此凭据和端点详细信息集中存放在一处。

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="多个工作流步骤引用同一个已保存的连接，该连接将凭据和端点集中保存在一处，并访问外部系统——数据库、云存储、ERP 或 REST API。" style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="cn-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">工作流步骤</text>
  <rect x="16" y="40" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="61" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">导入步骤</text>
  <rect x="16" y="88" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="109" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">导出步骤</text>
  <rect x="16" y="136" width="120" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="157" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">查找步骤</text>
  <path d="M136 57 C190 57 210 96 248 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 105 L248 108" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <path d="M136 153 C190 153 210 118 248 114" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="250" y="76" width="180" height="66" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="340" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">连接</text>
  <text x="340" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">凭据 + 端点，仅一次</text>
  <path d="M430 109 L512 109" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#cn-arrow)" />
  <rect x="514" y="80" width="150" height="58" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="589" y="104" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">外部系统</text>
  <text x="589" y="122" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">数据库 · 存储 · ERP · REST</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">只需配置一次连接；每个读取或写入外部系统的步骤都指向它，因此凭据和端点详细信息不会在各步骤之间重复。</figcaption>
</figure>

## 指南

- [创建和管理连接](/zh-cn/guides/connections/create-connection/) — 创建、编辑、测试和控制连接的访问权限，并按环境进行配置。
- [使用您自己的数据仓库](/zh-cn/guides/connections/external-lakehouse/) — 自行连接您自己的 Snowflake 或 Databricks 数据仓库，使用您自己的身份登录，管理多个数据仓库，并查看每次运行的成本。
- [PlaidCloud Git 连接](/zh-cn/guides/connections/plaidcloud-git/) — 连接到工作区自带的托管 Git 服务器，无需服务器 URL 或凭据，并据此自动构建 Panel 应用。
- [克隆连接](/zh-cn/guides/connections/clone-connection/) — 为新环境或新租户复制现有连接。
- [Data Foundation：Common Finance Model](/zh-cn/guides/projects/data-foundation/) — Common Finance Model 将来自多个 ERP 系统和实例的 ERP 数据汇集到一个模型中，拥有一套会计科目表、一组实体和一种报告货币，供报表、指标和 AI 助手统一读取。
- [Singer 数据源](/zh-cn/guides/connections/singer-sources/) — 使用 Singer tap 连接 Stripe、GitHub、Slack 和 BigQuery 等数据源，然后将其数据导入项目表。
- [连接到 NetSuite](/zh-cn/guides/connections/netsuite/) — 设置 NetSuite 连接，并使用 SuiteQL 拉取财务和运营数据。
- [Data Foundation 的 NetSuite 访问权限](/zh-cn/guides/connections/netsuite-access-for-data-foundation/) — NetSuite 管理员需要设置哪些内容，才能让 Data Foundation 直接读取 NetSuite，以及需要回传哪些信息。
- [导入 NetSuite 财务数据](/zh-cn/guides/connections/import-netsuite-financials/) — 使用预置的 NetSuite 导入步骤拉取余额、总账明细和主数据，无需编写 SuiteQL。
- [过账 NetSuite 日记账分录](/zh-cn/guides/connections/post-netsuite-journal-entries/) — 映射表头表和明细行表，预览并将日记账分录过账到 NetSuite。
- [连接到 Acumatica](/zh-cn/guides/connections/acumatica/) — 设置 Acumatica 连接，导入实体，并过账日记账交易、发票、账单和付款。
- [连接到 Business Central](/zh-cn/guides/connections/business-central/) — 使用 Azure AD 设置 Business Central 连接，导入 OData 实体，并过账总账日记账行。
- [连接到 Dynamics 365 Finance & Operations](/zh-cn/guides/connections/dynamics-365-fo/) — 使用 Azure AD 设置 D365 F&O 连接，导入 OData/DMF 实体，并过账日记账分录。
- [连接到 Oracle Fusion](/zh-cn/guides/connections/oracle-fusion/) — 设置 Oracle Fusion 连接，导入总账余额和日记账批次，并通过 FBDI 过账日记账。
- [连接到 Workday Financials](/zh-cn/guides/connections/workday-financials/) — 使用集成系统用户设置 Workday Financials 连接，导入 RaaS 报表，并过账日记账分录。
- [连接到 SAP S/4HANA Cloud](/zh-cn/guides/connections/s4hana-cloud/) — 使用 OAuth2 设置直接的 S/4HANA Cloud 连接，导入试算平衡表和日记账分录行项目，并通过 SOAP 过账日记账分录。
- [从 SAP ECC / S/4HANA 临时提取](/zh-cn/guides/connections/sap-adhoc-extract/) — 按表、事务代码或已保存的 SAP Query 搜索 SAP，预览并规划提取，然后通过 PlaidLink 代理将其落入表中。
- [连接到 Sage Intacct](/zh-cn/guides/connections/sage-intacct/) — 设置 Sage Intacct 连接并拉取财务和会计数据。
- [连接到 Xero](/zh-cn/guides/connections/xero/) — 一键授权 Xero 组织，导入 Accounting API 实体，并过账手工日记账、发票、账单、付款和贷项通知单。
- [连接到 Salesforce](/zh-cn/guides/connections/salesforce/) — 设置 Salesforce External Client App 和 Run As 用户，然后将 CRM 对象提取到项目表中。
- [从 HFM / FCCS 提取（临时）](/zh-cn/guides/connections/hfm-fccs/) — 连接到 Oracle FCCS，并通过视点选择器自助获取数据切片，无需向 HFM 团队提交工单。
- [连接到 TM1](/zh-cn/guides/connections/tm1/) — 连接到 IBM TM1 / Planning Analytics 服务器，并按视图或 MDX 读取多维数据集数据，按期间切片。
- [连接到 Anaplan](/zh-cn/guides/connections/anaplan/) — 连接到 Anaplan，读取已保存的视图，运行已有的导出操作，或将列表加载到 PlaidCloud 维度中。只读。
- [连接到 QuickBooks](/zh-cn/guides/connections/quickbooks/) — QuickBooks Online 的前提条件和当前限制。
- [查看过账登记簿](/zh-cn/guides/connections/posting-register/) — 租户级控制台，供财务和会计人员查看其可见的所有项目和连接中的 ERP 过账。

## 相关内容

- [连接器参考](/zh-cn/reference/connectors/) — 受支持系统的完整目录以及每个系统所需的字段。
