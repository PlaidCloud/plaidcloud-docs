---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN — ネストされた配列を 1 階層の配列に平坦化します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

ネストされた配列を 1 階層の配列に平坦化します。

## Analyzeの構文

```python
func.array_flatten([[1,2],[3,4]])
```

## Analyzeの例

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQLの構文

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## SQLの例

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
