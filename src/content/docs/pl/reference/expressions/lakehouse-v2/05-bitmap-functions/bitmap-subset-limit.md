---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT — zwraca podzbiór bitmapy zaczynający się od przesunięcia, z ograniczeniem liczności.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

Zwraca podzbiór bitmapy zaczynający się od przesunięcia, z ograniczeniem liczności.

## Składnia Analyze

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Przykłady Analyze

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
