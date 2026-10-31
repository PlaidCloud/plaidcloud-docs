---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — agrega valores enteros en un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

Agrega valores enteros en un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Ejemplos de Analyze

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_AGG(<id>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
