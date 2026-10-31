---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY — verifica se dois bitmaps têm elementos em comum.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

Verifica se dois bitmaps têm elementos em comum.

## Sintaxe do Analyze

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Exemplos do Analyze

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## Exemplos SQL

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```
