---
title: COALESCE (Lakehouse v2)
description: COALESCE — zwraca pierwsze wyrażenie różne od NULL z listy wyrażeń.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/coalesce.md
---

Zwraca pierwsze wyrażenie różne od NULL z listy wyrażeń.

## Składnia Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'))
```

## Przykłady Analyze

```python
func.coalesce(get_column(table, 'nickname'), get_column(table, 'name'), 'Unknown')
```

## Składnia SQL

```sql
COALESCE(<nickname>, <name>)
```

## Przykłady SQL

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
