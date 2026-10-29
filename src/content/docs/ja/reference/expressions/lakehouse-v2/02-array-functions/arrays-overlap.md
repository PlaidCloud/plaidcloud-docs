---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP — 2 つの配列に共通の要素があるかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

2 つの配列に共通の要素があるかどうかを確認します。

## Analyzeの構文

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Analyzeの例

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## SQLの例

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
