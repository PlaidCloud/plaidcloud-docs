---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: "BITMAP_SUBSET_LIMIT : génère un sous-bitmap du bitmap source, en partant d'une plage à partir de la valeur de début, avec une limite de taille."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

Génère un sous-bitmap du bitmap source, en partant d'une plage à partir de la valeur de début, avec une limite de taille.

## Syntaxe Analyze

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Exemples Analyze

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## Exemples SQL

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
