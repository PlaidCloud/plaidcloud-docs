---
title: PERCENTILE_APPROX_WEIGHT (Lakehouse v2)
description: PERCENTILE_APPROX_WEIGHT — 가중치를 적용한 근사 백분위수 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx-weight.md
---

가중치를 적용한 근사 백분위수 값을 반환합니다.

## Analyze 구문

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)
```

## Analyze 예제

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)

┌──────┐
│ 72.5 │
└──────┘
```

## SQL 구문

```sql
PERCENTILE_APPROX_WEIGHT(<val>, <weight>, 0.5)
```

## SQL 예제

```sql
SELECT PERCENTILE_APPROX_WEIGHT(val, weight, 0.5) FROM data;

┌──────┐
│ 72.5 │
└──────┘
```
