---
title: Business Central 步骤
description: 通过 Business Central 连接读取和写入 Microsoft Dynamics 365 Business Central 的工作流步骤：导入 OData 实体，以及过账总账日记账行。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

通过 [Business Central 连接](/zh-cn/guides/connections/business-central/)读取和写入 Business Central 的工作流步骤。导入步骤无需编写查询即可提取 Business Central 的标准 OData v2.0 实体；过账步骤通过 PlaidCloud 共享的 ERP 写入管道过账总账日记账行。

## 步骤

- [Import Business Central Entity 步骤](/zh-cn/reference/workflow-steps/business-central/import-business-central-entity/)：科目、总账条目、客户、供应商、物料和日记账，支持服务器端筛选器。
- [Business Central: Post General Journal Lines 步骤](/zh-cn/reference/workflow-steps/business-central/business-central-post/)：将行过账到现有日记账批次并过账该批次。

## 相关内容

- [Business Central REST 连接器](/zh-cn/reference/connectors/rest/business-central/)
- [连接到 Business Central](/zh-cn/guides/connections/business-central/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
