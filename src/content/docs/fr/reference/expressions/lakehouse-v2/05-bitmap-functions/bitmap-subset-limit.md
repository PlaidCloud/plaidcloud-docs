---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT — renvoie un sous-ensemble d'un bitmap à partir d'un décalage, avec une limite de cardinalité.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

Renvoie un sous-ensemble d'un bitmap à partir d'un décalage, avec une limite de cardinalité.

## Syntaxe Analyze

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Exemples Analyze

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
