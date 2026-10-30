---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP：将多个数组合并为单个数组元组。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

将多个数组合并为单个数组元组。

## Analyze 语法

```python
func.arrays_zip( <array1> [, ...] )
```

## Analyze 示例

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## SQL 语法

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## 参数

| 参数  | 说明       |
|------------|-------------------|
| `<arrayN>` | 输入的数组。 |

:::note
- 每个数组的长度必须相同。
:::

## 返回类型

Array(Tuple)。

## SQL 示例

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```
