---
title: func.ST_DistanceSpheroid
slug: func-st-distancespheroid
description: Returns minimum distance in meters between two lon/lat geometries given a particular spheroid
date: 2022-01-31T10:23:20
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_DistanceSpheroid(geometry geomlonlatA, geometry geomlonlatB, spheroid measurement_spheroid);
```


### PlaidCloud



```python
func.ST_DistanceSpheroid(geometry geomlonlatA, geometry geomlonlatB, spheroid measurement_spheroid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Distance_Spheroid.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

