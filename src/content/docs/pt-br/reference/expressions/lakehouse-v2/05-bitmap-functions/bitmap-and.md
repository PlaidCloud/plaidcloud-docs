---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — retorna a interseção de dois bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

Retorna a interseção de dois bitmaps.

## Sintaxe do Analyze

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Exemplos do Analyze

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
