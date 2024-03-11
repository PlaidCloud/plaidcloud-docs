---
title: func.ST_CPAWithin
slug: func-st-cpawithin
description: Checks whether two moving objects have ever been within the specified maximum distance
date: 2022-02-01T11:37:35
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_CPAWithin(geometry track1, geometry track2, float8 maxdist);
```


### PlaidCloud



```python
func.ST_CPAWithin(geometry track1, geometry track2, float8 maxdist)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_CPAWithin.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

