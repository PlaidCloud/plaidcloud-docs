---
title: func.ST_LineLocatePoint
slug: func-st-linelocatepoint
description: Returns a float between 0 and 1 representing the location of the closest point on LineString to the given Point
date: 2022-01-31T18:03:30
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineLocatePoint(geometry a_linestring, geometry a_point);
```


### PlaidCloud



```python
func.ST_LineLocatePoint(geometry a_linestring, geometry a_point)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineLocatePoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

