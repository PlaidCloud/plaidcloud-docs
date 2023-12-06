---
title: func.ST_Split
slug: func-st-split
description: The function supports splitting a line by a (multi)point, (multi)line or (multi)polygon boundary, or a (multi)polygon by line
date: 2022-01-31T10:51:44
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Split(geometry input, geometry blade);
```


### PlaidCloud



```python
func.ST_Split(geometry input, geometry blade)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Split.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

