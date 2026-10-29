---
title: AVG (Lakehouse v2)
description: AVG — zwraca średnią wartość kolumny numerycznej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

Zwraca średnią wartość kolumny numerycznej.

## Składnia w Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Przykłady w Analyze

```python
func.avg(get_column(table, 'salary'))
```

## Składnia SQL

```sql
AVG(<salary>)
```

## Przykłady SQL

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
