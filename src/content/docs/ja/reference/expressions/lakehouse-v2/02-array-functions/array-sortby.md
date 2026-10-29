---
title: ARRAY_SORTBY (Lakehouse v2)
description: ARRAY_SORTBY — 別の配列の対応する要素を基準に、配列の要素を並べ替えます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sortby.md
---

別の配列の対応する要素を基準に、配列の要素を並べ替えます。

## Analyzeの構文

```python
func.array_sortby(get_column(table, 'names'), get_column(table, 'scores'))
```

## Analyzeの例

```python
func.array_sortby(['c','a','b'], [3,1,2])

┌───────────────┐
│ ['a','b','c'] │
└───────────────┘
```

## SQLの構文

```sql
ARRAY_SORTBY(<names>, <scores>)
```

## SQLの例

```sql
SELECT ARRAY_SORTBY(['c','a','b'], [3,1,2]);

┌───────────────┐
│ ["a","b","c"] │
└───────────────┘
```
