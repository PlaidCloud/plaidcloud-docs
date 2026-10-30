---
title: MIN (Lakehouse v2)
description: MIN — 값 집합에서 최솟값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/min.md
---

값 집합에서 최솟값을 반환합니다.

## Analyze 구문

```python
func.min(get_column(table, 'salary'))
```

## Analyze 예제

```python
func.min(get_column(table, 'salary'))

┌───────┐
│ 35000 │
└───────┘
```

## SQL 구문

```sql
MIN(<salary>)
```

## SQL 예제

```sql
SELECT MIN(salary) FROM employees;

┌───────┐
│ 35000 │
└───────┘
```
