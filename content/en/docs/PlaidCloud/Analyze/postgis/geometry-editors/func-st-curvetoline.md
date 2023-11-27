---
title: func.ST_CurveToLine
slug: func-st-curvetoline
description: Converts a CIRCULAR STRING to LINESTRING or CURVEPOLYGON to POLYGON or MULTISURFACE to MULTIPOLYGON
date: 2022-01-28T13:17:58
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_CurveToLine(geometry curveGeom, float tolerance, integer tolerance_type, integer flags);
```


### PlaidCloud



```python
func.ST_CurveToLine(geometry curveGeom, float tolerance, integer tolerance_type, integer flags)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_CurveToLine.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

