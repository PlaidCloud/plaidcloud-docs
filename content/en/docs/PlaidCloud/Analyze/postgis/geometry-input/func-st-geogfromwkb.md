---
title: func.ST_GeogFromWKB
slug: func-st-geogfromwkb
description: This function, takes a well-known binary representation (WKB) of a geometry and creates an instance of the appropriate geography type
date: 2022-01-29T14:45:41
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeogFromWKB(bytea wkb);
```


### PlaidCloud



```python
func.ST_GeogFromWKB(bytea wkb)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeogFromWKB.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

