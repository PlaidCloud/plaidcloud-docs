---
title: func.ST_Distance
slug: func-st-distance
description: For geometry types returns the minimum 2D Cartesian (planar) distance between two geometries, in projected units (spatial ref units)
date: 2022-01-31T10:22:29
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Distance(geometry g1, geometry g2);
```


### PlaidCloud



```python
func.ST_Distance(geometry g1, geometry g2)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Distance.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

