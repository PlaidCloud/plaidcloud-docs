---
title: func.ST_GeomCollFromText
slug: func-st-geomcollfromtext
description: Makes a collection Geometry from the Well-Known-Text (WKT) representation with the given SRID
date: 2022-01-29T14:31:32
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeomCollFromText(text WKT, integer srid);
```


### PlaidCloud



```python
func.ST_GeomCollFromText(text WKT, integer srid)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeomCollFromText.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

