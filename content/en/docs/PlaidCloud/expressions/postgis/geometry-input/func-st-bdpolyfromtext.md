---
title: func.ST_BdPolyFromText
slug: func-st-bdpolyfromtext
description: Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString Well-Known text representation
date: 2022-01-29T14:26:43
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_BdPolyFromText(text WKT, integer srid);
```


### PlaidCloud



```python
func.ST_BdPolyFromText(text WKT, integer srid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_BdPolyFromText.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

