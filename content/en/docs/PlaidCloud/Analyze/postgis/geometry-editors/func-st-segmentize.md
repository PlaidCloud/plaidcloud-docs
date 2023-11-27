---
title: func.ST_Segmentize
slug: func-st-segmentize
description: Returns a modified geometry having no segment longer than the given max_segment_length
date: 2022-01-28T13:41:18
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_Segmentize(geometry geom, float max_segment_length);
```


### PlaidCloud



```python
func.ST_Segmentize(geometry geom, float max_segment_length)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_Segmentize.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

