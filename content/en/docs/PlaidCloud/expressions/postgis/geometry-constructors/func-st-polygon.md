---
title: func.ST_Polygon
slug: func-st-polygon
description: Returns a polygon built from the given LineString and sets the spatial reference system from the SRID
date: 2022-01-25T07:40:07
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Polygon(geometry lineString, integer srid);
```


### PlaidCloud



```python
func.ST_Polygon(geometry lineString, integer srid)
```


### External References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Polygon.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

