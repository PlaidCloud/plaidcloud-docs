---
title: func.ST_Project
slug: func-st-project
description: Returns a point projected from a start point along a geodesic using a given distance and azimuth (bearing)
date: 2022-01-31T10:43:45
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Project(geography g1, float distance, float azimuth);
```


### PlaidCloud



```python
func.ST_Project(geography g1, float distance, float azimuth)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Project.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

