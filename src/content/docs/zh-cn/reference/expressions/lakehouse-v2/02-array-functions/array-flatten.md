---
title: ARRAY_FLATTEN (Lakehouse v2)
description: ARRAY_FLATTEN：将嵌套数组展平为单层数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-flatten.md
---

将嵌套数组展平为单层数组。

## Analyze 语法

```python
func.array_flatten([[1,2],[3,4]])
```

## Analyze 示例

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL 语法

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## SQL 示例

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
