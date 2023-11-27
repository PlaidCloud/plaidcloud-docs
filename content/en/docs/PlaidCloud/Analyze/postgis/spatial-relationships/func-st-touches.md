---
title: func.ST_Touches
slug: func-st-touches
description: Returns TRUE if the only points in common between g1 and g2 lie in the union of the boundaries of g1 and g2
date: 2022-01-31T10:05:09
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Touches(geometry g1, geometry g2);
```


### PlaidCloud



```python
func.ST_Touches(geometry g1, geometry g2)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Touches.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

