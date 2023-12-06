---
title: func.ST_ConcaveHull
slug: func-st-concavehull
description: The concave hull of a geometry represents a possibly concave geometry that encloses the input geometry
date: 2022-01-31T11:01:44
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_ConcaveHull(geometry geom, float target_percent, boolean allow_holes = false);
```


### PlaidCloud



```python
func.ST_ConcaveHull(geometry geom, float target_percent, boolean allow_holes = false)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_ConcaveHull.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

