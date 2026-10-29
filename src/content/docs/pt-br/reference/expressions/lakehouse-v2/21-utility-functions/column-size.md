---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — retorna o tamanho em bytes de um valor de coluna em sua forma serializada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

Retorna o tamanho em bytes de um valor de coluna em sua forma serializada.

## Analyze Syntax

```python
func.column_size(get_column(table, 'name'))
```

## Analyze Examples

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## SQL Syntax

```sql
COLUMN_SIZE(<expr>)
```

## SQL Examples

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
