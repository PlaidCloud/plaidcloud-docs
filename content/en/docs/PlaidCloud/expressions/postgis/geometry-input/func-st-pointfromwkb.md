---
title: func.ST_PointFromWKB
slug: func-st-pointfromwkb
description: This function, takes a binary representation of geometry and a (SRID) and creates the appropriate geometry type - POINT GEOMETRY
date: 2022-01-29T14:52:42
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_PointFromWKB(bytea wkb);
```


### PlaidCloud



```python
func.ST_PointFromWKB(bytea wkb); 
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_PointFromWKB.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

