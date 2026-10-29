---
title: COALESCE (Lakehouse v2)
description: COALESCE — retorna a primeira expressão não NULL de uma lista de expressões.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

Retorna a primeira expressão não NULL de uma lista de expressões.

## Sintaxe do Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Exemplos do Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## Sintaxe SQL

```sql
COALESCE(<nickname>, <name>)
```

## Exemplos SQL

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
