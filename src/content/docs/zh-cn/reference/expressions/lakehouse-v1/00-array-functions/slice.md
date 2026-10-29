---
title: SLICE (Lakehouse v1)
description: SLICE：按索引（从 1 开始）提取数组的一个切片。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/slice.md
---

按索引（从 1 开始）提取数组的一个切片。

## Analyze 语法

```python
func.slice( <array>, <start>[, <end>] )
```

## Analyze 示例

```python
func.slice([1, 21, 32, 4], 2, 3)

┌──────────────────────────────────┐
│ func.slice([1, 21, 32, 4], 2, 3) │
├──────────────────────────────────┤
│ [21,32]                          │ 
└──────────────────────────────────┘
```

## SQL 语法

```sql
SLICE( <array>, <start>[, <end>] )
```

## 别名

- [ARRAY_SLICE](../array-slice)

## SQL 示例

```sql
SELECT ARRAY_SLICE([1, 21, 32, 4], 2, 3), SLICE([1, 21, 32, 4], 2, 3);

┌─────────────────────────────────────────────────────────────────┐
│ array_slice([1, 21, 32, 4], 2, 3) │ slice([1, 21, 32, 4], 2, 3) │
├───────────────────────────────────┼─────────────────────────────┤
│ [21,32]                           │ [21,32]                     │
└─────────────────────────────────────────────────────────────────┘
```
