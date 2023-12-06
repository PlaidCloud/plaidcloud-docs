---
title: func.ST_GeoHash
slug: func-st-geohash
description: Return a GeoHash representation (http://en.wikipedia.org/wiki/Geohash) of the geometry
date: 2022-01-29T19:22:58
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeoHash(geometry geom, integer maxchars=full_precision_of_point);
```


### PlaidCloud



```python
func.ST_GeoHash(geometry geom, integer maxchars=full_precision_of_point)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeoHash.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

