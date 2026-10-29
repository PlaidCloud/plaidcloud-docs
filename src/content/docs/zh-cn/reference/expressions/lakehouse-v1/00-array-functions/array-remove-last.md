---
title: ARRAY_REMOVE_LAST (Lakehouse v1)
description: ARRAY_REMOVE_LAST：删除数组的最后一个元素。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-remove-last.md
---

删除数组的最后一个元素。

## Analyze 语法

```python
func.array_remove_last( <array> )
```

## Analyze 示例

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_REMOVE_LAST( <array> )
```

## SQL 示例

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```
