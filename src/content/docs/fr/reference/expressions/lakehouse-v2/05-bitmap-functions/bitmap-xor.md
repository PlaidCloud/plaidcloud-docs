---
title: BITMAP_XOR (Lakehouse v2)
description: BITMAP_XOR — renvoie la différence symétrique de deux bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-xor.md
---

Renvoie la différence symétrique de deux bitmaps.

## Syntaxe Analyze

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Exemples Analyze

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
