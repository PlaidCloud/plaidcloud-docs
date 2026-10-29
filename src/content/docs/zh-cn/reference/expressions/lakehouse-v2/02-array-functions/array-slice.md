---
title: ARRAY_SLICE (Lakehouse v2)
description: ARRAY_SLICE：从指定起始位置开始，返回给定长度的数组切片。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-slice.md
---

从指定起始位置开始，返回给定长度的数组切片。

## Analyze 语法

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Analyze 示例

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## SQL 语法

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## SQL 示例

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
