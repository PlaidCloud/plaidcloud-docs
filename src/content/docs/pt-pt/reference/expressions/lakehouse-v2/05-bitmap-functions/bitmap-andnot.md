---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT — devolve a diferença de dois bitmaps (elementos presentes no primeiro mas não no segundo).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

Devolve a diferença de dois bitmaps (elementos presentes no primeiro mas não no segundo).

## Sintaxe do Analyze

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Exemplos do Analyze

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
