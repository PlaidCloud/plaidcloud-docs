---
title: func.ST_AsGML
slug: func-st-asgml
description: Return the geometry as a Geography Markup Language (GML) element
date: 2022-01-29T19:11:49
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_AsGML(geometry geom, integer maxdecimaldigits=15, integer options=0);
```


### PlaidCloud



```python
func.ST_AsGML(geometry geom, integer maxdecimaldigits=15, integer options=0)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_AsGML.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

