---
title: COALESCE (Lakehouse v2)
description: COALESCE – gibt aus einer Liste von Ausdrücken den ersten Ausdruck zurück, der nicht NULL ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

Gibt aus einer Liste von Ausdrücken den ersten Ausdruck zurück, der nicht NULL ist.

## Analyze-Syntax

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Analyze-Beispiele

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## SQL-Syntax

```sql
COALESCE(<nickname>, <name>)
```

## SQL-Beispiele

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
