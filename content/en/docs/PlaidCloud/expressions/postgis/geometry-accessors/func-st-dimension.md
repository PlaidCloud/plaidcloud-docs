---
title: func.ST_Dimension
slug: func-st-dimension
description: Return the topological dimension of this Geometry object, which must be less than or equal to the coordinate dimension
date: 2022-01-27T13:43:42
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Dimension(geometry g);
```


### PlaidCloud



```python
func.ST_Dimension(geometry g)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Dimension.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

