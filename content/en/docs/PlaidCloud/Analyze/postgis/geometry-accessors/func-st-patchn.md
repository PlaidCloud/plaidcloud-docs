---
title: func.ST_PatchN
slug: func-st-patchn
description: Returns the 1-based Nth geometry (face) if the geometry is a POLYHEDRALSURFACE or POLYHEDRALSURFACEM
date: 2022-01-27T14:34:44
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_PatchN(geometry geomA, integer n);
```


### PlaidCloud



```python
ST_PatchN(geometry geomA, integer n)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_PatchN.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

