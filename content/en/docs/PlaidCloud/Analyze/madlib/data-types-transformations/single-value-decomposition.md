---
title: Single Value Decomposition
slug: single-value-decomposition
weight: 9.0
description: Factorization of a real or complex matrix, with many useful applications in signal processing and statistics
date: 2022-01-25T07:40:19
---


PlaidCloud expressions and filters provide use of most non-administrative Apache MADLib methods. Apache MADLib methods are accessed by prefixing the standard method name with `func.madlib.`.



## In SQL



```sql
madlib.matrix_sparsify('mat', 'row=row_id, val=row_vec', 'mat_sparse', 'row=row_id, col=col_id, val=value');
```


## In PlaidCloud Expressions & Filters



```python
func.madlib.matrix_sparsify('mat', 'row=row_id, val=row_vec', 'mat_sparse', 'row=row_id, col=col_id, val=value')
```


## External References


Apache MADLib Official Documentation for these methods can be found [here](https://madlib.apache.org/docs/latest/group__grp__svd.html).



Additional capabilities and usage examples can be found in the Apache MADLib documentation.

