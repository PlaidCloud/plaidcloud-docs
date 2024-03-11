---
title: func.ST_OrderingEquals
slug: func-st-orderingequals
description: Compares two geometries and returns it (TRUE) if the geometries are equal and the coordinates are in the same order
date: 2022-01-31T10:00:28
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_OrderingEquals(geometry A, geometry B);
```


### PlaidCloud



```python
func.ST_OrderingEquals(geometry A, geometry B)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_OrderingEquals.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

