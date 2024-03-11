---
title: func.ST_Difference
slug: func-st-difference
description: Returns a geometry representing the part of geometry A that does not intersect geometry B
date: 2022-01-31T10:46:57
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Difference(geometry geomA, geometry geomB, float8 gridSize = -1);
```


### PlaidCloud



```python
func.ST_Difference(geometry geomA, geometry geomB, float8 gridSize = -1)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Difference.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

