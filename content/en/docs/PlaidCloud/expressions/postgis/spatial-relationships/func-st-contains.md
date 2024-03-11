---
title: func.ST_Contains
slug: func-st-contains
description: Geo 'A' contains Geo 'B' ONLY IF no points of B lie in the exterior of A, and at least one point of B interior lies in A interior
date: 2022-01-31T09:36:14
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Contains(geometry geomA, geometry geomB);
```


### PlaidCloud



```python
func.ST_Contains(geometry geomA, geometry geomB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Contains.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

