---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v1)
description: "BITMAP_SUBSET_IN_RANGE : génère un sous-bitmap du bitmap source dans une plage donnée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-in-range.md
---

Génère un sous-bitmap du bitmap source dans une plage donnée.

## Syntaxe Analyze

```python
func.bitmap_subset_in_range( <bitmap>, <start>, <end> )
```

## Exemples Analyze

```python
func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9)

┌─────────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_in_range(func.build_bitmap([5, 7, 9]), 6, 9) │
├─────────────────────────────────────────────────────────────────┤
│ 7                                                               │
└─────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_SUBSET_IN_RANGE( <bitmap>, <start>, <end> )
```

## Exemples SQL

```sql
SELECT BITMAP_SUBSET_IN_RANGE(BUILD_BITMAP([5,7,9]), 6, 9)::String;

┌───────────────────────────────────────────────────────────────┐
│ bitmap_subset_in_range(build_bitmap([5, 7, 9]), 6, 9)::string │
├───────────────────────────────────────────────────────────────┤
│ 7                                                             │
└───────────────────────────────────────────────────────────────┘
```
