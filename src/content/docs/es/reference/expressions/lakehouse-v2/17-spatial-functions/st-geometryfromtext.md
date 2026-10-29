---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — crea una geometría a partir de una cadena WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

Crea una geometría a partir de una cadena WKT (Well-Known Text).

## Sintaxis de Analyze

```python
func.st_geometryfromtext(<wkt>)
```

## Ejemplos de Analyze

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxis de SQL

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## Ejemplos de SQL

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
