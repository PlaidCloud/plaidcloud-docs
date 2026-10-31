---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON — erstellt eine Polygongeometrie aus einer WKT-Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

Erstellt eine Polygongeometrie aus einer WKT-Zeichenfolge.

## Analyze-Syntax

```python
func.st_polygon(<wkt>)
```

## Analyze-Beispiele

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## SQL-Syntax

```sql
ST_POLYGON(<wkt>)
```

## SQL-Beispiele

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
