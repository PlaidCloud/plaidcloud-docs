---
title: AVG (Lakehouse v2)
description: AVG — devuelve el valor promedio de una columna numérica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

Devuelve el valor promedio de una columna numérica.

## Analyze Syntax

```python
func.avg(get_column(table, 'salary'))
```

## Analyze Examples

```python
func.avg(get_column(table, 'salary'))
```

## SQL Syntax

```sql
AVG(<salary>)
```

## SQL Examples

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
