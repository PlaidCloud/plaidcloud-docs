---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT — devolve a contagem de valores inteiros distintos (agregação).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

Devolve a contagem de valores inteiros distintos (agregação).

## Sintaxe do Analyze

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Exemplos do Analyze

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## Sintaxe SQL

```sql
BITMAP_UNION_INT(<id>)
```

## Exemplos SQL

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
