---
title: SUM (Lakehouse v2)
description: SUM — 그룹에 속한 모든 값의 합계를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum.md
---

그룹에 속한 모든 값의 합계를 반환합니다.

## Analyze 구문

```python
func.sum(get_column(table, 'amount'))
```

## Analyze 예제

```python
func.sum(get_column(table, 'amount'))
```

## SQL 구문

```sql
SUM(<amount>)
```

## SQL 예제

```sql
SELECT department, SUM(salary) FROM employees GROUP BY department;

┌────────────┬─────────────┐
│ department │ sum(salary) │
├────────────┼─────────────┤
│ Sales      │      195000 │
│ IT         │      246000 │
│ HR         │      210000 │
└────────────┴─────────────┘
```
