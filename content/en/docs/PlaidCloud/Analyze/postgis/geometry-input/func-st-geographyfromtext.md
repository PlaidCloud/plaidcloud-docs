---
title: func.ST_GeographyFromText
slug: func-st-geographyfromtext
description: Returns a geography object from the well-known text representation. SRID 4326 is assumed if unspecified
date: 2022-01-29T14:29:58
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_GeographyFromText(text EWKT);
```


### PlaidCloud



```python
func.ST_GeographyFromText(text EWKT)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_GeographyFromText.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

