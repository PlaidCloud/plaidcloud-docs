---
title: func.ST_CoveredBy
slug: func-st-coveredby
description: Returns 1 (TRUE) if no point in Geometry/Geography A is outside Geometry/Geography B
date: 2022-01-31T09:46:30
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_CoveredBy(geometry geomA, geometry geomB);
```


### PlaidCloud



```python
func.ST_CoveredBy(geometry geomA, geometry geomB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_CoveredBy.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

