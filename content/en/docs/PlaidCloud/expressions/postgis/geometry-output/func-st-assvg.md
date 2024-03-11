---
title: func.ST_AsSVG
slug: func-st-assvg
description: Return the geometry as Scalar Vector Graphics (SVG) path data
date: 2022-01-29T19:19:53
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_AsSVG(geometry geom, integer rel=0, integer maxdecimaldigits=15);
```


### PlaidCloud



```python
func.ST_AsSVG(geometry geom, integer rel=0, integer maxdecimaldigits=15)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_AsSVG.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

