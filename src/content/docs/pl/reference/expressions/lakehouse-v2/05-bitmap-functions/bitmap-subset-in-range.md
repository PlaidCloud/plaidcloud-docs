---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE — zwraca podzbiór bitmapy mieszczący się w podanym zakresie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

Zwraca podzbiór bitmapy mieszczący się w podanym zakresie.

## Składnia Analyze

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Przykłady Analyze

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
