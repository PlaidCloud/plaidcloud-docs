---
title: ARRAY_MIN (Lakehouse v2)
description: ARRAY_MIN — 配列の最小の要素を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-min.md
---

配列の最小の要素を返します。

## Analyzeの構文

```python
func.array_min([3, 1, 4, 1, 5])
```

## Analyzeの例

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## SQLの例

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
