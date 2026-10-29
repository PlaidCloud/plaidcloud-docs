---
title: BITMAP_HAS_ANY (Lakehouse v1)
description: "BITMAP_HAS_ANY : vérifie si le premier bitmap contient au moins un bit correspondant aux bits du second bitmap."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-any.md
---

Vérifie si le premier bitmap contient au moins un bit correspondant aux bits du second bitmap.

## Syntaxe Analyze

```python
func.bitmap_has_any( <bitmap1>, <bitmap2> )
```

## Exemples Analyze

```python
func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))

┌───────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))  │
├───────────────────────────────────────────────────────────────────────────────┤
│ true                                                                          │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_HAS_ANY( <bitmap1>, <bitmap2> )
```

## Exemples SQL

```sql
SELECT BITMAP_HAS_ANY(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_any(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ true                                                          │
└───────────────────────────────────────────────────────────────┘
```
