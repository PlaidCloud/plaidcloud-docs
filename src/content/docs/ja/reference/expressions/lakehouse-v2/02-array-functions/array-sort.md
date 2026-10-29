---
title: ARRAY_SORT (Lakehouse v2)
description: ARRAY_SORT — 配列の要素を昇順に並べ替えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sort.md
---

配列の要素を昇順に並べ替えます。

## Analyzeの構文

```python
func.array_sort([3, 1, 4, 1, 5])
```

## Analyzeの例

```python
func.array_sort([3, 1, 4, 1, 5])

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```

## SQLの構文

```sql
ARRAY_SORT([3, 1, 4, 1, 5])
```

## SQLの例

```sql
SELECT ARRAY_SORT([3, 1, 4, 1, 5]);

┌─────────────┐
│ [1,1,3,4,5] │
└─────────────┘
```
