---
title: func.ST_IsValidDetail
slug: func-st-isvaliddetail
description: Returns a valid_detail row, formed by a boolean (valid) stating whether the geometry is valid or invalid
date: 2022-01-28T13:49:31
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_IsValidDetail(geometry geom, integer flags);
```


### PlaidCloud



```python
func.ST_IsValidDetail(geometry geom, integer flags)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_IsValidDetail.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

