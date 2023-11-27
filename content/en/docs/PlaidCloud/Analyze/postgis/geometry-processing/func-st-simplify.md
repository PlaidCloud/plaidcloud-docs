---
title: func.ST_Simplify
slug: func-st-simplify
description: Returns a "simplified" version of the given geometry using the Douglas-Peucker algorithm
date: 2022-01-31T11:12:28
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Simplify(geometry geomA, float tolerance, boolean preserveCollapsed);
```


### PlaidCloud



```python
func.ST_Simplify(geometry geomA, float tolerance, boolean preserveCollapsed)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Simplify.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

