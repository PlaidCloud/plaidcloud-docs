---
title: func.ST_Force3DZ
slug: func-st-force3dz
description: This function forces the geoms into XYZ mode. If a geom has no 'Z' compenent, then a 'Z coordinate' is automatically added
date: 2022-01-28T13:23:12
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Force3DZ(geometry geomA, float Zvalue = 0.0);
```


### PlaidCloud



```python
func.ST_Force3DZ(geometry geomA, float Zvalue = 0.0)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Force_3DZ.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

