---
title: SUM (Lakehouse v2)
description: SUM — zwraca sumę wszystkich wartości w grupie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

Zwraca sumę wszystkich wartości w grupie.

## Składnia Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Przykłady Analyze

```python
func.sum(get_column(table, 'amount'))
```

## Składnia SQL

```sql
SUM(<amount>)
```

## Przykłady SQL

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
