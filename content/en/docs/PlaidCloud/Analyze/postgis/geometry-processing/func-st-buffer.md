---
title: func.ST_Buffer
slug: func-st-buffer
description: Returns a geometry/geography that represents all points whose distance from this Geometry/geography is less than or equal to distance
date: 2022-01-31T10:58:04
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Buffer(geometry g1, float radius_of_buffer, text buffer_style_parameters = '');
```


### PlaidCloud



```python
func.ST_Buffer(geometry g1, float radius_of_buffer, text buffer_style_parameters = '')
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Buffer.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

