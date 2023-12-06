---
title: func.ST_Force3DM
slug: func-st-force3dm
description: Forces the geometries into XYM mode
date: 2022-01-28T13:25:05
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Force3DM(geometry geomA, float Mvalue = 0.0);
```


### PlaidCloud



```python
func.ST_Force3DM(geometry geomA, float Mvalue = 0.0)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Force_3DM.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

