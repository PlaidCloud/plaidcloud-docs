---
title: BITMAP_NOT_COUNT (Lakehouse v1)
description: "BITMAP_NOT_COUNT : compte le nombre de bits à 0 dans le bitmap en effectuant une opération NON logique."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not-count.md
---

Compte le nombre de bits à 0 dans le bitmap en effectuant une opération NON logique.

## Syntaxe Analyze

```python
func.bitmap_not_count( <bitmap> )
```

## Exemples Analyze

```python
func.bitmap_not_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_not_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_NOT_COUNT( <bitmap> )
```

## Exemples SQL

```sql
SELECT BITMAP_NOT_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_not_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
