---
title: MIN (Lakehouse v2)
description: MIN — zwraca minimalną wartość w zbiorze wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

Zwraca minimalną wartość w zbiorze wartości.

## Składnia Analyze

```python
func.min(get_column(table, 'salary'))
```

## Przykłady Analyze

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## Składnia SQL

```sql
MIN(<salary>)
```

## Przykłady SQL

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
