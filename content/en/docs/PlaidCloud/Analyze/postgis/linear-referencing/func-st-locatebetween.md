---
title: func.ST_LocateBetween
slug: func-st-locatebetween
description: Return a derived geometry collection with elements that match the specified range of measures inclusively
date: 2022-02-01T11:31:19
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LocateBetween(geometry geom, float8 measure_start, float8 measure_end, float8 offset);
```


### PlaidCloud



```python
func.ST_LocateBetween(geometry geom, float8 measure_start, float8 measure_end, float8 offset)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LocateBetween.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

