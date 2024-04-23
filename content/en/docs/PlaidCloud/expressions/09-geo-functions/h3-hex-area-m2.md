---
title: H3_HEX_AREA_M2
---

Returns the average hexagon area in square meters at the given resolution. Excludes pentagons. 

## Analyze Syntax

```python
func.h3_hex_area_m2(res)
```

## Analyze Examples

```python
func.h3_hex_area_m2(1)

┌────────────────────────┐
│ func.h3_hex_area_m2(1) │
├────────────────────────┤
│      609788441794.1339 │
└────────────────────────┘
```

## SQL Syntax

```sql
H3_HEX_AREA_M2(res)
```

## SQL Examples

```sql
SELECT H3_HEX_AREA_M2(1);

┌───────────────────┐
│ h3_hex_area_m2(1) │
├───────────────────┤
│ 609788441794.1339 │
└───────────────────┘
```