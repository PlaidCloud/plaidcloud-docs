---
title: func.ST_OffsetCurve
slug: func-st-offsetcurve
description: Return an offset line at a given distance and side from an input line
date: 2022-01-31T11:07:36
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_OffsetCurve(geometry line, float signed_distance, text style_parameters='');
```


### PlaidCloud



```python
func.ST_OffsetCurve(geometry line, float signed_distance, text style_parameters='')
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_OffsetCurve.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

