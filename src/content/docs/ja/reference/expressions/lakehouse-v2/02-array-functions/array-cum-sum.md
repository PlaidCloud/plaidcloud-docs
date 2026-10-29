---
title: ARRAY_CUM_SUM (Lakehouse v2)
description: ARRAY_CUM_SUM — 配列の要素の累積合計を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-cum-sum.md
---

配列の要素の累積合計を返します。

## Analyzeの構文

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Analyzeの例

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## SQLの構文

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## SQLの例

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
