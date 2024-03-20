---
title: func.ST_Union
slug: func-st-union
description: Unions the input geometries, merging geometry to produce a result geometry with no overlaps
date: 2022-01-31T10:55:27
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Union(geometry g1, geometry g2);
```


### PlaidCloud



```python
func.ST_Union(geometry g1, geometry g2)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Union.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

