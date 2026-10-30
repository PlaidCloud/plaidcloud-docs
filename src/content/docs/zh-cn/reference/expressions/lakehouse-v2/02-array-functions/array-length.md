---
title: ARRAY_LENGTH (Lakehouse v2)
description: ARRAY_LENGTH：返回数组中的元素个数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-length.md
---

返回数组中的元素个数。

## Analyze 语法

```python
func.array_length([1, 2, 3])
```

## Analyze 示例

```python
func.array_length([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL 语法

```sql
ARRAY_LENGTH([1, 2, 3])
```

## SQL 示例

```sql
SELECT ARRAY_LENGTH([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
