---
title: BITMAP_OR_COUNT (Lakehouse v1)
description: "BITMAP_OR_COUNT : compte le nombre de bits à 1 dans le bitmap en effectuant une opération OU logique."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or-count.md
---

Compte le nombre de bits à 1 dans le bitmap en effectuant une opération OU logique.

## Syntaxe Analyze

```python
func.bitmap_or_count( <bitmap> )
```

## Exemples Analyze

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## Exemples SQL

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```
