---
title: ARRAY_DIFFERENCE (Lakehouse v2)
description: ARRAY_DIFFERENCE — 隣接する要素間の差の配列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-difference.md
---

隣接する要素間の差の配列を返します。

## Analyzeの構文

```python
func.array_difference([1, 3, 6, 10])
```

## Analyzeの例

```python
func.array_difference([1, 3, 6, 10])

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```

## SQLの構文

```sql
ARRAY_DIFFERENCE([1, 3, 6, 10])
```

## SQLの例

```sql
SELECT ARRAY_DIFFERENCE([1, 3, 6, 10]);

┌───────────┐
│ [0,2,3,4] │
└───────────┘
```
