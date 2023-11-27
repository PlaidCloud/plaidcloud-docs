---
title: func.ST_SetSRID
slug: func-st-setsrid
description: Sets the SRID on a geometry to a particular integer value
date: 2022-01-29T14:22:36
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SetSRID(geometry geom, integer srid);
```


### PlaidCloud



```python
func.ST_SetSRID(geometry geom, integer srid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SetSRID.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

