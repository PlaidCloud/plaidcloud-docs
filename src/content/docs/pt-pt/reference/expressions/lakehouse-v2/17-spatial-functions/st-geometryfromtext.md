---
title: ST_GEOMETRYFROMTEXT (Lakehouse v2)
description: ST_GEOMETRYFROMTEXT — cria uma geometria a partir de uma cadeia de caracteres WKT (Well-Known Text).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/17-spatial-functions/st-geometryfromtext.md
---

Cria uma geometria a partir de uma cadeia de caracteres WKT (Well-Known Text).

## Sintaxe de Analyze

```python
func.st_geometryfromtext(<wkt>)
```

## Exemplos de Analyze

```python
func.st_geometryfromtext('POINT (1 2)')

┌────────────┐
│ (geometry)  │
└────────────┘
```

## Sintaxe SQL

```sql
ST_GEOMETRYFROMTEXT(<wkt>)
```

## Exemplos SQL

```sql
SELECT ST_ASTEXT(ST_GEOMETRYFROMTEXT('POINT (1 2)'));

┌─────────────┐
│ POINT (1 2)  │
└─────────────┘
```
