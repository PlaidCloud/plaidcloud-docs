---
title: 用于表达式和聚合的维度函数
description: 在 PlaidCloud 维度中使用函数表达式来定义计算值、条件逻辑和动态成员属性。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## 用于维度层次结构表达式的函数

在“维度层次结构”屏幕中，可以添加“聚合”和“表达式”。下文对它们作了说明。

## 聚合
聚合用于显示来自表的聚合值（可以是“Sum”、“Count”、“Min”或“Max”）。
下图显示了一个聚合，它被配置为从“Line Item Values”表中提取值，以便为层次结构中的每个“Period”显示值。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_1_agg.png)

聚合可以设置筛选器，使得只显示与筛选器匹配的项。在下图中，我们将聚合设置为显示“Account”维度中某个选定项的值。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_2_agg.png)

如果这些筛选器留空，则可以使用屏幕顶部的维度筛选栏来筛选数据，如下图所示：

![Dimension Load](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## 表达式

使用表达式，可以显示根据为维度显示的聚合值计算得出的值。
表达式使用数学公式构建，其中可以包含多种运算符和一些特殊函数。请参阅[运算符列表](https://mathjs.org/docs/expressions/syntax.html)。可用的函数说明如下


## 函数
### Column(`<column_name>`)
获取当前行/节点中指定名称的列的值。

下面是一个表达式的示例，其定义为显示行项目值乘以 2 的结果。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Dimension Load](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

返回当前行/节点的子级数量。如果当前行/节点是叶子项，则返回 0。

在下面的示例中，它用于返回某个父节点的子节点的平均值。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
返回在树中为当前行/节点找到的叶子项数量。如果当前行/节点是叶子项，则返回 1。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
返回在树中为当前行/节点找到的项的总数。如果当前行/节点是叶子项，则返回 0。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
返回当前行/节点的同级项数量。返回的值包括当前节点。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
返回指定节点中指定名称的列的值。
下面的示例用于显示每个行/节点占“LIV”总计的百分比。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
返回当前节点的父级在给定列中的值。
此示例显示子节点所占用的父节点值的百分比。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

返回一个数值结果，表示指定列中的文本大于、小于还是等于所提供的值。

如果列中的文本等于所提供的文本，则此函数返回 0。

如果列中的文本小于所提供的文本，则此函数返回 -1。

如果列中的文本大于所提供的文本，则此函数返回 0。


下面的示例将 Period 的名称与“Jun”进行比较


![Dimension Load](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## 条件表达式
上面显示的示例相当简单。在表达式中使用条件，可以创建更复杂的表达式。
在表达式中，条件采用以下形式：
`<condition>` ? `<value_if_true>` : `<value_if_false>`
例如 '12 > 6 ? 1000: 0'

通过组合同时包含条件和函数的表达式，可以构建更复杂的表达式，例如下面的示例：如果月份为“Jun”，则在行项目值上加 100,000

![Dimension Load](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## 另一个示例：简单分摊

此示例显示通过使用叶子节点的资源动因值，所消耗的父级行项目值的数额。

![Dimension Load](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## 限制：
目前无法构建基于其他表达式的值的表达式。表达式只能使用聚合的值来构建。
