---
title: ARRAY_CONTAINS_SEQ (Lakehouse v2)
description: ARRAY_CONTAINS_SEQ：检查一个数组是否按顺序包含另一个数组的所有元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains-seq.md
---

检查一个数组是否按顺序包含另一个数组的所有元素。

## Analyze 语法

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Analyze 示例

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## SQL 示例

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
