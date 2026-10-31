---
title: COUNT (Lakehouse v2)
description: COUNT — 행 또는 NULL이 아닌 값의 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/count.md
---

행 또는 NULL이 아닌 값의 개수를 반환합니다.

## Analyze 구문

```python
func.count()
```

## Analyze 예제

```python
func.count()
```

## SQL 구문

```sql
COUNT()
```

## SQL 예제

```sql
SELECT COUNT(*) FROM employees;

┌──────────┐
│ count(*) │
├──────────┤
│     1000 │
└──────────┘

SELECT COUNT(DISTINCT department) FROM employees;

┌──────────────────────────────┐
│ count(distinct department)   │
├──────────────────────────────┤
│                            5 │
└──────────────────────────────┘
```
