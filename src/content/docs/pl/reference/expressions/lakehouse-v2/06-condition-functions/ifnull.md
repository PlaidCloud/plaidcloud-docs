---
title: IFNULL (Lakehouse v2)
description: IFNULL — zwraca pierwsze wyrażenie, jeśli nie jest NULL; w przeciwnym razie zwraca drugie wyrażenie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/06-condition-functions/ifnull.md
---

Zwraca pierwsze wyrażenie, jeśli nie jest NULL; w przeciwnym razie zwraca drugie wyrażenie.

## Składnia Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Przykłady Analyze

```python
func.ifnull(get_column(table, 'phone'), 'N/A')
```

## Składnia SQL

```sql
IFNULL(<phone>, 'N/A')
```

## Przykłady SQL

```sql
SELECT name, IFNULL(phone, 'N/A') AS phone FROM contacts;

┌─────────┬──────────┐
│ name    │ phone    │
├─────────┼──────────┤
│ Alice   │ 555-1234 │
│ Bob     │ N/A      │
└─────────┴──────────┘
```
