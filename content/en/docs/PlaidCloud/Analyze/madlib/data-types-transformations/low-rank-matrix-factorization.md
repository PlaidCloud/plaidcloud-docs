---
title: Low-Rank Matrix Factorization
slug: low-rank-matrix-factorization
weight: 3.0
description: Represent an incomplete matrix using a low-rank approximation
date: 2022-01-25T07:40:19
---


PlaidCloud expressions and filters provide use of most non-administrative Apache MADLib methods. Apache MADLib methods are accessed by prefixing the standard method name with `func.madlib.`.



## In SQL



```sql
madlib.lmf_igd_run('lmf_model', 'lmf_data', 'row', 'col', 'val', 999, 10000, 3, 0.1, 2, 10, 1e-9);
```


## In PlaidCloud Expressions & Filters



```python
func.madlib.lmf_igd_run('lmf_model', 'lmf_data', 'row', 'col', 'val', 999, 10000, 3, 0.1, 2, 10, 1e-9)
```


## External References


Apache MADLib Official Documentation for these methods can be found [here](https://madlib.apache.org/docs/latest/group__grp__lmf.html).



Additional capabilities and usage examples can be found in the Apache MADLib documentation.

