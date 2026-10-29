---
title: 运行工作流中的一组步骤
description: 运行 PlaidCloud 工作流中指定范围的步骤，有选择地执行数据处理管道的一部分。
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

运行单个步骤很有用，但在开发、测试或故障排查时，运行整个工作流的一部分同样有用。要运行一部分步骤，请选择所有要运行的步骤，然后在工作流步骤层次结构顶部的**操作**菜单中选择**运行所选步骤**。这会触发正常的工作流处理，但从所选步骤的开头开始，并在最后一个所选步骤完成后停止。

如果最后一个所选步骤位于设置为[**并行执行**](/zh-cn/guides/workflows/controlling-parallel-execution/)的分组内，运行还会等待该分组中其他所有所选步骤完成后才停止。
