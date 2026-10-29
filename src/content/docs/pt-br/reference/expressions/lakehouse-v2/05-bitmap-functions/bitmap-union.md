---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION — retorna a união de um conjunto de bitmaps (agregação).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

Retorna a união de um conjunto de bitmaps (agregação).

## Sintaxe do Analyze

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Exemplos do Analyze

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_UNION(<bm>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
