---
title: Pivot
slug: pivot
weight: 7.0
description: Perform basic OLAP type operations on data
date: 2022-01-25T07:40:19
---


PlaidCloud expressions and filters provide use of most non-administrative Apache MADLib methods. Apache MADLib methods are accessed by prefixing the standard method name with `func.madlib.`.



## In SQL



```sql
madlib.pivot('pivset_ext', 'pivout', 'id', 'piv', 'val', 'sum');
```


## In PlaidCloud Expressions & Filters



```python
func.madlib.pivot('pivset_ext', 'pivout', 'id', 'piv', 'val', 'sum')
```


## External References


Apache MADLib Official Documentation for this method can be found [here](https://madlib.apache.org/docs/latest/group__grp__pivot.html).



Additional capabilities and usage examples can be found in the Apache MADLib documentation.

