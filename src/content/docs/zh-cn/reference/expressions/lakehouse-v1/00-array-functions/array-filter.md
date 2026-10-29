---
title: ARRAY_FILTER (Lakehouse v1)
description: ARRAY_FILTER：用输入数组中使 lambda 函数返回 true 的元素构造新数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-filter.md
---

用输入数组中使 lambda 函数返回 true 的元素构造新数组。

## Analyze 语法

```python
func.array_filter( <array>, <lambda> )
```

## Analyze 示例

```python
func.array_filter([1, 2, 3], x -> (x > 1))

┌─────────────────────────────────────────────┐
│ func.array_filter([1, 2, 3], x -> (x > 1))  │
├─────────────────────────────────────────────┤
│ [2,3]                                       │
└─────────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_FILTER( <array>, <lambda> )
```

## SQL 示例

```sql
SELECT ARRAY_FILTER([1, 2, 3], x -> x > 1);

┌───────────────────────────────────────┐
│ array_filter([1, 2, 3], x -> (x > 1)) │
├───────────────────────────────────────┤
│ [2,3]                                 │
└───────────────────────────────────────┘
```
