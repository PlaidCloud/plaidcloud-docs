---
title: ARRAY_APPEND (Lakehouse v1)
description: ARRAY_APPEND：在数组中追加一个元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-append.md
---

在数组中追加一个元素。

## Analyze 语法

```python
func.array_append( <array>, <element>)
```

## Analyze 示例

```python
func.array_append([3, 4], 5)

┌──────────────────────────────┐
│ func.array_append([3, 4], 5) │
├──────────────────────────────┤
│ [3,4,5]                      │
└──────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_APPEND( <array>, <element>)
```

## SQL 示例

```sql
SELECT ARRAY_APPEND([3, 4], 5);

┌─────────────────────────┐
│ array_append([3, 4], 5) │
├─────────────────────────┤
│ [3,4,5]                 │
└─────────────────────────┘
```
