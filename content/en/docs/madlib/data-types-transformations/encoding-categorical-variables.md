---
title: Encoding Categorical Variables
slug: encoding-categorical-variables
weight: 2.0
description: Coding categorical variables into one-hot, dummy, effects, orthogonal, and Helmert
date: 2022-01-25T07:40:19
---


PlaidCloud expressions and filters provide use of most non-administrative Apache MADLib methods. Apache MADLib methods are accessed by prefixing the standard method name with `func.madlib.`.



## In SQL



```sql
madlib.encode_categorical_variables ('abalone', 'abalone_out', 'height::TEXT');
```


## In PlaidCloud Expressions & Filters



```python
func.madlib.encode_categorical_variables ('abalone', 'abalone_out', 'height::TEXT')
```


## External References


Apache MADLib Official Documentation for these methods can be found [here](https://madlib.apache.org/docs/latest/group__grp__encode__categorical.html).



Additional capabilities and usage examples can be found in the Apache MADLib documentation.

