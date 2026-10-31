---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — sprawdza, czy bitmapa zawiera określoną wartość.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

Sprawdza, czy bitmapa zawiera określoną wartość.

## Składnia Analyze

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Przykłady Analyze

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## Składnia SQL

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## Przykłady SQL

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
