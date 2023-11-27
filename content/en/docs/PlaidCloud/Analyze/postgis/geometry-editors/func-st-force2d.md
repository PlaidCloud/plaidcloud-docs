---
title: func.ST_Force2D
slug: func-st-force2d
description: Forces the geometries into a "2-dimensional mode" so that all output representations will only have the X and Y coordinates
date: 2022-01-28T13:20:24
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Force2D(geometry geomA);
```


### PlaidCloud



```python
func.ST_Force2D(geometry geomA)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Force2D.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

