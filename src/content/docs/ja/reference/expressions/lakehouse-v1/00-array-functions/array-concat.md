---
title: ARRAY_CONCAT (Lakehouse v1)
description: ARRAY_CONCAT — 2つの配列を連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-concat.md
---

2つの配列を連結します。

## Analyzeの構文

```python
func.array_concat( <array1>, <array2> )
```

## Analyzeの例

```python
func.array_concat([1, 2], [3, 4])

┌────────────────────────────────────┐
│ func.array_concat([1, 2], [3, 4])  │
├────────────────────────────────────┤
│ [1,2,3,4]                          │
└────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_CONCAT( <array1>, <array2> )
```

## SQLの例

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌──────────────────────────────┐
│ array_concat([1, 2], [3, 4]) │
├──────────────────────────────┤
│ [1,2,3,4]                    │
└──────────────────────────────┘
```
