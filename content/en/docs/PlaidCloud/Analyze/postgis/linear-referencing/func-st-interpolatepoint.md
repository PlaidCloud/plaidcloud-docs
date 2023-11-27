---
title: func.ST_InterpolatePoint
slug: func-st-interpolatepoint
description: Return the value of the measure dimension of a geometry at the point closed to the provided point
date: 2022-02-01T11:33:16
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_InterpolatePoint(geometry line, geometry point);
```

### 
PlaidCloud



```
func.ST_InterpolatePoint(geometry line, geometry point)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_InterpolatePoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

