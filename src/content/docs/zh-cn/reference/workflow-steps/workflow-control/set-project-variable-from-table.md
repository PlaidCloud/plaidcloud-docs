---
title: Set Project Variable Values from Table 步骤
description: 从项目表中读取值并赋给项目变量，这些变量会在多次工作流运行之间保持。
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## 说明

从项目表中读取值，并将其赋给*项目*变量。与 [Set Workflow Variable Values from Table 步骤](/zh-cn/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)不同，这些值在运行结束后依然保留——项目中的每个工作流都能看到它们，直到有操作再次修改。

可用它保存比单次运行存活更久的状态：最近一次成功加载的期间、水位线时间戳或当前方案名称。

## 配置

### 源列

将每个源列映射到它所填充的项目变量。该步骤只读取一行，因此请在运行之前将表缩小到一行。

### 选择数据子集

用于缩小源行范围的筛选表达式。

### 对结果数据应用二级筛选器

在聚合之后应用的 `HAVING` 式筛选器。

### Final Data Table Slicing (Limit)

默认关闭，开启时限制为一行。当源可能返回多个候选行时，请在开启它的同时指定明确的排序。

## 相关内容

- [工作流控制步骤](/zh-cn/reference/workflow-steps/workflow-control/)
- [Set Project Variable 步骤](/zh-cn/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table 步骤](/zh-cn/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
