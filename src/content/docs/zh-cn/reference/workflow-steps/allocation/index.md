---
title: 分摊步骤
description: 跨维度分摊值的工作流步骤：拆分、规则和基于规则的标记，用于成本分摊、费用回收和转移定价。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/allocation/index.md
---

用于成本分摊、费用回收、转移定价以及类似值分配问题的工作流步骤。每个步骤都使用驱动因素数据和某种方法，将值从一组源行分摊到一组目标行。

## 步骤

- [Allocation Rules 步骤](/zh-cn/reference/workflow-steps/allocation/allocation-rules/)：定义并应用带有明确条件的分摊规则。
- [Allocation Split 步骤](/zh-cn/reference/workflow-steps/allocation/allocation-split/)：使用驱动因素表将源值拆分到多个目标。
- [基于规则的标记](/zh-cn/reference/workflow-steps/allocation/rule-based-tagging/)：在分摊之前，用维度中的属性标记行。

## 相关内容

- [分摊（指南）](/zh-cn/guides/allocations/)：分摊问题的概念和端到端工作流。
- [维度（指南）](/zh-cn/guides/dimensions/)：设置分摊用来分配值的层次结构。
