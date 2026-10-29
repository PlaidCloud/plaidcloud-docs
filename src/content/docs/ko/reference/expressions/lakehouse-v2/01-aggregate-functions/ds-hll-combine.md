---
title: DS_HLL_COMBINE (Lakehouse v2)
description: DS_HLL_COMBINE — 여러 DataSketches HLL 스케치를 하나의 스케치로 결합합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-combine.md
---

여러 DataSketches HLL 스케치를 하나의 스케치로 결합합니다.

## Analyze 구문

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))
```

## Analyze 예제

```python
func.ds_hll_combine(get_column(table, 'hll_sketch'))

┌───────────────────┐
│ (combined sketch) │
└───────────────────┘
```

## SQL 구문

```sql
DS_HLL_COMBINE(<sketch_column>)
```

## SQL 예제

```sql
SELECT DS_HLL_ESTIMATE(DS_HLL_COMBINE(sketch_col)) FROM daily_sketches;

┌───────┐
│ 25000 │
└───────┘
```
