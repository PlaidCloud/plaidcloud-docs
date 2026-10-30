---
title: ARRAY_PREPEND (Lakehouse v1)
description: ARRAY_PREPEND：在数组开头添加一个元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-prepend.md
---

在数组开头添加一个元素。

## Analyze 语法

```python
func.array_prepend( <element>, <array> )
```

## Analyze 示例

```python
func.array_prepend(1, [3, 4])

┌────────────────────────────────┐
│ func.array_prepend(1, [3, 4])  │
├────────────────────────────────┤
│ [1,3,4]                        │
└────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_PREPEND( <element>, <array> )
```

## SQL 示例

```sql
SELECT ARRAY_PREPEND(1, [3, 4]);

┌──────────────────────────┐
│ array_prepend(1, [3, 4]) │
├──────────────────────────┤
│ [1,3,4]                  │
└──────────────────────────┘
```
