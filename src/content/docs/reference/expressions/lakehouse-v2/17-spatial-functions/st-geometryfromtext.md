---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — creates a geometry from a WKT (Well-Known Text) string.
---

Creates a geometry from a WKT (Well-Known Text) string.

## Analyze Syntax

```python
func.st_geometryfromtext(<wkt>)
```

## Analyze Examples

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL Syntax

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## SQL Examples

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
