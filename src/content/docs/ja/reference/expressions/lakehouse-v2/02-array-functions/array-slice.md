---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE — 開始位置から指定した長さの配列の一部（スライス）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

開始位置から指定した長さの配列の一部（スライス）を返します。

## Analyzeの構文

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Analyzeの例

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## SQLの構文

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## SQLの例

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
