---
title: SAP S/4HANA Cloud 步骤
description: 通过 S/4HANA Cloud 连接读取和写入 SAP S/4HANA Cloud Public Edition 的工作流步骤：导入试算平衡表和日记账分录行项目，以及过账日记账分录。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

通过 [S/4HANA Cloud 连接](/zh-cn/guides/connections/s4hana-cloud/)读取和写入 SAP S/4HANA Cloud Public Edition 的工作流步骤。导入步骤拉取试算平衡表或日记账分录行项目数据，无需编写 OData；过账步骤通过 PlaidCloud 共享的 ERP 写入管道过账日记账分录。

## 步骤

- [Import S/4HANA Entity 步骤](/zh-cn/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)：试算平衡表和日记账分录行项目数据，支持服务器端筛选。
- [S/4HANA: Post Journal Entry 步骤](/zh-cn/reference/workflow-steps/s4hana-cloud/s4hana-post/)：通过 SOAP 过账日记账分录，更正时使用已过账的冲销分录。

## 相关内容

- [SAP S/4HANA Cloud REST 连接器](/zh-cn/reference/connectors/rest/s4hana-cloud/)
- [连接到 SAP S/4HANA Cloud](/zh-cn/guides/connections/s4hana-cloud/)
- [查看 ERP 过账历史](/zh-cn/guides/connections/erp-post-history/)
