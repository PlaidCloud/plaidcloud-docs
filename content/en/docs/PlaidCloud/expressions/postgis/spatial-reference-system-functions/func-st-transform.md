---
title: func.ST_Transform
slug: func-st-transform
description: Returns a new geometry with its coordinates transformed to a different spatial reference system
date: 2022-01-29T14:25:00
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Transform(geometry g1, integer srid);
```


### PlaidCloud



```python
func.ST_Transform(geometry g1, integer srid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Transform.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

