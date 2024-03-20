---
title: func.ST_Scale
slug: func-st-scale
description: Scales the geometry to a new size by multiplying the ordinates with the corresponding factor parameters
date: 2022-01-31T17:37:40
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Scale(geometry geom, geometry factor);
```


### PlaidCloud



```python
func.ST_Scale(geometry geom, geometry factor)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Scale.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

