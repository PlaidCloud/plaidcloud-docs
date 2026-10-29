---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN：返回数组中的最小元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

返回数组中的最小元素。

## Analyze 语法

```python
func.array_min([3, 1, 4, 1, 5])
```

## Analyze 示例

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## SQL 示例

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
