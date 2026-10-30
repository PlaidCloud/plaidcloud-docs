---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT — retorna a contagem de valores distintos na união de um conjunto de bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

Retorna a contagem de valores distintos na união de um conjunto de bitmaps.

## Sintaxe do Analyze

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Exemplos do Analyze

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## Sintaxe SQL

```sql
BITMAP_UNION_COUNT(<bm>)
```

## Exemplos SQL

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
