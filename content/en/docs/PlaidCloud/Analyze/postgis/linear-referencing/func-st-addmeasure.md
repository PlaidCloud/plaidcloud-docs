---
title: func.ST_AddMeasure
slug: func-st-addmeasure
description: Return a derived geometry with measure elements linearly interpolated between the start and end points
date: 2022-02-01T11:33:57
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_AddMeasure(geometry geom_mline, float8 measure_start, float8 measure_end);
```


### PlaidCloud



```python
func.ST_AddMeasure(geometry geom_mline, float8 measure_start, float8 measure_end)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_AddMeasure.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

