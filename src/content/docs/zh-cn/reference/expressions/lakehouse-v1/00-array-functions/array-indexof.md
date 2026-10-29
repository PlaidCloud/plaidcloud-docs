---
title: ARRAY_INDEXOF (Lakehouse v1)
description: ARRAY_INDEXOF：如果数组包含指定元素，则返回该元素的索引（从 1 开始）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-indexof.md
---

如果数组包含指定元素，则返回该元素的索引（从 1 开始）。

## Analyze 语法

```python
func.array_indexof( <array>, <element> )
```

## Analyze 示例

```python
func.array_indexof([1, 2, 9], 9)

┌───────────────────────────────────┐
│ func.array_indexof([1, 2, 9], 9)  │
├───────────────────────────────────┤
│                                 3 │
└───────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_INDEXOF( <array>, <element> )
```

## SQL 示例

```sql
SELECT ARRAY_INDEXOF([1, 2, 9], 9);

┌─────────────────────────────┐
│ array_indexof([1, 2, 9], 9) │
├─────────────────────────────┤
│                           3 │
└─────────────────────────────┘
```
