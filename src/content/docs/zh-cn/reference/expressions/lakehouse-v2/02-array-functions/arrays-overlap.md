---
title: ARRAYS_OVERLAP (Lakehouse v2)
description: ARRAYS_OVERLAP：检查两个数组是否有共同元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-overlap.md
---

检查两个数组是否有共同元素。

## Analyze 语法

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Analyze 示例

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## SQL 示例

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
