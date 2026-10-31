---
title: BOOL_OR (Lakehouse v2)
description: BOOL_OR — 그룹의 값 중 하나라도 TRUE이면 TRUE를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bool-or.md
---

그룹의 값 중 하나라도 TRUE이면 TRUE를 반환합니다.

## Analyze 구문

```python
func.bool_or(get_column(table, 'is_active'))
```

## Analyze 예제

```python
func.bool_or(get_column(table, 'is_active'))
```

## SQL 구문

```sql
BOOL_OR(<is_active>)
```

## SQL 예제

```sql
SELECT department, BOOL_OR(is_active) FROM employees GROUP BY department;

┌────────────┬─────────────────────┐
│ department │ bool_or(is_active)  │
├────────────┼─────────────────────┤
│ Sales      │                   1 │
│ IT         │                   1 │
└────────────┴─────────────────────┘
```
