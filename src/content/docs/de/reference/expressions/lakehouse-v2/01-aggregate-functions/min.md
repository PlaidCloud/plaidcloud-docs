---
title: MIN (Lakehouse v2)
description: MIN – gibt den Minimalwert einer Wertemenge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

Gibt den Minimalwert einer Wertemenge zurück.

## Analyze-Syntax

```python
func.min(get_column(table, 'salary'))
```

## Analyze-Beispiele

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## SQL-Syntax

```sql
MIN(<salary>)
```

## SQL-Beispiele

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
