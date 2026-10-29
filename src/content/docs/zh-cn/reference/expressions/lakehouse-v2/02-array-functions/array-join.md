---
title: ARRAY_JOIN (Lakehouse v2)
description: ARRAY_JOIN：使用分隔符将数组元素连接为字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-join.md
---

使用分隔符将数组元素连接为字符串。

## Analyze 语法

```python
func.array_join([1,2,3], '-')
```

## Analyze 示例

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## SQL 语法

```sql
ARRAY_JOIN([1,2,3], '-')
```

## SQL 示例

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
