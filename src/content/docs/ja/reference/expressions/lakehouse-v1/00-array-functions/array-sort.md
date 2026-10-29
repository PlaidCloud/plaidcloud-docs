---
title: ARRAY_SORT (Lakehouse v1)
description: ARRAY_SORT — 配列の要素を昇順に並べ替えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-sort.md
---

配列の要素を昇順に並べ替えます。

## Analyzeの構文

```sql
func.array_sort( <array>[, <order>, <nullposition>] )
```

| パラメーター | デフォルト | 説明 |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | 並べ替えの順序を、昇順（ASC）または降順（DESC）で指定します。 |
| nullposition | NULLS FIRST | 並べ替え結果でNULL値を配置する位置を、先頭（NULLS FIRST）または末尾（NULLS LAST）で指定します。 |

## Analyzeの例

```sql
func.array_sort([1, 4, 3, 2])

┌────────────────────────────────┐
│ func.array_sort([1, 4, 3, 2])  │
├────────────────────────────────┤
│ [1,2,3,4]                      │
└────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_SORT( <array>[, <order>, <nullposition>] )
```

| パラメーター | デフォルト | 説明 |
|--------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| order        | ASC         | 並べ替えの順序を、昇順（ASC）または降順（DESC）で指定します。 |
| nullposition | NULLS FIRST | 並べ替え結果でNULL値を配置する位置を、先頭（NULLS FIRST）または末尾（NULLS LAST）で指定します。 |

## SQLの例

```sql
SELECT ARRAY_SORT([1, 4, 3, 2]);

┌──────────────────────────┐
│ array_sort([1, 4, 3, 2]) │
├──────────────────────────┤
│ [1,2,3,4]                │
└──────────────────────────┘
```
