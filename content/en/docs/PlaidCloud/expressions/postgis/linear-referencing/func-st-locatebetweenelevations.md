---
title: func.ST_LocateBetweenElevations
slug: func-st-locatebetweenelevations
description: Return a derived geometry (collection) value with elements that intersect the specified range of elevations inclusively
date: 2022-02-01T11:32:01
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_LocateBetweenElevations(geometry geom, float8 elevation_start, float8 elevation_end);
```


### PlaidCloud



```python
func.ST_LocateBetweenElevations(geometry geom, float8 elevation_start, float8 elevation_end)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_LocateBetweenElevations.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

