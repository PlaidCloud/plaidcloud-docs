---
title: func.ST_LineCrossingDirection
slug: func-st-linecrossingdirection
description: Given 2 linestrings, returns an integer between -3 and 3 indicating what kind of crossing behavior exists between them
date: 2022-01-31T09:52:03
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineCrossingDirection(geometry linestringA, geometry linestringB);
```


### PlaidCloud



```python
func.ST_LineCrossingDirection(geometry linestringA, geometry linestringB)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineCrossingDirection.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

