---
title: func.ST_3DMakeBox
slug: func-st-3dmakebox
description: Creates a BOX3D defined by the given two 3D point geometries
date: 2022-01-31T17:52:47
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_3DMakeBox(geometry point3DLowLeftBottom, geometry point3DUpRightTop);
```


### PlaidCloud



```python
func.ST_3DMakeBox(geometry point3DLowLeftBottom, geometry point3DUpRightTop)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_3DMakeBox.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

