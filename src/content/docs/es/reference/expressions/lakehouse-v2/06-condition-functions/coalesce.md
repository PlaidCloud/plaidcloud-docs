---
title: COALESCE (Lakehouse v2)
description: COALESCE — devuelve la primera expresión que no es NULL de una lista de expresiones.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

Devuelve la primera expresión que no es NULL de una lista de expresiones.

## Sintaxis de Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Ejemplos de Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## Sintaxis de SQL

```sql
COALESCE(<nickname>, <name>)
```

## Ejemplos de SQL

```sql
SELECT COALESCE(nickname, first_name, 'Unknown') AS display_name FROM users;

┌──────────────┐
│ display_name │
├──────────────┤
│ Bob          │
│ Alice        │
│ Unknown      │
└──────────────┘
```
