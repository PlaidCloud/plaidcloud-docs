---
title: ARRAY_REPEAT (Lakehouse v2)
description: ARRAY_REPEAT：创建一个将指定元素重复 N 次的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-repeat.md
---

创建一个将指定元素重复 N 次的数组。

## Analyze 语法

```python
func.array_repeat('x', 3)
```

## Analyze 示例

```python
func.array_repeat('x', 3)

┌───────────────┐
│ ['x','x','x'] │
└───────────────┘
```

## SQL 语法

```sql
ARRAY_REPEAT('x', 3)
```

## SQL 示例

```sql
SELECT ARRAY_REPEAT('x', 3);

┌───────────────┐
│ ["x","x","x"] │
└───────────────┘
```
