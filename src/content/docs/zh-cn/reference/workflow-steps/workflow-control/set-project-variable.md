---
title: Set Project Variable 步骤
description: 在 PlaidCloud 工作流步骤中设置项目级变量，用于存储可供项目内所有工作流访问的值。
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable.md
---

## 说明


“Set Project Variable”用于设置在工作流中使用的项目变量。变量名称和值可以包含任意有效字符的组合，包括空格。在工作流中引用变量时，需将其放在花括号内。例如，*a_variable* 在转换中引用为 *\{a_variable}*，因此可用于公式或字段值等场景（例如 \{a_variable} * 2）。



## 变量列表


该表列出了项目中注册的每个变量，以及各自的**当前值**和**备注**，每次打开该步骤时都会重新读取——因此在决定设置什么值之前，可以先看到变量当前保存的内容。

要设置某个变量，请勾选其所在行的**设置**，并在**设置值**下输入新值。运行该步骤时只会写入已勾选的行，因此未勾选**设置**而输入的值会被忽略。也可以设置尚未注册的变量：添加一行并以同样方式设置——运行该步骤时会创建该变量。







## 示例


暂无示例……
