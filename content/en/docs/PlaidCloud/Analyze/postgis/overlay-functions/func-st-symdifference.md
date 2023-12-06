---
title: func.ST_SymDifference
slug: func-st-symdifference
description: Returns a geometry representing the portions of geonetries A and B that do not intersect
date: 2022-01-31T10:53:54
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SymDifference(geometry geomA, geometry geomB, float8 gridSize = -1);
```


### PlaidCloud



```python
func.ST_SymDifference(geometry geomA, geometry geomB, float8 gridSize = -1)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SymDifference.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

