---
title: func.ST_RemoveRepeatedPoints
slug: func-st-removerepeatedpoints
description: Returns a version of the given geometry with duplicated points removed
date: 2022-01-28T13:38:43
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_RemoveRepeatedPoints(geometry geom, float8 tolerance);
```


### PlaidCloud



```python
func.ST_RemoveRepeatedPoints(geometry geom, float8 tolerance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_RemoveRepeatedPoints.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

