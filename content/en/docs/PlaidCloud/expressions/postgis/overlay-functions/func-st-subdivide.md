---
title: func.ST_Subdivide
slug: func-st-subdivide
description: Divides geometry into parts using rectilinear lines, until each part can be represented using no more than max_vertices
date: 2022-01-31T10:53:12
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Subdivide(geometry geom, integer max_vertices=256, float8 gridSize = -1);
```


### PlaidCloud



```python
func.ST_Subdivide(geometry geom, integer max_vertices=256, float8 gridSize = -1)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Subdivide.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

