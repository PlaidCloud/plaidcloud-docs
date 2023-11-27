---
title: func.ST_Disjoint
slug: func-st-disjoint
description: Overlaps, Touches, Within imply geometries are not spatially disjoint, unless they return true, then they are not spatially disjoint
date: 2022-01-31T09:52:58
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Disjoint( geometry A , geometry B );
```


### PlaidCloud



```python
func.ST_Disjoint( geometry A , geometry B )
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Disjoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

