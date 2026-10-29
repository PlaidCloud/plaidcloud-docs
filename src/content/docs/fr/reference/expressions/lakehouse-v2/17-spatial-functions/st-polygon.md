---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON — crée une géométrie de type polygone à partir d'une chaîne WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

Crée une géométrie de type polygone à partir d'une chaîne WKT.

## Syntaxe Analyze

```python
func.st_polygon(<wkt>)
```

## Exemples Analyze

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Syntaxe SQL

```sql
ST_POLYGON(<wkt>)
```

## Exemples SQL

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
