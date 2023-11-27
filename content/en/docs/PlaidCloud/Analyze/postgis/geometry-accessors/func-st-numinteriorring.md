---
title: func.ST_NumInteriorRing
slug: func-st-numinteriorring
description: This function returns the number of interior rings of a polygon geom. It returns NULL if the geom is not a polygon.
date: 2022-01-27T14:29:47
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_NumInteriorRing(geometry a_polygon);
```


### PlaidCloud



```python
ST_NumInteriorRing(geometry a_polygon)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_NumInteriorRing.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

