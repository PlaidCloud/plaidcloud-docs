---
title: func.ST_LocateAlong
slug: func-st-locatealong
description: Return a derived geometry collection value with elements that match the specified measure
date: 2022-01-31T18:06:09
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LocateAlong(geometry ageom_with_measure, float8 a_measure, float8 offset);
```


### PlaidCloud



```python
func.ST_LocateAlong(geometry ageom_with_measure, float8 a_measure, float8 offset)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LocateAlong.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

