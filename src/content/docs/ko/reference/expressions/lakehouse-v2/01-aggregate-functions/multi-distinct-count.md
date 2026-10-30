---
title: MULTI_DISTINCT_COUNT (Lakehouse v2)
description: MULTI_DISTINCT_COUNT — 고유 값의 개수를 반환합니다. COUNT(DISTINCT)와 동일합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-count.md
---

고유 값의 개수를 반환합니다. COUNT(DISTINCT)와 동일합니다.

## Analyze 구문

```python
func.multi_distinct_count(get_column(table, 'dept'))
```

## Analyze 예제

```python
func.multi_distinct_count(get_column(table, 'department'))

┌───┐
│ 5 │
└───┘
```

## SQL 구문

```sql
MULTI_DISTINCT_COUNT(<dept>)
```

## SQL 예제

```sql
SELECT MULTI_DISTINCT_COUNT(department) FROM employees;

┌───┐
│ 5 │
└───┘
```
