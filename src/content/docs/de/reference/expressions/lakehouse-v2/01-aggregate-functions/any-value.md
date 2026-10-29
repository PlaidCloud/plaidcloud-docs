---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE gibt einen beliebigen Wert aus einer Gruppe von Zeilen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

Gibt einen beliebigen Wert aus einer Gruppe von Zeilen zurück.

## Analyze-Syntax

```python
func.any_value(get_column(table, 'department'))
```

## Analyze-Beispiele

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## SQL-Syntax

```sql
ANY_VALUE(<department>)
```

## SQL-Beispiele

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
