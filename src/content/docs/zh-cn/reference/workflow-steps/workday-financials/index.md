---
title: Workday Financials 步骤
description: 通过您的 Workday Financials 连接读取和写入 Workday Financials 的工作流步骤，包括通过 RaaS 报表导入数据以及过账会计日记账。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

通过您的 [Workday Financials 连接](/zh-cn/guides/connections/workday-financials/)读取和写入 Workday Financials 的工作流步骤。导入步骤拉取客户提供的报表即服务 (RaaS) 报表；过账步骤通过 PlaidCloud 共享的 ERP 写入管道过账会计日记账。

## 步骤

- [Import Workday Entity 步骤](/zh-cn/reference/workflow-steps/workday-financials/import-workday-entity/) — 拉取 RaaS 报表，并支持报表参数筛选。
- [Workday Financials: Post Journal Entry 步骤](/zh-cn/reference/workflow-steps/workday-financials/workday-post/) — 通过 `Submit_Accounting_Journal` 过账会计日记账，更正时使用已过账的冲销分录。

## 相关内容

- [Workday Financials 连接器](/zh-cn/reference/connectors/rest/workday-financials/)
- [连接到 Workday Financials](/zh-cn/guides/connections/workday-financials/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
