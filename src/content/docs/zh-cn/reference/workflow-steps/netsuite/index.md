---
title: NetSuite 步骤
description: NetSuite 工作流步骤：通过 NetSuite 连接导入余额、总账明细、主数据或您自己的 SuiteQL 查询，并过账日记账分录。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

通过 [NetSuite 连接](/zh-cn/guides/connections/netsuite/)读取和写入 NetSuite 的工作流步骤。预置导入步骤是拉取常用财务数据和参考数据的最简便方式：选择连接、目标表，以及日期范围或记录类型即可，无需编写 SuiteQL。

## 导入步骤

- [NetSuite：导入余额](/zh-cn/reference/workflow-steps/netsuite/import-balances/)：按日期范围和子公司导入科目余额（试算平衡表）。
- [NetSuite：导入总账明细](/zh-cn/reference/workflow-steps/netsuite/import-gl-detail/)：按日期范围和子公司导入总账交易行明细。
- [NetSuite：导入主数据](/zh-cn/reference/workflow-steps/netsuite/import-master-data/)：主列表，包括科目、子公司、部门、类别、位置、供应商或客户。
- [NetSuite:导入 SuiteQL 查询](/zh-cn/reference/workflow-steps/netsuite/import-suiteql-query/)：运行您自己的 SuiteQL 查询并将结果加载到带类型的表中，日期窗口和分页由系统处理。

## 过账步骤

- [Post NetSuite Journal Entry 步骤](/zh-cn/reference/workflow-steps/netsuite/post-netsuite-journal-entry/)：将表头/表行结构的日记账分录过账回 NetSuite。

## 自定义拉取

对于预置导入步骤未涵盖的数据（定制查询，或没有预置步骤的 NetSuite 记录），请使用 [NetSuite:导入 SuiteQL 查询](/zh-cn/reference/workflow-steps/netsuite/import-suiteql-query/)并编写您自己的 SuiteQL。可参阅 [NetSuite SuiteQL 查询示例](/zh-cn/guides/connections/netsuite-financial-queries/)作为起点。

## 相关内容

- [NetSuite REST 连接器](/zh-cn/reference/connectors/rest/netsuite/)
- [连接到 NetSuite](/zh-cn/guides/connections/netsuite/)
- [导入 NetSuite 财务数据](/zh-cn/guides/connections/import-netsuite-financials/)
