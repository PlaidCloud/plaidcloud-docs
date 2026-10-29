---
title: MAX_BY (Lakehouse v2)
description: MAX_BY — zwraca wartość jednej kolumny powiązaną z maksymalną wartością innej kolumny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

Zwraca wartość jednej kolumny powiązaną z maksymalną wartością innej kolumny.

## Składnia Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Przykłady Analyze

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## Składnia SQL

```sql
MAX_BY(<name>, <salary>)
```

## Przykłady SQL

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
