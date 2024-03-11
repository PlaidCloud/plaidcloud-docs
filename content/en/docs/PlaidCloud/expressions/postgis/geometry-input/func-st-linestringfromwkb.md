---
title: func.ST_LinestringFromWKB
slug: func-st-linestringfromwkb
description: This function, takes a binary representation of geometry and a (SRID) and creates the appropriate geometry type -LINESTRING GEOMETRY
date: 2022-01-29T14:51:06
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LinestringFromWKB(bytea WKB);
```



### PlaidCloud



```python
func.ST_LinestringFromWKB(bytea WKB);
```



### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LinestringFromWKB.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

