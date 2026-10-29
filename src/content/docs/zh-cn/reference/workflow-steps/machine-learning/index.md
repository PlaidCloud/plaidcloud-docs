---
title: 机器学习
description: 训练 scikit-learn 模型并用其对表进行评分的工作流步骤。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/machine-learning/index.md
---

在任意表上训练模型，将其作为模型表在工作流中传递，并用它对数据表进行评分。

## 步骤

- [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/)——在源表上拟合 scikit-learn 模型（分类或回归），并写出可查询的模型表，其中包含拟合后的模型、参数、特征列表和训练指标。
- [ML：评分](/zh-cn/reference/workflow-steps/machine-learning/ml-score/)——使用训练好的模型表对数据表进行评分，并追加一个预测列。

有关 Alteryx 辅助建模管道如何转换为这些步骤，请参阅[迁移 Alteryx 工作流](/zh-cn/guides/workflows/migrate-alteryx-workflows/#机器学习辅助建模转换)。
