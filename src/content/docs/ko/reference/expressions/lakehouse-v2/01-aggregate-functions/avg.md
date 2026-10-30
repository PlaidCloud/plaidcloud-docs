---
title: AVG (Lakehouse v2)
description: AVG — 숫자 열의 평균값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/avg.md
---

숫자 열의 평균값을 반환합니다.

## Analyze 구문

```python
func.avg(get_column(table, 'salary'))
```

## Analyze 예제

```python
func.avg(get_column(table, 'salary'))
```

## SQL 구문

```sql
AVG(<salary>)
```

## SQL 예제

```sql
SELECT department, AVG(salary) FROM employees GROUP BY department;

┌────────────┬──────────────┐
│ department │ avg(salary)  │
├────────────┼──────────────┤
│ Sales      │     65000.00 │
│ IT         │     82000.00 │
└────────────┴──────────────┘
```
