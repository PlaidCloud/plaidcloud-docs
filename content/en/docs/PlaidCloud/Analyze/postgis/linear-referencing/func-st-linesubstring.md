---
title: func.ST_LineSubstring
slug: func-st-linesubstring
description: Return a linestring being a substring of the input one starting and ending at the given fractions of total 2d length
date: 2022-01-31T18:05:28
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LineSubstring(geometry a_linestring, float8 startfraction, float8 endfraction);
```


### PlaidCloud



```python
func.ST_LineSubstring(geometry a_linestring, float8 startfraction, float8 endfraction)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LineSubstring.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

