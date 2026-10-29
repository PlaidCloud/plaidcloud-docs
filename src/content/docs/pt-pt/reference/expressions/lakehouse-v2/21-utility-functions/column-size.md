---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — devolve o tamanho, em bytes, do valor de uma coluna na sua forma serializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

Devolve o tamanho, em bytes, do valor de uma coluna na sua forma serializada.

## Sintaxe do Analyze

```python
func.column_size(get_column(table, 'name'))
```

## Exemplos do Analyze

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## Sintaxe SQL

```sql
COLUMN_SIZE(<expr>)
```

## Exemplos SQL

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
