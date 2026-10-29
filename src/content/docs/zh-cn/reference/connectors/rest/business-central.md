---
title: Business Central REST 连接器
description: 在 PlaidCloud 中使用 Azure AD 客户端凭据设置 Microsoft Dynamics 365 Business Central 连接，以导入 OData 实体并过账总账日记账行。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## API 文档

Business Central 的[标准 OData v2.0 API](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/)记录了此连接器所使用的实体以及 `$filter`/`$orderby` 选项。

## 身份验证的工作方式

该连接使用 Entra ID（Azure AD）**客户端凭据（S2S）** 以应用程序身份进行身份验证：将应用注册的客户端 ID 和密钥换取访问令牌，地址为 `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`，范围为 `https://api.businesscentral.dynamics.com/.default`。不涉及交互式登录。应用注册需要被授予 Business Central 的 API 权限（`API.ReadWrite.All`，或管理员颁发的更窄范围）。

每个请求都限定在一个**环境**（例如 `Production` 或沙盒环境）及其中的一个**公司**内，两者均在连接上设置，而非按请求选择。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 客户端 ID | 文本 | Entra 应用注册的应用程序（客户端）ID。 |
| 客户端密钥 | 文本 | 应用注册的客户端密钥。加密存储。 |
| 租户 ID | 文本 | 您的 Azure AD 租户 ID。 |
| 环境 | 文本 | Business Central 环境名称，例如 `Production`。 |
| 公司 | 文本 | 此连接读取和过账所针对的 Business Central 公司 ID。 |

## 可导入的实体

**Import Business Central Entity** 步骤涵盖六个实体：`accounts`、`generalLedgerEntries`、`customers`、`vendors`、`items`、`journals`。每次拉取均支持按实体设置的服务器端筛选器。完整的字段参考请参阅 [Import Business Central Entity](/zh-cn/reference/workflow-steps/business-central/import-business-central-entity/) 步骤。

`generalLedgerEntries` 为只读且仅含已过账数据，因此拉取试算平衡表或总账明细时应使用该实体，它从不包含仍留在未过账日记账批次中的行。

## 过账总账日记账行

**Business Central Post** 步骤在**已有的**日记账批次中创建行，并通过 PlaidCloud 共享的 ERP 写入管道过账该批次：过账前先确认该批次只包含此请求的行，过账后根据 `generalLedgerEntries`（而非日记账批次本身）确认过账结果。字段参考请参阅 [Business Central: Post General Journal Lines](/zh-cn/reference/workflow-steps/business-central/business-central-post/) 步骤，完整的过账操作步骤请参阅[连接到 Business Central](/zh-cn/guides/connections/business-central/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| 仅一种写入单据类型 | 仅支持总账日记账行过账。不支持草稿单据流程（销售/采购发票，草稿 → 已过账），因为 Microsoft 公开文档中并未明确该流程的过账操作。 |
| 仅过账到已有批次 | 此连接器从不在 Business Central 中创建日记账批次，请先在其中创建。 |
| 同一批次的并发过账 | 幂等保护的作用域是单据编号，而非日记账批次，因此不同单据编号并发过账到同一批次时，不保证串行执行。 |

## 相关内容

- [连接到 Business Central（指南）](/zh-cn/guides/connections/business-central/) — 分步说明：创建连接、测试连接、导入实体并过账日记账。
- [Import Business Central Entity](/zh-cn/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/zh-cn/reference/workflow-steps/business-central/business-central-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
