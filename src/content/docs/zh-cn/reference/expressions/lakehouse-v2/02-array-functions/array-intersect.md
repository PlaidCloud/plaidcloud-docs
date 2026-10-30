---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT：返回两个数组的交集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

返回两个数组的交集。

## Analyze 语法

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Analyze 示例

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## SQL 语法

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## SQL 示例

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
