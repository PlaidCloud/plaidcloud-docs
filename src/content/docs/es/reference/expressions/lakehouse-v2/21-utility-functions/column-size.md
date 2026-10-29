---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — Devuelve el tamaño, en bytes, del valor de una columna en su forma serializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

Devuelve el tamaño, en bytes, del valor de una columna en su forma serializada.

## Sintaxis de Analyze

```python
func.column_size(get_column(table, 'name'))
```

## Ejemplos de Analyze

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## Sintaxis de SQL

```sql
COLUMN_SIZE(<expr>)
```

## Ejemplos de SQL

```sql
SELECT name, COLUMN_SIZE(name) FROM users LIMIT 3;

┌──────���┬───────────────────┐
│ name  │ column_size(name) │
├───────┼───────────────────┤
│ Alice │                 5 │
│ Bob   │                 3 │
│ Eve   │                 3 │
└───────┴───────────────────┘
```
