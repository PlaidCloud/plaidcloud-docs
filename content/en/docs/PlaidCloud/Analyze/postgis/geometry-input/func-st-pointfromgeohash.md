---
title: func.ST_PointFromGeoHash
slug: func-st-pointfromgeohash
description: Return a point from a GeoHash string
date: 2022-01-29T15:13:09
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_PointFromGeoHash(text geohash, integer precision=full_precision_of_geohash);
```


### PlaidCloud



```python
func.ST_PointFromGeoHash(text geohash, integer precision=full_precision_of_geohash)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_PointFromGeoHash.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

