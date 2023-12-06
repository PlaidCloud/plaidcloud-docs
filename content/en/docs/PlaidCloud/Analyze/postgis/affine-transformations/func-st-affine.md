---
title: func.ST_Affine
slug: func-st-affine
description: Applies a 3D affine transformation to the geometry to do things like translate, rotate, scale in one step
date: 2022-01-31T17:32:22
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Affine(geometry geomA, float a, float b, float d, float e, float xoff, float yoff);
```


### PlaidCloud



```python
func.ST_Affine(geometry geomA, float a, float b, float d, float e, float xoff, float yoff)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Affine.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

