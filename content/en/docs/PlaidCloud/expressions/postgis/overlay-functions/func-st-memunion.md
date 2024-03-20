---
title: func.ST_MemUnion
slug: func-st-memunion
description: Aggregate function which unions geometry in a memory-efficent but slower way
date: 2022-01-31T10:49:21
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_MemUnion(geometry set geomfield);
```


### PlaidCloud



```python
func.ST_MemUnion(geometry set geomfield)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_MemUnion.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

