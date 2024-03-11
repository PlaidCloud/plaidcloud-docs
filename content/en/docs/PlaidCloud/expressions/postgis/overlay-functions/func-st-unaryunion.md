---
title: func.ST_UnaryUnion
slug: func-st-unaryunion
description: A single-input variant of ST_Union
date: 2022-01-31T10:56:12
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_UnaryUnion(geometry geom, float8 gridSize = -1);
```

  



### PlaidCloud



```python
func.ST_UnaryUnion(geometry geom, float8 gridSize = -1);
```

  



### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_UnaryUnion.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

