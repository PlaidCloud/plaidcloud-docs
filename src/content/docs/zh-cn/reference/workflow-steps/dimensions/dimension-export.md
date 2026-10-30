---
title: Dimension Export 步骤
description: 在工作流步骤中导出 PlaidCloud 的维度数据，以将层次结构保存为文件或传输到其他系统。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## 说明

将维度展平为表格形式的 PlaidCloud 表，每个成员一行，列包括父级、级别、值、别名和属性。当您需要查询、联接维度结构，或将其提供给无法直接读取 PlaidCloud 层次格式的下游系统时，可使用此步骤。

常见用法：先将维度导出为表，再使用常规导出步骤将其写入外部系统（BI 工具、报表数据库、文件交付）。

## 导出每个层次结构

选择**所有层次结构**可将每个层次结构放入同一个表中。结果会增加一个 `hierarchy` 列，用于指明每一行所属的层次结构；行的排序为主层次结构在前，其后是按字母顺序排列的备用层次结构。
