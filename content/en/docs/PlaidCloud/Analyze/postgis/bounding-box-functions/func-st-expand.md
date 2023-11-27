---
title: func.ST_Expand
slug: func-st-expand
description: This function returns a bounding box expanded from the bounding box of the input
date: 2022-01-31T17:48:22
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Expand(geometry geom, float units_to_expand);
```


### PlaidCloud



```python
func.ST_Expand(geometry geom, float units_to_expand)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Expand.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

