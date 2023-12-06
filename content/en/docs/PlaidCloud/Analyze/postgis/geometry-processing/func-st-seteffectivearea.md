---
title: func.ST_SetEffectiveArea
slug: func-st-seteffectivearea
description: Sets the effective area for each vertex, using the Visvalingam-Whyatt algorithm
date: 2022-01-31T17:30:36
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SetEffectiveArea(geometry geomA, float threshold = 0, integer set_area = 1);
```


### PlaidCloud



```python
func.ST_SetEffectiveArea(geometry geomA, float threshold = 0, integer set_area = 1)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SetEffectiveArea.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

