---
title: func.ST_Azimuth
slug: func-st-azimuth
description: Returns the azimuth in radians of the segment defined by the given point geometries, or NULL if the two points are coincident
date: 2022-01-31T10:15:19
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Azimuth(geometry pointA, geometry pointB);
```


### PlaidCloud



```python
func.ST_Azimuth(geometry pointA, geometry pointB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Azimuth.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

