---
title: func.ST_3DDFullyWithin
slug: func-st-3ddfullywithin
description: Returns true if the 3D geometries are fully within the specified distance of one another
date: 2022-01-31T09:47:25
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_3DDFullyWithin(geometry g1, geometry g2, double precision distance);
```


### PlaidCloud



```python
func.ST_3DDFullyWithin(geometry g1, geometry g2, double precision distance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_3DDFullyWithin.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

