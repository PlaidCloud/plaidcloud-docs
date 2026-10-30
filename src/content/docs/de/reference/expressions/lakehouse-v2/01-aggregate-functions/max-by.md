---
title: MAX_BY (Lakehouse v2)
description: MAX_BY – gibt den Wert einer Spalte zurück, der zum Maximalwert einer anderen Spalte gehört.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

Gibt den Wert einer Spalte zurück, der zum Maximalwert einer anderen Spalte gehört.

## Analyze-Syntax

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze-Beispiele

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## SQL-Syntax

```sql
MAX_BY(<name>, <salary>)
```

## SQL-Beispiele

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
