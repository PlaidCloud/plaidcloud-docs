---
title: func.ST_PointInsideCircle
slug: func-st-pointinsidecircle
description: Returns true if the geometry is a point and is inside the circle with center center_x,center_y and radius radius
date: 2022-01-31T10:12:27
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_PointInsideCircle(geometry a_point, float center_x, float center_y, float radius);
```


### PlaidCloud



```python
func.ST_PointInsideCircle(geometry a_point, float center_x, float center_y, float radius)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_PointInsideCircle.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

