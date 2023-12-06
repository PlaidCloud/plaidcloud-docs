---
title: func.ST_DFullyWithin
slug: func-st-dfullywithin
description: Returns true if the geometries are entirely within the specified distance of one another
date: 2022-01-31T10:09:02
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_DFullyWithin(geometry g1, geometry g2, double precision distance);
```


### PlaidCloud



```python
func.ST_DFullyWithin(geometry g1, geometry g2, double precision distance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_DFullyWithin.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

