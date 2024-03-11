---
title: func.ST_ShiftLongitude
slug: func-st-shiftlongitude
description: Reads every point/vertex in a geometry, and if the longitude coordinate is <0, adds 360 to it
date: 2022-01-28T13:43:49
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_ShiftLongitude(geometry geom);
```


### PlaidCloud



```python
func.ST_ShiftLongitude(geometry geom)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Shift_Longitude.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

