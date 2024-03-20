---
title: func.ST_ContainsProperly
slug: func-st-containsproperly
description: Returns true if B intersects the interior of A but not the boundary (or exterior)
date: 2022-01-31T09:43:02
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_ContainsProperly(geometry geomA, geometry geomB);
```

  



### PlaidCloud



```python
func.ST_ContainsProperly(geometry geomA, geometry geomB);
```

  



### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_ContainsProperly.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

