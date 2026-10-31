---
title: Dimension Sort 步骤
description: 在 PlaidCloud 工作流步骤中自动对维度成员排序，以保持层次结构内的顺序一致。
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## 说明

对维度中各父级之下的成员排序：按字母顺序、按值、按属性或按自定义顺序列。这样无需手动拖动层次结构成员来调整顺序，在批量加载或大幅调整结构之后尤其有用。

此步骤直接对维度就地操作，无需源表或目标表。


## 维度选择
### 动态指定维度
如果**维度**或**路径**是动态创建的，则可以使用相同的变量来对它们排序。在排序过程中使用变量很有用，因为这样无需定期手动更新 Dimension Sort 步骤。



下面的示例使用 `current_month` 变量动态对 Materials 维度排序：

```text
/Dimensions/{current_month}/Products/Materials
```

### 使用特定维度

使用下拉菜单选择要排序的特定维度。
