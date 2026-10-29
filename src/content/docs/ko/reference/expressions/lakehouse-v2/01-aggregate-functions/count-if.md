---
title: COUNT_IF (Lakehouse v2)
description: COUNT_IF — 식이 TRUE인 행의 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count-if.md
---

식이 TRUE인 행의 개수를 반환합니다.

## Analyze 구문

```python
func.count_if(get_column(table, 'salary') > 80000)
```

## Analyze 예제

```python
func.count_if(get_column(table, 'salary') > 80000)

┌────┐
│ 42 │
└────┘
```

## SQL 구문

```sql
COUNT_IF(<salary> > 80000)
```

## SQL 예제

```sql
SELECT COUNT_IF(salary > 80000) FROM employees;

┌────┐
│ 42 │
└────┘
```
