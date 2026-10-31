---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT — zwraca liczbę różnych wartości całkowitych (agregat).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

Zwraca liczbę różnych wartości całkowitych (agregat).

## Składnia Analyze

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Przykłady Analyze

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## Składnia SQL

```sql
BITMAP_UNION_INT(<id>)
```

## Przykłady SQL

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
