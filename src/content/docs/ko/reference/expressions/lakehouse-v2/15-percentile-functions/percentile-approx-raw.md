---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 PERCENTILE_APPROX_RAW 백분위수 함수를 사용합니다. 미리 계산된 백분위수 상태에서 근사 백분위수 값을 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

미리 계산된 백분위수 상태에서 근사 백분위수 값을 반환합니다.

## Analyze 구문

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Analyze 예제

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## SQL 구문

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## SQL 예제

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
