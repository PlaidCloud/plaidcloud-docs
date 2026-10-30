---
title: ARRAY_CONTAINS_ALL (Lakehouse v2)
description: ARRAY_CONTAINS_ALL：检查一个数组是否包含另一个数组的所有元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-all.md
---

检查一个数组是否包含另一个数组的所有元素。

## Analyze 语法

```python
func.array_contains_all([1,2,3], [1,2])
```

## Analyze 示例

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## SQL 示例

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
