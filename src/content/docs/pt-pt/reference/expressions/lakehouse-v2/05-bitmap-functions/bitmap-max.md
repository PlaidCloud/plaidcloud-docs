---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX — devolve o valor máximo de um bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

Devolve o valor máximo de um bitmap.

## Sintaxe do Analyze

```python
func.bitmap_max(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## Sintaxe SQL

```sql
BITMAP_MAX(<bitmap>)
```

## Exemplos SQL

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
