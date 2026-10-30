---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — convertit un tableau d'entiers en bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

Convertit un tableau d'entiers en bitmap.

## Syntaxe Analyze

```python
func.array_to_bitmap([1, 2, 3])
```

## Exemples Analyze

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
