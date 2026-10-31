---
title: ARRAY_FLATTEN (Lakehouse v1)
description: ARRAY_FLATTEN：展平嵌套数组，将其转换为单层数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-flatten.md
---

展平嵌套数组，将其转换为单层数组。

## Analyze 语法

```python
func.array_flatten( <array> )
```

## Analyze 示例

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_FLATTEN( <array> )
```

## SQL 示例

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```
