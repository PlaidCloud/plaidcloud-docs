---
title: func.ST_DumpRings
slug: func-st-dumprings
description: This is a set-returning function (SRF). It returns a set of geometry_dump rows, as an integer and a geometry, aliased "path" and "geom"
date: 2022-01-27T13:53:24
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_DumpRings(geometry a_polygon);
```

  



### PlaidCloud



```python
func.ST_DumpRings(geometry a_polygon)
```

  



**References**



PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_DumpRings.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

