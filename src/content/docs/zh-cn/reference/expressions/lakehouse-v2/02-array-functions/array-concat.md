---
title: ARRAY_CONCAT (Lakehouse v2)
description: ARRAY_CONCAT：将多个数组连接为一个数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-concat.md
---

将多个数组连接为一个数组。

## Analyze 语法

```python
func.array_concat([1, 2], [3, 4])
```

## Analyze 示例

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL 语法

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## SQL 示例

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
