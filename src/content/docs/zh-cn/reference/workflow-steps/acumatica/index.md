---
title: Acumatica 步骤
description: 通过 Acumatica 连接读取和写入 Acumatica 的工作流步骤：导入基于合约的 REST 实体，并过账日记账交易、发票、账单和付款。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

通过您的 [Acumatica 连接](/zh-cn/guides/connections/acumatica/)读取和写入 Acumatica 的工作流步骤。导入步骤无需编写 OData 即可拉取 Acumatica 基于合约的 REST 实体；过账步骤通过 PlaidCloud 共享的 ERP 写入管道过账日记账交易、销售发票、账单和付款。

## 步骤

- [Import Acumatica Entity 步骤](/zh-cn/reference/workflow-steps/acumatica/import-acumatica-entity/)：主数据和交易实体，支持服务器端筛选器。
- [Acumatica: Post Documents 步骤](/zh-cn/reference/workflow-steps/acumatica/acumatica-post/)：过账日记账交易、销售发票、账单和付款。

## 相关内容

- [Acumatica REST 连接器](/zh-cn/reference/connectors/rest/acumatica/)
- [连接到 Acumatica](/zh-cn/guides/connections/acumatica/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
