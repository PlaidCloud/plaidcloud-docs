---
title: func.ST_GeomFromGeoHash
slug: func-st-geomfromgeohash
description: Return a geometry from a GeoHash string.
date: 2022-01-29T14:56:37
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeomFromGeoHash(text geohash, integer precision=full_precision_of_geohash);
```


### PlaidCloud



```python
func.ST_GeomFromGeoHash(text geohash, integer precision=full_precision_of_geohash)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeomFromGeoHash.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

