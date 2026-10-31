---
title: Set Workflow Variable Values from Table 步骤
description: 从项目表中读取值并赋给工作流变量，使后续步骤依据数据而非硬编码的值进行分支或筛选。
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## 说明

从项目表中读取值，并将其赋给工作流变量。可用它让工作流由自身的数据驱动——从控制表中读取最近的已结账期间、行数或文件路径，供下游步骤引用。

此处设置的变量在整个工作流运行期间有效。若要设置在项目内各工作流之间保持的值，请使用 [Set Project Variable Values from Table 步骤](/zh-cn/reference/workflow-steps/workflow-control/set-project-variable-from-table/)。

## 配置

### 源列

将每个源列映射到它所填充的工作流变量。该步骤只读取一行，因此请在运行之前将表缩小到一行。

### 选择数据子集

用于缩小源行范围的筛选表达式——通常缩小到保存所需值的那一行。

### 对结果数据应用二级筛选器

在聚合之后应用的 `HAVING` 式筛选器，适用于值来自分组计算的情况。

### Final Data Table Slicing (Limit)

默认关闭，开启时限制为一行。当源可能返回多个候选行、而您需要其中特定的一行时，请在开启它的同时指定明确的排序。

## 相关内容

- [工作流控制步骤](/zh-cn/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable 步骤](/zh-cn/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table 步骤](/zh-cn/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)
