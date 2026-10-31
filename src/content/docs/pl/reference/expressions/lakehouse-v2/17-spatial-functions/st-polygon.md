---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON — tworzy geometrię wielokąta na podstawie ciągu WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

Tworzy geometrię wielokąta na podstawie ciągu WKT.

## Składnia Analyze

```python
func.st_polygon(<wkt>)
```

## Przykłady Analyze

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Składnia SQL

```sql
ST_POLYGON(<wkt>)
```

## Przykłady SQL

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
