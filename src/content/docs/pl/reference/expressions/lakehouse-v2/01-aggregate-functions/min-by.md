---
title: MIN_BY (Lakehouse v2)
description: MIN_BY — zwraca wartość jednej kolumny powiązaną z minimalną wartością innej kolumny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min-by.md
---

Zwraca wartość jednej kolumny powiązaną z minimalną wartością innej kolumny.

## Składnia Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Przykłady Analyze

```python
func.min_by(get_column(table, 'name'), get_column(table, 'salary'))

┌─────┐
│ Bob │
└─────┘
```

## Składnia SQL

```sql
MIN_BY(<name>, <salary>)
```

## Przykłady SQL

```sql
SELECT MIN_BY(name, salary) FROM employees;

┌─────┐
│ Bob │
└─────┘
```
