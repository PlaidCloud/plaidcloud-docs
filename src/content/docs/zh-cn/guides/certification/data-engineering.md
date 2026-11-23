---
title: 数据工程学习路径
description: 参加 PlaidCloud 数据工程实践者和专家实验之前应阅读的内容，以及每个实验的要求。
sidebar:
  label: 数据工程
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

数据工程赛道关注的是构建正确、由变量驱动且快速的工作流。请先从[基础](/zh-cn/guides/certification/foundations/)学习路径开始。有关实验的运作方式，请参阅 [PlaidCloud 认证](/zh-cn/guides/certification/)。

## 实践者

### 阅读顺序

1. [创建工作流](/zh-cn/guides/workflows/create-workflow/)
2. [工作流步骤](/zh-cn/reference/workflow-steps/)，尤其是 [Table Inner Join 步骤](/zh-cn/reference/workflow-steps/tables/table-inner-join/)和 [Table Extract 步骤](/zh-cn/reference/workflow-steps/tables/table-extract/)
3. [管理工作流变量](/zh-cn/guides/workflows/manage-workflow-variables/)
4. [复用您的成果：变量、宏和 UDF](/zh-cn/get-started/tutorials/reuse-variables-macros-udfs/)
5. [运行工作流](/zh-cn/guides/workflows/run-a-workflow/)
6. [查看工作流日志](/zh-cn/guides/workflows/viewing-workflow-log/)

### 实验要求

该实验名为 *数据工程：月度销售构建*。

加载了三个原始表：销售明细、门店和产品。在实验的工作流中，您需要构建一个月度汇总，针对某个月份中已售出的明细，按区域和产品类别各一行，包含数量和收入。月份来自项目变量，而不是步骤中键入的值：实验会更改该变量并再次运行工作流。只能使用标准步骤，不能使用 SQL 或代码步骤。

实验会检查工作流是否运行、是否只使用标准步骤，以及汇总对于该月份和另一个月份是否都正确。

## 专家

专家实验限时：从开始之时起您有 4 小时。

### 阅读顺序

1. [调试工作流](/zh-cn/get-started/tutorials/debug-a-workflow/)
2. [查看工作流日志](/zh-cn/guides/workflows/viewing-workflow-log/)
3. [管理步骤错误](/zh-cn/guides/workflows/managing-step-errors/)
4. [预览步骤数据](/zh-cn/guides/workflows/preview-step-data/)
5. [优化工作流](/zh-cn/guides/workflows/optimize-a-workflow/)
6. [工作流步骤](/zh-cn/reference/workflow-steps/)，尤其是 [Table Inner Join 步骤](/zh-cn/reference/workflow-steps/tables/table-inner-join/)

### 实验要求

该实验名为 *数据工程专家：修复并加速夜间构建*。

一个夜间工作流已停止运行，而在此之前它就慢得离谱。您需要阅读运行日志，找出所有原因，并修复工作流，使其成功运行、产生正确的汇总，并在远低于原先的时间内完成。没有账户的行需排除在外，重复列出的账户不得使计数虚高。只能使用标准步骤，并保持输入表不变。

实验会检查工作流是否运行、是否只使用标准步骤、汇总是否正确、输入表是否未变，以及工作流是否足够快。
