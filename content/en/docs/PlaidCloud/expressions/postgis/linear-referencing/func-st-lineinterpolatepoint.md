---
title: func.ST_LineInterpolatePoint
slug: func-st-lineinterpolatepoint
description: Returns a point interpolated along a line
date: 2022-01-31T18:02:44
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineInterpolatePoint(geometry a_linestring, float8 a_fraction);
```


### PlaidCloud



```python
func.ST_LineInterpolatePoint(geometry a_linestring, float8 a_fraction)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineInterpolatePoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

