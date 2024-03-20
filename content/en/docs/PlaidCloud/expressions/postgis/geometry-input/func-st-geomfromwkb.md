---
title: func.ST_GeomFromWKB
slug: func-st-geomfromwkb
description: This function takes a binary representation of a geometry and a Spatial Reference System ID (SRID) and creates the appropriate geometry type
date: 2022-01-29T14:48:25
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeomFromWKB(bytea geom);
```

  
 


### PlaidCloud



```python
func.ST_GeomFromWKB(bytea geom);
```

  
 


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeomFromWKB.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

