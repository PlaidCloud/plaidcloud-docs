---
title: func.ST_Translate
slug: func-st-translate
description: Returns a new geometry whose coordinates are translated delta x,delta y,delta z units
date: 2022-01-31T17:39:26
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Translate(geometry g1, float deltax, float deltay);
```


### PlaidCloud



```python
func.ST_Translate(geometry g1, float deltax, float deltay)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Translate.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

