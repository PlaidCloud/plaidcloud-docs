---
title: ALL_MATCH (Lakehouse v2)
description: ALL_MATCH — 配列のすべての要素が指定した述語に一致する場合に TRUE を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/all-match.md
---

配列のすべての要素が指定した述語に一致する場合に TRUE を返します。

## Analyzeの構文

```python
func.all_match(get_column(table, 'arr'), lambda x: x > 0)
```

## Analyzeの例

```python
func.all_match([1, 2, 3], lambda x: x > 0)

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ALL_MATCH(<arr>, lambda x: x > 0)
```

## SQLの例

```sql
SELECT ALL_MATCH([1, 2, 3], x -> x > 0);

┌───┐
│ 1 │
└───┘
```
