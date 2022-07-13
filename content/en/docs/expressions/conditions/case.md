---
title: case
slug: case
description: Checks if conditions are met
date: 2022-01-25T07:39:53
---


## Syntax



```
case((condition1, value1),(condition2, value2), else_ = None)
```


## Example 1



```
In this example is from a Table:Lookup step where we are updating the "dock_final" column when the table1. dock_final value is Null.

case(
    (table1.dock_final == Null, table2.dock_final), else_ = table1.dock_final
    )
```


## Example 2


```
This example is from a Table:Lookup step where we are updating the "Marketing Channel" column when "Marketing Channel" in table1 is not 'none' or the "Serial Number" contains a '_'.

case(
    (get_column(table1, 'Marketing Channel') != 'none', get_column(table1, 'Marketing Channel')),
    (get_column(table1, 'Serial Number').contains('_'), get_column(table1, 'Marketing Channel')),
    (get_column(table2, 'Marketing Channel') != Null, get_column(table2, 'Marketing Channel')), 
    else_ = 'none'
    )

```