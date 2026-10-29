---
title: 数据管理：表格数据
description: 使用表、视图和高性能 Lakehouse 引擎在 PlaidCloud 中管理表格数据，可处理任意规模的数据。
sidebar:
  label: 概览
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

PlaidCloud 的数据层围绕**表**（结构化的行列数据）和**视图**（基于表保存的查询）构建。二者都位于项目内，并由 Lakehouse 引擎提供支持，无需更改配置，即可从小型参考表扩展到十亿行级别的分析数据集。

## 本节内容

- [表和视图](/zh-cn/guides/data/tables-views/)：二者各是什么、何时使用哪一个，以及它们如何交互
- [表资源管理器](/zh-cn/guides/data/table-explorer/)：浏览和检查项目中的表
- [货币数据类型](/zh-cn/guides/data/currency-data-type/)：用于金额值的精确半角列类型，以及何时应选择它而不是 Numeric
- [向量数据类型](/zh-cn/guides/data/vector-data-type/)：在项目表中存储预先计算的嵌入向量，声明预期的宽度，并搜索最近的行
- [表快照](/zh-cn/guides/data/table-snapshots/)：浏览快照历史记录，查看过去某个快照时的数据，以及回退或还原表
- [发布数据](/zh-cn/guides/data/publish/)：让项目表可供仪表板、BI 工具和下游系统使用，并查看其性能指南
- [在大型历史表中选择最新记录](/zh-cn/guides/data/selecting-latest-record-in-large-history-table/)：一种常见模式，附带兼顾性能的解决方案
- [地理编码 API](/zh-cn/guides/data/geocoding-api/)：将 Google 或 Mapbox 地理编码集成迁移到 PlaidCloud 的 REST 地理编码端点
- [行车时间路由 API](/zh-cn/guides/data/drive-time-routing-api/)：需主动启用的预览功能，通过 REST 提供行车时间等时圈和按行车时间排序的最近邻

## 数据来源

表通常由**工作流**填充，工作流是自动化的管道，用于导入数据、转换数据并将结果写回。有关如何构建工作流，请参阅[工作流](/zh-cn/guides/workflows/)；有关可用的每种步骤类型，请参阅[工作流步骤参考](/zh-cn/reference/workflow-steps/)。

有关将外部系统连接为数据源，请参阅[连接（指南）](/zh-cn/guides/connections/)和[连接器（参考）](/zh-cn/reference/connectors/)。

## 相关内容

- [概念](/zh-cn/get-started/concepts/)：表与工作流、维度以及更广泛的数据模型之间的关系
- [项目](/zh-cn/guides/projects/)：项目拥有表，表不能脱离项目而存在
- [仪表板](/zh-cn/guides/dashboards/)：使用已发布的表进行可视化
