---
title: func.ST_IsRing
slug: func-st-isring
description: Returns TRUE if this LINESTRING is both ST_IsClosed and ST_IsSimple (does not self intersect)
date: 2022-01-27T14:17:13
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_IsRing(geometry g);
```


### PlaidCloud



```python
func.ST_IsRing(geometry g)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_IsRing.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

