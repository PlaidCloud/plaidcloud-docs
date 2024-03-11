---
title: func.ST_MinimumBoundingCircle
slug: func-st-minimumboundingcircle
description: Returns the smallest circle polygon that contains a geometry
date: 2022-01-31T11:06:48
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_MinimumBoundingCircle(geometry geomA, integer num_segs_per_qt_circ=48);
```

  



### PlaidCloud



```python
func.ST_MinimumBoundingCircle(geometry geomA, integer num_segs_per_qt_circ=48);
```

  



### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_MinimumBoundingCircle.html).



Additional capabilities and usage examples can be found in the PostGIS documentation.

