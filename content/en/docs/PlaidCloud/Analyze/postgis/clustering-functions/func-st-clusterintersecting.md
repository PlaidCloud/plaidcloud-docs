---
title: func.ST_ClusterIntersecting
slug: func-st-clusterintersecting
description: ClusterIntersecting is an aggregate function that returns an array of GeometryCollections that represent an interconnected set of geometries
date: 2022-01-31T17:41:46
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_ClusterIntersecting(geometry set g);
```


### PlaidCloud



```python
func.ST_ClusterIntersecting(geometry set g)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_ClusterIntersecting.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

