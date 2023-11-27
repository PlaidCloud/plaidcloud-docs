---
title: func.ST_IsValidReason
slug: func-st-isvalidreason
description: Returns text stating if a geometry is valid or not an if not valid, a reason why
date: 2022-01-28T13:51:10
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_IsValidReason(geometry geomA, integer flags);
```


### PlaidCloud



```python
func.ST_IsValidReason(geometry geomA, integer flags)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_IsValidReason.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

