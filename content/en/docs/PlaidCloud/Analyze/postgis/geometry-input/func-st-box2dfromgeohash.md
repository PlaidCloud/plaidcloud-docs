---
title: func.ST_Box2dFromGeoHash
slug: func-st-box2dfromgeohash
description: Return a BOX2D from a GeoHash string
date: 2022-01-29T14:55:44
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Box2dFromGeoHash(text geohash, integer precision=full_precision_of_geohash);
```


### PlaidCloud



```python
func.ST_Box2dFromGeoHash(text geohash, integer precision=full_precision_of_geohash)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Box2dFromGeoHash.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

