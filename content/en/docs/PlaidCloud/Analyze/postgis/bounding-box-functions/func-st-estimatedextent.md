---
title: func.ST_EstimatedExtent
slug: func-st-estimatedextent
description: Return the 'estimated' extent of the given spatial table
date: 2022-01-31T17:47:34
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_EstimatedExtent(text table_name, text geocolumn_name);
```


### PlaidCloud



```python
func.ST_EstimatedExtent(text table_name, text geocolumn_name)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_EstimatedExtent.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

