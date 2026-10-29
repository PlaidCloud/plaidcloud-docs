---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX：返回数组中的最大元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

返回数组中的最大元素。

## Analyze 语法

```python
func.array_max([3, 1, 4, 1, 5])
```

## Analyze 示例

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## SQL 语法

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## SQL 示例

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
