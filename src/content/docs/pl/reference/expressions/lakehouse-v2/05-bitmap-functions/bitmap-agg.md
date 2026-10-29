---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — agreguje wartości całkowite do bitmapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

Agreguje wartości całkowite do bitmapy.

## Składnia Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Przykłady Analyze

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_AGG(<id>)
```

## Przykłady SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
