---
title: func.ST_Polygonize
slug: func-st-polygonize
description: Creates a GeometryCollection containing the polygons formed by the constituent linework of a set of geometries
date: 2022-01-31T11:10:06
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Polygonize(geometry set geomfield);
```


### PlaidCloud



```python
func.ST_Polygonize(geometry set geomfield)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Polygonize.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

