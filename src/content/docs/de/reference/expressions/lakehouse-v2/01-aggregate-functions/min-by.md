---
title: MIN_BY (Lakehouse v2)
description: MIN_BY – gibt den Wert einer Spalte zurück, der zum Minimalwert einer anderen Spalte gehört.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

Gibt den Wert einer Spalte zurück, der zum Minimalwert einer anderen Spalte gehört.

## Analyze-Syntax

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze-Beispiele

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## SQL-Syntax

```sql
MIN_BY(<name>, <salary>)
```

## SQL-Beispiele

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
