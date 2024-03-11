---
title: func.ST_SimplifyPreserveTopology
slug: func-st-simplifypreservetopology
description: Simplifies a geometry by removing points that would fall within a specified distance tolerance.
date: 2022-01-31T17:28:22
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_SimplifyPreserveTopology(geometry geomA, float tolerance);
```


### PlaidCloud



```python
func.ST_SimplifyPreserveTopology(geometry geomA, float tolerance)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_SimplifyPreserveTopology.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

