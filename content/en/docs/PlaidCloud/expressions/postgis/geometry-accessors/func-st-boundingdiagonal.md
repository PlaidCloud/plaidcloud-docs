---
title: func.ST_BoundingDiagonal
slug: func-st-boundingdiagonal
description: Returns the diagonal of the supplied geometry's bounding box as a LineString
date: 2022-01-27T13:57:23
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_BoundingDiagonal(geometry geom, boolean fits=false);
```


### PlaidCloud



```python
func.ST_BoundingDiagonal(geometry geom, boolean fits=False)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_BoundingDiagonal.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

