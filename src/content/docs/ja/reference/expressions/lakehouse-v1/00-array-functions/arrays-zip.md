---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP — 複数の配列を、1つのタプルの配列にまとめます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

複数の配列を、1つのタプルの配列にまとめます。

## Analyzeの構文

```python
func.arrays_zip( <array1> [, ...] )
```

## Analyzeの例

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## 引数

| 引数 | 説明 |
|------------|-------------------|
| `<arrayN>` | 入力する配列です。 |

:::note
- 各配列の長さは同じである必要があります。
:::

## 戻り値の型

Array(Tuple)です。

## SQLの例

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```
