---
title: GROUPING (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 GROUPING 집계 함수를 사용합니다. GROUP BY 절의 지정한 열이 집계되었는지 여부를 나타내며, 집계되었으면 1을 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping.md
---

GROUP BY 절의 지정한 열이 집계되었는지 여부를 나타냅니다. 집계되었으면 1, 그렇지 않으면 0을 반환합니다.

## Analyze 구문

```python
func.grouping(get_column(table, 'department'))
```

## Analyze 예제

```python
func.grouping(get_column(table, 'department'))
```

## SQL 구문

```sql
GROUPING(<department>)
```

## SQL 예제

```sql
SELECT department, GROUPING(department), SUM(salary)
FROM employees GROUP BY ROLLUP(department);

┌────────────┬───────────────────────┬─────────────┐
│ department │ grouping(department)  │ sum(salary)  │
├────────────┼───────────────────────┼─────────────┤
│ Sales      │                     0 │      195000 │
│ IT         │                     0 │      246000 │
│ NULL       │                     1 │      441000 │
└────────────┴───────────────────────┴─────────────┘
```
