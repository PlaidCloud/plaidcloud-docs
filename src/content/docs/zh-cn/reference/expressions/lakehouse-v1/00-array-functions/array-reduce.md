---
title: ARRAY_REDUCE (Lakehouse v1)
description: ARRAY_REDUCE：对数组元素迭代应用 lambda 函数，将数组归约为单个值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-reduce.md
---

对数组元素迭代应用 lambda 函数，将数组归约为单个值。

## Analyze 语法

```python
func.array_reduce( <array>, <lambda> )
```

## Analyze 示例

```python
func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))

┌─────────────────────────────────────────────────────┐
│ func.array_reduce([1, 2, 3, 4], (x, y) -> (x + y))  │
├─────────────────────────────────────────────────────┤
│                                                  10 │
└─────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_REDUCE( <array>, <lambda> )
```

## SQL 示例

```sql
SELECT ARRAY_REDUCE([1, 2, 3, 4], (x,y) -> x + y);

┌───────────────────────────────────────────────┐
│ array_reduce([1, 2, 3, 4], (x, y) -> (x + y)) │
├───────────────────────────────────────────────┤
│                                            10 │
└───────────────────────────────────────────────┘
```
