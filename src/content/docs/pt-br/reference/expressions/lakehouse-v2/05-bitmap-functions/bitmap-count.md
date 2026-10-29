---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT — retorna o número de bits definidos em um bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

Retorna o número de bits definidos em um bitmap.

## Sintaxe do Analyze

```python
func.bitmap_count(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## Sintaxe SQL

```sql
BITMAP_COUNT(<bitmap>)
```

## Exemplos SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
