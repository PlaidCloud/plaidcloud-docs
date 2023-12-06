---
title: func.ST_LineToCurve
slug: func-st-linetocurve
description: Converts plain LINESTRING/POLYGON to CIRCULAR STRINGs and Curved Polygons
date: 2022-01-28T13:34:04
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineToCurve(geometry geomANoncircular);
```


### PlaidCloud



```python
func.ST_LineToCurve(geometry geomANoncircular)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineToCurve.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

