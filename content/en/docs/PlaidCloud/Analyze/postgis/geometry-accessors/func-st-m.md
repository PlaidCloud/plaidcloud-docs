---
title: func.ST_M
slug: func-st-m
description: Return the M coordinate of a Point, or NULL if not available. Input must be a Point
date: 2022-01-27T14:21:15
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_M(geometry a_point);
```


### PlaidCloud



```python
func.ST_M(geometry a_point)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_M.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

