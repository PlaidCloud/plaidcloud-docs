---
title: Matrix Operations
slug: matrix-operations
weight: 4.0
description: Provides basic matrix operations for matrices that are too big to fit in memory
date: 2022-01-25T07:40:19
---


PlaidCloud expressions and filters provide use of most non-administrative Apache MADLib methods. Apache MADLib methods are accessed by prefixing the standard method name with `func.madlib.`.



## In SQL



```sql
madlib.matrix_trans('"mat_B"', 'row=row_id, val=vector', 'mat_r');
```


## In PlaidCloud Expressions & Filters



```python
func.madlib.matrix_trans('"mat_B"', 'row=row_id, val=vector', 'mat_r')
```


## External References


Apache MADLib Official Documentation for these methods can be found [here](https://madlib.apache.org/docs/latest/group__grp__matrix.html).



Additional capabilities and usage examples can be found in the Apache MADLib documentation.

