---
title: func.ST_3DDWithin
slug: func-st-3ddwithin
description: For geometry type returns true if the 3d distance between two objects is within distance_of_srid specified projected units
date: 2022-01-31T09:50:26
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_3DDWithin(geometry g1, geometry g2, double precision distance_of_srid);
```


### PlaidCloud



```python
func.ST_3DDWithin(geometry g1, geometry g2, double precision distance_of_srid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_3DDWithin.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

