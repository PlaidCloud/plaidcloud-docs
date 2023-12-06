---
title: func.ST_DWithin
slug: func-st-dwithin
description: Returns true if the geometries are within a given distance
date: 2022-01-31T10:09:58
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_DWithin(geometry g1, geometry g2, double precision distance_of_srid);
```


### PlaidCloud



```python
func.ST_DWithin(geometry g1, geometry g2, double precision distance_of_srid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_DWithin.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

