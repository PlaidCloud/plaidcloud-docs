---
title: func.ST_Snap
slug: func-st-snap
description: Snaps the vertices and segments of a geometry to another Geometry's vertices
date: 2022-01-28T13:46:05
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Snap(geometry input, geometry reference, float tolerance);
```


### PlaidCloud



```python
func.ST_Snap(geometry input, geometry reference, float tolerance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Snap.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

