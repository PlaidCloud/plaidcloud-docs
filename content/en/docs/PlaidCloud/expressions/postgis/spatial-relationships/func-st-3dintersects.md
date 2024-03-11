---
title: func.ST_3DIntersects
slug: func-st-3dintersects
description: Overlaps, Touches, Within all imply spatial intersection and if any returns true, then the geometries also spatially intersect
date: 2022-01-31T09:35:26
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_3DIntersects( geometry geomA , geometry geomB );
```


### PlaidCloud



```python
func.ST_3DIntersects( geometry geomA , geometry geomB )
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_3DIntersects.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

