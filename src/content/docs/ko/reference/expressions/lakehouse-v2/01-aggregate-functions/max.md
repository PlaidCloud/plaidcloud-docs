---
title: MAX (Lakehouse v2)
description: MAX — 값 집합에서 최댓값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max.md
---

값 집합에서 최댓값을 반환합니다.

## Analyze 구문

```python
func.max(get_column(table, 'salary'))
```

## Analyze 예제

```python
func.max(get_column(table, 'salary'))

┌────────┐
│ 150000 │
└────────┘
```

## SQL 구문

```sql
MAX(<salary>)
```

## SQL 예제

```sql
SELECT MAX(salary) FROM employees;

┌────────┐
│ 150000 │
└────────┘
```
