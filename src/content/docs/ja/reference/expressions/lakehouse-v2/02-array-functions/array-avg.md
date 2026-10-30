---
title: ARRAY_AVG (Lakehouse v2)
description: ARRAY_AVG — 配列の要素の平均を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-avg.md
---

配列の要素の平均を返します。

## Analyzeの構文

```python
func.array_avg([1, 2, 3, 4])
```

## Analyzeの例

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## SQLの構文

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## SQLの例

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
