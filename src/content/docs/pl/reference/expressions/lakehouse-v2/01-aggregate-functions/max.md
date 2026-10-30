---
title: MAX (Lakehouse v2)
description: MAX — zwraca maksymalną wartość w zbiorze wartości.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

Zwraca maksymalną wartość w zbiorze wartości.

## Składnia Analyze

```python
func.max(get_column(table, 'salary'))
```

## Przykłady Analyze

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## Składnia SQL

```sql
MAX(<salary>)
```

## Przykłady SQL

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
