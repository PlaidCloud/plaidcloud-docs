---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR — renvoie l'union de deux bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-or.md
---

Renvoie l'union de deux bitmaps.

## Syntaxe Analyze

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Exemples Analyze

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
