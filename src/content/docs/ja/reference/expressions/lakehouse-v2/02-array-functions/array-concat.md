---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT — 複数の配列を 1 つの配列に連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

複数の配列を 1 つの配列に連結します。

## Analyzeの構文

```python
func.array_concat([1, 2], [3, 4])
```

## Analyzeの例

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQLの構文

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## SQLの例

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
