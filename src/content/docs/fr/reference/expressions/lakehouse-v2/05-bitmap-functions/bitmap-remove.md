---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE — supprime une valeur donnée d'un bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

Supprime une valeur donnée d'un bitmap.

## Syntaxe Analyze

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Exemples Analyze

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
