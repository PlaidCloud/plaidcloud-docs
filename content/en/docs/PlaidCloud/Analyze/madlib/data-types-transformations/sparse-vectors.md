---
title: Sparse Vectors
slug: sparse-vectors
weight: 10.0
description: Provides compressed storage of vectors that have many duplicate elements
date: 2022-01-25T07:40:19
---


PlaidCloud expressions and filters provide use of most non-administrative Apache MADLib methods. Apache MADLib methods are accessed by prefixing the standard method name with `func.madlib.`.



## In SQL



```sql
madlib.gen_doc_svecs('svec_output', 'dictionary_table', 'id', 'term', 'documents_table', 'id', 'term', 'count');
```


## In PlaidCloud Expressions & Filters



```python
func.madlib.gen_doc_svecs('svec_output', 'dictionary_table', 'id', 'term', 'documents_table', 'id', 'term', 'count')
```


## External References


Apache MADLib Official Documentation for these methods can be found [here](https://madlib.apache.org/docs/latest/group__grp__svec.html).



Additional capabilities and usage examples can be found in the Apache MADLib documentation.

