---
title: ARRAY_SUM (Lakehouse v2)
description: ARRAY_SUM — 配列の要素の合計を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-sum.md
---

配列の要素の合計を返します。

## Analyzeの構文

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Analyzeの例

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## SQLの構文

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## SQLの例

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
