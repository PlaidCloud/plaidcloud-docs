---
title: BITMAP_UNION (Lakehouse v1)
description: "BITMAP_UNION : compte le nombre de bits à 1 dans le bitmap en effectuant une opération UNION logique."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

Compte le nombre de bits à 1 dans le bitmap en effectuant une opération UNION logique.

## Syntaxe Analyze

```python
func.bitmap_union( <bitmap> )
```

## Exemples Analyze

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_UNION( <bitmap> )
```

## Exemples SQL

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
