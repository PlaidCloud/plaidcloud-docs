---
title: func.ST_Relate
slug: func-st-relate
description: These functions allow testing and evaluating the spatial (topological) relationship between two geometries
date: 2022-01-31T10:02:04
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Relate(geometry geomA, geometry geomB);
```


### PlaidCloud



```python
func.ST_Relate(geometry geomA, geometry geomB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Relate.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

