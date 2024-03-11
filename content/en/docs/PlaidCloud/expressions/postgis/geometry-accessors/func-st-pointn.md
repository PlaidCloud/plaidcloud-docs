---
title: func.ST_PointN
slug: func-st-pointn
description: Return the Nth point in a single linestring or circular linestring in the geometry
date: 2022-01-27T14:35:33
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_PointN(geometry a_linestring, integer n);
```


### PlaidCloud



```python
func.ST_PointN(geometry a_linestring, integer n)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_PointN.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

