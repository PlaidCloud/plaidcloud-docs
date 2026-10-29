---
title: Oracle Fusion 步骤
description: 通过 Oracle Fusion 连接读取和写入 Oracle Fusion Cloud 的工作流步骤：通过 OData/BIP 或 FBDI 批量提取导入总账余额和日记账批次，以及过账日记账分录。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

通过 [Oracle Fusion 连接](/zh-cn/guides/connections/oracle-fusion/)读取和写入 Oracle Fusion Cloud 的工作流步骤。两个导入步骤对应不同的拉取规模：常规拉取使用直接的 OData/BIP 调用，大数据量拉取使用异步 FBDI/BIP 批量提取；过账步骤通过 PlaidCloud 共享的 ERP 写入管道过账日记账批次。

## 步骤

- [Import Fusion Entity 步骤](/zh-cn/reference/workflow-steps/oracle-fusion/import-fusion-entity/)：导入总账余额和日记账批次，支持服务器端日期、期间和数值范围筛选。
- [Import Fusion Bulk Extract 步骤](/zh-cn/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/)：导入相同的实体，通过异步 FBDI/BIP 导出作业处理大数据量拉取。
- [Oracle Fusion: Post Journal Entry 步骤](/zh-cn/reference/workflow-steps/oracle-fusion/oracle-fusion-post/)：通过 FBDI 总账接口过账总账日记账批次，更正时使用已过账的冲销分录。

## 相关内容

- [Oracle Fusion 连接器](/zh-cn/reference/connectors/erp/oracle-fusion/)
- [连接到 Oracle Fusion](/zh-cn/guides/connections/oracle-fusion/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
