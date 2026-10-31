---
title: IBM TM1 / Planning Analytics 步骤
description: 通过 TM1 连接从 IBM TM1 / Planning Analytics 服务器读取数据的工作流步骤——按已保存视图或 MDX 读取多维数据集数据，以及读取维度层次结构——可云端直连，也可通过本地 PlaidLink 代理。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

通过 [TM1 连接](/zh-cn/guides/connections/tm1/)从 IBM **TM1 / Planning Analytics** 读取数据的工作流步骤：按已保存视图或 MDX 读取多维数据集数据（可选视点切片），以及将维度层次结构加载到 PlaidCloud 维度中。可云端直连 TM1；如果服务器只能从您自己的网络内部访问，则通过本地 PlaidLink 代理。

## 步骤

- [TM1：查询多维数据集](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query/)——按已保存视图或 MDX 读取多维数据集，带视点切片和保存前预览。云端直连。
- [TM1：查询多维数据集（代理）](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/)——TM1：查询多维数据集的本地对应版本，通过已安装的 PlaidLink 代理调度。
- [TM1：读取维度](/zh-cn/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/)——将 TM1 层次结构加载到 PlaidCloud 维度中。云端直连。

## 相关内容

- [连接到 TM1（指南）](/zh-cn/guides/connections/tm1/)
- [TM1 连接器](/zh-cn/reference/connectors/rest/tm1/)
