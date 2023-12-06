---
title: func.ST_LengthSpheroid
slug: func-st-lengthspheroid
description: Returns the 2D or 3D length/perimeter of a lon/lat geometry on a spheroid
date: 2022-01-31T10:32:10
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LengthSpheroid(geometry a_geometry, spheroid a_spheroid);
```


### PlaidCloud



```python
func.ST_LengthSpheroid(geometry a_geometry, spheroid a_spheroid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Length_Spheroid.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

