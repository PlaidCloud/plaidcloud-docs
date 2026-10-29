---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING — convertit une chaîne d'entiers séparés par des virgules en bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

Convertit une chaîne d'entiers séparés par des virgules en bitmap.

## Syntaxe Analyze

```python
func.bitmap_from_string(<str>)
```

## Exemples Analyze

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_FROM_STRING(<str>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
