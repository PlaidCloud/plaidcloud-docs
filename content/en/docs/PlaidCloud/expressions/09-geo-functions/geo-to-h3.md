---
title: GEO_TO_H3
---

Returns the [H3](https://eng.uber.com/h3/) index of the hexagon cell where the given location resides. Returning 0 means an error occurred.

## SQL Syntax

```sql
GEO_TO_H3(lon, lat, res)
```

## SQL Examples

```sql
SELECT GEO_TO_H3(37.79506683, 55.71290588, 15);

┌─────────────────────────────────────────┐
│ geo_to_h3(37.79506683, 55.71290588, 15) │
├─────────────────────────────────────────┤
│                      644325524701193974 │
└─────────────────────────────────────────┘
```