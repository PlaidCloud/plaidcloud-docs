---
title: REST 连接
description: 将 PlaidCloud 连接到 REST API 服务，包括 Salesforce、NetSuite、Workday、Dynamics 以及其他云平台。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloud 使用标准身份验证方式（OAuth、API 密钥、基本身份验证）连接到 REST API 服务。各提供商在令牌流程、范围处理和分页方面各有特点，下方的专用连接器已封装这些细节，您无需自行处理。

对于没有专用连接器的 REST 服务，PlaidCloud 提供通用 REST 连接器，可配置以适配大多数身份验证和响应解析模式。

## 通用连接器

- [通用 REST 连接](/zh-cn/reference/connectors/rest/generic-rest/) — 配置任意 HTTP API：无/基本/API 密钥/持有者令牌/OAuth 2.0 身份验证、默认标头、重定向处理和请求测试。

## CRM 与销售

- [Salesforce](/zh-cn/reference/connectors/rest/salesforce/)
- [Dynamics](/zh-cn/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## 财务与会计

- [NetSuite](/zh-cn/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/zh-cn/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud（Financial Consolidation and Close）
- [TM1](/zh-cn/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/zh-cn/reference/connectors/rest/acumatica/)
- [Business Central](/zh-cn/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/zh-cn/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/zh-cn/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/zh-cn/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/zh-cn/reference/connectors/rest/quickbooks/)
- [Xero](/zh-cn/reference/connectors/rest/xero/)
- [Sage Intacct](/zh-cn/reference/connectors/rest/sage-intacct/)
- [Stripe](/zh-cn/reference/connectors/rest/stripe/)
- [Ramp](/zh-cn/reference/connectors/rest/ramp/)

## 人力资源与薪资

- [Workday](/zh-cn/reference/connectors/rest/workday/)
- [Paycor](/zh-cn/reference/connectors/rest/paycor/)
- [Gusto](/zh-cn/reference/connectors/rest/gusto/)

## 集成平台

- [MuleSoft](/zh-cn/reference/connectors/rest/mulesoft/)
