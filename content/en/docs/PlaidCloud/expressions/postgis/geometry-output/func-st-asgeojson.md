---
title: func.ST_AsGeoJSON
slug: func-st-asgeojson
description: Return the geometry as a GeoJSON "geometry" object, or the row as a GeoJSON "feature" object
date: 2022-01-29T19:11:07
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_AsGeoJSON(geography geog, integer maxdecimaldigits=9, integer options=0);
```


### PlaidCloud



```python
func.ST_AsGeoJSON(geography geog, integer maxdecimaldigits=9, integer options=0)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_AsGeoJSON.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

