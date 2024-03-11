---
title: func.ST_Covers
slug: func-st-covers
description: Returns 1 (TRUE) if no point in Geometry/Geography B is outside Geometry/Geography A
date: 2022-01-31T09:40:15
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Covers(geometry geomA, geometry geomB);
```


### PlaidCloud



```python
func.ST_Covers(geometry geomA, geometry geomB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Covers.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

