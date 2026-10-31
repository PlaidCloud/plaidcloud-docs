---
title: COALESCE (Lakehouse v2)
description: COALESCE — renvoie la première expression non NULL d'une liste d'expressions.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

Renvoie la première expression non NULL d'une liste d'expressions.

## Syntaxe Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Exemples Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## Syntaxe SQL

```sql
COALESCE(<nickname>, <name>)
```

## Exemples SQL

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
