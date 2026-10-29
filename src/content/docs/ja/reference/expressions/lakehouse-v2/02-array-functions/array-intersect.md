---
title: ARRAY_INTERSECT (Lakehouse v2)
description: ARRAY_INTERSECT — 2 つの配列の共通部分（積集合）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-intersect.md
---

2 つの配列の共通部分（積集合）を返します。

## Analyzeの構文

```python
func.array_intersect([1,2,3], [2,3,4])
```

## Analyzeの例

```python
func.array_intersect([1, 2, 3], [2, 3, 4])

┌───────┐
│ [2,3] │
└───────┘
```

## SQLの構文

```sql
ARRAY_INTERSECT([1,2,3], [2,3,4])
```

## SQLの例

```sql
SELECT ARRAY_INTERSECT([1, 2, 3], [2, 3, 4]);

┌───────┐
│ [2,3] │
└───────┘
```
