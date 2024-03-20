---
title: func.ST_MakeValid
slug: func-st-makevalid
description: The function attempts to create a valid representation of a given invalid geometry without losing any of the input vertices
date: 2022-01-28T13:51:54
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_MakeValid(geometry input);
```


### PlaidCloud



```python
func.ST_MakeValid(geometry input)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_MakeValid.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

