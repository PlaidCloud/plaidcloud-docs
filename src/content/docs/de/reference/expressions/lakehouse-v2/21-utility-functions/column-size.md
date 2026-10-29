---
title: COLUMN_SIZE (Lakehouse v2)
description: COLUMN_SIZE — gibt die Größe eines Spaltenwerts in seiner serialisierten Form in Bytes zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/column-size.md
---

Gibt die Größe eines Spaltenwerts in seiner serialisierten Form in Bytes zurück.

## Analyze-Syntax

```python
func.column_size(get_column(table, 'name'))
```

## Analyze-Beispiele

```python
func.column_size(get_column(table, 'name'))

┌───┐
│ 5 │
└───┘
```

## SQL-Syntax

```sql
COLUMN_SIZE(<expr>)
```

## SQL-Beispiele

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
