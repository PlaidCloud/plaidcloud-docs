---
title: ST_ASTEXT
---

Converts a geometry to its WKT (Well-Known Text) representation.

## Analyze Syntax

```python
func.st_astext(<geometry>)
```

## Analyze Examples

```python
func.st_astext(func.st_point(1, 2))

┌───────────────┐
│ 'POINT (1 2)'  │
└───────────────┘
```

## SQL Syntax

```sql
ST_ASTEXT(<geometry>)
```

## SQL Examples

```sql
SELECT ST_ASTEXT(ST_POINT(1, 2));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
