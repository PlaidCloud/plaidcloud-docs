---
title: IFNULL (Lakehouse v2)
description: IFNULL — devuelve la primera expresión si no es NULL; de lo contrario, devuelve la segunda expresión.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

Devuelve la primera expresión si no es NULL; de lo contrario, devuelve la segunda expresión.

## Sintaxis de Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Ejemplos de Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Sintaxis de SQL

```sql
IFNULL(<phone>, 'N/A')
```

## Ejemplos de SQL

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
