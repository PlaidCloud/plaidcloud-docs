---
title: ANY_VALUE (Lakehouse v2)
description: ANY_VALUE — 행 그룹에서 임의의 값 하나를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/any-value.md
---

행 그룹에서 임의의 값 하나를 반환합니다.

## Analyze 구문

```python
func.any_value(get_column(table, 'department'))
```

## Analyze 예제

```python
func.any_value(get_column(table, 'department'))

┌───────┐
│ Sales │
└───────┘
```

## SQL 구문

```sql
ANY_VALUE(<department>)
```

## SQL 예제

```sql
SELECT ANY_VALUE(department) FROM employees;

┌───────┐
│ Sales │
└───────┘
```
