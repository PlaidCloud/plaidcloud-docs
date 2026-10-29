---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT — HyperLogLog를 사용하여 고유 값의 근사 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

HyperLogLog를 사용하여 고유 값의 근사 개수를 반환합니다.

## Analyze 구문

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Analyze 예제

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## SQL 구문

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## SQL 예제

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
