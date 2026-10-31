---
title: ARRAY_DISTINCT (Lakehouse v1)
description: ARRAY_DISTINCT：删除数组中所有重复项和 NULL，不保留原有顺序。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-distinct.md
---

删除数组中所有重复项和 NULL，不保留原有顺序。

## Analyze 语法

```python
func.array_distinct( <array> )
```

## Analyze 示例

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_DISTINCT( <array> )
```

## SQL 示例

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```
