---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — agrega valores inteiros num bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

Agrega valores inteiros num bitmap.

## Sintaxe do Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Exemplos do Analyze

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_AGG(<id>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
