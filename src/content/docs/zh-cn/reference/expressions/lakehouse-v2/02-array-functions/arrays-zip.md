---
title: ARRAYS_ZIP (Lakehouse v2)
description: ARRAYS_ZIP：将多个数组合并为由结构体组成的数组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-zip.md
---

将多个数组合并为由结构体组成的数组。

## Analyze 语法

```python
func.arrays_zip([1,2], ['a','b'])
```

## Analyze 示例

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌───────────────────────────┐
│ [{1,'a'},{2,'b'},{3,'c'}] │
└───────────────────────────┘
```

## SQL 语法

```sql
ARRAYS_ZIP([1,2], ['a','b'])
```

## SQL 示例

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);

┌───────────────────────────────────────────────────┐
│ [{"0":1,"1":"a"},{"0":2,"1":"b"},{"0":3,"1":"c"}] │
└───────────────────────────────────────────────────┘
```
