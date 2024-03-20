---
title: func.ST_RemovePoint
slug: func-st-removepoint
description: Remove a point from a linestring, given its 0-based index
date: 2022-01-28T13:36:48
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_RemovePoint(geometry linestring, integer offset);
```


### PlaidCloud



```python
func.ST_RemovePoint(geometry linestring, integer offset)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_RemovePoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

