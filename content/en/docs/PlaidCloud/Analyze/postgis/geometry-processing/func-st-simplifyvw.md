---
title: func.ST_SimplifyVW
slug: func-st-simplifyvw
description: Returns a "simplified" version of the given geometry using the Visvalingam-Whyatt algorithm
date: 2022-01-31T17:29:46
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SimplifyVW(geometry geomA, float tolerance);
```


### PlaidCloud



```python
func.ST_SimplifyVW(geometry geomA, float tolerance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SimplifyVW.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

