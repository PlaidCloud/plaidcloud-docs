---
title: func.ST_Length
slug: func-st-length
description: Returns the 2D Cartesian length of the geometry for geometry types and uses the inverse geodesic calculation for geography types
date: 2022-01-31T10:25:51
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Length(geometry a_2dlinestring);
```


### PlaidCloud



```python
func.ST_Length(geometry a_2dlinestring)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Length.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

