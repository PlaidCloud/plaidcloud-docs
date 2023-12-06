---
title: func.ST_ClosestPointOfApproach
slug: func-st-closestpointofapproach
description: Returns the smallest measure at which points interpolated along the given trajectories are at the smallest distance
date: 2022-02-01T11:36:07
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_ClosestPointOfApproach(geometry track1, geometry track2);
```


### PlaidCloud



```python
func.ST_ClosestPointOfApproach(geometry track1, geometry track2)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_ClosestPointOfApproach.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

