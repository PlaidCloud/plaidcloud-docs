---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE — zwraca dowolną wartość z grupy wierszy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

Zwraca dowolną wartość z grupy wierszy.

## Składnia Analyze

```python
func.any_value(get_column(table, 'department'))
```

## Przykłady Analyze

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## Składnia SQL

```sql
ANY_VALUE(<department>)
```

## Przykłady SQL

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
