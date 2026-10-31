---
title: DS_HLL_ACCUMULATE (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 DS_HLL_ACCUMULATE 집계 함수를 사용합니다. 근사 고유 개수 계산을 위해 값을 DataSketches HLL 스케치로 누적합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-accumulate.md
---

근사 고유 개수 계산을 위해 값을 DataSketches HLL 스케치로 누적합니다.

## Analyze 구문

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))
```

## Analyze 예제

```python
func.ds_hll_accumulate(get_column(table, 'user_id'))

┌──────────────┐
│ (hll sketch) │
└──────────────┘
```

## SQL 구문

```sql
DS_HLL_ACCUMULATE(<expr>)
```

## SQL 예제

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_ACCUMULATE(user_id)) FROM visits;

┌──────┐
│ 9856 │
└──────┘
```
