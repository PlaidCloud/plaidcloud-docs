---
title: 引发工作流错误
description: 在 PlaidCloud 工作流步骤中引发自定义错误，以在条件不满足时触发错误处理并中止执行。
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## 说明

使工作流进入错误状态，并附带自定义消息。当某个步骤需要根据前面步骤检测到的数据条件使工作流失败时，请使用它，例如“行数为零则失败”“关键验证表中存在未映射的值则失败”或“余额检查未对平则失败”。

请与[步骤条件](/zh-cn/guides/workflows/step-conditions/)搭配使用，使错误仅在确实出现问题时触发。该步骤运行时会立即停止工作流，并将错误写入工作流日志；如果配置了补救工作流，日志中的错误还可触发该工作流。


## 引发工作流错误


主要与步骤条件配合使用：可将该步骤设置为在条件满足时执行，并在工作流中引发错误
