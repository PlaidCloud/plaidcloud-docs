---
title: MAX (Lakehouse v2)
description: MAX – gibt den Maximalwert einer Wertemenge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

Gibt den Maximalwert einer Wertemenge zurück.

## Analyze-Syntax

```python
func.max(get_column(table, 'salary'))
```

## Analyze-Beispiele

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## SQL-Syntax

```sql
MAX(<salary>)
```

## SQL-Beispiele

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
