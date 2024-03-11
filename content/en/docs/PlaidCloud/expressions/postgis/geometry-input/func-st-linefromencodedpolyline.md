---
title: func.ST_LineFromEncodedPolyline
slug: func-st-linefromencodedpolyline
description: Creates a LineString from an Encoded Polyline string
date: 2022-01-29T15:12:17
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineFromEncodedPolyline(text polyline, integer precision=5);
```


### PlaidCloud



```python
func.ST_LineFromEncodedPolyline(text polyline, integer precision=5)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineFromEncodedPolyline.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

