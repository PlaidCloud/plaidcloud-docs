---
title: BITMAP (Lakehouse v2)
description: BITMAP devuelve la unión de mapas de bits de un conjunto de valores. Se suele usar con BITMAP_AGG.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

Devuelve la unión de mapas de bits de un conjunto de valores. Se suele usar con BITMAP_AGG.

## Sintaxis de Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Ejemplos de Analyze

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP(<id>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
