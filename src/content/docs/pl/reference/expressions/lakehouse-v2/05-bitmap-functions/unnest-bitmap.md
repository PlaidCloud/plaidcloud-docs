---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP — rozwija bitmapę do zbioru wierszy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

Rozwija bitmapę do zbioru wierszy.

## Składnia Analyze

```python
func.unnest_bitmap(<bitmap>)
```

## Przykłady Analyze

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## Składnia SQL

```sql
UNNEST_BITMAP(<bitmap>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
