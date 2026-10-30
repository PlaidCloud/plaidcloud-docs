---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP — zwraca podbitmapę zaczynającą się od podanej pozycji, z ograniczeniem liczności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

Zwraca podbitmapę zaczynającą się od podanej pozycji, z ograniczeniem liczności.

## Składnia Analyze

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Przykłady Analyze

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
