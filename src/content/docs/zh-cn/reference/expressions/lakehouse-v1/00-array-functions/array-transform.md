---
title: ARRAY_TRANSFORM (Lakehouse v1)
description: ARRAY_TRANSFORM：返回对输入数组的每个元素应用 lambda 函数后得到的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-transform.md
---

返回对输入数组的每个元素应用 lambda 函数后得到的数组。

## Analyze 语法

```python
func.array_transform( <array>, <lambda> )
```

## Analyze 示例

```python
func.array_transform([1, 2, 3], x -> (x + 1))

┌───────────────────────────────────────────────┐
│ func.array_transform([1, 2, 3], x -> (x + 1)) │
├───────────────────────────────────────────────┤
│ [2,3,4]                                       │
└───────────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_TRANSFORM( <array>, <lambda> )
```

## 别名

- [ARRAY_APPLY](../array-apply)

## SQL 示例

```sql
SELECT ARRAY_TRANSFORM([1, 2, 3], x -> x + 1);

┌──────────────────────────────────────────┐
│ array_transform([1, 2, 3], x -> (x + 1)) │
├──────────────────────────────────────────┤
│ [2,3,4]                                  │
└──────────────────────────────────────────┘
```
