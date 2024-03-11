---
title: func.ST_DumpPoints
slug: func-st-dumppoints
description: This set-returning function (SRF) returns a set of geometry_dump rows formed by a geometry (geom) and an array of integers (path)
date: 2022-01-27T13:46:28
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_DumpPoints(geometry geom);
```


### PlaidCloud



```python
func.ST_DumpPoints(geometry geom)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_DumpPoints.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

