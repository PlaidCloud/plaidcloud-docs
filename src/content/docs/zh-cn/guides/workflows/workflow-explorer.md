---
title: 工作流探索器
description: 使用 PlaidCloud 工作流探索器查看工作流详情、步骤配置、执行历史和依赖关系信息。
sidebar:
  order: 1.1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/workflow-explorer.md
---

要查看工作流中的详细信息，请在项目中找到它，然后双击将其在探索器中打开。

![工作流探索器](/images/workflow_explorer.png)

在这里可以管理工作流步骤，包括创建或修改现有的工作流步骤、更改顺序、执行步骤等。

## 创建步骤

单击**创建步骤**并选择步骤类型。如果列表中选中了一个步骤，则新的 Table Extract、Table Inner Join、Table Outer Join、Table Anti Join、Table Cross Join 或 Table Lookup 步骤会以该步骤所写入的表为起点：该表成为新步骤的源（联接步骤中为 **Table 1**），并且各列会按照**检查源**的方式自动填充。表单底部的说明会提示这一点。如果新步骤应读取其他内容，请更改源。在您保存该步骤之前不会保存任何内容。
