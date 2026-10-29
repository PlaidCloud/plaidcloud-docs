---
title: AVG (Lakehouse v2)
description: AVG – gibt den Durchschnittswert einer numerischen Spalte zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

Gibt den Durchschnittswert einer numerischen Spalte zurück.

## Analyze-Syntax

```python
func.avg(get_column(table, 'salary'))
```

## Analyze-Beispiele

```python
func.avg(get_column(table, 'salary'))
```

## SQL-Syntax

```sql
AVG(<salary>)
```

## SQL-Beispiele

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
