---
title: BITMAP_CONTAINS (Lakehouse v1)
description: "BITMAP_CONTAINS : vérifie si le bitmap contient une valeur donnée."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

Vérifie si le bitmap contient une valeur donnée.


## Syntaxe Analyze

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Exemples Analyze

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## Exemples SQL

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
