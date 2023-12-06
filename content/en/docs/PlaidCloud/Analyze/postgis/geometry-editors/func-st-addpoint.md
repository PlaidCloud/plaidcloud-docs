---
title: func.ST_AddPoint
slug: func-st-addpoint
description: Adds a point to a LineString before point <position> (0-based index)
date: 2022-01-28T13:14:09
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_AddPoint(geometry linestring, geometry point);
```


### PlaidCloud



```python
func.ST_AddPoint(geometry linestring, geometry point)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_AddPoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

