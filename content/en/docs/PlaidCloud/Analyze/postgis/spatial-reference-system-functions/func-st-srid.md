---
title: func.ST_SRID
slug: func-st-srid
description: Returns the spatial reference identifier for the ST_Geometry as defined in spatial_ref_sys table
date: 2022-01-29T14:23:27
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SRID(geometry g1);
```


### PlaidCloud



```python
func.ST_SRID(geometry g1)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SRID.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

