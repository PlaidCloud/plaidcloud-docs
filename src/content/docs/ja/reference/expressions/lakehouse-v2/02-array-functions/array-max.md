---
title: ARRAY_MAX (Lakehouse v2)
description: ARRAY_MAX — 配列の最大の要素を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-max.md
---

配列の最大の要素を返します。

## Analyzeの構文

```python
func.array_max([3, 1, 4, 1, 5])
```

## Analyzeの例

```python
func.array_max([3, 1, 4, 1, 5])

┌───┐
│ 5 │
└───┘
```

## SQLの構文

```sql
ARRAY_MAX([3, 1, 4, 1, 5])
```

## SQLの例

```sql
SELECT ARRAY_MAX([3, 1, 4, 1, 5]);

┌───┐
│ 5 │
└───┘
```
