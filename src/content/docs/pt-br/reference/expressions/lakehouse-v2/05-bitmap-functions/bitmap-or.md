---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR — retorna a união de dois bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-or.md
---

Retorna a união de dois bitmaps.

## Sintaxe do Analyze

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Exemplos do Analyze

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
