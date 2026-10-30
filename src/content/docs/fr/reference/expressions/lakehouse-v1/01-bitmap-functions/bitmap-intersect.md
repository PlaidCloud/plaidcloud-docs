---
title: BITMAP_INTERSECT (Lakehouse v1)
description: "BITMAP_INTERSECT : compte le nombre de bits à 1 dans le bitmap en effectuant une opération INTERSECT logique."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

Compte le nombre de bits à 1 dans le bitmap en effectuant une opération INTERSECT logique.

## Syntaxe Analyze

```python
func.bitmap_intersect( <bitmap> )
```

## Exemples Analyze

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_INTERSECT( <bitmap> )
```

## Exemples SQL

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
