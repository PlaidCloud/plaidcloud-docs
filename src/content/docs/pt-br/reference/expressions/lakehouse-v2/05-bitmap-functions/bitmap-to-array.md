---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY — converte um bitmap em um array de inteiros.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-array.md
---

Converte um bitmap em um array de inteiros.

## Sintaxe do Analyze

```python
func.bitmap_to_array(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## Sintaxe SQL

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
