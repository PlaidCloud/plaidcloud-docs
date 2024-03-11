---
title: func.ST_MakeEnvelope
slug: func-st-makeenvelope
description: Creates a rectangular Polygon from the minimum and maximum values for X and Y
date: 2022-01-25T07:40:10
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### **SQL**



```
ST_MakeEnvelope(float xmin, float ymin, float xmax, float ymax, integer srid=unknown);
```


### PlaidCloud



```python
func.ST_MakeEnvelope(float xmin, float ymin, float xmax, float ymax, integer srid=unknown); 
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_MakeEnvelope.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

