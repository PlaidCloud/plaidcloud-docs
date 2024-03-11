---
title: func.ST_SetPoint
slug: func-st-setpoint
description: Replace point N of linestring with given point
date: 2022-01-28T13:42:02
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SetPoint(geometry linestring, integer zerobasedposition, geometry point);
```


### PlaidCloud



```python
func.ST_SetPoint(geometry linestring, integer zerobasedposition,   
geometry point)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SetPoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

