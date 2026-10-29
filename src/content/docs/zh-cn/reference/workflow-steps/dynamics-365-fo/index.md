---
title: Dynamics 365 F&O 步骤
description: 通过您的 D365 F&O 连接读取和写入 Dynamics 365 Finance & Operations 的工作流步骤 — 导入 OData/DMF 实体，以及过账日记账分录。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

通过您的 [D365 F&O 连接](/zh-cn/guides/connections/dynamics-365-fo/)读取和写入 Dynamics 365 Finance & Operations（D365 F&O）的工作流步骤。导入步骤拉取 OData 实体或批量 DMF 提取数据，无需编写 OData；过账步骤通过 PlaidCloud 共享的 ERP 写入管道过账总账日记账分录。

## 步骤

- [Import D365 F&O Entity 步骤](/zh-cn/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — 主数据和日记账标题，支持 OData 或 DMF 批量模式，带服务器端筛选器。
- [D365 F&O: Post Journal Entry 步骤](/zh-cn/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — 过账总账日记账分录，更正时使用已过账的冲销分录。

## 相关内容

- [Dynamics 365 F&O REST 连接器](/zh-cn/reference/connectors/rest/dynamics-365-fo/)
- [连接到 Dynamics 365 Finance & Operations](/zh-cn/guides/connections/dynamics-365-fo/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
