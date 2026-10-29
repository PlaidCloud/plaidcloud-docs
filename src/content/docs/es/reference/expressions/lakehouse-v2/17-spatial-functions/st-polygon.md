---
title: ST_POLYGON (Lakehouse v2)
description: ST_POLYGON — Crea una geometría de polígono a partir de una cadena WKT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-polygon.md
---

Crea una geometría de polígono a partir de una cadena WKT.

## Sintaxis de Analyze

```python
func.st_polygon(<wkt>)
```

## Ejemplos de Analyze

```python
func.st_polygon('POLYGON((0 0,10 0,10 10,0 10,0 0))')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxis de SQL

```sql
ST_POLYGON(<wkt>)
```

## Ejemplos de SQL

```sql
SELECT ST_ASTEXT(ST_POLYGON('POLYGON((0 0,10 0,10 10,0 10,0 0))'));

┌─────────────────────────────────────────┐
│ POLYGON ((0 0, 10 0, 10 10, 0 10, 0 0))  │
└─────────────────────────────────────────┘
```
