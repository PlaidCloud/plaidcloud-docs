---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — t-digest 알고리즘을 사용하여 근사 백분위수 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

t-digest 알고리즘을 사용하여 근사 백분위수 값을 반환합니다.

## Analyze 구문

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Analyze 예제

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## SQL 구문

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## SQL 예제

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
