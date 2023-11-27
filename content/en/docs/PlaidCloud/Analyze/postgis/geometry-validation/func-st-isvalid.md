---
title: func.ST_IsValid
slug: func-st-isvalid
description: Test if an ST_Geometry value is well-formed in 2D according to the OGC rules
date: 2022-01-28T13:48:43
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_IsValid(geometry g);
```


### PlaidCloud



```python
func.ST_IsValid(geometry g)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_IsValid.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

