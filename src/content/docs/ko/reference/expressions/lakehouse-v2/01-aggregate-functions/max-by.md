---
title: MAX_BY (Lakehouse v2)
description: MAX_BY — 다른 열의 최댓값에 대응하는 한 열의 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/max-by.md
---

다른 열의 최댓값에 대응하는 한 열의 값을 반환합니다.

## Analyze 구문

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))
```

## Analyze 예제

```python
func.max_by(get_column(table, 'name'), get_column(table, 'salary'))

┌───────┐
│ Alice │
└───────┘
```

## SQL 구문

```sql
MAX_BY(<name>, <salary>)
```

## SQL 예제

```sql
SELECT MAX_BY(name, salary) FROM employees;

┌───────┐
│ Alice │
└───────┘
```
