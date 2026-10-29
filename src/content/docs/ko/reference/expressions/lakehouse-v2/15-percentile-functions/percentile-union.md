---
title: PERCENTILE_UNION (Lakehouse v2)
description: PERCENTILE_UNION — 여러 백분위수 상태의 합집합을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-union.md
---

여러 백분위수 상태의 합집합을 반환합니다.

## Analyze 구문

```python
func.percentile_union(<state>)
```

## Analyze 예제

```python
func.percentile_union(get_column(table, 'pct_state'))

┌────────────────┐
│ (merged state)  │
└────────────────┘
```

## SQL 구문

```sql
PERCENTILE_UNION(<state>)
```

## SQL 예제

```sql
SELECT PERCENTILE_APPROX_RAW(PERCENTILE_UNION(pct_state), 0.5) FROM agg_table;

┌───────┐
│ 72500  │
└───────┘
```
