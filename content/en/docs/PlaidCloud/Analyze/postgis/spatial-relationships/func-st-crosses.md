---
title: func.ST_Crosses
slug: func-st-crosses
description: Takes two geometry objects and returns TRUE if their intersection "spatially cross", but not all interior points in common
date: 2022-01-31T09:49:40
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Crosses(geometry g1, geometry g2);
```


### PlaidCloud



```python
func.ST_Crosses(geometry g1, geometry g2)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Crosses.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

