---
title: func.ST_Force3D
slug: func-st-force3d
description: Forces the geometries into XYZ mode
date: 2022-01-28T13:22:20
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Force3D(geometry geomA, float Zvalue = 0.0);
```


### PlaidCloud



```python
func.ST_Force3D(geometry geomA, float Zvalue = 0.0)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Force_3D.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

