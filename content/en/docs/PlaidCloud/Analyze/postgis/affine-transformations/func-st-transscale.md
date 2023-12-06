---
title: func.ST_TransScale
slug: func-st-transscale
description: Translates the geometry using the deltaX and deltaY args, then scales it using the XFactor, YFactor args, working in 2D only
date: 2022-01-31T17:40:10
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_TransScale(geometry geomA, float deltaX, float deltaY, float XFactor, float YFactor);
```


### PlaidCloud



```python
func.ST_TransScale(geometry geomA, float deltaX, float deltaY, float XFactor, float YFactor)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_TransScale.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

