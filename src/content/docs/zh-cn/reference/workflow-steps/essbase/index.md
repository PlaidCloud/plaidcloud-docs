---
title: Oracle Essbase 步骤
description: 通过您的 Essbase 连接从 Oracle Essbase 多维数据集读取数据的工作流步骤 — 实时 MDX 查询，以及加载到 PlaidCloud 维度中的维度大纲 — 云直连。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

通过您的 [Oracle Essbase 连接](/zh-cn/guides/connections/essbase/)从 Oracle **Essbase** 读取数据的工作流步骤：通过实时 MDX 查询获取多维数据集数据，以及将维度大纲加载到 PlaidCloud 维度。Essbase 通过其 REST API 以**云直连**方式访问 — 这些步骤没有本地代理路径。

## 步骤

- [Essbase：查询多维数据集](/zh-cn/reference/workflow-steps/essbase/essbase-query/) — 对多维数据集运行实时 MDX 查询，并将结果网格写入为表。云直连。
- [Essbase：读取维度](/zh-cn/reference/workflow-steps/essbase/essbase-dimension-read/) — 将 Essbase 维度大纲加载到 PlaidCloud 维度。云直连。

## 相关内容

- [连接到 Oracle Essbase（指南）](/zh-cn/guides/connections/essbase/)
- [Oracle Essbase 连接器](/zh-cn/reference/connectors/erp/oracle-essbase/)
