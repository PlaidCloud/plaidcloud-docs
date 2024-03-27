---
title: H3_HEX_AREA_KM2
---

Returns the average hexagon area in square kilometers at the given resolution. Excludes pentagons.

## SQL Syntax

```sql
H3_HEX_AREA_KM2(res)
```

## SQL Examples

```sql
SELECT H3_HEX_AREA_KM2(1);

┌────────────────────┐
│ h3_hex_area_km2(1) │
├────────────────────┤
│  609788.4417941332 │
└────────────────────┘
```