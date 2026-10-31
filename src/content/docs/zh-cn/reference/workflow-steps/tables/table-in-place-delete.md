---
title: Table In-Place Delete 步骤
description: 在 PlaidCloud 工作流步骤中使用筛选条件从表中删除特定行，就地移除目标记录。
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-in-place-delete.md
---

## 说明


使用指定的筛选条件对表执行删除。该操作直接在指定的表上执行，因此不会创建额外的表。只会删除满足筛选条件的行。当遇到与数据量有关的问题时，这可能是一种有效的方法。



## 删除参数


从下拉列表中选择要删除数据的 **源** 表。此列表包含所有*项目*和*工作流*数据表。

![Table In-Place Delete](/images/table_inplace_table_selection.png)

## 删除的数据筛选器

![Table In-Place Delete](/images/table_in-place_table_filter.png)




## 示例
