---
title: func.ST_3DExtent
slug: func-st-3dextent
description: ST_3DExtent returns a box3d (includes Z coordinate) bounding box that encloses a set of geometries
date: 2022-01-31T17:50:41
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_3DExtent(geometry set geomfield);
```


### PlaidCloud



```python
func.ST_3DExtent(geometry set geomfield)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_3DExtent.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

