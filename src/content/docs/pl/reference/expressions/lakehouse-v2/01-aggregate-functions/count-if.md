---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF — zwraca liczbę wierszy, dla których wyrażenie ma wartość TRUE.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

Zwraca liczbę wierszy, dla których wyrażenie ma wartość TRUE.

## Składnia Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Przykłady Analyze

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## Składnia SQL

```sql
COUNT_IF(<salary> > 80000)
```

## Przykłady SQL

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
