---
title: func.ST_GeomFromEWKB
slug: func-st-geomfromewkb
description: Constructs a PostGIS ST_Geometry object from the OGC Extended Well-Known binary (EWKT) representation
date: 2022-01-29T14:47:23
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeomFromEWKB(bytea EWKB);
```


### PlaidCloud



```python
func.ST_GeomFromEWKB(bytea EWKB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeomFromEWKB.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

