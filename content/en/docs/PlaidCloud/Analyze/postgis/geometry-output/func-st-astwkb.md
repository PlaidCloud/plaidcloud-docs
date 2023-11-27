---
title: func.ST_AsTWKB
slug: func-st-astwkb
description: Returns the geometry in TWKB (Tiny Well-Known Binary) format
date: 2022-01-29T19:19:07
---


## Description


PlaidCloud expressions and filters provide use of most non-administrative PostGIS methods. PostGIS methods are accessed by prefixing the standard method name with `func.`.



## Examples


### SQL



```
ST_AsTWKB(geometry g1, integer decimaldigits_xy=0, integer decimaldigits_z=0, integer decimaldigits_m=0, boolean include_sizes=false, boolean include_bounding boxes=false);
```


### PlaidCloud



```python
func.ST_AsTWKB(geometry g1, integer decimaldigits_xy=0, integer decimaldigits_z=0, integer decimaldigits_m=0, boolean include_sizes=false, boolean include_bounding boxes=false)
```


### References


PostGIS Official Documentation for this method can be found [here](https://postgis.net/docs/manual-3.1/ST_AsTWKB.html).



Additional capabilities and usage examples can be found in the PostGIS documentation

