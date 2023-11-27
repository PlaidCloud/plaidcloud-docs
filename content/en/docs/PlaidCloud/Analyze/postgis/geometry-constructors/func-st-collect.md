---
title: func.ST_Collect
slug: func-st-collect
description: Collects geometries into a geometry collection
date: 2022-01-25T07:40:15
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


**SQL**



```
ST_Collect(geometry g1, geometry g2)
```


### PlaidCloud



```python
func.ST_Collect(geometry g1, geometry g2)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/ST_Collect.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

