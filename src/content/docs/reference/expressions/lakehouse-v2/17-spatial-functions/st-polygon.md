---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON — creates a polygon geometry from a WKT string.
---

Creates a polygon geometry from a WKT string.

## Analyze Syntax

```python
func.st_polygon(<wkt>)
```

## Analyze Examples

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL Syntax

```sql
ST_POLYGON(<wkt>)
```

## SQL Examples

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
