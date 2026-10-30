---
title: GROUPING_ID (Lakehouse v2)
description: GROUPING_ID — 열의 그룹화에 해당하는 비트 마스크를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/grouping-id.md
---

열의 그룹화에 해당하는 비트 마스크를 반환합니다.

## Analyze 구문

```python
func.grouping_id(get_column(table, 'a'), get_column(table, 'b'))
```

## Analyze 예제

```python
func.grouping_id(get_column(table, 'department'), get_column(table, 'year'))

┌───┐
│ 0 │
└───┘
```

## SQL 구문

```sql
GROUPING_ID(<a>, <b>)
```

## SQL 예제

```sql
SELECT department, year, GROUPING_ID(department, year), SUM(salary)
FROM employees GROUP BY ROLLUP(department, year);

┌───┐
│ 0 │
└───┘
```
