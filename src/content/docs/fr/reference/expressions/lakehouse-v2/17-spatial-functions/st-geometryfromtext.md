---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — crée une géométrie à partir d'une chaîne WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

Crée une géométrie à partir d'une chaîne WKT (Well-Known Text).

## Syntaxe Analyze

```python
func.st_geometryfromtext(<wkt>)
```

## Exemples Analyze

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Syntaxe SQL

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## Exemples SQL

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
