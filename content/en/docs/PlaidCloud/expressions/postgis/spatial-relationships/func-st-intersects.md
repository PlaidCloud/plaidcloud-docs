---
title: func.ST_Intersects
slug: func-st-intersects
description: If a geometry or geography shares any portion of space then they intersect
date: 2022-01-31T09:55:17
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Intersects( geometry geomA , geometry geomB );
```


### PlaidCloud



```python
func.ST_Intersects( geometry geomA , geometry geomB )
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Intersects.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

