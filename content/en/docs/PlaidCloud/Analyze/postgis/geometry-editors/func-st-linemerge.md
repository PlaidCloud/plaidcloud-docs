---
title: func.ST_LineMerge
slug: func-st-linemerge
description: Returns a (set of) LineString(s) formed by sewing together the constituent line work of a MULTILINESTRING
date: 2022-01-28T13:33:14
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineMerge(geometry amultilinestring);
```


### PlaidCloud



```python
func.ST_LineMerge(geometry amultilinestring)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineMerge.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

