---
title: func.ST_ClusterWithin
slug: func-st-clusterwithin
description: Aggregate function that returns an array of GeometryCollections that represent a set of geometries separated by a specified distance
date: 2022-01-31T17:42:30
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_ClusterWithin(geometry set g, float8 distance);
```


### PlaidCloud



```python
func.ST_ClusterWithin(geometry set g, float8 distance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_ClusterWithin.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

