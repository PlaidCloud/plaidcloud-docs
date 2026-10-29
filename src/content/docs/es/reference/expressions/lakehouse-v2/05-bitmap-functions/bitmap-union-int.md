---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT — devuelve el número de valores enteros distintos (agregación).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

Devuelve el número de valores enteros distintos (agregación).

## Sintaxis de Analyze

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Ejemplos de Analyze

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## Sintaxis de SQL

```sql
BITMAP_UNION_INT(<id>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
