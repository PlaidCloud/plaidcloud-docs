---
title: func.ST_SnapToGrid
slug: func-st-snaptogrid
description: Snap all points of the input geometry to the grid defined by its origin and cell size
date: 2022-01-28T13:44:34
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SnapToGrid(geometry geomA, float originX, float originY, float sizeX, float sizeY);
```


### PlaidCloud



```python
func.ST_SnapToGrid(geometry geomA, float originX, float originY, float sizeX, float sizeY)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SnapToGrid.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

