---
title: ARRAY_UNIQUE (Lakehouse v1)
description: ARRAY_UNIQUE：统计数组中唯一元素的数量（不包括 NULL）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-unique.md
---

统计数组中唯一元素的数量（不包括 NULL）。

## Analyze 语法

```python
func.array_unique( <array> )
```

## Analyze 示例

```python
func.array_unique([1, 2, 3, 3, 4])

┌─────────────────────────────────────┐
│ func.array_unique([1, 2, 3, 3, 4])  │
├─────────────────────────────────────┤
│                                   4 │
└─────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_UNIQUE( <array> )
```

## SQL 示例

```sql
SELECT ARRAY_UNIQUE([1, 2, 3, 3, 4]);

┌───────────────────────────────┐
│ array_unique([1, 2, 3, 3, 4]) │
├───────────────────────────────┤
│                             4 │
└───────────────────────────────┘
```
