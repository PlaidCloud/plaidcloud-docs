---
title: func.ST_DelaunayTriangles
slug: func-st-delaunaytriangles
description: Return the Delaunay triangulation of the vertices of the input geometry
date: 2022-01-31T11:04:51
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_DelaunayTriangles(geometry g1, float tolerance, int4 flags);
```


### PlaidCloud



```python
func.ST_DelaunayTriangles(geometry g1, float tolerance, int4 flags)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_DelaunayTriangles.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

