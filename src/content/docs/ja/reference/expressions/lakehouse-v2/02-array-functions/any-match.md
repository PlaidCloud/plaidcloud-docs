---
title: ANY_MATCH (Lakehouse v2)
description: ANY_MATCH — 配列のいずれかの要素が指定した述語に一致する場合に TRUE を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/any-match.md
---

配列のいずれかの要素が指定した述語に一致する場合に TRUE を返します。

## Analyzeの構文

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Analyzeの例

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## SQLの例

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
