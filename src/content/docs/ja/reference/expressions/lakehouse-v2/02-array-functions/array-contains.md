---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — 配列が特定の要素を含んでいるかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-contains.md
---

配列が特定の要素を含んでいるかどうかを確認します。

## Analyzeの構文

```python
func.array_contains([1, 2, 3], 2)
```

## Analyzeの例

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## SQLの例

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
