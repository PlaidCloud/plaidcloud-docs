---
title: func.ST_MakeLine
slug: func-st-makeline
description: Creates a LineString containing the points of Point, MultiPoint, or LineString geometries
date: 2022-01-25T07:40:10
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### **SQL**



```
ST_MakeLine(geometry geom1, geometry geom2); 
```


### PlaidCloud



```python
func.ST_MakeLine(geometry geom1, geometry geom2)
```


**References**



PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_MakeLine.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

