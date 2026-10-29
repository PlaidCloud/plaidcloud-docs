---
title: Dynamics 365 Finance & Operations REST 连接器
description: 在 PlaidCloud 中设置 Dynamics 365 Finance & Operations 连接，以导入 OData/DMF 实体并异步过账日记账分录。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## API 文档

D365 F&O 的 [OData v4 端点](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata)和[数据管理框架](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export)记录了此连接器所使用的端点和批量提取路径。

## 身份验证的工作方式

该连接使用 Entra ID（Azure AD）**客户端凭据**以应用程序身份进行身份验证：将应用注册的客户端 ID 和密钥换取访问令牌，范围为环境的资源。不涉及交互式登录。

## 配置

| 字段 | 类型 | 说明 |
|---|---|---|
| 名称 | 文本 | 此连接的显示名称。 |
| 环境 URL | 文本 | 您的 D365 F&O 环境 URL，例如 `https://yourorg.operations.dynamics.com`。 |
| 客户端 ID | 文本 | Entra 应用注册的应用程序（客户端）ID。 |
| 客户端密钥 | 文本 | 应用注册的客户端密钥。加密存储。 |
| 租户 ID | 文本 | 您的 Azure AD 租户 ID。 |
| 资源/范围 | 文本 | 请求的 OAuth2 范围，通常为环境 URL 加上 `/.default`。 |

## 可导入的实体

**Import D365 F&O Entity** 步骤涵盖六个实体：`main_accounts`、`currencies`、`customers`、`vendors`、`released_products`、`ledger_journal_headers`。每次拉取以 `odata` 同步模式（直接调用，适用于常规拉取）或 `dmf` 批量模式（异步的数据管理框架导出作业，适用于大规模提取）运行，并支持按实体设置的服务器端筛选器，包括日期、科目和维度范围。完整的字段参考请参阅 [Import D365 F&O Entity](/zh-cn/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) 步骤。

## 过账日记账分录

**D365 F&O: Post Journal Entry** 步骤通过 PlaidCloud 共享的 ERP 写入管道过账总账日记账分录：提交到 D365 F&O 的异步自定义服务日记账过账操作，轮询至终态，并在报告分录已过账之前进行确认。更正时会过账一笔借贷互换的新冲销分录，而不是修改原分录。字段参考请参阅 [D365 F&O: Post Journal Entry](/zh-cn/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) 步骤，完整的过账操作步骤请参阅[连接到 Dynamics 365 Finance & Operations](/zh-cn/guides/connections/dynamics-365-fo/)。

## 已知限制

| 限制 | 含义 |
|---|---|
| DMF 同步模式存在提取延迟 | `dmf` 拉取需要等待异步导出作业，在数据量相同的情况下明显慢于 `odata` 拉取。 |
| 维度筛选取决于结构 | 不属于科目结构的财务维度无法在服务器端筛选；请在拉取之后于工作流中限定其范围。 |

## 相关内容

- [连接到 Dynamics 365 Finance & Operations（指南）](/zh-cn/guides/connections/dynamics-365-fo/) — 分步说明：创建连接、测试连接、导入实体并过账日记账。
- [Import D365 F&O Entity](/zh-cn/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/zh-cn/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
