---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT — renvoie la différence entre deux bitmaps (éléments du premier absents du second).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

Renvoie la différence entre deux bitmaps (éléments du premier absents du second).

## Syntaxe Analyze

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Exemples Analyze

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
