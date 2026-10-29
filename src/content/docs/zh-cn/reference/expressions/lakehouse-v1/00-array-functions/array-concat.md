---
title: ARRAY_CONCAT (Lakehouse v1)
description: ARRAY_CONCAT：连接两个数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-concat.md
---

连接两个数组。

## Analyze 语法

```python
func.array_concat( <array1>, <array2> )
```

## Analyze 示例

```python
func.array_concat([1, 2], [3, 4])

┌────────────────────────────────────┐
│ func.array_concat([1, 2], [3, 4])  │
├────────────────────────────────────┤
│ [1,2,3,4]                          │
└────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAY_CONCAT( <array1>, <array2> )
```

## SQL 示例

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌──────────────────────────────┐
│ array_concat([1, 2], [3, 4]) │
├──────────────────────────────┤
│ [1,2,3,4]                    │
└──────────────────────────────┘
```
