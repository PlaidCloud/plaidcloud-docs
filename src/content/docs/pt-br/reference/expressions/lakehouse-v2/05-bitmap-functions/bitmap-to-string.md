---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING — converte um bitmap em uma string separada por vírgulas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

Converte um bitmap em uma string separada por vírgulas.

## Sintaxe do Analyze

```python
func.bitmap_to_string(<bitmap>)
```

## Exemplos do Analyze

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## Sintaxe SQL

```sql
BITMAP_TO_STRING(<bitmap>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
