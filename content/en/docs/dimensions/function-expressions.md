---
title: Dimension Functions for Expressions and Aggregations
slug: dimension_expressions
description: Within the Dimension Hierarchy screen it is possible to add 'Aggregations' and 'Expressions'
date: 2022-01-25T07:39:48
weight: 3.0
---

## Functions for use in Dimension Hierarchy Expressions

Within the Dimension Hierarchy screen it is possible to add 'Aggregations' and 'Expressions'. A description for these is included below.

## Aggregations
An Aggregation is used to display an aggregated value from a table (which can be 'Sum', 'Count', 'Min' or 'Max')
The following image shows an Aggregation that has been configured to pull values from a 'Line Item Values' table so that values can be displayed for each 'Period' in the hierarchy.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_1_agg.png)

Aggregations can be filtered so that only items matching the filter are displayed. In the following image we have set up the aggregation to show values for a selected item in the 'Account' dimension.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_2_agg.png)

If these filters are left blank then the data can be filtered by using the dimension filter bar at the top of the screen, as can be seen in the following image:

![Dimension Load](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Expressions

Using Expressions it is possible to display values which are calculated based on values from Aggregations displayed for the dimension.
Expressions are built using mathematical formulae, which can contain many kinds of operators, and some special functions.  The list of operators available can be found [here](https://mathjs.org/docs/expressions/syntax.html). The functions available are described below


## Functions
### column(<column_name>)
Fetch a value from a named column for the current row/node.

Below we see an example of an Expression being defined to display the result of multiplying the Line Item Value by 2.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Dimension Load](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### childCount()

Returns the number of children for the current row/node. If the current row/node is a leaf item this will return 0.

In the following example this is being used to return the average value for the child nodes of a parent node.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### leafCount()
Returns the number of leaf items found in the tree for the current row/node. If the current row/node is a leaf item this will return 1.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### descendantCount()
Returns the total number of items found in the tree for the current row/node. If the current row/node is a leaf item this will return 0.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### siblingCount()
Returns the number of sibling items for the current row/node.  The value returned includes the current node.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### nodeValue("<node_name>","<column_name>")
Returns the value from a named column for a named node.
Here's an example which is used to show the percentage of the "LIV" total for each row/node.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### parentValue("<column_name")
Returns the value from a given column for the parent of the current node.
This example shows the percentage of the value from a parent node being used by a child node.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### columnTextCompare("<column_name", "<text>")

Returns a numerical result representing if the text in a named column is greater than, less to, or equal to a provided value.

If the text from the column equals the provided text then this function returns 0.

If the text from the column is less than the provided text then this function returns -1.

If the text from the column is greater than the provided text then this function returns 0.


The following example compares the name of the Period to "Jun"


![Dimension Load](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Conditional Expressions
The examples shown above are fairly simplistic. By using conditionals within expressions it is possible to create more complex expressions.
Within Expressions conditionals take the following form:
<condition> ? <value_if_true> : <value_if_false>
e.g '12 > 6 ? 1000: 0'

By combining expressions containing both conditionals and functions we can build more complex expressions, such as this example where 100,000 is added to a Line Item Value if the month is "Jun"

![Dimension Load](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Another example: Simple Allocation

This example shows the amount of a parent's Line Item Value consumed by using the Resource Driver Value for a leaf node.

![Dimension Load](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Dimension Load](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Limitations:
It is currently not possible to build Expressions which are based on values from other Expressions. Expressions can only be built using values from Aggregations.
