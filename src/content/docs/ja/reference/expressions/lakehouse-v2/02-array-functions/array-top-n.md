---
title: ARRAY_TOP_N (Lakehouse v2)
description: ARRAY_TOP_N — 配列から上位 N 個の要素を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-top-n.md
---

配列から上位 N 個の要素を返します。

## Analyzeの構文

```python
func.array_top_n([3,1,4,1,5], 3)
```

## Analyzeの例

```python
func.array_top_n([3, 1, 4, 1, 5], 3)

┌─────────┐
│ [5,4,3] │
└─────────┘
```

## SQLの構文

```sql
ARRAY_TOP_N([3,1,4,1,5], 3)
```

## SQLの例

```sql
SELECT ARRAY_TOP_N([3, 1, 4, 1, 5], 3);

┌─────────┐
│ [5,4,3] │
└─────────┘
```
