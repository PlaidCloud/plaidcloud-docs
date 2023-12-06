---
title: func.ST_EndPoint
slug: func-st-endpoint
description: Returns the last point of a LINESTRING as a POINT. Returns NULL if the input is not a LINESTRING
date: 2022-01-27T13:54:46
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_EndPoint(geometry g);
```

  



### PlaidCloud



```python
func.ST_EndPoint(geometry g)
```

  



### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_EndPoint.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

