---
title: IFNULL (Lakehouse v2)
description: IFNULL – gibt den ersten Ausdruck zurück, wenn er nicht NULL ist, andernfalls den zweiten Ausdruck.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

Gibt den ersten Ausdruck zurück, wenn er nicht NULL ist, andernfalls den zweiten Ausdruck.

## Analyze-Syntax

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Analyze-Beispiele

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## SQL-Syntax

```sql
IFNULL(<phone>, 'N/A')
```

## SQL-Beispiele

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
