---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY — convertit un bitmap en tableau d'entiers.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-array.md
---

Convertit un bitmap en tableau d'entiers.

## Syntaxe Analyze

```python
func.bitmap_to_array(<bitmap>)
```

## Exemples Analyze

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Syntaxe SQL

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
