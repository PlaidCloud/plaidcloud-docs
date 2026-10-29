---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: "BITMAP_AND_COUNT : compte le nombre de bits à 1 dans le bitmap en effectuant une opération ET logique."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

Compte le nombre de bits à 1 dans le bitmap en effectuant une opération ET logique.

## Syntaxe Analyze

```python
func.bitmap_and_count( <bitmap> )
```

## Exemples Analyze

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## Exemples SQL

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
