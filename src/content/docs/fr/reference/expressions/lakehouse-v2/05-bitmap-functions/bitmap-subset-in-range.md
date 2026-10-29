---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE — renvoie un sous-ensemble d'un bitmap compris dans une plage donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

Renvoie un sous-ensemble d'un bitmap compris dans une plage donnée.

## Syntaxe Analyze

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Exemples Analyze

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
