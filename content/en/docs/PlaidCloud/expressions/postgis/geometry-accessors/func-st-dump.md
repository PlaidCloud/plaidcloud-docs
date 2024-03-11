---
title: func.ST_Dump
slug: func-st-dump
description: This is a set-returning function (SRF). It returns a set of geometry_dump rows, formed by a geometry (geom) and an array of integers (path)
date: 2022-01-27T13:45:06
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Dump(geometry g1);
```


### PlaidCloud



```python
func.ST_Dump(geometry g1)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Dump.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

