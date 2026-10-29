---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — retorna o valor mínimo de um bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

Retorna o valor mínimo de um bitmap.

## Sintaxe do Analyze

```python
func.bitmap_min(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
BITMAP_MIN(<bitmap>)
```

## Exemplos SQL

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
